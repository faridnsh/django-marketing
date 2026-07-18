# Engineering leaders accountable for technology fit and team delivery

## Audience definition and boundaries

This audience comprises people accountable for turning engineering choices into business and team outcomes: hands-on founder-CTOs, later-stage CTOs or VPs of Engineering, directors, and engineering managers or team leads. The shared characteristic is **organizational accountability**, not title or coding seniority.

The label conceals major differences. A founder-CTO may research, choose, implement, fund, and operate the stack alone. A manager in a larger company may control staffing and delivery but not framework approval; a large-company CTO may set principles yet never evaluate Django. In the 2025 Django survey, 16% selected Team Lead, 15% Architect, and 13% CTO/CIO/CEO, but roles were multi-select, no role cross-tabs are published, and recruitment ran through Django channels ([Django Developers Survey 2025](https://lp.jetbrains.com/django-developer-survey-2025/), fielded November 2024–January 2025). **Direct evidence about respondents; Medium confidence that these roles matter, Low confidence about incidence or authority.**

Backend engineers acting only as implementers/evaluators, procurement staff, and executives without engineering responsibility are excluded as primary members but remain in the decision system. Company size, stage, regulation, and incumbent/new status are contexts, not interchangeable audience labels.

## Important subsegments

- **Pre-product-market-fit founder-CTO or technical co-founder:** usually hands-on, runway-constrained, and close to customer discovery. Stack choice is often bundled with product feasibility, first hiring, cloud, and delivery decisions. A practitioner stage account describes the CTO choosing architecture and stack while coding the MVP, then shifting toward stabilization, hiring, and management after product-market fit ([Antler interview with startup CTO Chris Brooke](https://www.antler.co/blog/how-cto-role-evolves-as-startup-grows), 5 September 2019). **Direct qualitative account; Medium-Low confidence beyond startups.**
- **Growth-stage CTO, VP Engineering, or Head of Engineering:** delegates more investigation while remaining accountable for delivery, architecture, hiring, due diligence, and evolution.
- **Engineering manager or team lead:** optimizes team delivery, learning, ownership, and operating load. They may recommend or veto locally while approval sits elsewhere. Microsoft’s study found that enabling the team, rather than technical skill alone, characterized great managers; it is one large-company case, not framework-selection research ([Kalliamvakou et al.](https://www.microsoft.com/en-us/research/publication/what-makes-a-great-manager-of-software-engineers/), 2018). **Direct general evidence; Medium confidence.**
- **Multi-team director or platform/architecture sponsor:** balances team autonomy with interoperability, shared tooling, and risk. Two Ericsson cases found authority shared among teams, managers, supporting roles, and technical communities; allocation varied ([Moe, Šmite, Paasivaara & Lassenius](https://link.springer.com/article/10.1007/s10664-021-09967-3), 2021). **Direct case evidence; Medium confidence.**
- **Leader inheriting or already dependent on Django:** the immediate job is usually safe stewardship—delivery, upgrades, staffing, reliability, and risk reduction—not a greenfield framework choice.
- **Regulated or high-assurance leader:** security, privacy, evidence retention, software-supply-chain controls, support windows, and reviewer approval are potential showstoppers. These concerns can appear at any size but usually add stakeholders and documentation.

Do not rank these subsegments. Company size poorly proxies decision rights: the Django survey spans solo companies to organizations over 5,000 people, while 59% report teams of 2–7.

## Primary job to be done

> When a product or team needs a backend foundation, or its current foundation is being challenged, I want team-backed evidence that the choice fits our product, people, operating, and lifecycle constraints, so I can enable useful delivery now without committing the organization to unacceptable risk or cost later.

This is a **researcher inference with High confidence**. A peer-reviewed, industry-co-designed software-selection model begins with the need and usage environment, considers business, organizational, technical, ecosystem, integration, lifecycle, quality, and cost factors, and ends with stakeholder impact analysis ([Bjarnason, Åberg & Ali](https://link.springer.com/article/10.1007/s10664-023-10288-w), 28 February 2023). The exact wording and trade-off between “now” and “later” require direct interviews with Django adopters and rejecters.

## Additional jobs to be done

There are six important jobs in total, including the primary job.

1. **Choose or reconfirm a fitting foundation (primary).** When a product or review creates a consequential choice, I want evidence against real constraints, so I can commit resources defensibly.
2. **Translate a technical choice into an organizational case.** When stakeholders need justification, I want to connect delivery, reliability, staffing, lifecycle, and switching implications to business outcomes, so I can make the decision understandable and fundable. **Inference; High confidence.**
3. **Give the team productive autonomy within safe boundaries.** When engineers will live with the choice, I want conventions and decision rights that reduce repeated work without suppressing necessary judgment, so I can enable teams to deliver and own the system. **Direct general evidence; Medium confidence.**
4. **Keep production responsibility manageable.** When advisories, incidents, upgrades, compliance, and dependencies recur, I want clear ownership and an affordable cadence, so I can help the team avoid emergency work and unsupported software. **Direct context, inferred job; High confidence.**
5. **Preserve adaptability and an exit path.** When product, scale, regulation, or organization changes, I want boundaries and transferable knowledge, so I can enable incremental evolution without a business-threatening rewrite. **Inference; Medium-High confidence**, supported by DoorDash and Sentry.
6. **Sustain delivery capability.** When choosing or retaining a stack, I want to understand learning, hiring, onboarding, satisfaction, and key-person risk, so I can keep delivery from depending on a few specialists. **Direct general criterion; Medium confidence.** Developer availability and documentation appear in a seven-company study ([Farshidi, Jansen & Deldar](https://dspace.library.uu.nl/handle/1874/420503), 2021).

## Functional, emotional, and social dimensions

| Job | Core functional job | Emotional job | Social job | Supporting jobs |
|---|---|---|---|---|
| Choose or reconfirm a foundation | Match product, team, risk, and lifecycle constraints to an implementable foundation | **Hypothesis:** reduce anxiety about a costly, hard-to-reverse commitment | Be seen as evidence-led rather than fashion- or familiarity-led (**hypothesis**) | Elicit requirements; delegate research; prototype; model cost; record assumptions and exit conditions |
| Build an organizational case | Express technical trade-offs as delivery, risk, and investment consequences | Feel confident requesting budget or defending a choice (**hypothesis**) | Maintain credibility with executives, engineers, customers, or investors (**inference**) | Quantify directional outcomes; expose uncertainty; identify consequence bearers; obtain review |
| Enable productive autonomy | Establish useful defaults and boundaries without creating bottlenecks | Reduce frustration from repeated coordination and unnecessary approval (**hypothesis**) | Be regarded as a leader who enables rather than micromanages (**hypothesis**) | Consult teams; define decision rights; standardize shared concerns; support exceptions |
| Manage production responsibility | Maintain, patch, upgrade, observe, recover, and comply | Reduce fear of incidents, audit failure, and unsustainable on-call load (**hypothesis**) | Demonstrate responsible stewardship to staff and stakeholders (**hypothesis**) | Assign ownership; plan releases; review dependencies; test recovery; budget maintenance |
| Preserve adaptability | Evolve system boundaries and replace parts when assumptions change | Avoid feeling trapped by an earlier decision (**hypothesis**) | Protect the organization from visible “rewrite failure” (**hypothesis**) | Document boundaries; test compatibility; isolate exceptional workloads; define migration options |
| Sustain capability | Maintain enough skill, knowledge, and staffing to operate the system | Reduce key-person and hiring anxiety (**hypothesis**) | Build a team seen as capable and employable (**hypothesis**) | Assess labor market; trial onboarding; document; coach; plan succession |

The functional dimensions are **Medium-to-High confidence**. Emotional and social dimensions are **Low-to-Medium confidence**: accountability and leader/engineer misalignment are observable, but no reviewed study directly interviews this Django-specific audience about reputation, fear, or identity.

## Triggering situations

**Event-triggered situations**

- A company is validating an idea, funding an MVP, or adding a backend service.
- Product-market fit, funding, customer growth, hiring, or multiple teams expose limits in an informal early architecture.
- A new capability—API program, internal operations, data-heavy workflow, realtime behavior, regional data residency, or integration—changes the workload.
- An incident, vulnerability, audit, unsupported version, poor upgrade, or key-person departure makes latent risk visible.
- New leadership, acquisition, reorganization, or an architecture review reopens a standard.
- Delivery stalls, duplicated work grows, or a stakeholder requests security, resilience, residency, or lifecycle evidence.

**Recurring situations**

- Allocating capacity among product work, reliability, maintenance, and architecture.
- Hiring and onboarding developers; reviewing whether conventions help or hinder them.
- Tracking delivery, quality, incidents, costs, dependencies, releases, deprecations, and security advisories.
- Approving or reviewing service-level exceptions to an organizational stack.
- Explaining risk and investment needs upward while maintaining team trust.

The event/recurring distinction is **inference, High confidence**. Frequency and the actual point at which leaders revisit the framework require primary research.

## Desired outcomes

- Reduce elapsed time from identified need to a reversible, evidence-backed decision.
- Reduce time and engineering effort to a production-capable customer outcome, not merely a demo.
- Increase delivery predictability while maintaining acceptable change-failure, recovery, reliability, and security outcomes.
- Reduce bespoke glue, duplicated platform work, and technologies owned where standardization helps.
- Reduce onboarding time, key-person dependency, and maintenance/on-call burden.
- Keep upgrade lag, unsupported dependencies, and unresolved critical vulnerabilities within an explicitly accepted policy.
- Meet workload-specific latency, throughput, availability, recovery, privacy, and cost constraints in representative conditions.
- Preserve team autonomy while achieving cross-team compatibility and governance.
- Reduce lifecycle and switching cost; increase the share of change that can be incremental.

These are **directional inferred outcomes; Medium-to-High confidence**. No evidence supports universal target values. DORA’s 2024 research reinforces that productivity, team performance, organizational performance, stability, throughput, and well-being can move in different directions; a single “developer velocity” number is insufficient ([Accelerate State of DevOps Report 2024](https://dora.dev/research/2024/dora-report/), 2024).

## Current behaviour or status quo

In early companies, the default is commonly the founder’s or first engineers’ known language, framework, host, and deployment pattern, optimized for learning and time-to-market. After product-market fit, stabilization, hiring, maintainability, and deployability become more salient in the practitioner stage account. **Qualitative direct evidence; Medium-Low confidence.**

In established organizations, the status quo is an approved stack, internal platform, existing skills, and incremental maintenance. In a cross-domain survey of 188 practitioners, expert judgment dominated, functional suitability filtered options, and reliability was the most important subsequent quality ([Petersen et al.](https://www.sciencedirect.com/science/article/pii/S0950584919300710), August 2019). The later selection study says decisions remain often ad hoc.

Leaders rarely act alone even when they approve. In Stack Overflow’s 2025 survey, 48% of developer respondents had endorsed or influenced a technology choice in the preceding year, including 19.8% who influenced a substantial stack addition ([Work section](https://survey.stackoverflow.co/2025/work)). This is **direct broad-developer evidence; Medium confidence** for the evaluator/influencer role, not for final approval.

For incumbent systems, staged evolution is an alternative to replacement. DoorDash’s early Django monolith reduced time-to-market and operational overhead, but growth led to a coordinated rearchitecture involving task forces, team representatives, executive buy-in, a code freeze, and substantial allocation ([DoorDash Engineering](https://careersatdoordash.com/blog/how-doordash-transitioned-from-a-monolith-to-microservices/), 2 December 2020). Sentry used simulations and 35,000 tests to prepare a large Django application for regional data separation ([Sentry Engineering](https://blog.sentry.io/removing-risk-from-our-multiregion-design-with-simulations/), 16 May 2024). **Direct cases; Medium confidence as possibilities, Low confidence for typical cost/outcomes.**

## Pushes

- Runway or delivery pressure makes custom integration and repeated routine backend work costly.
- Team growth exposes inconsistent patterns, ownership ambiguity, duplicated work, and coordination overhead.
- Upgrade backlog, end-of-life software, dependency drift, incidents, or compliance needs make inaction risky. In the 2025 State of Open Source survey, keeping up with patches, meeting security/compliance requirements, and maintaining EOL versions were the three highest-weighted challenges ([OpenLogic/OSI/Eclipse Foundation](https://www.openlogic.com/system/files/2025-05/report-openlogic-2025-state-of-open-source-support.pdf), survey September–December 2024; report 2025). **Direct cross-OSS evidence; Medium confidence for Django leaders.**
- Poor onboarding, hiring, key-person risk, growth, or new requirements pressure the existing foundation.

## Pulls

- Integrated conventions can reduce early decision and integration load. Current respondents value models, admin, migrations, and authentication, but this is self-selected evidence, not comparative proof.
- Python fit, existing organizational skill, and available learning material can lower adoption and staffing friction. Ecosystem-selection research supports developer availability and consistent documentation as criteria, not a claim that Django has the best labor market.
- Open source can reduce license cost and vendor lock-in and offer transparency. In the 2025 cross-industry OSS survey, cost reduction (53%), reduced vendor lock-in (33%), interoperability (28%), and stable technology with community long-term support (24%) were selected motivations. **Direct survey evidence; Medium confidence; not Django-specific and the sample consists of OSS users.**
- Explicit release, deprecation, security, and LTS policies can make lifecycle planning possible. Django documents roughly eight-month feature releases, backwards-compatible patch releases, and typically three-year LTS security/data-loss support ([release process](https://docs.djangoproject.com/en/6.0/internals/release-process/), current 6.0 documentation, accessed 18 July 2026). **Direct project fact; High confidence about policy.**
- Production histories reduce “is it possible?” uncertainty. DoorDash and Sentry show leverage and adaptation cost, not easy scale or transferable fit.

## Anxieties

- **Accountability:** approving a foundation that later slows delivery, fails an audit, raises infrastructure cost, or triggers a rewrite. **Hypothesis; Low-to-Medium confidence.**
- **Team adoption:** whether engineers can become productive, accept the conventions, and retain enough autonomy. Software-selection research directly includes engineer satisfaction and recommends prototyping it.
- **Longevity and maintenance capacity:** whether core and critical packages will be patched, upgraded, and staffed for the system’s expected life.
- **Hiring and key-person risk:** whether suitable experience is available; evidence establishes the criterion, not Django-specific supply/demand.
- **Performance and operating economics:** whether the actual workload meets its service and cost constraints.
- **Architecture trajectory:** whether a productive monolith becomes an organizational bottleneck and can evolve incrementally.
- **Loss of credibility or control:** a manager may fear either looking outdated for choosing a mature framework or looking trend-driven for changing a proven stack. **Hypothesis; Low confidence.**

## Habits and inertia

- Founder or senior-engineer familiarity favors the stack they can ship and debug today.
- Existing platform, data, security, and delivery investments favor approved paths.
- Domain models, tests, integrations, operational knowledge, and staff experience make replacement costly even when the incumbent is imperfect.
- Hiring, training, and peer networks reinforce existing ecosystems; time pressure favors prior success and expert judgment.
- Standardization is self-reinforcing. It can reduce duplication, yet central control can weaken team influence; the Ericsson cases support context-dependent balance.

Application to Django is **inference, High confidence**; relative strength varies by stage and organization.

## Decision criteria

Only one cross-developer ordering is evidence-backed. For **work projects**, Stack Overflow’s 2025 respondents ranked robust/complete API first, reputation for quality second, easy-to-use API third, reliability/low latency fourth, manageable cost fifth, open-source connection sixth, a customizable/manageable codebase seventh, public image eighth, and AI integration ninth. Security/privacy was the top rejection reason. **Direct broad-developer evidence; Medium confidence for leader decisions** because the survey is not role- or framework-specific.

Leader-specific criteria below are intentionally **not globally ranked**:

| Criterion | Why it matters to this audience | Importance | Confidence |
|---|---|---|---|
| Functional and architecture fit | Must serve the actual domain, data model, interfaces, integrations, and boundary strategy | Potential showstopper | High |
| Reliability, security, privacy, recovery, and compliance | Leaders bear customer, operational, regulatory, and reputational consequences | Potential showstopper in high-assurance contexts | High |
| Time to useful production outcome | Determines runway, opportunity cost, and capacity for product learning | High, especially early stage | High |
| Team productivity and comprehensibility | Affects onboarding, safe change, coordination, satisfaction, and ownership | High but context-dependent | Medium-High |
| Lifecycle and ecosystem health | Release/support policy, dependency compatibility, maintenance capacity, and upgrade effort determine future risk | High for long-lived systems | High |
| Total lifecycle cost | Includes people, cloud, integration, maintenance, incidents, support, and switching—not only licenses | High but organization-dependent | High |
| Performance under representative conditions | Synthetic reputation cannot replace target workload, data, hardware, and cost tests | Potential showstopper for constrained workloads | High |
| Skills, hiring, onboarding, and external expertise | Determines delivery capacity and concentration risk | Context-dependent | Medium-High |
| Fit with organizational standards | Deployment, observability, identity, data, security, and service ownership can block local technical fit | High in established organizations | High |
| Governance, control, and exit options | License, source access, decision transparency, support routes, and replaceable boundaries affect dependency risk | Context-dependent | Medium-High |

The strongest evidence supports a **gated process**, not a universal score: high-level requirements first; showstoppers next; realistic prototype and impact analysis thereafter.

## Main concerns

**Practical concerns:** delivery time, learning, reliability, staffing, platform integration, observability, deployment, upgrades, package quality, and lifecycle cost.

**Legitimate limitations and responsibility boundaries:** an integrated framework does not supply deployment, SRE, recovery, dependency, or compliance programs. Django’s security policy defines disclosure/support behavior but places input sanitation and some proxy/header configuration on developers ([security policies](https://docs.djangoproject.com/en/6.0/internals/security/), current 6.0 documentation, accessed 18 July 2026). Mixed sync/async dependencies, workload-specific resource cost, ORM behavior, and package lag are valid fit questions. Evolving boundaries can require custom tooling and coordination.

**Organizational concerns:** ownership, standards, reviewer approval, and whether exceptions burden adjacent teams. Authority varies; “the CTO decides” is not a safe default.

**Emotional resistance (hypotheses):** fear of being blamed for a mature choice perceived as old, fear of disrupting a working system to appear current, and discomfort losing either executive control or team autonomy. **Low confidence pending interviews.**

## Objections and perceived risks

- **“Django is too old or not current enough.”** This is a perception, not evidence of unfitness. Continued releases do not remove the need to test required capabilities/packages.
- **“Django cannot scale.”** As a universal claim this is contradicted by direct production cases. The defensible concern is the staff, architecture, and infrastructure cost needed to meet a specific scale; famous companies are not transferable guarantees.
- **“A batteries-included monolith inevitably blocks growth.”** DoorDash and Sentry counter inevitability while showing that boundary changes can be expensive.
- **“Open source means free support and low total cost.”** Unsupported. The DSF says corporate membership provides neither technical support nor preferential roadmap input ([corporate membership](https://www.djangoproject.com/foundation/corporate-membership/), accessed 18 July 2026).
- **“The framework standard alone guarantees secure delivery.”** Contradicted by Django’s own responsibility boundaries and by cross-OSS evidence on patching, EOL, and compliance.
- **“Hiring will be easy because Python is popular.”** Requires further research. Developer availability matters, but relevant Django, domain, and production skill supply varies by market.
- **“Standardizing on one framework will automatically improve productivity.”** Unsupported. DORA 2024 and the autonomy research show trade-offs: platforms and alignment can improve performance, but stability, throughput, independence, and team influence require active design.

## Information needed to make progress

All segments need an explicit constraint profile, decision/exception owners, representative proof results, lifecycle facts, critical dependencies, production responsibilities, cost assumptions, and clear unknowns.

Stage-specific needs differ:

- **Pre-PMF:** time and effort to a deployed vertical slice; authentication/admin/data/integration fit; minimum operating burden; cloud cost at plausible demand; ability for the next hires to understand the system.
- **Growth stage:** ownership boundaries, scaling bottlenecks/remedies, deployment/recovery, onboarding/upgrades, and isolation of exceptional workloads.
- **Multi-team/enterprise:** platform/policy fit, supply-chain review, security/support windows, governance/exception model, comparable references, and accountable owner.
- **Regulated/high assurance:** data flow/residency, threat model, patch expectations, dependency inventory, audit/recovery evidence, and precise responsibility boundaries.
- **Incumbent Django:** actual version/package status, incident and delivery bottlenecks, upgrade path, operational cost, knowledge concentration, incremental change options, and the counterfactual cost/risk of migration.

Leaders also need negative evidence: where Django was adapted, isolated, or left; staff and time required; what failed; and why the case is comparable. This is **inference, High confidence** from realistic-context selection research, but public Django rejection and migration data are sparse.

## Trusted content formats

- A **time-bounded, representative proof of concept** with stated success/failure criteria is the highest-confidence evaluation format; selection research directly recommends prototypes and target-context performance tests.
- A **technical decision record or impact analysis** exposes requirements, assumptions, stakeholders, costs, and exit conditions.
- **Primary technical and policy documentation**, release/security records, source code, issue history, and package compatibility data validate current facts.
- **Detailed engineering accounts and postmortems** with context, adaptation cost, and limitations are useful existence proofs; generic logos are not.
- **Peer review by engineers and operators** who will implement or bear consequences validates team and production fit; experts dominate real selection behavior.
- **Threat models, recovery exercises, upgrade trials, and dependency inventories** validate consequential risks. Concise executive summaries can translate, but should link to the evidence. **Inference; Medium confidence.**

## Discovery, evaluation, validation, and engagement channels

**Discovery:** prior experience, trusted engineers, technical communities, peers, search, engineering publications, talks, and surveys surface options. Evidence supports expert judgment and internet/experience-report searches, but not LinkedIn, podcasts, short-form social, or generic executive media as decisive here. **Medium confidence.**

**Evaluation:** official documentation, release/security policy, source and issue history, package repositories, production engineering accounts, research/surveys, and internal technical communities answer fit and lifecycle questions. Stack Overflow’s developer influence data supports engineers as active evaluators; it does not show that CTOs personally use each channel.

**Validation:** representative internal prototypes, load/cost tests, security and architecture review, deployment/recovery exercises, references with comparable constraints, and review by future users/operators turn claims into a decision. This is the best-supported stage behavior from Bjarnason et al.; company logos alone are weak validation.

**Ongoing engagement:** among engaged Django respondents, djangoproject.com (60%) leads reported ways to follow development, then YouTube (22%), Stack Overflow and Reddit (18% each), Forum (15%), newsletter (12%), and lower-share channels. This does not isolate leaders. Release notes/docs support monitoring; Forum/peers support interpretation; GitHub/issues support verification/escalation; conferences support peer learning. **Direct usage, inferred role; Medium-Low confidence.**

## Decision-makers and influencers

| Context | Initiator | Researcher/evaluator | Influencer | Approver/economic buyer | Blockers/reviewers | Users and consequence bearers |
|---|---|---|---|---|---|---|
| Pre-PMF startup | Founder-CTO, CEO, first engineer, or product need | Often the founder-CTO/first engineers | Co-founders, early hires, customers/investors through requirements | Founder-CTO and/or CEO; budget may be implicit | Runway, customer commitments, security needs, unavailable skills | Founder-engineers first; company bears delay, outage, and rewrite risk |
| Growth company | Lead/staff engineer, EM, platform owner, or product initiative | Senior engineers and future service owners | EMs, product, SRE, data, security, existing Django experts | CTO/VP Engineering/director depending scope; finance for material spend | Platform standards, security/privacy, operations, hiring capacity | Product teams, operators, support, customers; leaders bear delivery and investment consequences |
| Large/multi-team organization | Team, architecture/platform group, modernization program | Cross-functional technical group or proof team | Technical communities, architects, managers, product/business owners | Architecture/technology authority, director/VP, or delegated team; CTO may set principles rather than approve a framework | Security, compliance, legal/OSS program, platform, data, procurement for paid support/services | Multiple teams and downstream systems; organization and users bear systemic consequences |
| Incumbent Django system | Service owner, EM, incident/audit, upgrade need | Maintainers, staff engineers, SRE/security | Product owners, adjacent teams, Django/package experts | Service/director level for maintenance; executive/finance approval for major rearchitecture or funding | Change risk, version/package constraints, compliance, opportunity cost | Engineers/operators carry maintenance and on-call; customers/business carry reliability and migration consequences |

This map is **inference with High confidence** at the role-category level and **Medium confidence** for allocation. The large-scale autonomy study directly shows that authority can rest with management, teams, or a community; organization-specific decision rights must be discovered, not assumed. “Marketing executive” is not supported as a normal framework approver.

## Appropriate next actions for Django to encourage

These are job-progress actions, not the underlying jobs and not prescriptions for marketing assets.

1. **Name the decision context and authority.** Identify lifecycle stage, workload, incumbent/new status, decision owner, evaluators, reviewers, users, and consequence bearers. This advances the primary selection job.
2. **Write high-level requirements and showstoppers before evaluating.** Include product, team, lifecycle, security, integration, performance, and cost constraints. This reduces familiarity- and trend-led choice.
3. **Verify current lifecycle and responsibility facts.** Review supported versions, deprecations, security process, deployment responsibilities, and critical-package compatibility. This serves production stewardship.
4. **Run a representative vertical-slice proof.** Include the riskiest data, auth, integration, async, load, deployment, or recovery path and measure effort as well as runtime behavior. This advances fit validation.
5. **Have future users and operators review the result.** Capture engineer satisfaction, comprehensibility, operational ownership, and exception needs. This serves productive autonomy and capability.
6. **Record a decision with assumptions, costs, risks, and exit conditions.** This translates technical evidence into an organizational case and preserves adaptability.
7. **For incumbent teams, assess before proposing replacement.** Measure version/package status, delivery and incident friction, upgrade cost, knowledge risk, and incremental boundary options. This serves stewardship rather than a framework-first action.
8. **If organizational dependency makes project continuity material, evaluate appropriate support and sustainability actions.** These may include allocating upgrade capacity, engaging expert services, contributing fixes, or funding the DSF, while recognizing that DSF corporate membership is philanthropic rather than support or control. This connects maintenance continuity to risk stewardship; funding motivation remains a separate job requiring its own approval case.

## Overlaps with other audiences

- **Technical leads and architects:** commonly own evaluation and standards; this lens adds people, budget, delivery, and business accountability.
- **Experienced backend engineers:** often conduct the proof and bear implementation/on-call consequences; they may influence without final authority.
- **Existing professional Django developers:** overlap when a leader is hands-on or manages an incumbent service; use is not approval.
- **Founders/startups:** a founder-CTO’s job is inseparable from product validation and runway, while “startup” itself is a company context.
- **Enterprise/regulated organizations:** add governance and risk stakeholders; they are not synonymous with CTOs.
- **Security, platform, SRE, legal, procurement, and finance:** reviewers/approvers, not usually primary users.
- **Corporate funders:** the same CTO may sponsor sustainability, but selecting/stewarding a framework and making a philanthropic or strategic funding case are distinct jobs.
- **Contributors/maintainers:** dependence may lead to contribution, but organizational delivery accountability is not maintainer motivation.

## Possible segmentation problems

“CTOs and engineering managers” should not remain one prioritization segment. Title does not reveal authority, stage, hands-on involvement, incumbent status, or risk context and implies a false top-down model.

Research recruitment should split along these axes:

1. **Decision role:** sole decider/implementer; evaluator-recommender; economic approver; governance owner; manager without stack authority.
2. **Lifecycle/stage:** pre-PMF greenfield; post-PMF stabilization; multi-team standardization; incumbent stewardship; major rearchitecture/migration.
3. **Organizational scale:** one team; interacting teams; formal platform/architecture governance. Interdependence matters more than headcount.
4. **Constraint profile:** conventional data-centric application; API/service platform; async/realtime or compute-sensitive workload; regulated/high assurance; legacy integration.
5. **Django relationship:** considering; adopted recently; inherited; retained through growth; rejected; migrated away; materially dependent.

The highest-value split is **hands-on early technical leader**, **growth/multi-team approver**, and **engineering manager as recommender/steward**. **Inference, High confidence** that jobs differ; size/priority need primary research.

## Existing-analysis claim audit

| Existing claim relevant to this lens | Assessment | Audit note |
|---|---|---|
| A mid-to-large-company “marketing executive or technical decision-maker” approves framework standards based on currency/relevance, long-term reliance, community/support, security, and hiring. | **Partially supported** | Currency, quality, lifecycle, ecosystem, security, cost, integration, and developer availability are supported criteria. Approval varies among teams, technical communities, architecture/platform authorities, managers, and executives. No evidence supports a marketing executive as a normal framework approver. |
| Enterprise examples, production architecture, and testimonials influence decision-makers. | **Partially supported** | Detailed, comparable production accounts can support discovery and validation. DoorDash and Sentry show benefits, costs, and evolution. Generic testimonials or famous-company logos without workload, stage, staffing, and adaptation detail are not shown to change decisions. |
| Companies depending on Django want maintenance continuity to avoid migration costs and may fund it; corporate approval can involve finance and leadership. | **Partially supported** | Switching cost and continuity are strong inferences from incumbent cases and lifecycle evidence. Organizations demonstrably fund the DSF through tiered corporate membership, including Django-dependent companies, and the DSF says members support development; it provides no support SLA or roadmap control. The causal claim that migration avoidance motivates funding, and the exact internal approval chain, require interviews. |
| Existing professional Django developers seek releases/upgrades, scaling help, greater expertise, and possible progression from user to contributor. | **Partially supported** | Leaders of incumbent systems have recurring upgrade, scaling, staffing, and stewardship jobs. The evidence does not establish a universal desire for “greater expertise” or progression to contributor; contribution is a separate job and may be organizationally funded. |
| Claimed touchpoints include docs/release notes, forums/Discord, GitHub/issue tracker, mailing lists, conferences/sprints, podcasts, professional peer networks, and short-form social. | **Partially supported** | Django survey data supports official channels, Forum, Discord, podcasts, and several social/community sources among current users, with very different reach. Selection research supports experts, internet search, and experience reports. GitHub/issues have a validation/escalation role by inference. Mailing lists, sprints, professional networks, and short-form social were not validated as important leader channels. |

Claims about individual donors, early-career learners, and contributor recognition/burnout are not audited because they are outside this audience’s primary job.

## Evidence table

| Finding | Source (title, publisher/author, date, URL) | Evidence type | Direct evidence or inference | Confidence | Research notes |
|---|---|---|---|---|---|
| Software selection should start from the need and usage environment and consider business, organizational, technical, ecosystem, integration, quality, lifecycle, legal, and cost effects with all relevant stakeholders. | *Software selection in large-scale software engineering*, Bjarnason, Åberg & Ali, *Empirical Software Engineering*, 28 Feb 2023, [link](https://link.springer.com/article/10.1007/s10664-023-10288-w) | Peer-reviewed rapid reviews, industry co-design, focus group, case use | Direct general evidence; Django application inferred | High | Strong decision-process fit; validation centered on Ericsson and not web-framework-specific. |
| Realistic prototypes and target-context performance tests, plus engineer satisfaction, support a defensible decision. | Same Bjarnason et al. study, 28 Feb 2023, [link](https://link.springer.com/article/10.1007/s10664-023-10288-w) | Peer-reviewed selection study | Direct general evidence | High | Supports job-progress actions and trusted formats; does not prescribe thresholds. |
| In 188 industry responses, expert judgment dominated sourcing decisions; functional suitability filtered options and reliability was the most important subsequent quality. | *Selecting component sourcing options*, Petersen et al., *Information and Software Technology* 112, Aug 2019, [link](https://www.sciencedirect.com/science/article/pii/S0950584919300710) | Cross-domain practitioner survey | Direct | Medium-High | Component sourcing is broader than frameworks; useful evidence against purely executive or scorecard-driven choice. |
| Ecosystem choice depends on project/environment; developer availability and consistent documentation are material criteria. | *A decision model for programming language ecosystem selection: Seven industry case studies*, Farshidi, Jansen & Deldar, 2021, [link](https://dspace.library.uu.nl/handle/1874/420503) | Peer-reviewed seven-company case evaluation | Direct general evidence; Django application inferred | Medium-High | Supports hiring/documentation criteria without measuring Django labor supply. |
| Developers frequently influence organizational technology choices; work projects emphasize API, quality, reliability/latency, and cost, while security/privacy leads rejection. | *Stack Overflow Developer Survey 2025 — Work*, Stack Overflow, 2025, [link](https://survey.stackoverflow.co/2025/work) | Large self-selected developer survey | Direct | Medium | Broad developer sample; no CTO/EM cross-tab. Ranking is not generalized to leader-specific criteria. |
| Platform choices can improve productivity and organizational performance while harming stability/throughput if independence and implementation are mishandled. | *Accelerate State of DevOps Report 2024*, DORA/Google Cloud, 2024, [link](https://dora.dev/research/2024/dora-report/) | Cross-industry survey/model research | Direct general evidence; framework implication inferred | Medium-High | Supports multi-outcome evaluation and cautions against one productivity metric. |
| Great engineering management is perceived as enabling team potential; technical skill alone does not define greatness. | *What Makes a Great Manager of Software Engineers?*, Kalliamvakou et al., Microsoft Research/IEEE TSE, 2018, [link](https://www.microsoft.com/en-us/research/publication/what-makes-a-great-manager-of-software-engineers/) | Mixed-method empirical study at Microsoft | Direct general evidence | Medium | One large company and not a technology-selection study; supports manager/team boundary. |
| Large-scale technical authority can rest with teams, management, supporting roles, or technical communities; neither full team autonomy nor full autocracy is universal. | *Finding the sweet spot for organizational control and team autonomy*, Moe, Šmite, Paasivaara & Lassenius, *Empirical Software Engineering*, 2021, [link](https://link.springer.com/article/10.1007/s10664-021-09967-3) | Two-case interview/workshop study at Ericsson | Direct | Medium-High | Strong evidence against assuming CTO approval; context is large-scale agile telecom development. |
| A startup CTO’s work shifts from feasibility/stack/MVP coding toward stabilization, hiring, management, and technical strategy as the company grows. | *How the Role of a CTO Evolves as a Startup Grows*, Antler interview with Chris Brooke, 5 Sep 2019, [link](https://www.antler.co/blog/how-cto-role-evolves-as-startup-grows) | First-person practitioner stage account | Direct qualitative evidence | Medium-Low | One experienced startup CTO; useful segmentation hypothesis, not prevalence evidence. |
| Engaged Django respondents span leadership roles, company sizes, and team sizes; professional/team use and recurring upgrades are common. | *Django Developers Survey 2025 Results*, DSF & JetBrains/PyCharm, fielded Nov 2024–Jan 2025, published 2025, [link](https://lp.jetbrains.com/django-developer-survey-2025/) | Self-selected survey, about 4,600 respondents | Direct | Medium | 16% Team Lead, 15% Architect, 13% CTO/CIO/CEO; multi-select and Django-channel recruitment prevent market inference. |
| Current Django users value integrated components and use both full-stack and API patterns; this supplies plausible pulls, not comparative superiority. | Same *Django Developers Survey 2025*, 2025, [link](https://lp.jetbrains.com/django-developer-survey-2025/) | Self-selected current-user survey | Direct | Medium | Models/admin/migrations/auth are favorite components; 80% full-stack and 51% DRF API use. No leader cross-tabs. |
| Among OSS-using organizations, cost, lock-in, interoperability, and community support motivate use; patching, security/compliance, and EOL maintenance are leading challenges. | *2025 State of Open Source Report*, OpenLogic by Perforce with OSI & Eclipse Foundation, survey 17 Sep–20 Dec 2024, report 2025, [PDF](https://www.openlogic.com/system/files/2025-05/report-openlogic-2025-state-of-open-source-support.pdf) | Anonymous global survey, 433 respondents | Direct | Medium | Mixed roles/sizes, all already work with OSS, vendor involved; not Django-specific. |
| Django’s cadence, deprecation rules, patch compatibility, and typical three-year LTS window are explicit. | *Django’s release process*, Django documentation 6.0, accessed 18 Jul 2026, [link](https://docs.djangoproject.com/en/6.0/internals/release-process/) | Primary project policy | Direct fact | High | Appropriate for project behavior; says nothing about comparative upgrade labor or package readiness. |
| Django has a responsible-disclosure process and supported-version policy while leaving important application/deployment security responsibilities to developers/operators. | *Django’s security policies*, Django documentation 6.0, accessed 18 Jul 2026, [link](https://docs.djangoproject.com/en/6.0/internals/security/) | Primary project policy/guidance | Direct fact | High | Supports responsibility-boundary concern; not a comparative security assessment. |
| Django reduced early DoorDash time-to-market and operational surface, while later rearchitecture required standardization, task forces, cross-team representatives, management buy-in, planning, and major capacity. | *Future-proofing: How DoorDash Transitioned from a Code Monolith to a Microservice Architecture*, Cesare Celozzi, DoorDash Engineering, 2 Dec 2020, [link](https://careersatdoordash.com/blog/how-doordash-transitioned-from-a-monolith-to-microservices/) | First-party production/rearchitecture account | Direct case evidence | Medium | Valuable benefits/costs account; one high-growth company, older architecture, no counterfactual. |
| A mature Django system can evolve incrementally, but separating data/operational boundaries required extensive tests, simulation, CI cost, coordination, and new concepts. | *Removing risk from our multi-region design with simulations*, Mark Story, Sentry Engineering, 16 May 2024, [link](https://blog.sentry.io/removing-risk-from-our-multiregion-design-with-simulations/) | First-party production architecture account | Direct case evidence | Medium | Shows a path and costs, not general ease; Sentry is also a Django corporate member. |
| Organizations demonstrably fund the DSF at tiered levels; motives include supporting continued development, while membership confers neither support services nor preferential technical influence. | *Corporate membership*, Django Software Foundation, current page accessed 18 Jul 2026, [link](https://www.djangoproject.com/foundation/corporate-membership/); *Corporate members*, current page, [link](https://www.djangoproject.com/foundation/corporate-members/) | Primary program terms and observed member list | Direct facts; dependency motivation partly inferred | High for program facts; Low-Medium for internal ROI | Some listed members explicitly say their backends/ecosystems are built on Django. The pages do not expose approval processes or causal motives by company. |

## Unanswered research questions

1. In recent real framework decisions, who initiated, evaluated, approved, blocked, paid, used, and bore consequences at each company stage?
2. When does a founder-CTO’s fast-learning job give way to a growth leader’s standardization, staffing, and governance job—and which Django concerns emerge at that transition?
3. How often can engineering managers choose a framework, versus only recommend, staff, or steward it? What exception processes do they face?
4. Which outcomes do leaders actually measure after a framework decision: production lead time, onboarding, change failure, incident load, cloud cost, upgrade effort, retention, or something else?
5. What evidence makes a Django production account transferable? Which combinations of workload, architecture, team size, regulation, and stage matter most?
6. Why do leaders reject Django after serious evaluation? Public evidence is heavily skewed toward current users and successful/interesting adopters.
7. What effort and failures occur in proofs, first releases, onboarding, major upgrades, and migrations?
8. Which concerns decide API-first, async/realtime, high-throughput, data-heavy, internal-workflow, and regulated cases?
9. What is the regional supply of production-capable Django skills, and how do wages, onboarding, and adjacent Python skills affect choice?
10. How do leaders use peers, technical communities, docs/source, surveys, engineering accounts, events, and social channels at each decision stage?
11. What evidence and approval support unlock maintenance capacity, expert support, contribution, or DSF funding?
12. Which emotional/social jobs are real rather than researcher projection?

The highest-priority gap is **comparative interviews around a recent consequential decision**, sampled across early founder-CTOs, growth leaders, engineering managers with and without approval authority, large-company governance owners, incumbent Django stewards, rejecters, and former users. Existing evidence is strong on general selection method and project facts, moderate on current-user behavior and production possibilities, and weak on causal leader motivations and internal approval systems.

<!-- RESEARCH PROVENANCE: BEGIN -->
## Research provenance

This section was generated from the recorded Codex session JSONL logs. File attribution uses successful patch events; searches and domains use nested web-tool calls.

### Session `019f7543-711e-72d0-9647-9cccd33a1be0`
- Log: `rollout-2026-07-18T14-46-21-019f7543-711e-72d0-9647-9cccd33a1be0.jsonl`
- This document: `add, update`
- Search queries:
  - None recorded.
- Website domains:
  - `2022.djangocon.us`
  - `administraciondesistemas.com`
  - `antler.co`
  - `apache.org`
  - `arxiv.org`
  - `assets.ctfassets.net`
  - `axios.com`
  - `blog.ahmadwkhan.com`
  - `blog.clubhouse.com`
  - `blog.sentry.io`
  - `botreetechnologies.com`
  - `cabird.com`
  - `careersatdoordash.com`
  - `ceur-ws.org`
  - `code.djangoproject.com`
  - `cortex.io`
  - `datadrivendaily.com`
  - `dejawu.me`
  - `django.ac.cn`
  - `djangobook.py3k.cn`
  - `djangochat.com`
  - `djangoproject.com`
  - `docs.djangoproject.com`
  - `doi.org`
  - `dokk.org`
  - `dora.dev`
  - `dspace.library.uu.nl`
  - `eliot.blog`
  - `en.wikipedia.org`
  - `engineering.kraken.tech`
  - `fcto.ai`
  - `forrester.com`
  - `gartner.com`
  - `github.com`
  - `hapy.co`
  - `i-programmer.info`
  - `incaseofstairs.com`
  - `itpro.com`
  - `jellyfish.co`
  - `jetbrains.com`
  - `johnkealy.com`
  - `link.springer.com`
  - `linuxfoundation.org`
  - `llamaindex.ai`
  - `lp.jetbrains.com`
  - `media.djangoproject.com`
  - `medium.com`
  - `microsoft.com`
  - `mudassirkhan.me`
  - `nimble.gt`
  - `openlogic.com`
  - `opensource.org`
  - `papers.ssrn.com`
  - `planeks.net`
  - `pure.tudelft.nl`
  - `pyfound.blogspot.com`
  - `reddit.com`
  - `reintech.io`
  - `research.chalmers.se`
  - `russellreynolds.com`
  - `sciencedirect.com`
  - `scitepress.org`
  - `sentry.engineering`
  - `sixfeetup.com.\n\n`
  - `solidmatics.com`
  - `sonatype.com`
  - `startups.com`
  - `stepchange.work`
  - `storn.co`
  - `survey.stackoverflow.co`
  - `tandfonline.com`
  - `techradar.com`
  - `tier.engineering`
  - `tomshardware.com`
  - `trio.dev`
  - `ubuntu.com`
  - `windowscentral.com`
  - `witarist.com`
  - `youtube.com`

### Session `019f7589-343f-74b3-a65e-b423e48d9776`
- Log: `rollout-2026-07-18T16-02-33-019f7589-343f-74b3-a65e-b423e48d9776.jsonl`
- This document: `update`
- Search queries:
  - `"Social Barriers Faced by Newcomers Placing Their First Contribution" PDF`
  - `"Software selection in large-scale software engineering" Badampudi DOI`
  - `site:give.org "Public Eye on Charitable Accountability" 2024 infographic`
  - `site:give.org 2024 "Impact" donor trust special report infographic`
  - `site:give.org/donor-trust-report "Public Eye on Charitable Accountability"`
  - `site:give.org/news 2024 accountability donor trust how charity spends money truthful accurate 76% 73%`
- Website domains:
  - `creativecommons.org`
  - `ctreude.ca`
  - `dblp.org`
  - `doi.org`
  - `give.org`
  - `igor.pro.br`
  - `isr.uci.edu`
  - `link.springer.com`
  - `repositorio.usp.br`
  - `researchgate.net`
  - `sciencedirect.com`

<!-- RESEARCH PROVENANCE: END -->
