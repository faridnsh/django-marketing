# Prioritized segmentation changes

## Decision rule

Priority reflects the risk that the current label will recruit the wrong people, combine incompatible jobs, or misattribute authority—not audience value. These changes guide future research only. They do not determine audience priority, positioning, or execution.

## Prioritized changes

### 1. Replace the flat persona list with a multidimensional coding model

**Action:** Convert every lens into a composition of readiness, decision role, organization/delivery context, risk overlay, Django lifecycle, ecosystem participation, and funding relationship. Retain the original 17 labels only as source-report indexes.

**Evidence:** Nearly every report identifies overlap and title/context ambiguity; one person can be implementer, evaluator, approver, and consequence bearer, while one organizational choice distributes those roles ([technical leads](../audiences/05-technical-leads-software-architects.md), [large organizations](../audiences/08-large-organizations-stakeholders.md)). **Implication for research:** screen and code recent episodes on all dimensions; do not quota only by label. **Confidence:** High. **Validate:** whether these dimensions explain materially different decision behavior in pilot coding and whether any omitted dimension repeatedly predicts variation.

### 2. Split “CTOs and engineering managers”

**Action:** Create at least three recruitment groups: hands-on early technical leader; growth/multi-team economic or risk approver; engineering manager/recommender-steward without framework authority.

**Evidence:** Founder-CTOs may hold all decision roles; managers often optimize team delivery without final stack authority; large-company executives may set principles but not evaluate Django ([06](../audiences/06-ctos-engineering-managers.md)). **Implication:** compare who initiates, evaluates, approves, and bears consequences rather than treating title as authority. **Confidence:** High that the jobs differ; Low on group incidence. **Validate:** actual decision rights, lifecycle triggers, and evidence used by company stage and governance model.

### 3. Convert “industry contexts” into risk, duty, and jurisdiction overlays

**Action:** Do not retain government, education, media, healthcare, and finance as one audience. Tag sector, service criticality, affected population, regulatory/accreditation duty, data sensitivity, accessibility, resilience, jurisdiction, and sourcing separately. Run sector-specific studies only where the duty genuinely changes the job.

**Evidence:** The five sectors have different duties, and within-sector variance can exceed between-sector variance; media evidence is unlike finance resilience regulation ([09](../audiences/09-industry-contexts-government-education-media-healthcare-finance.md)). **Implication:** recruit roles inside decision episodes and use risk/duty to select comparison cases. **Confidence:** High. **Validate:** which overlays actually change elimination criteria, review sequence, and acceptable evidence.

### 4. Rename and split “first-time programmers” by readiness and learning control

**Action:** Rename to “people seeking a first programming mastery experience,” then screen for no-code/basic-syntax/small-program independence; independent, formal, workplace, or coached context; artifact/curiosity/task/career goal; and access constraints.

**Evidence:** A minor in class, an adult hobbyist, and a displaced worker share low readiness but not authority, time, risk, or desired outcome. Django is plausible as a scaffolded first-project context, not well established as a standalone first abstraction ([01](../audiences/01-first-time-programmers.md)). **Implication:** compare pathways and observed sessions; do not call all early-career developers beginners. **Confidence:** High conceptually. **Validate:** readiness thresholds that predict comprehension, independent modification, and continuation.

### 5. Rename “Python developers new to web” and split web novelty

**Action:** Use “Python-capable, web-system-new builders.” Record Python independence, knowledge of HTTP/browser/client-server/data/auth/deployment, desired outcome (site/API/internal tool), work versus career intent, and structured versus self-directed context.

**Evidence:** Python tenure does not determine web-system knowledge, and “beginner friendly” can mean opposing things: fewer abstractions or more integrated capabilities ([02](../audiences/02-python-developers-new-to-web.md)). **Implication:** recruit by the missing mental model and real intended artifact, not “years of Python.” **Confidence:** High on the boundary, Medium on best subgroups. **Validate:** which knowledge gaps cause abandonment or unsafe deployment and which support produces transfer.

### 6. Merge the decision-work core of engineers, architects, leaders, and organizational stakeholders

**Action:** Create one cross-role “consequential foundation decision” research program spanning reports 03, 05, 06, 08, and the assurance portions of 09. Preserve practitioner, evaluator, recommender, approver, reviewer, operator, and consequence-bearer strata.

**Evidence:** All seek contextual evidence for a defensible commitment, but with different criteria and authority ([03](../audiences/03-experienced-backend-engineers.md), [05](../audiences/05-technical-leads-software-architects.md), [06](../audiences/06-ctos-engineering-managers.md), [08](../audiences/08-large-organizations-stakeholders.md), [09](../audiences/09-industry-contexts-government-education-media-healthcare-finance.md)). **Implication:** reconstruct the same episode from multiple roles instead of conducting disconnected title studies. **Confidence:** High for shared core; Medium for feasible multi-party recruitment. **Validate:** evidence translation, conflicts, vetoes, and which role’s criteria actually determine outcomes.

### 7. Treat startup as a stage/resource context, not an anthropomorphic audience

**Action:** Retain “startup” only as an overlay. Recruit founder-CTO, first engineer, non-technical founder/budget approver, growth leader, and customer/security reviewer separately; stratify by product stage, customer assurance, technicality, runway, incumbent status, and no-build/buy option.

**Evidence:** Headcount and funding round weakly proxy governance and consequence; roles can be compressed or separated ([07](../audiences/07-startups-technical-decision-makers.md)). **Implication:** sample decision episodes including teams that bought, postponed, or did not build. **Confidence:** High. **Validate:** when learning-loop speed gives way to staffing, assurance, and estate-stewardship jobs.

### 8. Treat large organization as governance/interdependence context

**Action:** Retain as a sampling context, not a persona. Segment by service criticality, governance centralization, platform maturity, installed-estate depth, sourcing model, internal expertise, and team interdependence rather than headcount.

**Evidence:** A large technology firm may grant more autonomy than a smaller regulated organization; one organization contains both tightly governed and low-risk systems ([08](../audiences/08-large-organizations-stakeholders.md)). **Implication:** sample specific decisions and map the committee/exception path. **Confidence:** High. **Validate:** which governance configurations add distinct blockers or reusable approval evidence.

### 9. Rename “existing Django users” around responsibility

**Action:** Use “people responsible for changing or operating an existing Django system.” Split tutorial/project familiarity, delivery-capable users, inherited-system maintainers, production operators, technical guides, and estate stewards. Tag support status, criticality, workload, team topology, and upgrade debt.

**Evidence:** “Existing” ranges from one tutorial to a decade of critical-service responsibility; elapsed time and version alone are misleading ([13](../audiences/13-existing-django-users.md)). **Implication:** recruit by recurring responsibility and consequence. **Confidence:** High. **Validate:** distribution of operating jobs, silent legacy estates, upgrade triggers, and progression into teaching/contribution.

### 10. Convert “former Django user” to lifecycle/prior-experience state

**Action:** Tag full departure, no-new-project use, partial coexistence, maintained legacy, active migration, and return. Study former users under their current role and workload unless prior experience materially shapes the episode.

**Evidence:** Departure is confounded with architecture, employer, product, language, database, frontend, and time; public postmortems overrepresent notable migrations and strong opinions ([14](../audiences/14-former-django-users.md)). **Implication:** recruit quiet leavers and reconstruct before/after decisions with contemporaneous artifacts. **Confidence:** High structural, Low on prevalence/causes. **Validate:** which prior pains persist, which were contextual, and what triggers return without assuming return is preferred.

### 11. Keep individual educators separate from institutional curriculum decision-makers

**Action:** Retain both lenses, explicitly link them. Split individual educators by learner readiness, cohort/format, assessment stakes, instructor autonomy, and whether Django is object, vehicle, or incidental infrastructure. Split institutions by program type, approval level, market, capacity, and economics.

**Evidence:** Teachers need teachability, observation, intervention, and current runnable environments; institutions balance portfolio, standards, demand, delivery capacity, and finance. Framework teacher and selector may be different people ([12](../audiences/12-individual-educators-instructors-bootcamp-teachers.md), [17](../audiences/17-educational-institutions-training-curriculum-decision-makers.md)). **Implication:** pair instructor and program-owner interviews around the same course decision. **Confidence:** High. **Validate:** delegated authority, actual outcome measures, and differences among K–12, degree, bootcamp, marketplace, and corporate training.

### 12. Retain agency/client delivery as a decision system, not one audience

**Action:** Rename to “agency-client-operator delivery systems.” Code supplier business model, client skill, procurement/assurance, scope/pricing model, post-launch operator, risk allocation, and handover plan. Keep agency owner, technical lead, consultant, client sponsor, reviewer, and future maintainer separate.

**Evidence:** The primary job couples client value, supportability, commercial uncertainty, and ownership; supplier-authored evidence and public-sector procurement are overrepresented ([10](../audiences/10-agencies-consultancies.md)). **Implication:** recruit both sides, including failed fixed bids, replaced suppliers, and post-handover operators. **Confidence:** High functional, Medium on subgroup boundaries. **Validate:** how framework choice interacts with reuse, margin, client control, and long-term support.

### 13. Retain package maintainers but split governance, authority, and lifecycle

**Action:** Keep as a distinct stewardship lens. Split creator/release owner/triager/security contact/community lead; independent/Jazzband/Django Commons/other governance; growth/caretaking/security-only/transfer/archive; paid time; team reality; and downstream criticality.

**Evidence:** Nominal maintainer teams can retain a single failure point; download counts do not measure burden or criticality; active-maintainer surveys omit quiet leavers ([11](../audiences/11-django-python-package-maintainers.md)). **Implication:** oversample solo critical maintainers, recent leavers, transfers, and failed succession. **Confidence:** High. **Validate:** burden distribution, compatibility choices, effective help, funding-to-capacity mechanisms, and safe exit conditions.

### 14. Retain contributors, but replace the linear “prospective to existing” funnel

**Action:** Segment by contribution stage, form, motive, authority, payment, and desired commitment. Allow one-off contribution, re-entry, review/mentoring, formal team, and governance as distinct outcomes rather than a mandatory ladder.

**Evidence:** Contribution includes docs, triage, translation, support, code, review, organizing, and governance; first-time does not mean junior and occasional does not mean failed retention ([15](../audiences/15-prospective-existing-django-contributors.md)). **Implication:** sample unsuccessful attempts and people who deliberately stop after a bounded contribution. **Confidence:** High conceptual, Medium on transition mechanisms. **Validate:** task matching, feedback timing, legitimacy, mentor dependence, paid time, and re-entry.

### 15. Split donors, sponsors, corporate members, and contribution of employee time

**Action:** Retain funding relationship as a dimension with separate individual donor, organizational sponsor/member, direct maintainer/project funder, grant/in-kind supporter, and employee-time contributor categories. Record target, motivation, approver, rights, recognition preference, and accountability.

**Evidence:** User is not automatically funder; corporate motivations coexist; unrestricted DSF support, Fellow support, package funding, events, and in-kind help solve different jobs. DSF individual membership is contribution recognition, not a donation tier ([16](../audiences/16-donors-sponsors-corporate-members.md)). **Implication:** reconstruct first-gift and renewal/non-renewal episodes separately for individuals and organizations. **Confidence:** High structural, Medium on causal motives. **Validate:** internal champion/approval path, measurable desired outcomes, anonymity/recognition preferences, and what actually drives renewal.

### 16. Retain full-stack as responsibility-span tag; keep it distinct from backend depth

**Action:** Code “full-stack” as cross-layer responsibility, with front/back leaning, interaction complexity, operating responsibility, and decision authority. Do not equate a self-reported role with Django’s “full-stack use” survey response.

**Evidence:** Solo owners and specialist-team developers share a title but not breadth or consequence; full-stack and backend engineers overlap without becoming the same lens ([04](../audiences/04-full-stack-developers.md)). **Implication:** recruit around real end-to-end tasks and seams. **Confidence:** High measurement caution, Medium taxonomy. **Validate:** which integration seams and operating jobs distinguish behavior after controlling for experience.

## What not to infer yet

These changes do not establish segment size, value, reachability, adoption propensity, or priority. They also do not show that any audience wants the same evidence in the same form. Those questions require the matched decision-episode, observational, survey, and longitudinal work specified in [the primary-research plan](05-primary-research-plan.md).

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
