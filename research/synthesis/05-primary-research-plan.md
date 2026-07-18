# Primary research plan

## Research objective and prioritization

The plan reduces the largest uncertainties that could distort later audience prioritization and evidence assessment. Priority is based on **uncertainty × likely consequence**, not presumed audience value. The central design principle is to study recent, consequential episodes—including rejection and inaction—rather than ask decontextualized opinions about Django.

Sample-size ranges are qualitative research-design guidance. They support variation and thematic saturation; they are not statistically precise estimates. Any quantitative prevalence claim requires a separately powered and probability-aware design.

## Shared decision-episode protocol

For every decision-oriented study, anchor the interview on an episode preferably within the previous 6–18 months and reconstruct:

1. What changed, for whom, and why action became necessary.
2. The current/status-quo solution, including no-build/buy/continue options.
3. Who initiated, researched, influenced, approved, blocked, implemented, operated, and bore consequences.
4. The initial shortlist and how options entered or left it.
5. Criteria stated before the decision versus reasons narrated afterward.
6. Proofs, prototypes, benchmarks, course pilots, reviews, and acceptance thresholds.
7. Channel sequence: discovery, evaluation, validation, approval, and ongoing engagement.
8. Artifacts: decision records, tickets, proof plans/results, architecture diagrams, risk reviews, procurement questions, course proposals, contribution threads, budgets, or renewal proposals.
9. The turning point, unresolved uncertainty, final outcome, and counterfactual.
10. What happened afterward: delivery, learning, incidents, upgrades, staffing, contribution, funding, migration, or reversal.

Interview multiple roles from the same episode where practical. Ask for redacted artifacts and clearly separate contemporaneous evidence from retrospective interpretation.

## Study 1 — Consequential foundation decisions

**Priority: 1. Decision informed:** whether practitioner, evaluator, leader, and reviewer lenses represent distinct jobs or stages of one decision system; which uncertainties deserve later comparative analysis.

**Groups:** recent Django adopters; serious evaluators who rejected it; teams that retained an incumbent; teams migrating/coexisting; teams that bought, used an internal platform, postponed, or did not build.

**Recruitment characteristics:**

- 24–36 decision episodes, with 1–3 participants per episode; target roughly 40–60 interviews.
- Balance one-team and multi-team settings; greenfield and incumbent; ordinary and regulated/high-assurance; conventional data-centric, API-centered, rich-interaction, and async/performance-sensitive workloads.
- Recruit actual evaluators, implementers/operators, approvers/service owners, and reviewers rather than quota by title.
- Include at least 8 serious reject/no-build/buy episodes and 6 reconsideration/migration/retention episodes.
- Seek geographic and language variation; do not rely only on community-visible organizations.

**Comparison cases:** adopted versus rejected after comparable needs; Django retained versus migrated under similar estate pressure; practitioner-led versus governance-led; low- versus high-assurance; proof conducted versus familiarity/standard-driven choice.

**Concrete questions:**

- Which criteria eliminated an option, and which merely required mitigation or a proof?
- Which workload and organizational assumptions were tested in context? What threshold counted as acceptable?
- How were integration, security, staffing, lifecycle, package, operations, and switching costs represented?
- Where did practitioner evidence change when translated for leaders, security, procurement, or finance?
- Who could veto, who accepted residual risk, and who later bore unexpected work?
- What would have changed the decision? Which concerns were legitimate constraints, misconceptions, status pressure, or habits?
- At 3–12 months, which expected benefits/costs materialized, and which were actually caused by other architecture, platform, team, or scope choices?

**Method:** decision-episode interviews plus artifact analysis; follow 8–12 episodes at 6 and 12 months. **Sequence:** first, because its language and role map should refine all later instruments.

## Study 2 — Quiet former users and silent incumbent stewards

**Priority: 2. Decision informed:** how lifecycle state changes jobs and what can legitimately be inferred from migration, retention, and return.

**Groups:** quiet leavers with no public postmortem; people who stopped new Django work but maintain an estate; active migrators; former users who did not return; returners; incumbents who considered leaving but stayed; unsupported or high-debt estate stewards.

**Recruitment characteristics:** 24–32 interviews, stratified by departure recency (current supported-era versus older), individual versus organizational decision, full departure versus coexistence, and current role/workload. Recruit through alumni networks, employers, package/user traces, training cohorts, and broader Python/web communities—not only Django channels.

**Comparison cases:** matched leaver/stayer episodes with similar workload; public postmortem authors versus quiet leavers; returner versus non-returner; migration completed versus coexistence/abandonment.

**Concrete questions:**

- What exactly stopped: new projects, part of the stack, employment use, or all operation?
- Which pain belonged to Django, a third-party package, architecture, frontend, data model, deployment, team practice, or changed product need?
- What evidence existed before leaving, what changed during transition, and what was learned only afterward?
- How much delivery, migration, dual-operation, data, and learning work occurred?
- Why did comparable incumbents stay? What would trigger reconsideration?
- For returners, what changed in workload or team, and how much did familiarity dominate?

**Method:** episode reconstruction with before/after artifact timelines; optional short survey to size lifecycle states after qualitative categories stabilize. **Sequence:** alongside Study 1.

## Study 3 — First programming and Python-to-web pathways

**Priority: 3. Decision informed:** where the R0/R1 boundary lies, which paths produce independent capability, and which jobs should remain separate.

**Groups:** no-code/basic-syntax learners; independently capable Python users new to web; teacher-led, coached-workshop, and self-directed learners; career, hobby, work-task, and personal-artifact goals; access-constrained and non-English-primary participants.

**Recruitment characteristics:**

- 32–48 participants across two readiness bands; avoid treating age or career intent as readiness.
- 12–16 observed first sessions for each readiness band, followed by interviews.
- Include common operating systems, lower-spec devices, intermittent connectivity, assistive technology, and at least two non-English-primary cohorts where feasible.
- Follow 20–30 participants at 4 and 12 weeks.

**Comparison cases:** Python-first versus integrated web-project path; coached versus self-paced; completed artifact with versus without independent modification; human help versus AI-dominant help patterns (observational first; randomized microtasks only if ethical and useful).

**Concrete questions:**

- What can participants explain and debug before starting, and which missing concept first blocks progress?
- Can they make an unscripted change and recover from an introduced error?
- What creates a mastery experience versus a copied artifact?
- How do setup, versions, deployment, vocabulary, language, accessibility, time, and device constraints interact?
- Which channel is used for discovery, then for a specific evaluation or unblock? What answer is trusted and why?
- How is AI used—explanation, diagnosis, substitution, or verification—and what transfers to a second task?
- What determines continuation, a change of path, or an informed decision to stop?

**Method:** contextual inquiry, task observation, pre/post mental-model probes, diary/telemetry with consent, and longitudinal interviews. **Sequence:** instrument design after early Study 1 findings, fieldwork can run concurrently.

## Study 4 — Full-stack and backend workload-fit investigations

**Priority: 4. Decision informed:** whether “full-stack” and “experienced backend” predict distinct evaluation/delivery jobs after controlling for lifecycle and authority.

**Groups:** front-end-leaning full-stack developers, back-end-leaning full-stack developers, backend specialists, solo end-to-end owners, specialist-team implementers, and operators investigating performance/async/data/integration concerns.

**Recruitment characteristics:** 20–28 participants around 12–18 recent feature or proof episodes; mix Django adopters, rejecters, incumbents, and former users. Stratify by interaction model and workload rather than generic “scale.”

**Comparison cases:** integrated server-rendered path versus separate client/backend where both were plausible; solo versus specialist team; conventional data workflow versus realtime/latency-sensitive or API platform.

**Concrete questions:**

- Which seams consume design, synchronization, test, deployment, and debugging effort?
- Which integrated capabilities remove work, and which conventions obscure or constrain necessary behavior?
- What representative evidence resolved a performance, async, frontend, or deployment uncertainty?
- Which costs are framework-specific versus architecture, package, platform, or team-topology effects?
- What must another developer understand to change the feature safely?

**Method:** episode interviews, workflow/architecture walkthroughs, and artifact/code-boundary mapping; no generic benchmark contest. **Sequence:** after Study 1 identifies recurring workload categories.

## Study 5 — Agency-client-operator delivery systems

**Priority: 5. Decision informed:** how commercial delivery, framework reuse, client ownership, and post-launch support change the job and decision roles.

**Groups:** agency owner/commercial lead, agency technical lead/developer, client sponsor/product owner, client technical/security reviewer, and post-launch operator. Include successful handovers, retained support, failed fixed bids, replaced suppliers, and projects that rejected Django.

**Recruitment characteristics:** 12–16 engagements, preferably paired or triad interviews; 28–40 interviews. Vary agency size, pricing/scope model, client technical capability, assurance burden, and operator after launch.

**Comparison cases:** fixed versus adaptive commercial model; agency-operated versus client-operated; repeatable internal Django platform versus project-specific stack; high- versus low-client capability.

**Concrete questions:**

- Who chose the foundation, and whose cost/risk did the choice optimize?
- How did uncertainty enter scope, price, acceptance, and change control?
- Which reusable practices reduced effort and which created poor fit?
- When and how were code, credentials, environments, decisions, and knowledge transferred?
- What support/upgrade burden appeared after launch, and who had budget and authority to address it?

**Method:** paired decision-episode reconstruction and handover artifact review. **Sequence:** after the shared role protocol is tested in Study 1.

## Study 6 — Contributor attempts and maintainer capacity

**Priority: 6. Decision informed:** which participation and sustainability problems are distinct, which transitions are real, and which interventions warrant later testing.

**Groups:** people who considered but did not attempt; unsuccessful first attempts; one-time/occasional contributors; recurring reviewers/mentors; non-code contributors; active maintainers; recent quiet leavers; transferred/archived projects; downstream users expecting support.

**Recruitment characteristics:**

- 30–45 contributor interviews across stages/forms, deliberately oversampling failed attempts and re-entry.
- 20–30 maintainer interviews across independent, Django Commons/Jazzband-history/other governance, solo/nominal team, paid/unpaid time, and growth/caretaking/transfer/archive states.
- 8–12 downstream organizational users to compare expectations with actual maintenance capacity.

**Comparison cases:** accepted versus stalled first contributions with similar task types; program-supported versus organic entrants; retained versus deliberately one-off contributors; funded versus unfunded or pre/post funding maintainers; successful versus failed succession.

**Concrete questions:**

- How was a task found and judged tractable? What context, setup, and permission were missing?
- What was the timing and quality of human feedback? Which delays or interactions changed the decision to continue?
- Which contribution forms and levels of commitment were actually desired?
- How are triage, review, release, compatibility, security, support, and governance hours distributed?
- What demand is legitimate, what exceeds scope, and how are boundaries communicated?
- Did money, employer time, co-maintainers, automation, governance transfer, or scope reduction change actual capacity and continuity?
- What made stopping, transferring, or archiving safe or unsafe?

**Method:** journey interviews, live/recorded onboarding and triage contextual inquiry with consent, repository/process data, and 6–12 month follow-up. Avoid GitHub-only measurement. **Sequence:** qualitative mapping before any funnel survey or intervention trial.

## Study 7 — Individual and organizational funding episodes

**Priority: 7. Decision informed:** whether individual reciprocity and organizational dependency stewardship are separate jobs; how funding targets, rights, approval, and accountability affect action and renewal.

**Groups:** first-time and recurring individual donors; aware non-donors; lapsed donors; organizational sponsors/corporate members; materially dependent non-funders; direct package/maintainer funders; employee-time contributors; finance/legal approvers and declined proposal champions.

**Recruitment characteristics:** 18–24 individual interviews split among donor/non-donor/lapsed; 18–26 organizational interviews spanning champion, technical dependency owner, approver, finance/legal where possible. Include anonymous/low-visibility supporters and geographic variety.

**Comparison cases:** donor versus aware non-donor with similar engagement; renewed versus lapsed; dependent funder versus dependent non-funder; unrestricted versus targeted support; cash versus employee time.

**Concrete questions:**

- What triggered the first consideration, and what other ways of reciprocating or managing dependency were considered?
- What target and outcome did the supporter expect, and what rights did they explicitly not expect?
- Who translated technical dependence into a proposal? Which budget, legal, tax, procurement, and reporting steps mattered?
- What evidence supported approval, rejection, or renewal? How did recognition/anonymity affect the relationship?
- Did support change maintenance capacity, continuity, or only perceived association? What counterfactual is credible?

**Method:** decision-episode interviews and redacted proposal/renewal artifact analysis; later survey only after motive/path categories stabilize. **Sequence:** after Studies 1 and 6 clarify organizational dependency and maintainer outcomes.

## Study 8 — Course selection, delivery, and learner outcomes

**Priority: 8. Decision informed:** how institutional approval and educator delivery interact; when Django is object, teaching vehicle, or incidental technology.

**Groups:** K–12 program owners, university course/program leads, bootcamp/training-provider owners, corporate training leads, instructors with high and low autonomy, teaching assistants, learners, and employer/advisory participants.

**Recruitment characteristics:** 12–18 course/program decision episodes with paired institutional and instructor interviews; 6–10 classroom/cohort observations; learner follow-up samples of 6–10 per observed cohort for qualitative variation. Include approved, rejected/deferred, revised, and retired offerings across jurisdictions and program types.

**Comparison cases:** Django-specific versus concepts-first Python web courses; new approval versus routine instructor tool change; high versus low instructor capacity; comparable course completed versus abandoned; framework retained versus replaced.

**Concrete questions:**

- Who controlled program, course, and implementation-technology decisions?
- Which learning outcomes, standards, local demand, enrollment, staffing, lab/support, assessment, and economics were decisive?
- How were Django and web concepts sequenced, and where did instructors intervene most?
- Can learners explain, debug, and extend work under controlled assistance/AI conditions?
- What maintenance burden arises from versions, dependencies, OS, hosting, and assessment integrity?
- Which outcomes are actually measured, over what horizon, and what can be attributed to framework choice?

**Method:** paired episode reconstruction, curriculum/artifact analysis, contextual classroom inquiry, learner task probes, and longitudinal follow-up. **Sequence:** policy interviews first, then observation built around the real course distinctions found.

## Cross-study channel module

Do not run a stand-alone “where do you get information?” study first. Embed a common timeline module in Studies 1–8:

- show the first traceable encounter with the option;
- identify what created a shortlist, not merely awareness;
- show searches/questions/documents used to resolve each uncertainty;
- identify private peer or organizational channels;
- record credibility tests, failed searches, and handoffs;
- connect each channel exposure to the next observable action;
- ask what would have happened without it.

After 40–60 coded episodes, decide whether a survey/data study is warranted to estimate channel patterns by role, lifecycle, language, and geography.

## Sequencing and synthesis gates

1. **Weeks 1–3:** finalize screeners, consent/artifact protocol, taxonomy codebook, and pilot 4–6 Study 1 episodes including at least two reject/no-build cases.
2. **Weeks 3–8:** run Studies 1 and 2; update role/lifecycle categories after a blinded dual-code review.
3. **Weeks 5–10:** begin Study 3 observations; field Studies 4 and 5 using refined episode language.
4. **Weeks 8–14:** run Study 6; use its capacity model to shape funding recruitment for Study 7.
5. **Weeks 10–16:** run Studies 7 and 8; continue selected longitudinal follow-ups.
6. **Gate A:** after roughly 20 diverse decision episodes, test whether saturation is occurring by role/context, not globally. Add targeted cases where negative evidence is absent.
7. **Gate B:** before any prevalence survey, confirm categories are understandable across languages and do not encode Django-community assumptions.
8. **Gate C:** before later audience prioritization, require at least one adopter, rejecter/alternative, incumbent, and former/reconsidering comparison for every high-consequence job claim.

## Analysis and quality controls

- Maintain separate codes for direct participant evidence, contemporaneous artifact, retrospective inference, and researcher synthesis.
- Use negative-case analysis: actively search for episodes contradicting each emerging pattern.
- Code role and consequence before title and organization size.
- Do not treat repeated references to the same public survey as independent triangulation.
- Translate instruments and use local researchers/interpreters where language or institutional context affects meaning; document translation decisions.
- Compensate participants appropriately, protect sensitive organizational details, and avoid extracting unpaid troubleshooting or maintainer labor during research.
- Report ranges and pattern boundaries, not invented rankings or market-size precision.
- Preserve outcomes where Django was rejected, contribution stopped, funding declined, or a course was retired; these may represent successful job completion.

<!-- RESEARCH PROVENANCE: BEGIN -->
## Research provenance

This section was generated from the recorded Codex session JSONL logs. File attribution uses successful patch events; searches and domains use nested web-tool calls.

### Session `019f7578-bbf8-74b1-b98e-f430f5b27ab5`
- Log: `rollout-2026-07-18T15-44-34-019f7578-bbf8-74b1-b98e-f430f5b27ab5.jsonl`
- This document: `add`
- Search queries:
  - None recorded.
- Website domains:
  - None recorded.

<!-- RESEARCH PROVENANCE: END -->
