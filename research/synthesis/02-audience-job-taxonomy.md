# Audience and job taxonomy

## Purpose and unit of analysis

This is a composable taxonomy for recruiting, coding evidence, and comparing decision episodes. It is not a mutually exclusive persona list. The recommended unit is:

> **A person or role, in a specific decision episode, with a readiness level, authority, organization/risk context, Django lifecycle state, and underlying progress job.**

One person can occupy several contexts over time. One organizational decision normally contains several people with different jobs. “Django user,” “startup,” “finance,” and “CTO” are therefore incomplete audience definitions on their own.

## Audience dimensions

### A. Capability/readiness

| Code | Category | Operational boundary |
|---|---|---|
| R0 | First programming steps | Cannot yet independently write/debug a small program or explain basic web request/response |
| R1 | Programming-capable, web-system-new | Can create useful programs, but not independently reason across HTTP, browser/server, persistence, auth, and deployment |
| R2 | Web-capable, Django-new | Understands web systems and can compare foundations, but lacks Django-specific operating knowledge |
| R3 | Django delivery-capable | Can independently build, test, deploy, and diagnose a Django application |
| R4 | Django system steward/expert | Owns upgrades, architecture, incidents, team practices, packages, or consequential decisions |

Readiness is task-specific: a senior data engineer can be R1 for web systems; a strong Django developer can be a novice in governance or teaching.

### B. Decision role

| Code | Role | Question it answers |
|---|---|---|
| D1 | Initiator | Who causes the option or need to be considered? |
| D2 | Researcher/evaluator | Who gathers evidence and tests fit? |
| D3 | Influencer/recommender | Whose judgment shapes the choice without necessarily approving it? |
| D4 | Approver/economic buyer | Who accepts cost and residual risk? |
| D5 | Blocker/reviewer | Who can reject, condition, or delay? |
| D6 | Implementer/operator | Who builds, teaches, deploys, maintains, or supports it? |
| D7 | Consequence bearer | Who bears learning failure, delivery delay, outage, harm, migration, or opportunity cost? |

Code roles per episode, not permanently by title. A founder may hold D1–D7; a large-company CTO may only set principles; a learner may be D6/D7 while an educator chooses the stack.

### C. Organization and delivery context

| Code | Category | Salient variation |
|---|---|---|
| O1 | Independent/personal | Authority compressed; personal time, money, confidence, and maintenance |
| O2 | Coached/formal learning | Teacher/curriculum selects; cohort, assessment, access, and support constraints |
| O3 | One-team product/startup | Scarce attention, runway, customer learning, role compression |
| O4 | Multi-team product organization | Standards, shared platforms, hiring, ownership, coordination |
| O5 | Agency/client delivery system | Split buyer/user/operator, commercial risk, handover and sourcing |
| O6 | Large/institutional system | Formal governance, procurement, assurance, long service life |
| O7 | Open-source/community system | Volunteer/paid mixtures, public governance, diffuse beneficiaries |

These categories can combine: an agency may serve a regulated institution; a university course is O2 inside O6.

### D. Risk and constraint overlay

Use multiple tags: service criticality (low/consequential/critical); personal/data sensitivity; regulatory or accreditation burden; accessibility duty; real-time/async/performance profile; legacy integration; low-bandwidth/device/language/access constraints; and jurisdiction. “Government,” “education,” “media,” “healthcare,” and “finance” are optional sector tags, not motivational segments.

### E. Django lifecycle

| Code | State | Typical transition question |
|---|---|---|
| L0 | Unaware/not considering | What created a relevant need and shortlist? |
| L1 | Considering | Is serious evaluation warranted? |
| L2 | Proving/reviewing | What assumptions and approval conditions must be tested? |
| L3 | Adopting/onboarding | Can people reach safe independent delivery? |
| L4 | Operating/incumbent | Can the next change be made safely? |
| L5 | Upgrading/deepening | Can capability and supportability grow affordably? |
| L6 | Reconsidering | Should the system stay, adapt, decompose, or migrate? |
| L7 | Leaving/coexisting | How can transition preserve service, data, and reversibility? |
| L8 | Former/returning | Do prior reasons still apply to the current context? |

### F. Ecosystem participation

E0 consumer/beneficiary; E1 helper/advocate; E2 first-time contributor; E3 recurring contributor/reviewer/mentor; E4 package or subsystem maintainer; E5 formal project/team/governance participant. Participation is multi-form: code, docs, triage, translation, support, events, security, and governance all count when relevant.

### G. Funding relationship

F0 beneficiary/non-funder; F1 individual recurring or one-off donor; F2 organizational sponsor/corporate member; F3 direct project/maintainer funder; F4 employee-time contributor; F5 grant or in-kind supporter. Record funding target, rights, approver, desired outcome, and accountability expectation separately.

## How to compose an audience/job context

Use a compact expression, then add the progress job:

> **R1 + D1/D2/D6/D7 + O1 + low-consequence + L1:** an independent Python-capable builder evaluating a first web application, trying to turn existing Python skill into a deployable, understandable result.

> **R4 + D2/D3 + O4 + regulated + L6:** a staff engineer evaluating an incumbent Django service under security and integration constraints, trying to recommend upgrade, containment, decomposition, or migration with evidence.

> **R3 teaching capability + D3/D6 + O2/O6 + L2:** an instructor piloting Django inside an approved course, trying to make the sequence teachable and assessable; the curriculum committee remains D4/D5.

> **E4 + F3 candidate + O7:** a package maintainer trying to bound compatibility and obtain sustainable capacity; a dependent company’s engineering champion initiates while finance/legal approve.

This format makes comparison cases explicit and prevents accidental claims that all members of a title, industry, or lifecycle state share one job.

## Mapping the 17 supplied lenses

| # | Supplied lens | Primary taxonomy placement | Necessary correction |
|---:|---|---|---|
| 01 | [First-time programmers](../audiences/01-first-time-programmers.md) | R0; O1/O2; D6/D7, sometimes D1–D4; L0–L3 | Segment by readiness, learning context, goal, and access; not “junior developer” |
| 02 | [Python developers new to web](../audiences/02-python-developers-new-to-web.md) | R1; O1–O4; D1–D3/D6/D7; L1–L3 | Separate Python proficiency, web novelty, outcome type, and career/work intent |
| 03 | [Experienced backend engineers](../audiences/03-experienced-backend-engineers.md) | R2–R4; D2/D3/D6/D7; O3–O6; L1–L8 | Recruit by lifecycle, authority, and workload; experience alone is not a segment |
| 04 | [Full-stack developers](../audiences/04-full-stack-developers.md) | R1–R4; D2/D3/D6; O1–O6; L1–L7 | Responsibility span is a context; record front/back leaning, authority, and operating consequence |
| 05 | [Technical leads/architects](../audiences/05-technical-leads-software-architects.md) | R3–R4; D2–D5/D7; O3–O6; L1–L7 | Keep role; replace title assumptions with actual authority and greenfield/incumbent state |
| 06 | [CTOs/engineering managers](../audiences/06-ctos-engineering-managers.md) | D3–D5/D7, sometimes D1/D2/D6; O3–O6; all lifecycle states | Split hands-on early leader, growth approver, and manager/recommender-steward |
| 07 | [Startup technical decision-makers](../audiences/07-startups-technical-decision-makers.md) | O3 overlay; D1–D7 often compressed; L1–L7 | Treat startup/stage/runway as context; sample no-build and bought-service episodes |
| 08 | [Large-organization stakeholders](../audiences/08-large-organizations-stakeholders.md) | O4/O6 overlay; D1–D7 distributed; L1–L7 | Segment by criticality, governance, sourcing, and installed estate, not headcount |
| 09 | [Industry contexts](../audiences/09-industry-contexts-government-education-media-healthcare-finance.md) | Risk/sector/jurisdiction overlay across O2–O6 and D1–D7 | Convert to overlays or separate sector studies; do not imply one regulated audience |
| 10 | [Agencies/consultancies](../audiences/10-agencies-consultancies.md) | O5; supplier roles D1–D3/D6, client roles D4/D5/D7; L1–L7 | Model the agency-client-operator system and delivery/risk allocation |
| 11 | [Package maintainers](../audiences/11-django-python-package-maintainers.md) | E4/E5; O7; R4 in package domain; often D1–D7 for package | Split governance state, authority, lifecycle, criticality, paid time, and succession |
| 12 | [Individual educators](../audiences/12-individual-educators-instructors-bootcamp-teachers.md) | O2; D3/D6/D7, sometimes D1/D2/D4; R varies by teaching domain | Keep distinct from institution; segment by learner level, cohort, assessment, and autonomy |
| 13 | [Existing Django users](../audiences/13-existing-django-users.md) | L4/L5; R3/R4; D2/D3/D6/D7; O1–O6 | Rename around responsibility; separate tutorial familiarity from production stewardship |
| 14 | [Former Django users](../audiences/14-former-django-users.md) | L6–L8 overlay; any R/O/D | Treat as lifecycle/prior-experience state; distinguish partial coexistence and reason for departure |
| 15 | [Django contributors](../audiences/15-prospective-existing-django-contributors.md) | E2/E3/E5; O7; D1–D7 within contribution | Split stage, contribution form, authority, motive, and payment; first-time is not junior |
| 16 | [Donors/sponsors/corporate members](../audiences/16-donors-sponsors-corporate-members.md) | F1–F5; O1/O3–O7; D1–D5 distributed | Retain separate relationship types; funding target and rights matter more than one “funder” persona |
| 17 | [Institutional curriculum decision-makers](../audiences/17-educational-institutions-training-curriculum-decision-makers.md) | O6/O2; D1–D5/D7; L1–L6 for curriculum technology | Split program type, framework-level authority, learner market, and delivery economics |

## Normalized job taxonomy

Confidence below reflects cross-audience support. Each job must still be coded with its participants and context; the same words can conceal different consequences.

| ID | Job cluster | Normalized progress statement | Common contexts | Participants/roles | Desired outcomes | Confidence |
|---|---|---|---|---|---|---|
| J1 | Produce a bounded useful outcome | When a need is uncertain or capability is unproven, I want a small understandable result, so I can learn, deliver value, or decide the next investment | Learning, prototype, product feature, client engagement | Learner, practitioner, founder, educator, client/user | Working result; observable feedback; independent modification; decision clarity | Medium-High |
| J2 | Acquire an actionable mental model | When the system is unfamiliar, I want to understand its causes, boundaries, and failure modes, so I can act and debug independently | First web work, inherited system, new layer, contribution process | Learner, implementer, operator, contributor, client maintainer | Correct explanation; effective diagnosis; reduced reliance; safe change | High functional |
| J3 | Get unstuck without losing agency | When progress is blocked, I want timely context-appropriate feedback, so I can continue while retaining understanding and ownership | Learning, contribution, maintenance, incidents | Learner, developer, contributor, maintainer, mentor/reviewer | Shorter blocked time; verified resolution; preserved learning; bounded review load | Medium-High |
| J4 | Evaluate fit in the real context | When a consequential option arises, I want evidence against actual requirements and constraints, so I can choose, reject, or defer defensibly | Greenfield, proof, standard, course review, reconsideration | Evaluator, practitioner, architect, educator, domain expert | Critical assumptions tested; explicit criteria; alternatives/no-build considered | High general, Medium Django-specific |
| J5 | Translate evidence into a shared decision | When stakeholders use different languages and bear different consequences, I want an explicit rationale, ownership, cost, and residual-risk record, so approval and accountability are informed | Team, enterprise, agency/client, institution, funding | Recommender, service owner, approver, reviewer, finance/legal | Clear decision rights; accepted conditions; budget/owner; traceable rationale | High functional |
| J6 | Deliver end to end with fewer unnecessary seams | When work crosses interface, server, data, test, and release, I want coherent conventions and interfaces, so I can deliver without avoidable integration effort | Full-stack product, startup, agency | Full-stack developer, team, operator | Lead time; fewer fragile handoffs; traceability; reproducible workflow | Medium-High |
| J7 | Ship and operate safely | When software serves real users, I want secure, observable, reproducible delivery and recovery, so incidents and harm are bounded | Production, regulated/high-assurance, client handover | Developer, operator/SRE, security, service owner | Controlled release; detection; recovery; acceptable security/reliability | High job, variable threshold |
| J8 | Change and upgrade safely | When behavior or dependencies change, I want compatibility and regression evidence, so I can keep delivering without unsupported accumulation | Incumbent systems, courses, packages | Existing user, maintainer, educator, technical lead | Supported versions; bounded upgrade effort; preserved behavior; current materials | High |
| J9 | Resolve workload/architecture uncertainty | When performance, async, data, integration, or interaction requirements become material, I want representative evidence, so I can optimize, isolate, adapt, or reconsider | Architecture proof, scaling, former-user reassessment | Backend engineer, architect, operator, reviewer | Measured critical path; known bottleneck; proportionate architectural response | High existence, Low prevalence |
| J10 | Preserve adaptability and an exit | When product, team, ecosystem, or personal capacity changes, I want reversible boundaries and a bounded transition, so commitment does not become an indefinite trap | Startup growth, estate evolution, agency exit, package wind-down | Leader, architect, practitioner, maintainer, client | Incremental change; data/service continuity; rollback; transfer/archive path | Medium-High |
| J11 | Distribute capability and ownership | When valuable work depends on scarce people, I want knowledge, authority, and capacity distributed, so continuity does not depend on one person | Team growth, handover, teaching, contribution, maintenance | Manager, educator, agency, contributor, maintainer | Faster onboarding; shared ownership; succession; lower key-person risk | Medium-High |
| J12 | Demonstrate/assess credible capability | When capability must be judged, I want evidence of what a person or team can explain, produce, and operate, so decisions do not rely on a copied artifact or title | Learning, hiring, client trust, assessment | Learner, educator, employer, client | Authentic explanation; process evidence; fair assessment; transfer to new task | Medium; Django employment causality Low |
| J13 | Establish legitimate participation and influence | When I want to improve shared infrastructure, I want a tractable contribution, timely human feedback, and legible authority, so effort can become useful participation without overcommitment | OSS contribution/governance | Contributor, reviewer, mentor, governance participant | Accepted outcome; feedback; retention by choice; appropriate voice | Medium-High |
| J14 | Sustain a truthful maintenance contract | When others rely on a package, I want support scope, releases, security, ownership, and capacity to match, so users are not promised more than maintainers can provide | Package/subsystem maintenance | Maintainer, co-maintainer, downstream user, funder | Explicit matrix; bounded queue; response path; succession or archive | High |
| J15 | Convert dependence/appreciation into capacity | When shared infrastructure creates value, I want an affordable accountable support relationship, so continuity improves without requiring me to do all the work or purchasing technical control | Individual/company funding, employee time | Champion, donor, engineering owner, finance/legal, recipient | Approved resource; clear target; accountable use; rights boundary; renewal decision | High functional, Medium causal path |
| J16 | Deliver instruction repeatably | When a varied cohort must learn under constraints, I want a teachable, current progression with observable understanding, so learners can complete, explain, and extend work | Workshop, school, university, bootcamp | Educator, TA, curriculum owner, learner | Completion plus comprehension; timely intervention; fair assessment; runnable environment | High general, Medium Django-specific |
| J17 | Keep a program viable and credible | When a curriculum portfolio is reviewed, I want learning outcomes, demand, capacity, standards, and economics aligned, so the program remains current, deliverable, and trustworthy | Institution/training provider | Program lead, instructor, academic board, employer adviser, finance, learner | Approved curriculum; qualified staff; viable enrollment/cost; outcome evidence | High functional |

## Coding rules

1. Code the underlying progress, not a Django-desired action. “Learn Django,” “adopt Django,” “contribute,” and “donate” are possible behaviors, not jobs.
2. Preserve negative outcomes: rejection, no-build, buying a service, leaving, declining a contribution, or archiving may satisfy the job.
3. Record functional evidence separately from inferred emotional/social jobs. Do not promote reputation, belonging, confidence, or fear to universal drivers without direct evidence.
4. Distinguish a recurring operating job from an event trigger. An upgrade deadline can trigger J8; supportability is the continuing outcome.
5. Record whose outcome is optimized and who bears trade-offs. An agency’s margin, a client’s ownership, an operator’s on-call burden, and an end user’s continuity are not interchangeable.
6. Use High/Medium/Low with a reason. A repeated cross-report pattern based on the same self-selected survey is not independent triangulation.

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
