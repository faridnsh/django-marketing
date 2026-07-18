# Cross-audience evidence gaps

## Overall assessment

The evidence is sufficient to define plausible jobs and a better research taxonomy. It is not sufficient to estimate audience size, rank audiences, infer causal adoption drivers, or claim that a channel changes behavior. The recurring biases are:

- **Survivorship/incumbency:** Django surveys and community channels disproportionately observe people who adopted, remained, or participate publicly.
- **Self-selection:** technology surveys, maintainer surveys, events, forums, and program follow-ups attract engaged respondents and people with strong experiences.
- **Public-account bias:** published production stories and migrations favor unusual scale, successful resolution, organizational permission to publish, and strong opinions.
- **Geography/language:** evidence is predominantly English-language, with Europe and North America prominent; local labor markets, giving norms, regulation, access, and community pathways differ.
- **Role attribution:** titles and single-respondent reports rarely show who initiated, evaluated, vetoed, approved, implemented, and bore consequences.
- **Weak causality:** most evidence is cross-sectional behavior, stated preference, guidance, or retrospective narrative; it cannot establish what caused adoption, retention, learning, contribution, or funding.
- **Channel ambiguity:** sources show that people use documentation, search, peers, forums, video, events, and social media, but rarely identify each channel’s behavioral role or counterfactual effect.

## Strength and bias by supplied audience lens

| Lens | What is comparatively strong | Principal weakness/bias | Confidence in current job definition | Most consequential missing evidence |
|---|---|---|---|---|
| [01 First-time programmers](../audiences/01-first-time-programmers.md) | General learner motives, pedagogy, beginner debugging; coached Django feasibility | Mixed-experience surveys; higher-education/workshop selection; little independent or access-constrained Django observation | Medium-High functional | Comparative pathway completion, comprehension, independent modification, and continuation by readiness/access |
| [02 Python developers new to web](../audiences/02-python-developers-new-to-web.md) | Boundary between Python and web knowledge; general learning behavior; deployment as visible transition | No clean population data; forum anecdotes; career and task builders pooled | High functional, Medium wording | Observed first-project journeys by missing web concepts, desired artifact, and structured/self-directed context |
| [03 Experienced backend engineers](../audiences/03-experienced-backend-engineers.md) | General software-selection method and realistic-context evaluation | Little direct Django rejecter evidence; seniority/title do not reveal authority; public production cases atypical | High general job | Recent matched evaluations, including eliminated criteria, proof results, no-build/buy, and post-decision outcomes |
| [04 Full-stack developers](../audiences/04-full-stack-developers.md) | Current engaged-user technology combinations and end-to-end work | Role/use-case denominator mismatch; official-channel incumbency; little front-end-leaning rejecter evidence | Medium-High | Real cross-layer decision episodes, seam costs, and interaction-model mismatches |
| [05 Technical leads/architects](../audiences/05-technical-leads-software-architects.md) | Architecture decision, prototyping, assurance, lifecycle guidance | Public-sector/large-tech skew; sparse small-firm and failed-selection evidence; title/authority ambiguity | High functional | Multi-role reconstructions of greenfield and estate decisions with actual vetoes and accepted residual risk |
| [06 CTOs/engineering managers](../audiences/06-ctos-engineering-managers.md) | General organizational selection and management/accountability concepts | Combined titles; no published Django role cross-tabs; little direct executive/manager motivation | High shared job, Low group incidence | Authority by stage; translation from technical evidence to budget/staffing decision; rejecter episodes |
| [07 Startup technical decision-makers](../audiences/07-startups-technical-decision-makers.md) | Lean learning, scarce-resource and stage-transition logic; practitioner accounts | Success-story and survivor bias; “startup” variance; teams that bought or never built are missing | High functional | Matched recent build/adopt/buy/no-build/rewrite choices across stage and assurance burden |
| [08 Large-organization stakeholders](../audiences/08-large-organizations-stakeholders.md) | Authoritative assurance, security, procurement, lifecycle, OSS-risk practices | Prescriptive guidance does not reveal actual behavior; organization-visible successes; committee roles inferred | High functional, Medium role allocation | Decision records plus interviews across evaluator, reviewer, approver, operator, and affected service owner |
| [09 Industry contexts](../audiences/09-industry-contexts-government-education-media-healthcare-finance.md) | Duties and controls from authoritative sources, especially government/finance | Uneven sectors; jurisdiction-specific rules; prescriptions richer than discovery/rejection/emotion evidence | High as overlay, Low as one audience | Sector- and jurisdiction-specific episodes showing which duties actually change framework criteria |
| [10 Agencies/consultancies](../audiences/10-agencies-consultancies.md) | Commercial delivery, collaboration, knowledge-transfer, sourcing risks | Supplier-authored and UK/North American public-sector skew; thin client/post-handover views | High functional | Paired supplier-client-operator studies, including failed fixed bids, replaced suppliers, and handover outcomes |
| [11 Package maintainers](../audiences/11-django-python-package-maintainers.md) | Maintainer burden, compatibility, governance transfer, sustainability mechanisms | Active-maintainer survivor bias; broad OSS surveys; demographic concentration; criticality metrics weak | High | Quiet leavers, abandoned/transfer cases, actual labor allocation, downstream expectations, and funding effects |
| [12 Individual educators](../audiences/12-individual-educators-instructors-bootcamp-teachers.md) | General CS pedagogy, assessment, teacher knowledge, deployed curriculum examples | Intro-programming and US K–12 overrepresentation; limited Django comparative outcomes | High general, Medium Django-specific | Classroom observation and matched course outcomes by readiness, format, assessment, instructor autonomy, and AI use |
| [13 Existing Django users](../audiences/13-existing-django-users.md) | Engaged-user stack, upgrade patterns, public production/upgrade accounts | Official-channel survivor bias; silent legacy estates absent; scale stories atypical; English/geographic skew | High job existence, Low prevalence | Representative operating burden, upgrade debt, inherited systems, unsupported estates, and non-community-visible users |
| [14 Former Django users](../audiences/14-former-django-users.md) | Detailed public migration/return mechanisms | Strong-opinion and notable-migration selection; framework confounded with product/team/architecture changes; quiet leavers missing | High reassessment job, Low causal prevalence | Contemporaneous before/after evidence from quiet leavers, partial users, non-returners, and matched stayers |
| [15 Contributors](../audiences/15-prospective-existing-django-contributors.md) | Governance/process facts; newcomer-barrier research; some program follow-up | Selected program participants; GitHub undercounts other work; unsuccessful attempts and occasional contributors thin | Medium-High | Attempt-level funnel across contribution forms, feedback latency/quality, drop-off, re-entry, and paid-time effects |
| [16 Donors/sponsors/corporate members](../audiences/16-donors-sponsors-corporate-members.md) | OSS funding motivations, DSF relationship facts, organizational funding reality | US giving evidence; public supporters; non-donors/lapsed donors and internal corporate approval sparse | High functional, Medium motivation | First-gift, non-gift, renewal, lapse, and corporate proposal episodes; target/rights/accountability expectations |
| [17 Institutional curriculum decision-makers](../audiences/17-educational-institutions-training-curriculum-decision-makers.md) | Policies, accreditation, curricula, program and training-market practices | Heterogeneous institutions; open curriculum feasibility confused with demand; local labor data absent | High functional | Real approval/rejection/retirement episodes, delegated authority, capacity/economic data, and learner outcomes |

## Strength and bias by normalized job cluster

| Job cluster | Current evidence | Confidence | Main uncertainty |
|---|---|---|---|
| Bounded useful outcome / learning loop | Repeated across learner, startup, delivery, and education sources | Medium-High | Which outcome and feedback actually cause continued progress versus merely correlate with engaged samples |
| Actionable mental model / independent effectiveness | Strong general learning and developer-experience support; qualitative Django signals | High functional | Readiness thresholds, transfer to a second task, and the role of human versus AI help |
| Fit-for-context evaluation | Strong general software-selection and official assurance guidance | High general, Medium Django-specific | Actual elimination criteria, evidence thresholds, and authority in Django decisions |
| Shared organizational decision | Strong prescriptive role logic; weak multi-party episode evidence | Medium-High | How evidence is translated, distorted, vetoed, funded, and accepted across roles |
| End-to-end delivery / reduced seams | Strong incumbent use signals; contextual architectural evidence | Medium-High | Counterfactual integration costs and which interaction/workload contexts reverse the benefit |
| Safe production, operation, and recovery | Strong general necessity and public cases | High existence | Typical burden, accepted threshold, and causal framework contribution versus team/platform practice |
| Change, upgrade, and supportability | Direct incumbent and maintainer behavior; release/support facts | High existence | Distribution of effort, silent deferral, forced migration, and package-stack contribution |
| Adaptability / bounded exit | Repeated migration, startup, architecture, and maintainer logic | Medium-High | Typical cost and causal benefit of particular boundaries; quiet stay/leave comparisons |
| Capability and ownership distribution | General management, education, OSS, and handover evidence | Medium-High | Which intervention—training, hiring, documentation, governance, funding—relieves which bottleneck |
| Credible capability assessment | Good general pedagogy; weak Django-to-employment evidence | Medium | What employers/clients actually infer and whether portfolio/course outcomes transfer |
| Contribution legitimacy and retention | Process facts and broad OSS/newcomer research | Medium-High | Natural newcomer funnel, non-code work, unsuccessful attempts, feedback causality, and desired bounded participation |
| Maintainer sustainability | Strong burden and governance-mechanism evidence | High job, Medium intervention effects | Whether money, co-maintainers, tooling, scope reduction, recognition, or governance transfer changes continuity |
| Funding shared infrastructure | Strong existence/motive categories, weak Django decision episodes | High job, Medium pathway | What dependence converts to action, who champions/approves, and what produces renewal |
| Teachable, viable curriculum | Strong general institutional and pedagogy evidence | High job, Medium Django fit | Comparative learning, local demand, delivery cost, and framework specificity decisions |

## Missing rejecter, non-adopter, and former-user evidence

The most important missing comparison is not “people who dislike Django.” It is people who encountered a relevant job and chose a different path:

- Django was eliminated before a proof, failed a representative proof, or lost during organizational review.
- The team bought a product/service, used an internal platform, postponed the work, or chose not to build.
- A learner abandoned web development, changed course, or completed a tutorial without independent capability.
- An incumbent retained Django despite dissatisfaction because switching cost dominated.
- A former user quietly changed employer, workload, or architecture and never published a migration story.
- A prospective contributor attempted to start but received no usable task or feedback.
- A dependent organization did not fund, or a previous funder did not renew.
- A curriculum committee rejected, deferred, diluted, or retired Django-related content.

Without these cases, “pulls” are easily inferred from survivors, and observed current behavior is mistaken for selection causality.

## Role-attribution problems

Single-person surveys and public accounts commonly collapse the decision system. Future evidence must separately identify:

1. the triggering need and initiator;
2. who constructed the shortlist and proof;
3. domain, user, operations, security, privacy, legal, procurement, finance, and educator influences;
4. who could veto or impose conditions;
5. who approved money and residual risk;
6. who implemented, operated, taught, or maintained;
7. who experienced harm, burden, delay, or switching cost;
8. whose judgment was retrospectively credited for the outcome.

This is especially important for “CTO,” “architect,” “decision-maker,” “institution,” “agency,” and “company sponsor” claims. Titles should be metadata, not authority codes.

## Channel-behavior gaps

The reports collectively mention documentation and release notes, search, technical Q&A, forums/Discord, GitHub/issue trackers, mailing lists, peers and professional networks, courses/video, conferences/sprints, podcasts, and short-form social. The evidence rarely distinguishes:

- **Discovery:** first awareness of a relevant option, not passive exposure.
- **Evaluation:** development of a shortlist or criteria.
- **Validation:** evidence that reduced a material uncertainty or satisfied another stakeholder.
- **Approval:** evidence carried into a formal or informal decision.
- **Ongoing engagement:** operating, upgrading, teaching, contributing, funding, or re-entry.

Missing are event-level sequences, failed searches, cross-channel handoffs, credibility judgments, private peer conversations, language/access differences, and behavioral outcomes. Self-reported “used this resource” cannot establish that the resource caused a decision. Channel questions should be tied to a dated episode and verified with histories/artifacts where consent permits.

## Weak causal evidence

Current sources cannot establish that Django’s integrated capabilities caused delivery speed, that community contact caused belonging or retention, that a portfolio caused employment, that contribution programs caused long-term participation, that funding caused maintenance continuity, or that a framework caused a migration outcome independent of architecture, staffing, scope, and product changes. Plausible mechanisms should remain hypotheses.

Stronger designs include matched comparison cases, within-person before/after tasks, longitudinal follow-up, interrupted time series for upgrades or funding where data exist, and decision-episode reconstruction with contemporaneous artifacts. Randomization is practical only for bounded learning/help/interface questions; it is rarely ethical or feasible for consequential framework choices.

## Which method can resolve which gap

| Method | Best-resolved gaps | Cannot resolve alone |
|---|---|---|
| Desk research | Release/support facts; governance and legal rules; public decision records; curricula; labor-market definitions; documented migrations; regional ecosystem mapping | Private motives, unseen rejecters, causal behavior, true authority |
| Survey/data analysis | Incidence of roles/states; distributions of burden; version/upgrade patterns; awareness-to-attempt funnels; geographic/language differences; recruitment screen | Deep causal explanation; exact decision sequence; rare complex episodes without oversampling |
| Interviews | Underlying jobs, anxieties, criteria, language, hidden alternatives, perceived turning points, internal approval and funding logic | Recall bias, actual behavior, prevalence, detailed moment-to-moment failure |
| Contextual inquiry/observation | Beginner setup/debugging; evaluator proof work; educator intervention; contributor onboarding/review; maintainer triage/release; handover practice | Long lifecycle outcomes unless followed longitudinally; sensitive executive/procurement episodes can be hard to observe |
| Decision-episode reconstruction | Role map, trigger, shortlist, evidence, channel sequence, veto/approval, trade-offs, and consequence attribution using artifacts | Population size; long-term causality if only successful episodes are sampled |
| Longitudinal follow-up | Persistence, independent transfer, upgrade outcomes, contribution retention/re-entry, funding renewal, migration consequences | Rapid answers; attribution without comparison cases |

## Prioritized gap list

1. **Recent matched Django decision episodes**: adopted, rejected, no-build/buy, retained, and migrated cases, with multiple roles where possible. High uncertainty and high consequence.
2. **Quiet former users and silent incumbents**: correct the strongest survivorship bias and causal overreading of public migrations.
3. **Beginner/Python-to-web observed pathways**: establish readiness, transfer, deployment cliffs, AI/help behavior, and access constraints.
4. **Contributor-attempt and maintainer-capacity evidence**: include unsuccessful attempts, quiet leavers, non-code work, labor, ownership, and intervention effects.
5. **Funding episodes**: compare donors/non-donors and renewals/lapses; map organizational champion, approval, target, rights, and accountability.
6. **Paired educator/institution course decisions and observed delivery**: connect approval logic to actual comprehension, assessment, capacity, and outcomes.
7. **Channel sequences by lifecycle and role**: only after the episodes above supply concrete events to trace.

These priorities use uncertainty × likely consequence; they do not imply future audience or marketing priority.
