# Technical leads and software architects

## Audience definition and boundaries

This audience consists of people accountable for the technical direction of a product, service, platform, or portfolio who may evaluate Django as part of an application architecture. Titles include technical lead, lead engineer, staff/principal engineer, solution architect, software architect, platform architect, and—especially in smaller organizations—CTO or engineering manager. Their common boundary is responsibility for consequential, cross-cutting choices: fitness to requirements, system qualities, delivery constraints, operational ownership, and the decision's future cost.

The label is a role-in-context, not a demographic or a single buyer persona. A startup lead can initiate, evaluate, approve, and use a stack; an enterprise evaluator may only recommend while security, architecture, platform, procurement, finance, and a service owner approve or block aspects. The UK Government service manual says technical architects work with teams and third parties on robust, scalable, open, secure systems, while the service owner retains final service-quality responsibility ([GOV.UK, role guidance, updated November 6, 2023](https://www.gov.uk/service-manual/the-team/what-each-role-does-in-service-team)). **Direct evidence; High confidence** for complex public-sector organizations and **Medium confidence** across industries.

Included are greenfield selection, approval of an organizational standard or exception, inherited-Django stewardship, modernization, and “stay, evolve, or migrate” decisions. Excluded are developers choosing a framework only for personal learning, executives who approve money without evaluating technology, procurement specialists acting only on commercial terms, and contributors maintaining Django itself—although one person may occupy several of these audiences.

## Important subsegments

- **Hands-on product technical leads:** close to code and delivery; may combine initiation, evaluation, influence, use, approval, and consequence-bearing.
- **Solution/software architects:** translate business and non-functional requirements into a system design, compare options, document rationale, and align development, data, security, and operations stakeholders.
- **Enterprise/platform architects:** evaluate consistency with approved languages, deployment platforms, identity, observability, data, and governance. They may set guardrails across many teams and act as evaluator, influencer, or blocker rather than user.
- **CTO/VP-level technical decision-makers in smaller organizations:** combine technical, economic, staffing, and risk decisions. Their framework choice is tightly coupled to runway, hiring, and time to market.
- **Leads of established Django estates:** optimize continuity, upgrades, standardization, and progressive decomposition; migration cost and expertise make this unlike greenfield selection.
- **Regulated or high-assurance architects:** give greater weight to security response, privacy, supply-chain evidence, auditability, support windows, and explicit risk acceptance.
- **Workload specialists:** API/backend leads, full-stack/server-rendered product leads, data/AI-adjacent leads, and high-concurrency or low-latency architects have materially different fit questions. “Django evaluator” should not collapse these contexts.

## Primary job to be done

> **When** my organization must commit a team and a service to a web application foundation, **I want to** determine and explain whether the proposed stack fits our user needs, system qualities, team capabilities, operating model, and risk appetite, **so I can** enable delivery now without creating an unsafe, expensive, or hard-to-reverse constraint later.

Job hierarchy:

- **Core functional job:** synthesize functional and non-functional requirements, test the highest-risk assumptions, make a decision, and preserve its rationale.
- **Supporting jobs:** map integration and deployment constraints; estimate total ownership and switching cost; establish an upgrade/security path; define boundaries and guardrails; identify who will own production.
- **Emotional job (hypothesis):** feel appropriately confident that important unknowns have been exposed rather than hidden. Empirical work calls architectural decision-making cognitively challenging and finds organizational, process, and human challenges; evidence specific to Django evaluators is absent ([Dasanayake et al., 2017](https://arxiv.org/abs/1707.00107)). **Inference; Medium confidence.**
- **Social job (hypothesis):** be seen by delivery, security, operations, and leadership as exercising sound judgment rather than following novelty or habit. Architecture decisions are commonly collaborative and stakeholder-negotiated, but reputation was not directly measured in the reviewed studies. **Inference; Low-to-Medium confidence.**

## Additional jobs to be done

1. > **When** a team proposes Django, **I want to** validate its behavior on our critical paths and operational environment, **so I can** replace generic claims with evidence relevant to our workload.
   - **Core functional:** prototype integrations and measure performance, deployment, failure, and development workflow.
   - **Supporting:** define acceptance thresholds, representative data, observability, and rollback; compare against the current baseline.
   - **Emotional (hypothesis):** reduce uncertainty before attaching my name to the decision.
   - **Social:** give reviewers a shared artifact and evidence base. GOV.UK explicitly recommends prototypes to test security, integration, compliance, and technical constraints ([updated October 15, 2024](https://www.gov.uk/service-manual/technology/choosing-technology-an-introduction)). **Direct evidence for the functional/supporting job; High confidence.**

2. > **When** several teams need architectural guidance, **I want to** establish enabling constraints and a reusable default with a clear exception path, **so I can** reduce duplicated decisions without trapping teams in a poor fit.
   - **Core functional:** standardize the common path while preserving justified variation.
   - **Supporting:** reference architecture, ownership, decision record, supported versions, dependency policy, and exception criteria.
   - **Emotional (hypothesis):** avoid becoming either a bottleneck or an absentee authority.
   - **Social:** create alignment across teams. DORA finds that independent test/deploy/change capability matters more than fashionable architecture labels and that approval and coordination dependencies are measurable ([DORA, “Loosely coupled teams,” current page](https://dora.dev/capabilities/loosely-coupled-teams/)). **Direct evidence about team outcomes; Medium-to-High confidence for this inferred job.**

3. > **When** I inherit or revisit a Django estate, **I want to** decide whether to stay, upgrade, contain, decompose, or migrate, **so I can** improve outcomes without paying unnecessary rewrite cost or preserving avoidable risk.
   - **Core functional:** assess current fitness and identify the smallest safe architectural change.
   - **Supporting:** inventory versions/dependencies, incident and performance data, coupling, skills, data migration constraints, and incremental exit routes.
   - **Emotional (hypothesis):** avoid both sunk-cost denial and rewrite enthusiasm.
   - **Social:** make the trade-off legible to product and finance. Architectural decisions were the most important reported source of technical debt in a survey of 1,831 engineers and architects ([Ernst et al., ACM/CMU SEI, August 2015](https://www.sei.cmu.edu/library/measure-it-manage-it-ignore-it-software-practitioners-and-technical-debt/)). **Direct evidence for the consequence; Medium confidence for this Django-specific job.**

4. > **When** the chosen open-source foundation becomes business-critical, **I want to** monitor its maintenance, security, release, and ecosystem health, **so I can** keep operational exposure and future upgrade effort within our risk tolerance.
   - **Core functional:** turn adoption into lifecycle stewardship.
   - **Supporting:** subscribe to advisories; plan supported-version upgrades; evaluate third-party packages; maintain inventory and owners; decide whether contribution or funding is justified.
   - **Emotional (hypothesis):** avoid surprise from an abandoned component or overdue upgrade.
   - **Social:** demonstrate responsible stewardship to risk owners and service users. OpenSSF explicitly treats unmaintained software as a security risk and asks consumers to examine activity, maintainer diversity, releases, security response, LTS, tests, license, and dependencies ([March 28, 2025](https://best.openssf.org/Concise-Guide-for-Evaluating-Open-Source-Software.html)). **Direct evidence; High confidence.**

## Functional, emotional, and social dimensions

**Functional (evidenced):** satisfy requirements; balance security, reliability, performance, operations, cost, and sustainability; preserve evolvability; enable team delivery; and manage dependencies. AWS formalizes these qualities, while government guidance adds reversibility, data control, standards, and total ownership ([AWS, 2024 framework](https://docs.aws.amazon.com/wellarchitected/2024-06-27/framework/definitions.html); [GOV.UK, updated 2024](https://www.gov.uk/service-manual/technology/choosing-technology-an-introduction)). **Direct evidence; High confidence.**

**Emotional (hypotheses):** seek confidence under incomplete information; fear avoidable outages, security exposure, a costly reversal, or being held responsible for an inadequately tested standard; feel tension between delivery pressure and architectural stewardship. These are plausible consequences of uncertainty and technical debt evidence, but no reviewed study isolates Django-evaluating leads. **Inference; Low-to-Medium confidence.**

**Social (partly evidenced hypotheses):** build consensus without surrendering technical integrity; make reasoning understandable to non-specialists; protect team autonomy while satisfying reviewers; maintain credibility by acknowledging trade-offs. Collaborative architecture research based on 15 architect interviews found consultative decision-making preferred, and ADR guidance names delivery, adjacent architecture, and security teams as readers ([Dasanayake et al., 2017](https://arxiv.org/abs/1707.00107); [Google Cloud, last reviewed August 16, 2024](https://docs.cloud.google.com/architecture/architecture-decision-records)). **Direct evidence for collaboration; inference for status/credibility; Medium confidence.**

## Triggering situations

**Recurring triggers:** quarterly/annual technology reviews; release and support-window changes; security advisories; dependency-health review; capacity and cost review; architecture governance; hiring/onboarding friction; incident/postmortem actions; and roadmap planning.

**Event-triggered situations:** a new product or major capability; a prototype entering production; acquisition or team handover; audit or regulatory requirement; severe incident; sudden traffic growth; platform/cloud migration; end-of-support notice; inability to recruit or retain skills; unacceptable latency/cost; organizational standardization; or a proposal to split or rewrite a monolith.

Django-specific examples show both positive and negative triggers. Meta reused Instagram's Django backend, data models, business logic, security features, and infrastructure to accelerate Threads, which reached 100 million users without major downtime; that is evidence that installed capability can pull an adjacent product toward the incumbent stack, not proof that a fresh organization can reproduce Meta's results ([Meta Engineering, September 7, 2023](https://engineering.fb.com/2023/09/07/culture/threads-inside-story-metas-newest-social-app/)). **Direct case evidence; High confidence about Meta, Low confidence for general performance prediction.** Kraken describes slow deployments, configuration liability, and long-running migration problems as triggers for a three-year infrastructure evolution around its Django estate ([Kraken Engineering, February 11, 2026](https://engineering.kraken.tech/news/2026/02/11/django-kubernetes-health-checks-continuous-delivery.html)). **Direct case evidence; Medium confidence for recurrence elsewhere.**

## Desired outcomes

- Critical user journeys and non-functional requirements meet agreed thresholds under representative load and failure modes.
- Teams can implement, test, deploy, and recover with fewer external approvals, handoffs, and coordinated releases; DORA suggests measuring these directly rather than inferring them from “monolith” or “microservices” labels.
- Lower lead time for change and deployment friction without a higher change-failure or rework rate.
- Security requirements, dependency provenance, supported-version policy, disclosure route, patch SLA, and risk ownership are explicit.
- Predictable total cost across engineering labor, infrastructure, security, upgrades, operations, training, and potential exit—not merely license cost.
- New maintainers can understand why the choice was made and what would cause it to be revisited; an ADR remains current.
- The team can hire, train, and retain enough capability and does not rely on one internal expert or one external maintainer.
- Migration or decomposition remains possible through understood interfaces, data ownership, and bounded coupling.

These are directional outcomes, not claimed benchmarks. DORA's standard delivery measures—lead time, deployment frequency, failed-deployment recovery time, change failure percentage, and deployment rework—offer observable measures ([DORA research questions, current](https://dora.dev/research/core/questions/)). **Direct evidence for measurement constructs; High confidence.**

## Current behaviour or status quo

Leads commonly start from standards, skills, platforms, prior decisions, and integration constraints. They consult colleagues, documentation, engineering accounts, repositories, and release/security records, then prototype uncertain areas. Decisions are often collaborative; rationale may be preserved in ADRs or left as informal precedent.

Established estates usually evolve incrementally: supported-version upgrades, deployment/observability improvements, and isolation of exceptional workloads. Meta's custom Python runtime/JIT and memory work shows that a very large Django deployment can persist with specialized optimization investment; it proves neither effortless scaling nor a need to migrate ([Meta Engineering, May 2, 2022](https://engineering.fb.com/2022/05/02/open-source/cinder-jits-instagram/); [August 15, 2023](https://engineering.fb.com/2023/08/15/developer-tools/immortal-objects-for-python-instagram-meta/)). **Direct case evidence; High confidence about Meta, Low generalizability.**

## Pushes

- Slow or risky delivery, rising coordination cost, recurring incidents, security findings, upgrade backlog, operational toil, and architecture debt.
- A workload mismatch: sustained low-latency or compute-efficiency targets, high-concurrency long-lived connections, unusual data requirements, or unsupported integration.
- Dependency abandonment, weak disclosure/patch practice, narrow maintainer base, or an incompatible release/support window.
- Hiring or onboarding difficulty and excessive reliance on tribal knowledge.
- Business pressure for faster capability, lower cost, platform consolidation, auditability, or an exit from legacy/vendor constraints.
- Evidence that the current architecture prevents independent test, deployment, or ownership.

LeadDev's 2024 survey of 1,100+ engineering leaders reports simultaneous pressure for features (77%), technical debt/maintenance (66%), cost/productivity/efficiency (63%), and reliability/uptime (53%), supporting the multi-objective pressure behind reconsideration rather than any Django-specific ranking ([LeadDev, 2024](https://leaddev.com/wp-content/uploads/2024/10/LeadDev-Engineering-Leadership-Performance-Report-2024__LDMO___0.pdf)). **Direct evidence; Medium confidence due to sample/self-report limitations.**

## Pulls

- An integrated application foundation that reduces bespoke assembly for common web-product needs such as data modeling, authentication, administration, forms, sessions, and security controls.
- Existing Python capability and the ability to share language, tooling, data/AI knowledge, or infrastructure.
- A mature release process, LTS window, public security history, documentation, and open governance that make lifecycle risk inspectable.
- Reuse of established models, business logic, operational practices, and organizational expertise.
- A broad enough professional ecosystem to support common full-stack and API work: in the 2025 Django Developers Survey (responses collected November 2024–January 2025), 82% said they wrote Django professionally; 80% used it for full-stack development and 51% for REST APIs with DRF ([DSF/JetBrains, October 31, 2025](https://lp.jetbrains.com/django-developer-survey-2025/)). This demonstrates respondent practice, not market share or hiring supply. **Direct survey evidence; Medium confidence.**
- Visible production precedent can reduce perceived novelty risk, but case fit matters more than logo similarity.

## Anxieties

- “Will a convenient start become an expensive ceiling in throughput, concurrency, team scale, or architecture?”
- “Are we evaluating Django core or silently depending on a stack of unevenly maintained third-party packages?”
- “Can we operate and patch it reliably for the service lifetime, including zero-downtime database changes?”
- “Does the Python/Django talent pool match our location, compensation, and domain—and can general Python developers become effective maintainers?”
- “Will a server-rendered/full-stack default fit our frontend and API strategy?”
- “Will async boundaries add complexity or prevent a critical concurrency model?” Django 6.0 supports an async request stack and many async APIs, but transactions still do not work in async mode, synchronous middleware can require adaptation, and connection pooling needs deliberate treatment ([Django 6.0 async documentation, current](https://docs.djangoproject.com/en/6.0/topics/async/)). **Direct evidence; High confidence.**
- “Will reviewers interpret maturity as outdatedness, or novelty as irresponsibility?” This is plausible but unmeasured. **Hypothesis; Low confidence.**
- “Who carries outage, migration, compliance, and reputation consequences?”

## Habits and inertia

Existing language standards, deployment platforms, libraries, CI/CD, observability, identity systems, database expertise, and hiring pipelines strongly shape the feasible set. Teams reuse decisions they already know; a 2018 case study found architecture-decision reuse frequent but ad hoc and confined by architects' existing knowledge ([Manteuffel, Avgeriou &amp; Hamberg, *Journal of Systems and Software*, October 2018](https://www.sciencedirect.com/science/article/pii/S0164121218301110)). **Direct evidence; Medium confidence.**

For an installed Django estate, accumulated models, migrations, admin workflows, package choices, runbooks, and staff expertise create rational switching costs. Familiarity can also conceal risk: unsupported versions, inherited conventions, or “Django cannot/can scale” beliefs may go untested. For greenfield work, a company-approved stack can win by default because exception review costs time. Inertia is therefore both a useful risk control and a possible source of architectural debt.

## Decision criteria

No reviewed evidence supports a universal ranking. The following importance levels are context-dependent gates, not a scorecard order.

| Criterion | Importance hypothesis | Confidence | What the evaluator needs to establish |
|---|---|---:|---|
| User/business and workload fit | Critical | High | Critical journeys, data model, integrations, latency/concurrency, accessibility, privacy, and roadmap fit |
| Security and compliance posture | Critical, especially regulated contexts | High | Secure defaults and limits, disclosure/patch process, dependency/supply-chain controls, audit evidence, accountable risk owner |
| Operability and reliability | Critical for production | High | Deployment model, health checks, observability, capacity, failure isolation, recovery, database-change practice, on-call ownership |
| Evolvability and reversibility | Critical for long-lived services | High | Modular boundaries, interface/data control, upgrade path, exception path, and cost of changing direction |
| Total cost of ownership | High | High | Delivery labor, infrastructure, operations, security, upgrades, training, support, and exit cost |
| Team capability and delivery flow | High | High | Current skills, onboarding, maintainability, test/deploy independence, tooling fit, availability of hiring/training/consulting |
| Performance efficiency and scalability | Critical only against explicit workload thresholds | High | Measured behavior and resource cost on representative paths; likely bottlenecks and mitigation complexity |
| Project/ecosystem health | High for open-source dependency | High | Release recency, maintainer diversity, governance, security response, LTS, license, package health, and credible ownership |
| Integrated capability versus assembly burden | High for many product teams | Medium | Which built-ins remove work; which third-party components add risk; how much customization fights defaults |
| Organizational/platform compatibility | High in multi-team estates | High | Approved runtime, databases, cloud/platform, identity, CI/CD, observability, architecture standards, and support model |
| Hiring-market depth | High where growth/turnover is material | Medium | Evidence from the actual labor market, not global popularity proxies; transferability from Python skills |

The OpenSSF evaluation guide directly supports project-health criteria. AWS and GOV.UK directly support system-quality, TCO, security, and reversibility criteria. Django production cases support the need for workload-specific validation, not a general ranking. **Mixed direct evidence and synthesis; High confidence in the criterion set, Low confidence in any universal weighting.**

## Main concerns

**Practical concerns:** representative performance; production topology; database changes/pooling; async boundaries; API/frontend integration; dependency selection; observability; testing; upgrades; platform fit; talent; and ownership.

**Legitimate limitations:** extreme scale can demand specialized Python optimization; async Django retains constraints; security depends on deployment and design; database support is finite; package quality varies. Django itself calls out web-server/OS, upload, throttling, secret, cache/database, and design-level risks ([Django 6.0 security documentation](https://docs.djangoproject.com/en/6.0/topics/security/)). **Direct evidence; High confidence.**

**Perceived risks requiring validation:** “monolith prevents independence,” “Python cannot scale,” “batteries always means faster,” or “a famous adopter proves our fit.” DORA rejects label-based conclusions; Meta demonstrates achievable scale with custom investment. **Direct evidence against categorical claims; High confidence.**

**Misconceptions:** an LTS eliminates upgrade work; built-in controls make an application secure; framework popularity establishes local hiring feasibility; open source has zero ownership cost; or a framework decision alone determines system architecture.

**Organizational objections:** unapproved runtime; weak ownership; security/legal gaps; platform divergence; infrastructure/hiring cost; time-to-market; and on-call burden.

**Emotional resistance (hypothesis):** status attached to newer architectures, fear of defending an unfashionable choice, sunk-cost attachment to the incumbent, or fear of blame for change. **Low confidence; requires interviews.**

## Objections and perceived risks

- **“It is not modern/current.”** Currency should be resolved through release cadence, supported Python versions, async/API capabilities, and fit to the roadmap—not aesthetic age. Django publishes a live support roadmap; 5.2 is LTS through April 2028 and 6.0 through April 2027 as of July 18, 2026 ([Django download/support roadmap](https://www.djangoproject.com/download/)). **Direct factual evidence; High confidence.**
- **“It will not scale.”** Contradicted as an absolute by Meta's deployments, but those cases also expose custom runtime, memory, and infrastructure work. The valid question is cost and complexity at the target workload. **Direct evidence; High confidence.**
- **“It is automatically enterprise-ready/secure because it has batteries.”** Unsupported. Django provides controls, checks, a disclosure process, and patches, but its deployment checklist explicitly requires environment-specific security, performance, operations, production server, HTTPS, logging, and secret decisions ([Django deployment checklist](https://docs.djangoproject.com/en/dev/howto/deployment/checklist/)). **Direct evidence; High confidence.**
- **“A monolith prevents autonomous teams.”** Overgeneralized. DORA says the outcome is independent change/test/deploy and notes modern labels can still yield tight coupling. **Direct evidence; High confidence.**
- **“There will always be enough Django maintainers.”** Requires local labor-market evidence. Survey respondents demonstrate professional use, while the broader PSF survey shows a large Python ecosystem, but neither proves employer-specific supply. **Requires further research; Medium confidence.**
- **“Migration is safer than incremental evolution” / “migration is never worth it.”** Both are unsupported absolutes. Current constraints, target state, data movement, team topology, and incremental options determine risk.

## Information needed to make progress

1. User journeys, horizon, regulation, risk appetite, data sensitivity, and non-functional thresholds.
2. Workload shape: request mix, concurrency, latency, background/streaming work, data growth, geography, and availability.
3. A production-like prototype covering the riskiest integration, authorization, data access, deployment, telemetry, and failure path.
4. Reference architecture and ownership: boundaries, data/cache/queue, API/frontend, secrets, scaling, health, recovery, and on-call.
5. Lifecycle evidence: support/deprecations, security history, releases, package inventory, maintainer/license signals, and upgrade rehearsal.
6. Team evidence: capability, onboarding, maintainability, local hiring, training/support, and bus factor.
7. Economics: delivery/operation, upgrades/security, opportunity, migration/exit, and approved-alternative costs.
8. An ADR with context, options, requirements, decision, rationale, consequences, owner, date, and revisit triggers.

## Trusted content formats

- **Executable prototypes and workload-specific performance/reliability results:** evaluation and risk reduction.
- **Architecture diagrams and ADRs:** context, boundaries, trade-offs, and consequences for reviewers and future owners.
- **Versioned documentation, release notes, advisories, support policy, and upgrade guides:** lifecycle and compatibility evidence.
- **Firsthand postmortems and architecture talks with constraints and numbers:** analogous validation; context-free testimonials are weaker.
- **Source repositories, issue history, package metadata, test/CI evidence, OpenSSF-style assessments, and licenses:** due diligence on core and dependencies.
- **Hands-on workshops or technical deep dives with maintainers/practitioners:** resolve specific unknowns and reveal operational tacit knowledge.
- **Peer-reviewed empirical studies and survey datasets:** establish broader decision and engineering patterns, with sampling limits stated.

The PSF/JetBrains 2024 survey of more than 30,000 Python respondents found documentation/APIs (58%), YouTube (51%), Python.org (41%), Stack Overflow (43%), and blogs (38%) used to learn about relevant tools; this is broad Python evidence, not a technical-lead-only preference ranking ([PSF/JetBrains, responses collected October–November 2024](https://lp.jetbrains.com/python-developers-survey-2024/)). **Direct evidence; Medium confidence for this audience.**

## Discovery, evaluation, validation, and engagement channels

- **Discovery:** peers, internal architecture communities, engineering blogs, events/podcasts, search, Python.org, social links, and radars expand the option set; they are not approval evidence.
- **Evaluation:** official documentation, releases, security/support policies, repositories/issues, package metadata, ADRs, and practitioner discussions answer fit and lifecycle questions.
- **Validation:** prototypes, production-like load/failure tests, security/architecture review, peer references, and detailed production accounts test claims in context. Prototyping has the strongest direct evidence.
- **Ongoing engagement:** release/security lists, docs, GitHub/issues, Forum/Discord, internal communities, events/sprints, and consultants support operation. Social mainly discovers; releases monitor lifecycle; forums solve problems and provide qualitative validation; GitHub exposes implementation and project health.

Evidence does not establish a universal channel order for technical leads. The claimed docs/release notes, forums/Discord, GitHub/issue tracker, mailing lists, conferences/sprints, podcasts, peer networks, and short-form social all have plausible distinct roles, but audience-specific conversion or trust data is missing.

## Decision-makers and influencers

The same person may hold several roles in small organizations; in larger ones these roles should be explicitly mapped:

| Decision role | Typical actors | Interest and authority | Likely Django-specific contribution |
|---|---|---|---|
| **Initiator** | Product technical lead, staff engineer, founder/CTO, product manager, platform team | Frames a new capability, delivery problem, or architecture review | Proposes evaluation, incumbent continuation, or reconsideration |
| **Researcher/evaluator** | Technical lead, software/solution architect, senior developers, platform/SRE, security architect | Tests functional and non-functional fit and documents trade-offs | Prototype, architecture, dependency/security review, TCO and skills assessment |
| **Influencer** | Delivery developers, operations/SRE, data engineers, frontend leads, peer architects, external practitioners/consultants | Supplies experience and bears implementation friction; may lack formal veto | Challenges assumptions about ORM, APIs, async, deployment, packages, upgrades, and maintainability |
| **Approver / economic buyer** | CTO/VP Engineering, accountable service owner, architecture review body, budget owner; finance/procurement where spend is material | Accepts investment, standard/exception, and residual business risk | Approves team/infrastructure/support/training/migration cost; may not select the framework personally |
| **Blocker / reviewer** | Security, privacy/data protection, legal/license, compliance, enterprise architecture, platform/cloud governance, procurement | Can reject or condition adoption when controls, standards, ownership, or evidence are inadequate | Requires patch/support policy, supply-chain review, data controls, approved deployment, license and ownership evidence |
| **User** | Application developers, testers, DevOps/SRE, support and operations staff | Builds, tests, deploys, upgrades, debugs, and operates the system | Experiences daily APIs, tooling, docs, package, migration, and incident workflows |
| **Consequence bearer** | End users/data subjects, on-call engineers, delivery team, service owner, organization/customers | Bears outages, breaches, delivery delay, cost escalation, migration, inaccessible service, or reputation loss | Often has less decision power than the evaluator; consequences must appear in requirements and risk acceptance |

This map is a synthesis. GOV.UK directly distinguishes technical architect, security/risk owner, multidisciplinary team, and accountable service owner; architecture studies directly show stakeholder collaboration. Exact authority varies by organization. **Inference from authoritative role guidance and empirical studies; Medium-to-High confidence.** A “marketing executive” is not evidenced as a normal framework-standard approver; they might be a product/business stakeholder but should not be conflated with the technical evaluator.

## Appropriate next actions for Django to encourage

These are audience progress actions, not proposed campaigns or assets:

- **Translate the service into explicit requirements and revisit triggers** → advances the primary job of a defensible fit decision.
- **Run a production-like Django spike on the highest-risk path** → advances the job of replacing generic scalability/security claims with contextual evidence.
- **Record the choice, trade-offs, ownership, consequences, and exception path in an ADR** → advances organizational alignment and future reversibility.
- **Review core and planned third-party components against maintenance, security, license, and support criteria** → advances lifecycle stewardship.
- **Create and rehearse an upgrade, security-advisory, backup/recovery, and production-ownership plan before commitment** → advances safe long-term operation.
- **Engage practitioners or maintainers with a bounded technical question; validate answers in the prototype** → advances uncertainty reduction without treating community opinion as proof.
- **For established users, quantify stay/upgrade/evolve/migrate options before authorizing a rewrite** → advances the modernization job and makes switching cost legible.
- **Where business dependence and risk justify it, evaluate contribution or corporate funding through normal finance/leadership approval** → advances maintenance continuity; it is not a substitute for support or preferential product influence.

## Overlaps with other audiences

- **Existing professional Django developers:** hands-on leads share upgrade, scaling, and expertise jobs but carry broader accountability.
- **CTOs/engineering executives and economic buyers:** overlap in small firms; in larger firms executives approve risk/budget while architects evaluate.
- **Platform engineering/SRE/DevOps:** overlap on deployment, reliability, observability, cost, and golden paths.
- **Security, privacy, legal, and procurement reviewers:** overlap on supply-chain, compliance, license, and risk acceptance; they may block without being framework users.
- **Companies dependent on Django and corporate funders:** leads may initiate or justify funding because they understand operational dependence; finance/leadership commonly approve.
- **Contributors/maintainers:** a lead may contribute fixes or governance input, but adoption and project stewardship are distinct jobs.
- **Developers entering the ecosystem:** hiring/onboarding connects the audiences, but career investment is not the architect's primary job.

## Possible segmentation problems

- Title is a poor proxy for authority: “architect” can be advisory; “lead developer” can own the entire decision.
- Company size alone does not determine process; domain risk, team topology, standards, and procurement maturity matter.
- Greenfield evaluation and installed-estate stewardship have different switching forces and should not share one journey without qualification.
- Framework choice, application architecture, deployment platform, and organizational topology are related but separate decisions. Treating “Django” as synonymous with “monolith” corrupts the segment.
- Full-stack, API-first, event-driven/long-lived-connection, internal-tool, and data-adjacent workloads require different evidence.
- Regulated and non-regulated contexts weight disclosure, evidence, and approval differently.
- Global survey popularity cannot stand in for a local senior-talent market.
- Technical leads can be users, evaluators, approvers, blockers, and consequence bearers simultaneously; a persona that assigns them only “decision-maker” loses critical jobs.
- Evidence skews toward public-sector guidance, large technology companies, and self-selected surveys; small firms and failed Django selections are underrepresented.

## Existing-analysis claim audit

| Existing-analysis claim | Audit | Rationale |
|---|---|---|
| A mid-to-large-company “marketing executive or technical decision-maker” approves framework standards based on currency/relevance, long-term reliance, community/support, security, and hiring; enterprise examples, production architecture, and testimonials influence them. | **Partially supported** | Technical decision-makers and cross-functional reviewers are supported; currency/support, security, sustainability, TCO, team skill, and architecture evidence are valid criteria. A marketing executive as normal framework approver is unsupported. Detailed production accounts can validate feasibility, but evidence does not show testimonials as a strong trust format or a universal criterion ranking. |
| Existing professional Django developers seek current best practice, releases/upgrades, scaling help, greater expertise, and possible progression from user to contributor. | **Partially supported (overlap only)** | Release/upgrade, scaling, operational, and expertise needs clearly apply to hands-on leads and inherited estates. Progression to contributor is possible but not established as an important job for this audience. |
| Companies depending on Django want maintenance continuity to avoid migration costs and may fund it; corporate approval can involve finance and leadership. | **Supported, with qualification** | OpenSSF directly links maintenance and security risk; TCO guidance includes change/lock-in cost. Kraken says Django/Python are fundamental to its business and sponsorship is “the right thing,” and DSF corporate membership is an annual paid program. Funding motivation and approval workflow beyond specific cases remain under-researched. |
| Claimed touchpoints include docs/release notes, forums/Discord, GitHub/issue tracker, mailing lists, conferences/sprints, podcasts, professional peer networks, and short-form social. | **Partially supported** | Documentation is strongly supported for learning/evaluation; release/security channels and repositories directly support lifecycle due diligence; prototypes and detailed practitioner accounts support validation. Forums/Discord and peers plausibly support problem solving; conferences/podcasts/social primarily enable discovery and engagement. Technical-lead-specific usage and trust rates are unavailable. |

## Evidence table

| Finding | Source (title, publisher/author, date, URL) | Evidence type | Direct evidence or inference | Confidence | Research notes |
|---|---|---|---|---|---|
| Technology choices affect service quality and the team's ability to operate/iterate; reversibility, security, TCO, context, prototypes, and evolution matter. | [“Choosing technology: an introduction,” GOV.UK Service Manual, published May 23, 2016; updated October 15, 2024](https://www.gov.uk/service-manual/technology/choosing-technology-an-introduction) | Authoritative public-sector guidance | Direct | High | Strong decision-process evidence; public-sector context may add governance not present in startups. |
| Technical architects work with teams/third parties and ensure robust, scalable, open, secure systems; service owners retain final quality responsibility. | [“What each role does in a service team,” GOV.UK Service Manual, published March 3, 2016; updated November 6, 2023](https://www.gov.uk/service-manual/the-team/what-each-role-does-in-service-team) | Authoritative role guidance | Direct | High for role distinction; Medium cross-industry | Supports separating evaluator from approver/consequence owner. |
| Architecture review should cover operational excellence, security, reliability, performance efficiency, cost optimization, and sustainability. | [“Definitions,” AWS Well-Architected Framework, 2024 edition](https://docs.aws.amazon.com/wellarchitected/2024-06-27/framework/definitions.html) | Authoritative industry framework | Direct | High | Vendor-authored/cloud-oriented but broadly used quality model; not framework-specific. |
| Open-source consumers should inspect maintenance, activity, maintainer diversity, releases, security response/LTS, tests, dependencies, license, and repository security. | [“Concise Guide for Evaluating Open Source Software,” OpenSSF Best Practices WG, March 28, 2025](https://best.openssf.org/Concise-Guide-for-Evaluating-Open-Source-Software.html) | Foundation/industry best-practice guidance | Direct | High | Directly relevant to Django core and each third-party package; checklist is guidance, not an adoption outcome study. |
| NIST's SSDF ties secure development to business needs, risk tolerance, resources, cost, feasibility, and design-decision tracking. | [“Secure Software Development Framework,” NIST CSRC; SP 800-218 v1.1, February 2022](https://csrc.nist.gov/projects/ssdf) | Government standard/guidance | Direct | High | Supports security reviewer/risk-owner concerns, not a Django evaluation. |
| Independent change/test/deploy capability predicts continuous-delivery outcomes; technology labels alone do not ensure it. | [“Loosely coupled teams,” DORA/Google Cloud, current capability page, accessed July 18, 2026](https://dora.dev/capabilities/loosely-coupled-teams/) | Multi-year empirical research synthesis/guidance | Direct | Medium-to-High | Useful counter to monolith/microservice absolutes; page synthesizes DORA research and practitioner guidance. |
| Delivery outcomes can be measured via change lead time, deployment frequency, recovery time, change failure, and rework. | [“DORA Research Questions,” DORA/Google Cloud, current, accessed July 18, 2026](https://dora.dev/research/core/questions/) | Research instrument | Direct | High for constructs | Measures architecture-associated outcomes, not framework causality. |
| Engineering leaders balance features, debt/maintenance, cost/productivity, reliability, performance, and developer experience. | [“Engineering Leadership Report 2024,” LeadDev, 2024](https://leaddev.com/wp-content/uploads/2024/10/LeadDev-Engineering-Leadership-Performance-Report-2024__LDMO___0.pdf) | Survey of 1,100+ engineering leaders | Direct | Medium | Self-selected sample; percentages are priorities, not ordered framework criteria. |
| ADRs capture requirements, options, reasons, affected journeys, and history for teams, security, onboarding, and future change. | [“Architecture decision records overview,” Google Cloud Architecture Center, last reviewed August 16, 2024](https://docs.cloud.google.com/architecture/architecture-decision-records) | Authoritative practitioner guidance | Direct | High | Vendor context does not materially limit the lightweight decision-record pattern. |
| Architecture decisions are often collaborative; consultative style was preferred in one large-company case. | [“An Empirical Study on Collaborative Architecture Decision Making in Software Teams,” Dasanayake et al., July 2017](https://arxiv.org/abs/1707.00107) | Exploratory case study; 15 architect interviews | Direct | Medium | One European company and older study; useful role signal, not universal authority map. |
| Architectural decisions were the most important reported source of technical debt. | [“Measure It? Manage It? Ignore It? Software Practitioners and Technical Debt,” Ernst et al., ACM/CMU SEI, August 2015](https://www.sei.cmu.edu/library/measure-it-manage-it-ignore-it-software-practitioners-and-technical-debt/) | Survey of 1,831 practitioners plus interviews | Direct | Medium-to-High | Long-lived systems in three large organizations; persistent pattern but older. |
| Meta reused Instagram's Django stack for speed and successful large-scale launch of Threads. | [“Threads: The inside story of Meta's newest social app,” Meta Engineering, September 7, 2023](https://engineering.fb.com/2023/09/07/culture/threads-inside-story-metas-newest-social-app/) | Firsthand adoption account | Direct | High for case; Low generalizability | Shows value of incumbent stack and organizational capability, not ordinary out-of-box scale. |
| Very large Django/Python deployments can require specialized runtime, concurrency, and memory optimization. | [“Introducing Immortal Objects for Python,” Meta Engineering, August 15, 2023](https://engineering.fb.com/2023/08/15/developer-tools/immortal-objects-for-python-instagram-meta/); [“How the Cinder JIT's function inliner helps us optimize Instagram,” May 2, 2022](https://engineering.fb.com/2022/05/02/open-source/cinder-jits-instagram/) | Firsthand production engineering accounts | Direct | High for Meta; Low-to-Medium generalization | Corrects both “cannot scale” and “scales without special cost” narratives. |
| Most surveyed Django respondents use it professionally and across full-stack/API work; async and cloud stacks are varied. | [“Django Developers Survey 2025 Results,” DSF/JetBrains, published October 31, 2025; responses November 2024–January 2025](https://lp.jetbrains.com/django-developer-survey-2025/) | Self-selected developer survey, 4,600+ respondents | Direct | Medium | 82% professional, 80% full-stack, 51% REST/DRF; respondent usage is not market share or hiring availability. |
| Django supports a broad async stack but retains constraints including no async transactions. | [“Asynchronous support,” Django 6.0 documentation, accessed July 18, 2026](https://docs.djangoproject.com/en/6.0/topics/async/) | Official technical documentation | Direct | High | Exact current limitation; must be tested against workload and package/middleware mix. |
| Django's security depends on correct application design and production deployment as well as built-in features. | [“Security in Django,” Django 6.0 documentation, accessed July 18, 2026](https://docs.djangoproject.com/en/6.0/topics/security/); [“Deployment checklist,” development docs, accessed July 18, 2026](https://docs.djangoproject.com/en/dev/howto/deployment/checklist/) | Official technical documentation | Direct | High | Django-controlled but authoritative about its own capabilities and limits. |
| Django has transparent supported-version/LTS windows and disclosed security releases. | [“Download Django,” DSF, live roadmap accessed July 18, 2026](https://www.djangoproject.com/download/); [“Archive of security issues,” Django documentation, accessed July 18, 2026](https://docs.djangoproject.com/en/dev/releases/security/) | Official project records | Direct | High | Evidence of process and transparency, not proof of zero vulnerability or adopter patch speed. |
| A Django-dependent company can evolve infrastructure over years, invest in upgrades/tooling, and fund upstream because of business dependence. | [“How we ship in 2026,” Kraken Engineering, March 9, 2026](https://engineering.kraken.tech/news/2026/03/09/how-we-ship-2026.html); [“Django, Kubernetes Health Checks and Continuous Delivery,” February 11, 2026](https://engineering.kraken.tech/news/2026/02/11/django-kubernetes-health-checks-continuous-delivery.html) | Firsthand production/stewardship account | Direct | Medium-to-High | One sophisticated corporate user; supports continuity/funding claim but not prevalence. |
| DSF corporate dues fund project priorities but do not buy support or preferential technical influence. | [“Corporate membership,” Django Software Foundation, accessed July 18, 2026](https://www.djangoproject.com/foundation/corporate-membership/); [“2024 Annual Impact Report,” DSF, 2024](https://www.djangoproject.com/foundation/reports/2024/) | Official governance/funding records | Direct | High | Useful for organizational funding role; Django-controlled and not evidence of buyer motivation across firms. |
| Documentation and multiple media are used to learn about Python tools, but broad survey usage cannot establish technical-lead trust order. | [“Python Developers Survey 2024 Results,” PSF/JetBrains; responses October–November 2024](https://lp.jetbrains.com/python-developers-survey-2024/) | Survey of 30,000+ Python respondents | Direct plus audience inference | Medium | Documentation/APIs 58%, YouTube 51%, Stack Overflow 43%, Python.org 41%, blogs 38%; all Python respondents, not architects only. |

## Unanswered research questions

1. In real Django evaluations, who initiates, vetoes, accepts residual risk, controls budget, and bears production consequences by company size and regulated status?
2. Which criteria actually eliminate Django, and which only prompt a prototype or architectural mitigation?
3. How do technical leads compare Django core risk with the aggregate risk of common third-party packages?
4. What evidence changes a skeptical architect's decision: a peer reference, transparent benchmark, code spike, security review, detailed case, or supported-version plan?
5. How large are upgrade, operations, and migration costs in typical Django estates, not exceptional large-company cases?
6. How does local senior Django hiring supply compare with the transferability and training cost of broader Python experience?
7. Which workloads most often reveal a decisive async, latency, resource-efficiency, frontend, data, or organizational-topology mismatch?
8. How frequently do organizations approve Django as a default, approve it by exception, inherit it through acquisition, or reject it after evaluation?
9. Which channels do technical leads use at each stage, and which do security, finance, and service-owner reviewers trust?
10. What emotional and status pressures actually influence framework decisions, and how do they interact with documented evidence?
11. Do corporate Django funders initiate support from engineering dependency owners, executives, procurement, or social-impact teams, and what internal ROI case is required?
12. Where are the failed or reversed Django adoption accounts? Public evidence is disproportionately successful and therefore vulnerable to survivorship bias.

<!-- RESEARCH PROVENANCE: BEGIN -->
## Research provenance

This section was generated from the recorded Codex session JSONL logs. File attribution uses successful patch events; searches and domains use nested web-tool calls.

### Session `019f7541-679e-7e30-a311-cd383ea341fb`
- Log: `rollout-2026-07-18T14-44-08-019f7541-679e-7e30-a311-cd383ea341fb.jsonl`
- This document: `add, update`
- Search queries:
  - `Django Developers Survey 2024 results technical challenges deployment performance async`
  - `Django architecture engineering case study scale site:engineering.* Django Python`
  - `Django at scale engineering blog architecture technical decision migration Django monolith`
  - `Django at scale engineering site:sentry.engineering OR site:blog.sentry.io Django monolith`
  - `Django migration engineering blog why moved from Django performance architecture`
  - `Instagram engineering Django scale Python monolith site:engineering.fb.com OR site:instagram-engineering.com`
  - `enterprise architecture technology selection roles approver security procurement technical lead framework standards`
  - `site:aws.amazon.com architecture framework pillars security reliability performance efficiency cost optimization sustainability operational excellence`
  - `site:cloud.google.com architecture framework software architecture decision records teams`
  - `site:ddat-capability-framework.service.gov.uk technical architect responsibilities`
  - `site:dl.acm.org software architecture decision making stakeholders empirical study architect`
  - `site:docs.djangoproject.com/en/5.2/releases/5.2 long term support async ORM limitations Django`
  - `site:docs.djangoproject.com/en/6.0/faq/install production WSGI ASGI Django deployment checklist`
  - `site:docs.djangoproject.com/en/6.0/howto/deployment/checklist Django deployment checklist security performance operations`
  - `site:docs.djangoproject.com/en/6.0/ref/databases PostgreSQL connection pooling async Django limitations`
  - `site:docs.djangoproject.com/en/6.0/topics/async asynchronous support ORM transactions do not yet work async mode Django`
  - `site:docs.djangoproject.com/en/dev/internals/security Django security releases supported versions policy`
  - `site:dora.dev capabilities loosely coupled architecture software delivery performance teams`
  - `site:dora.dev research software delivery performance architecture documentation 2024`
  - `site:dora.dev/research 2024 documentation quality platform engineering developer productivity software delivery performance`
  - `site:github.blog engineering Django monolith architecture case study`
  - `site:gov.uk digital data profession capability framework technical architect role accountable technology strategy decisions stakeholders security`
  - `site:gov.uk technology code of practice choose technology open source total cost ownership avoid lock in`
  - `site:gov.uk/service-manual technical architect discovery business case security role`
  - `site:gov.uk/service-manual/technology choosing technology team skills recruitment capability maintain service`
  - `site:ieeexplore.ieee.org software architects responsibilities decisions stakeholders study`
  - `site:leaddev.com engineering leadership report 2024 technical debt architecture developer productivity survey`
  - `site:lp.jetbrains.com/python-developers-survey-2024 Django web development survey deployment cloud database`
  - `site:martinfowler.com architecture decision framework selection team skills reversibility`
  - `site:nist.gov Secure Software Development Framework software acquisition open source risk decision makers`
  - `site:openssf.org consuming open source software guide evaluate project security maintenance governance`
  - `site:queue.acm.org framework selection software architecture technical decision developer productivity`
  - `site:survey.stackoverflow.co 2024 developer survey Python web frameworks Django professional developers`
  - `site:survey.stackoverflow.co/2025 technology Python Django professional developers web frameworks asynchronous tools`
  - `site:thoughtworks.com technology radar framework adoption team skills architecture decision risk open source`
  - `site:www.djangoproject.com/download supported versions release roadmap LTS 2026`
  - `site:www.djangoproject.com/fundraising corporate members fellowship maintenance security Django`
  - `software architects decision making study stakeholders uncertainty architecture decisions empirical interview`
  - `technical debt software architects pressure tradeoffs qualitative study practitioners`
  - `technical leaders survey framework selection criteria hiring skills maintainability security open source software`
- Website domains:
  - `architecture.cddo.cabinetoffice.gov.uk`
  - `arxiv.org`
  - `assets.applytosupply.digitalmarketplace.service.gov.uk`
  - `assets.publishing.service.gov.uk`
  - `atlasgo.io`
  - `aws.amazon.com`
  - `baseline.openssf.org`
  - `best.openssf.org`
  - `blog.jetbrains.com`
  - `collectionscanada.gc.ca`
  - `cs.gmu.edu`
  - `csrc.nist.gov`
  - `ddat-capability-framework.service.gov.uk`
  - `deps.dev†deps.dev`
  - `djangoproject.com`
  - `docs.aws.amazon.com`
  - `docs.cloud.google.com`
  - `docs.djangoproject.com`
  - `docs.python.org`
  - `doi.org`
  - `dora.dev`
  - `en.wikipedia.org`
  - `engineering.fb.com`
  - `engineering.kraken.tech`
  - `forum.djangoproject.com`
  - `gartner.com`
  - `github.blog`
  - `gov.uk`
  - `governmentdigitalanddatahub.campaign.gov.uk`
  - `hakibenita.com`
  - `hodigital.blog.gov.uk`
  - `ijprems.com`
  - `insights.sei.cmu.edu`
  - `juta.co.za`
  - `kth.diva-portal.org`
  - `leaddev.com`
  - `learn.microsoft.com`
  - `lfprojects.org`
  - `link.springer.com`
  - `linuxfoundation.org`
  - `lists.openssf.org`
  - `lp.jetbrains.com`
  - `makimo.pl`
  - `members.ciisec.org`
  - `nascio.org`
  - `nist.gov`
  - `openssf.org`
  - `opus.cloud1.lib.uts.edu.au`
  - `orbilu.uni.lu`
  - `policy.openssf.org`
  - `portal.fis.tum.de`
  - `project-archive.inf.ed.ac.uk`
  - `python.org`
  - `reddit.com`
  - `repository.bilkent.edu.tr`
  - `research.chalmers.se`
  - `research.google`
  - `research.vu.nl`
  - `researchgate.net`
  - `robertoverdecchia.github.io`
  - `sciencedirect.com`
  - `scs4privatebeta.ddat-capability-framework.service.gov.uk`
  - `se.jku.at`
  - `sei.cmu.edu`
  - `shop.linuxnewmedia.com`
  - `sixfeetup.com.\n\n`
  - `sonarsource.com`
  - `survey.stackoverflow.co`
  - `thoughtworks.com`
  - `typing.readthedocs.io`
  - `wa.aws.amazon.com`

<!-- RESEARCH PROVENANCE: END -->
