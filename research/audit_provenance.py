#!/usr/bin/env python3
"""Audit Codex research sessions and annotate final research deliverables.

The session files are JSONL containing nested JavaScript tool-call payloads. This
script deliberately parses only the structured fields and the small subset of
JavaScript literals needed for search-query extraction; it never executes log
content.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path
from urllib.parse import urlparse


BEGIN_MARKER = "<!-- RESEARCH PROVENANCE: BEGIN -->"
END_MARKER = "<!-- RESEARCH PROVENANCE: END -->"
URL_RE = re.compile(r"https?://[^\s<>\"'`]+", re.IGNORECASE)
QUERY_RE = re.compile(r"\bq\s*:\s*\"((?:\\.|[^\"\\])*)\"")


@dataclass
class WebCall:
    call_id: str
    turn_id: str | None
    input_text: str
    queries: set[str] = field(default_factory=set)
    domains: set[str] = field(default_factory=set)


@dataclass
class SessionAudit:
    session_id: str
    log_path: Path
    started_at: str = ""
    active_turn_ids: set[str] = field(default_factory=set)
    changed_files: dict[str, set[str]] = field(default_factory=lambda: defaultdict(set))
    web_calls: list[WebCall] = field(default_factory=list)

    @property
    def queries(self) -> list[str]:
        return sorted({query for call in self.web_calls for query in call.queries})

    @property
    def domains(self) -> list[str]:
        return sorted({domain for call in self.web_calls for domain in call.domains})


def decode_js_string(value: str) -> str:
    """Decode the JSON-compatible escapes used in logged JS string literals."""

    try:
        return json.loads(f'"{value}"')
    except json.JSONDecodeError:
        return value.replace(r'\"', '"').replace(r"\\", "\\")


def domain_from_url(url: str) -> str | None:
    url = url.rstrip(".,;:)]}>")
    try:
        parsed = urlparse(url)
    except ValueError:
        return None
    if parsed.scheme not in {"http", "https"} or not parsed.hostname:
        return None
    return parsed.hostname.lower().removeprefix("www.")


def urls_to_domains(text: str) -> set[str]:
    domains: set[str] = set()
    for match in URL_RE.finditer(text):
        domain = domain_from_url(match.group(0))
        if domain:
            domains.add(domain)
    return domains


def output_text(output: object) -> str:
    if isinstance(output, str):
        return output
    return json.dumps(output, ensure_ascii=False)


def relative_repo_path(path: str, repo_root: Path) -> str | None:
    candidate = Path(path)
    if not candidate.is_absolute():
        candidate = repo_root / candidate
    try:
        return candidate.resolve().relative_to(repo_root.resolve()).as_posix()
    except ValueError:
        return None


def target_files(repo_root: Path) -> list[Path]:
    paths = []
    for directory in (
        repo_root / "research" / "audiences",
        repo_root / "research" / "synthesis",
        repo_root / "research" / "review",
    ):
        paths.extend(path for path in directory.glob("*.md") if path.is_file())
    return sorted(paths)


def parse_session(log_path: Path, repo_root: Path) -> SessionAudit:
    session_id = log_path.stem.rsplit("-", 1)[-1]
    audit = SessionAudit(session_id=session_id, log_path=log_path)
    records: list[dict] = []
    parent_session_id = ""
    task_turn_ids: list[str] = []

    with log_path.open(encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, 1):
            try:
                record = json.loads(line)
            except json.JSONDecodeError as exc:
                raise ValueError(f"{log_path}:{line_number}: invalid JSON: {exc}") from exc
            records.append(record)

            if record.get("type") == "session_meta":
                payload = record.get("payload", {})
                if not audit.started_at:
                    audit.session_id = payload.get("id") or payload.get("session_id") or audit.session_id
                    parent_session_id = payload.get("session_id", "")
                    audit.started_at = payload.get("timestamp", "")

            if record.get("type") == "event_msg" and record.get("payload", {}).get("type") == "task_started":
                turn_id = record["payload"].get("turn_id")
                if turn_id:
                    task_turn_ids.append(turn_id)

            payload = record.get("payload", {})
            if record.get("type") == "response_item":
                metadata = payload.get("internal_chat_message_metadata_passthrough") or {}
                turn_id = metadata.get("turn_id")
                if turn_id:
                    audit.active_turn_ids.add(turn_id)

    # Child logs include the parent turn's initial events. The first
    # task_started turn is the inherited parent turn; later task_started turns
    # belong to this session. Top-level logs retain all their own turns.
    if task_turn_ids:
        inherited_parent_turn = parent_session_id and parent_session_id != audit.session_id and len(task_turn_ids) > 1
        owned_turn_ids = set(task_turn_ids[1:] if inherited_parent_turn else task_turn_ids)
    else:
        owned_turn_ids = audit.active_turn_ids

    # Parse actual patch events, excluding inherited events.
    for record in records:
        payload = record.get("payload", {})
        if record.get("type") != "event_msg" or payload.get("type") != "patch_apply_end":
            continue
        if not payload.get("success") or payload.get("turn_id") not in owned_turn_ids:
            continue
        for raw_path, change in (payload.get("changes") or {}).items():
            repo_path = relative_repo_path(raw_path, repo_root)
            if repo_path:
                audit.changed_files[repo_path].add(change.get("type", "changed"))

    # Collect web calls and their query literals from exec wrapper payloads.
    web_call_ids: set[str] = set()
    for record in records:
        payload = record.get("payload", {})
        if record.get("type") != "response_item" or payload.get("type") != "custom_tool_call":
            continue
        input_text = payload.get("input") or ""
        if "tools.web__run" not in input_text:
            continue
        metadata = payload.get("internal_chat_message_metadata_passthrough") or {}
        turn_id = metadata.get("turn_id")
        if turn_id not in owned_turn_ids:
            continue
        call = WebCall(
            call_id=payload.get("call_id", ""),
            turn_id=turn_id,
            input_text=input_text,
            queries={decode_js_string(match.group(1)) for match in QUERY_RE.finditer(input_text)},
            domains=urls_to_domains(input_text),
        )
        audit.web_calls.append(call)
        web_call_ids.add(call.call_id)

    # Web results are returned as custom-tool outputs for the enclosing exec
    # call. URLs in those outputs are the deterministic record of result sites
    # consulted, even when the web call opened a ref_id rather than a URL.
    for record in records:
        payload = record.get("payload", {})
        if record.get("type") != "response_item" or payload.get("type") != "custom_tool_call_output":
            continue
        if payload.get("call_id") not in web_call_ids:
            continue
        output = payload.get("output") or ""
        output_domains = urls_to_domains(output_text(output))
        for call in audit.web_calls:
            if call.call_id == payload.get("call_id"):
                call.domains.update(output_domains)
                break

    return audit


def audit_sessions(sessions_dir: Path, repo_root: Path) -> list[SessionAudit]:
    logs = sorted(sessions_dir.glob("*.jsonl"))
    if not logs:
        raise FileNotFoundError(f"no JSONL session logs found in {sessions_dir}")
    return [parse_session(log, repo_root) for log in logs]


def changed_files_report(audits: list[SessionAudit], repo_root: Path) -> str:
    lines = ["# Research session provenance audit", ""]
    for audit in sorted(audits, key=lambda item: (item.started_at, item.session_id)):
        if not audit.changed_files:
            continue
        lines.append(f"## Session `{audit.session_id}`")
        lines.append(f"- Log: `{audit.log_path.name}`")
        lines.append("- Changed files:")
        for path in sorted(audit.changed_files):
            operations = ", ".join(sorted(audit.changed_files[path]))
            lines.append(f"  - `{path}` ({operations})")
        lines.append(f"- Search queries recorded: {len(audit.queries)}")
        for query in audit.queries:
            lines.append(f"  - `{query}`")
        lines.append(f"- Website domains recorded: {len(audit.domains)}")
        for domain in audit.domains:
            lines.append(f"  - `{domain}`")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def provenance_block(file_path: Path, writers: list[SessionAudit], repo_root: Path) -> str:
    lines = [BEGIN_MARKER, "## Research provenance", ""]
    lines.append(
        "This section was generated from the recorded Codex session JSONL logs. "
        "File attribution uses successful patch events; searches and domains use nested web-tool calls."
    )
    lines.append("")

    for audit in sorted(writers, key=lambda item: (item.started_at, item.session_id)):
        operations = ", ".join(sorted(audit.changed_files.get(file_path.relative_to(repo_root).as_posix(), {"changed"})))
        lines.append(f"### Session `{audit.session_id}`")
        lines.append(f"- Log: `{audit.log_path.name}`")
        lines.append(f"- This document: `{operations}`")
        lines.append("- Search queries:")
        if audit.queries:
            lines.extend(f"  - `{query}`" for query in audit.queries)
        else:
            lines.append("  - None recorded.")
        lines.append("- Website domains:")
        if audit.domains:
            lines.extend(f"  - `{domain}`" for domain in audit.domains)
        else:
            lines.append("  - None recorded.")
        lines.append("")

    lines.append(END_MARKER)
    return "\n".join(lines)


def replace_block(content: str, block: str) -> str:
    pattern = re.compile(
        rf"\n?{re.escape(BEGIN_MARKER)}.*?{re.escape(END_MARKER)}\n?",
        re.DOTALL,
    )
    content = pattern.sub("", content).rstrip()
    return f"{content}\n\n{block}\n"


def annotate_documents(audits: list[SessionAudit], repo_root: Path, write: bool) -> list[str]:
    writers_by_file: dict[str, list[SessionAudit]] = defaultdict(list)
    for audit in audits:
        for path in audit.changed_files:
            writers_by_file[path].append(audit)

    errors: list[str] = []
    for file_path in target_files(repo_root):
        relative = file_path.relative_to(repo_root).as_posix()
        writers = writers_by_file.get(relative, [])
        if not writers:
            errors.append(f"no recorded writer session for {relative}")
            continue
        content = file_path.read_text(encoding="utf-8")
        block = provenance_block(file_path, writers, repo_root)
        updated = replace_block(content, block)
        if write and updated != content:
            file_path.write_text(updated, encoding="utf-8")
    return errors


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--sessions", type=Path, required=True, help="Directory containing session JSONL files")
    parser.add_argument("--repo", type=Path, default=Path.cwd(), help="Repository root")
    parser.add_argument("--write", action="store_true", help="Write provenance blocks to final research documents")
    parser.add_argument("--check", action="store_true", help="Validate attribution and generated blocks without writing")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    repo_root = args.repo.resolve()
    sessions_dir = args.sessions.expanduser().resolve()
    audits = audit_sessions(sessions_dir, repo_root)

    if args.write and args.check:
        print("--write and --check are mutually exclusive", file=sys.stderr)
        return 2

    errors = annotate_documents(audits, repo_root, write=args.write)
    print(changed_files_report(audits, repo_root))
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    if args.check:
        for file_path in target_files(repo_root):
            content = file_path.read_text(encoding="utf-8")
            if content.count(BEGIN_MARKER) != 1 or content.count(END_MARKER) != 1:
                print(f"ERROR: expected one provenance block in {file_path}", file=sys.stderr)
                return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
