# Experienced backend engineers evaluating or operating web systems

## Audience definition and boundaries

This audience comprises individual contributors with several years of professional responsibility for server-side software: data models and persistence, APIs, authentication and authorization, background work, integrations, testing, deployment, reliability, and production diagnosis. “Experienced” here means demonstrated responsibility for consequential backend systems, not a particular title, age, or fixed years-of-experience threshold. The audience includes engineers who have never used Django, engineers transferring from another backend stack, and engineers who already use or inherit Django but are not acting primarily as leads, architects, managers, or maintainers.

Excluded as primary members are first-time programmers, Python developers new to web development, people whose work is mainly frontend, and people whose main job in the decision is organizational approval. A staff engineer or architect may still write backend code, but when they set organization-wide standards or approve architecture they belong primarily in the technical-lead/architect lens. An existing Django user is a lifecycle segment that can overlap this role rather than a synonym for it.

This is primarily a **professional role plus experience lens**. It is not an organization type, industry, or Django lifecycle stage. Public data supports the relevance of experienced practitioners to Django—56% of the 2025 Django survey respondents reported at least six years of professional coding experience and 82% wrote Django professionally—but the survey recruited through DSF channels and therefore describes engaged Django users, not all experienced backend engineers ([Django Developers Survey 2025](https://lp.jetbrains.com/django-developer-survey-2025/), fielded November 2024–January 2025). **Direct evidence; Medium confidence** because of self-selection and audience-channel bias.

## Important subsegments

- **Django-naive, Python-capable evaluators:** understand backend architecture and perhaps Python, but must test whether Django's conventions, runtime model, ecosystem, and operational profile suit a real workload.
- **Backend engineers transferring from another language or framework:** can reason about web systems but must translate established mental models and assess the cost of changing language, tooling, and deployment habits.
- **Engineers inheriting an existing Django service:** the choice has already been made; their job is to form an accurate system model and change it safely.
- **Current Django practitioners starting a new service or major subsystem:** have productive habits and ecosystem knowledge but must avoid choosing from familiarity alone.
- **Performance-, async-, or integration-constrained engineers:** face a specific workload—high concurrency, latency sensitivity, streaming, websockets, large datasets, or a frontend/API contract—that may make some generic evidence irrelevant.
- **Solo technical deciders versus team recommenders:** some can choose directly; others produce the proof, trade-off analysis, or prototype on which a lead, architect, security reviewer, or manager decides.

These subsegments should not be ranked without primary research. The available evidence shows meaningful variation in role, team, and use: the 2025 Django survey had 67% working in teams, while respondents reported use for full-stack development (80%) and REST APIs with DRF (51%). **Direct evidence about current respondents; Medium confidence for segmentation, not market incidence.**

## Primary job to be done

> When I must start or substantially reshape a backend service, I want to determine which technical foundation fits the real workload and team constraints, so I can deliver useful software soon without creating unacceptable security, reliability, or maintenance risk.

This job is a **researcher inference with High confidence**. It is grounded in an industry-co-designed software-selection study that starts with a gap or opportunity, requires assessment against the business, organizational, technical, integration, quality, lifecycle, and cost context, and recommends realistic-context evaluation rather than feature comparison alone ([Bjarnason, Åberg & Ali, 2023](https://link.springer.com/article/10.1007/s10664-023-10288-w)). The inference is that a web framework is one such consequential software component; the study did not test Django or backend engineers as a discrete population.

## Additional jobs to be done

There are five important jobs in total, including the primary job.

1. **Choose a fitting foundation (primary).** When a new product, service, rewrite, or major capability creates an architectural choice, I want to evaluate the foundation against the actual workload and constraints, so I can ship without imposing avoidable lifecycle risk.
2. **Become safely productive in an inherited system.** When I join a Django team or take responsibility for an unfamiliar Django service, I want to map its conventions, extension points, dependencies, and operational failure modes, so I can make reliable changes without regressions. **Inference; Medium confidence.** The recurring upgrade and production practices in the Django survey establish the context, but direct interviews with inheriting engineers are absent.
3. **Resolve a fit or scaling uncertainty.** When latency, throughput, async I/O, database behavior, deployment, or integration requirements become material, I want evidence from a representative implementation, so I can decide whether to optimize, adapt the architecture, isolate a workload, or reconsider the foundation. **Inference; High confidence.** The software-selection research explicitly says performance must be tested in the target context; Django's own performance guidance says performance is multidimensional.
4. **Make a defensible technical recommendation.** When colleagues or leaders need a framework recommendation, I want to expose assumptions, trade-offs, evidence, and migration costs, so I can help the team reach a fact-based decision and stand behind its consequences. **Direct evidence for the general selection process; Medium confidence for the personal dimension.** Nearly half of 2025 Stack Overflow survey respondents had endorsed or influenced a technology choice in the prior year; 19.8% reported influencing a substantial stack addition ([Stack Overflow Developer Survey 2025, Work](https://survey.stackoverflow.co/2025/work)).
5. **Keep a production service supportable.** When releases, vulnerabilities, dependencies, and requirements continue to change, I want to upgrade and evolve the service at a manageable rate, so I can keep it secure, operable, and economical rather than face a forced migration. **Direct evidence for recurring upgrade behavior; Medium confidence for the inferred motivation.** In the Django survey, 48% upgraded every stable release, 27% on LTS releases, and 4% reported an unsupported version.

## Functional, emotional, and social dimensions

| Job | Core functional job | Emotional job | Social job | Supporting jobs |
|---|---|---|---|---|
| Choose a fitting foundation | Match application, team, and lifecycle requirements to a workable backend foundation | **Hypothesis:** reduce anxiety about an expensive, hard-to-reverse choice | **Hypothesis:** be seen as pragmatic rather than trend-driven or conservative by default | Elicit requirements; identify constraints; inspect ecosystem health; prototype; estimate operating and switching costs |
| Become safely productive | Build an accurate working model and deliver changes without regressions | **Hypothesis:** regain confidence and autonomy in an unfamiliar codebase | Earn trust from teammates and reviewers through safe changes (**inference**) | Trace requests and data; run tests; inspect configuration; learn local conventions and dependencies |
| Resolve fit/scaling uncertainty | Diagnose the actual bottleneck and validate remedies under representative load | Reduce fear that an architectural limit will surface after commitment (**hypothesis**) | Demonstrate engineering rigor to peers and operators (**hypothesis**) | Profile; benchmark; examine queries; test failure modes; consult operators and domain experts |
| Make a defensible recommendation | Turn evaluation evidence into a decision others can inspect | Feel confident bearing professional responsibility for the recommendation (**hypothesis**) | Preserve credibility with leads, security, operations, and peers (**hypothesis**) | Record assumptions; compare against requirements; disclose limitations; define rollback or exit conditions |
| Keep service supportable | Patch, upgrade, test, and simplify without destabilizing production | Reduce on-call and upgrade anxiety (**hypothesis**) | Be regarded as a responsible steward of shared systems (**hypothesis**) | Monitor releases; assess dependencies; automate tests; plan deprecations; document decisions |

The emotional and social dimensions are plausible but **Low-to-Medium confidence**: the selection study found value in objective, fact-based discussion and engineer satisfaction, but public evidence does not directly interview experienced Django evaluators about identity, confidence, or peer judgment.

## Triggering situations

**Event-triggered situations**

- A greenfield application, funded product, client engagement, or new backend service needs a foundation.
- A major feature—API, admin workflow, authentication, data-heavy operation, realtime interaction, or external integration—changes the workload shape.
- The engineer joins a team, inherits a service, or replaces someone with key system knowledge.
- A performance incident, security disclosure, unsupported dependency, production outage, or compliance review exposes risk.
- A framework/Python upgrade or a long-delayed dependency refresh becomes unavoidable.
- Hiring, team reorganization, or an organizational technology review requires the engineer to justify the current stack or investigate a change.

**Recurring situations**

- Shipping features while preserving correctness, security, and operability.
- Evaluating packages and integrations, reviewing architecture changes, and diagnosing database or runtime behavior.
- Tracking patch releases, deprecations, support windows, and ecosystem compatibility.
- Helping teammates and validating answers from documentation, community discussions, search, or AI tools.

The distinction is **inference, High confidence**. Django respondents' mixed stable/LTS upgrade patterns show the recurring maintenance cadence; general software-selection research directly describes gap/opportunity triggers. Exact prevalence and urgency require interviews.

## Desired outcomes

- Reduce elapsed time from architectural question to a decision supported by representative evidence.
- Reduce time to a production-capable first increment, not merely a local demo.
- Reduce the number of bespoke decisions and components needed for routine backend concerns where integrated conventions are appropriate.
- Reduce uncertainty about security support, backwards compatibility, dependency compatibility, and upgrade effort.
- Reduce defects and operational surprises during onboarding, change, deployment, and upgrade.
- Meet workload-specific latency, throughput, availability, data-integrity, and recovery requirements with acceptable resource cost.
- Increase the percentage of the system the team can understand, test, observe, and modify confidently.
- Increase confidence that relevant developers can be onboarded and that knowledge is not concentrated in one person.
- Preserve an affordable exit path if assumptions change.

These are **inferred directional outcomes; Medium-to-High confidence**. No reviewed source establishes universal thresholds, and raw throughput is not a substitute for context. The 2023 selection study explicitly cautions that criteria and priorities depend on the usage environment.

## Current behaviour or status quo

Experienced engineers commonly begin with the team's current language, deployment platform, internal libraries, and proven architecture. They supplement memory and peer advice with search, technical documentation, public source repositories, Q&A, and increasingly AI, then validate consequential claims with human or primary sources. In Stack Overflow's 2025 survey, 82% of respondents visited Stack Overflow at least a few times a month; public GitHub was used as a community platform by 66.9%. Experienced respondents were the least likely to “highly trust” AI output (2.6%) and the most likely to “highly distrust” it (20%), which supports a verification job, not an inference that they avoid AI altogether ([2025 survey overview](https://survey.stackoverflow.co/2025/)). **Direct evidence across developers; Medium confidence for experienced backend engineers specifically.**

Within the self-selected Django audience, current behavior is heterogeneous: 59% start new Django projects from scratch, 48% upgrade every stable release and 27% on LTS releases, 63% use type hints, 37% use ASGI, and 14% use Django async views. Most respondents use Django for both work and personal/educational/side projects (70%). This suggests evaluation is shaped by accumulated practice as well as formal work requirements. It does **not** show why non-users reject Django.

The status quo for an inherited system is usually continued incremental maintenance rather than replacement. That statement is a **Medium-confidence inference** from switching costs and recurring upgrade behavior; no representative Django migration dataset was found.

## Pushes

- Delivery pressure exposes the cost of assembling, integrating, and maintaining many separate backend decisions.
- A legacy or bespoke stack slows safe change, onboarding, patching, or operational diagnosis.
- Security incidents, support expiry, deprecations, and incompatible dependencies make “do nothing” riskier.
- Repeated authentication, admin, data-model, forms, permissions, or API work creates demand for coherent conventions and reusable components.
- Performance or reliability problems create pressure to replace intuition with profiling and representative testing.
- An unfamiliar inherited service makes authoritative technical guidance and a comprehensible execution model urgent.

These are **inferences, Medium confidence**. The evidence establishes the selection and maintenance contexts, but not how often each push initiates Django evaluation.

## Pulls

- A coherent Python web stack can reduce integration work and architectural choice for applications whose needs align with its conventions. In the 2025 Django survey, models (68%), admin (48%), migrations (30%), and authentication (28%) were among respondents' favorite core components. **Direct evidence of current-user preference; Medium confidence as pull for evaluators.**
- A mature production history and a broad body of operational knowledge can lower uncertainty. Instagram's 2017 engineering keynote named productivity, practicality, team growth, popular language, and maturity of Python/Django as valued qualities, while describing substantial custom scaling work; its 2019 PyCon session described a million-line, thousand-endpoint Django application and tooling needed to manage its complexity. **Direct organizational account; Medium confidence as an existence proof, Low confidence for transferability.**
- Predictable release and security processes can support lifecycle planning. Django documents roughly eight-month feature releases, backwards-compatible patch releases, and typically three-year LTS security/data-loss support. **Direct project fact; High confidence about policy, not perceived value.**
- Compatibility with both server-rendered applications and API work broadens possible use. Current Django respondents report both patterns, but this is usage evidence rather than proof of suitability for every backend.
- Familiar Python skills, existing packages, and team experience can shorten evaluation and onboarding. **Inference; Medium confidence**, supported indirectly by language-ecosystem selection research that includes developer availability and consistent documentation.

## Anxieties

- **Performance and scalability:** whether Python/runtime overhead, ORM use, or architectural coupling can meet latency and throughput targets economically. A famous large deployment shows possibility, not effortless or universal fit.
- **Async and realtime fit:** whether the complete request path and required libraries are async-capable. Django 6.0 documents an async request stack under ASGI but also thread adaptation and performance costs when synchronous middleware is present ([Django async documentation](https://docs.djangoproject.com/en/6.0/topics/async/), current documentation). This is a legitimate fit question, not merely a misconception.
- **Typing and refactor safety:** 63% of Django survey respondents used type hints and 84% favored adding type hints to core; the latter question may be leading, a concern participants themselves raised in the survey feedback thread. Treat typing demand as a signal, not a market estimate.
- **Framework “weight” and coupling:** whether integrated conventions accelerate this application or constrain a narrow service and make later replacement harder.
- **Ecosystem lifecycle:** whether critical third-party packages keep pace with Django and Python releases. Django's upgrade guidance explicitly notes that poorly maintained dependencies may lag a new Django version.
- **Operational responsibility:** whether deployment, security configuration, observability, background work, and failure recovery are sufficiently understood. Django's deployment checklist makes clear that settings and infrastructure choices remain the deployer's responsibility.
- **Professional accountability:** being blamed for selecting a familiar or unfashionable technology without enough evidence. **Hypothesis; Low confidence** pending interviews.

## Habits and inertia

- Existing language expertise, internal templates, libraries, CI/CD, observability, deployment platforms, and security controls favor the current stack.
- Team familiarity reduces near-term delivery risk even if another option looks attractive in isolation.
- Sunk cost in domain models, tests, APIs, integrations, and operational playbooks makes a rewrite expensive and risky.
- Current hiring pipelines and peer support make established organizational standards easier to defend.
- Experienced engineers develop trusted heuristics and preferred architectures; these speed decisions but can cause both appropriate conservatism and familiarity bias.
- Current Django practitioners have reusable knowledge of the ORM, settings, middleware, packages, and upgrades, encouraging continued use where fit remains adequate.

The 2023 selection model directly treats the existing technical ecosystem, organizational processes, lifecycle, culture, and integration as constraints. Application to Django is **inference, High confidence**; relative strength of each habit is unknown.

## Decision criteria

Only the first group below is ranked because evidence allows it. Stack Overflow's 2025 survey ranked criteria across all respondents, not experienced backend engineers alone. For **work projects**, robust/complete API ranked first, reputation for quality second, easy-to-use API third, reliability/low latency fourth, manageable cost fifth, open-source connection sixth, customizable/manageable codebase seventh, public image eighth, and AI integration ninth. Security/privacy was the top overall rejection reason. **Direct evidence; Medium confidence for this audience.**

Context-dependent criteria that should not be globally ranked are:

- **Functional fit:** data model, authentication/authorization, admin/workflow, API, background work, realtime needs, and integrations. **High likely importance; High confidence.**
- **Maintainability and evolvability:** comprehensibility, testability, typing/tool support, backwards compatibility, deprecation policy, upgrade effort, and dependency health. **High likely importance; High confidence.**
- **Security and compliance:** default protections, disclosure/patch process, configuration burden, dependency exposure, and auditability. **High likely importance; High confidence.**
- **Performance and operability:** realistic latency/throughput/resource use, database behavior, observability, deployment model, failure recovery, and on-call burden. **Importance varies by workload; High confidence.**
- **Ecosystem and support:** package maturity, maintainership, documentation reliability, peer expertise, and availability of paid help where needed. **Medium-to-high likely importance; Medium confidence.**
- **Team and organizational fit:** Python skill, onboarding time, existing standards, platform compatibility, and hiring. **High in organizational contexts; High confidence.**
- **Total cost and reversibility:** delivery, hosting, integration, maintenance, migration, and exit costs. **High for long-lived systems; Medium-to-high confidence.**

The breadth is supported by the 2023 empirical selection model, which found technical-only comparison insufficient and organized criteria across market strength, culture/strategy, productivity, quality, integration, cost, legal/ethical aspects, and control.

## Main concerns

**Practical concerns:** time to a representative proof, production deployment knowledge, dependency compatibility, database/query behavior, async boundaries, testing, observability, and availability of colleagues who can maintain the result.

**Legitimate limitations:** not every workload benefits from a full-stack framework; synchronous components can reduce the benefit of an async stack; ORM abstractions do not remove the need for database knowledge; integrated conventions may be excess coupling for a narrowly scoped service; third-party packages have independent support policies.

**Internal organizational concerns:** an approved language/platform standard, security review, support ownership, skills/hiring, roadmap compatibility, and the opportunity cost of introducing another stack.

**Personal concerns (hypotheses):** protecting credibility, avoiding avoidable on-call burden, and not losing hard-won expertise while learning a new ecosystem. **Low confidence** until directly studied.

## Objections and perceived risks

- **“Django cannot scale.”** Overgeneralized. Instagram provides a strong counterexample to impossibility, but its custom sharding, multi-datacenter work, and large-scale tooling also show that scale requires engineering. The correct question is fit and cost under the target workload. **Part misconception, part legitimate concern.**
- **“Django's batteries solve production security.”** Misleading. Django supplies security mechanisms and a security-release process, but the deployment checklist requires correct secrets, HTTPS, host, cookie, logging, and server configuration. **Misconception with a legitimate configuration-risk core.**
- **“A mature framework is automatically obsolete.”** Unsupported as a rule. The broader 2025 developer survey does identify outdated/obsolete technology as a rejection factor, while current Django respondents show professional use and active upgrades. Whether Django is current enough for a particular requirement still needs evidence. **Perceived risk, not resolved globally.**
- **“Integrated conventions necessarily reduce maintenance.”** Not always. They can reduce assembly and local variation, but misfit, framework coupling, and unfamiliar abstractions can increase costs. **Legitimate trade-off.**
- **“A synthetic benchmark decides framework suitability.”** Too narrow. The empirical selection study says performance must be measured with realistic users, data, hardware, and context; maintainability, integration, security, and lifecycle also matter. **Misconception.**
- **“Framework choice is the engineer's decision alone.”** Often false in organizational settings; technical leads, platform/SRE, security, managers, product constraints, and procurement/legal can influence or block. **Organizational objection and segmentation warning.**

## Information needed to make progress

- A precise suitability model: application shapes that align well, conditional fits, and requirements that demand careful validation.
- Supported-version, security, backwards-compatibility, release-cadence, and deprecation facts.
- The production responsibility boundary: what the framework handles versus what application, database, infrastructure, and operators must handle.
- Representative architecture and operational evidence, including constraints and custom work—not just organization names.
- Workload-specific evidence on database access, async boundaries, concurrency, latency, memory, background work, and deployment.
- API and integration behavior, including typing/tooling, testing, schema/documentation, and frontend or service boundaries.
- Third-party dependency activity, compatibility, ownership, release history, and feasible substitutes or exit paths.
- Upgrade and migration feasibility for the engineer's actual starting point.
- Team evidence: onboarding effort, Python/Django availability, internal support ownership, and compatibility with organizational standards.
- A reproducible path to a proof of concept and criteria for deciding whether the result is good enough.

This describes needs, not whether Django presently supplies them. **Inference; High confidence** from the software-selection model and observed developer decision criteria.

## Trusted content formats

- **Versioned technical documentation and reference material** answer exact API, compatibility, deployment, security, and upgrade questions. DORA research links documentation clarity, findability, and reliability to stronger technical practice and organizational performance ([DORA, Documentation quality](https://dora.dev/capabilities/documentation-quality/), based on 2021–2022 research). This supports the format's importance, not any assessment of Django's documentation.
- **Runnable examples and small proofs of concept** test mental-model fit, integration, and developer effectiveness. The 2023 selection study explicitly identifies prototypes/demonstrations as a way to assess engineer satisfaction and effectiveness.
- **Source code, issue history, release history, and package metadata** validate maintenance and implementation claims. Public GitHub's high reported community use supports reach, while trust for any specific signal remains unmeasured.
- **Detailed engineering talks and postmortems** validate production claims when they include workload, architecture, constraints, incidents, and custom work. Instagram's 2017 and 2019 talks are examples of direct operational accounts, not representative outcome studies.
- **Benchmarks with code and methodology** answer narrow performance questions when the workload is representative; unexplained headline charts do not complete the job.
- **Peer review and direct conversation with practitioners/operators** help expose local constraints and tacit failure knowledge. This is **Medium-confidence inference**; the Django survey shows friends/coworkers are used for learning by 13%, but does not measure trust by seniority.
- **Long-form technical articles and decision records** let engineers inspect assumptions and trade-offs. Stack Overflow's 2025 content-preference data shows long-form articles desired by 40.8% overall, but it is not backend- or experience-specific.

## Discovery, evaluation, validation, and engagement channels

**Discovery:** general web search, Stack Overflow, public GitHub, coworkers, Python/backend communities, Reddit, Hacker News, conference talks, and AI-assisted search can surface candidate approaches. Stack Overflow reports frequent site visitation across its sample and broad use of public GitHub, YouTube, and Reddit as community platforms; it also shows experienced developers verify AI more cautiously. Their role is candidate discovery and problem orientation, not final proof.

**Evaluation:** versioned official technical documentation; source and issue repositories; package registries; release/security policies; reproducible examples; and a local proof against representative requirements. Their role is to establish facts, inspect implementation and lifecycle, and measure fit. The selection study provides the strongest behavioral rationale for this stage.

**Validation:** trusted colleagues, Django/Python practitioners with comparable production constraints, security/SRE/database reviewers, detailed production accounts, and reproducible load or integration tests. Their role is to challenge assumptions and test transferability. Production logos or isolated social comments are weak validation without context.

**Ongoing engagement:** release notes and security announcements for maintenance; Stack Overflow/search for bounded problems; issue trackers and forums for unresolved behavior; newsletters/blogs/podcasts/talks for ambient awareness; local or conference communities for deeper peer learning. The 2025 Django survey reports following Django via djangoproject.com (60%), YouTube (22%), Stack Overflow (18%), Reddit (18%), Django Forum (15%), newsletter (12%), friends (9%), Hacker News (8%), podcasts (7%), and X (7%). It reports preferred learning via djangoproject.com (79%), Stack Overflow (39%), AI tools (38%), YouTube (38%), blogs (33%), books (22%), friends/coworkers (13%), and podcasts (5%). **Direct evidence among DSF-channel respondents; Medium confidence.** Event reach should not be overstated: 71% reported never attending a Django-related event, 21% a small/local event, and 8% a DjangoCon-scale event.

## Decision-makers and influencers

- **Initiator:** product need, incident, inherited system, engineer, lead, or architect may create the evaluation.
- **Researcher/evaluator:** the experienced backend engineer often translates requirements, prototypes, inspects implementation, and estimates delivery/operating cost.
- **Influencers:** backend peers, frontend/API consumers, database engineers, SRE/platform staff, security/compliance, and experienced Django/Python practitioners.
- **Approver:** in a small team the engineer may decide; otherwise a tech lead, architect, engineering manager, CTO, or architecture review body approves.
- **Potential blockers:** security/compliance, platform standards, operations/support ownership, procurement/legal for commercial dependencies, and teams that must integrate or maintain the result.
- **Users after decision:** backend engineers plus adjacent frontend, QA, data, operations, support, and product teams.
- **Consequence bearers:** engineers and operators carry defect/on-call/upgrade costs; the organization and end users carry delivery, outage, security, and switching consequences.

This map is **inference, High confidence** for organizational software selection. The 2023 study explicitly names developers, architects, line managers, legal/financial experts, and technical experts as stakeholders; role allocation varies by organization.

## Appropriate next actions for Django to encourage

These are progression steps, not the underlying jobs and not prescriptions for particular marketing assets.

1. **Classify the intended application and constraints.** This connects to the primary job by preventing a framework-first decision before workload, security, team, and lifecycle requirements are explicit.
2. **Verify lifecycle and production-responsibility facts.** Review support, security, compatibility, deployment, and upgrade behavior relevant to the project. This reduces maintenance and operational uncertainty.
3. **Trace one representative vertical slice.** Build or inspect a small slice covering the project's real data model, authentication, API/UI boundary, tests, and deployment path. This tests mental-model and integration fit.
4. **Run a time-bounded proof of concept with decision criteria.** Include the riskiest query, concurrency pattern, integration, or operational concern. This connects directly to resolving fit uncertainty.
5. **Seek review from the people who will operate, secure, integrate, and approve it.** This turns an individual experiment into a defensible team decision.
6. **For an inherited system, complete a safe first change and support assessment.** Map versions/dependencies, run tests and deployment checks, then deliver a bounded change. This serves the onboarding job better than asking for immediate advocacy or contribution.
7. **For current practitioners, choose an evidence-based upgrade/maintenance cadence.** This serves continued supportability. Contribution or community participation may follow only if a separate participation job appears.

## Overlaps with other audiences

- **Python developers new to web:** both may learn Django, but experienced backend engineers already understand HTTP, databases, production risk, and architecture; their learning job is translation and fit validation.
- **Full-stack developers:** overlap when one person owns browser and server concerns; this lens centers backend and production consequences.
- **Technical leads and architects:** overlap in evaluation and recommendation; leads/architects have broader standard-setting and cross-team accountability.
- **CTOs/engineering managers:** may approve and bear business consequences; the engineer supplies technical evidence and often bears implementation/on-call consequences.
- **Start-ups, large organizations, agencies, and regulated industries:** these are contexts that change constraints and the decision system, not alternative descriptions of the engineer.
- **Existing Django users:** lifecycle overlap; not every experienced backend engineer is a Django user, and not every Django user is experienced.
- **Former Django users:** may bring high-specificity switching evidence and established objections.
- **Package maintainers and contributors:** an engineer may participate, but maintaining public infrastructure is a different job relationship.

## Possible segmentation problems

“Experienced backend engineers” is too broad for prioritization by itself. Experience does not reveal Django familiarity, Python familiarity, decision authority, workload, organizational constraint, or whether the task is greenfield, inheritance, recovery, or migration. It also risks the stereotype that seniority automatically means architectural authority or a preference for terse technical content.

Consider splitting research recruitment along three primary axes:

1. **Lifecycle/job context:** greenfield evaluator; inheriting operator; scaling/fit investigator; current Django maintainer; returning/former evaluator.
2. **Decision role:** sole decider; technical evaluator/recommender; implementation user without approval authority.
3. **Constraint profile:** conventional data-centric web application; API-centered system; async/realtime or latency-sensitive workload; regulated/high-assurance environment; constrained legacy/platform integration.

Python familiarity is a useful fourth axis. Organization size and industry should remain contextual variables unless evidence shows distinct jobs. **Inference; High confidence** that the current label hides materially different jobs; the best final cuts require primary interviews.

## Existing-analysis claim audit

| Existing claim relevant to this lens | Assessment | Audit note |
|---|---|---|
| Existing professional Django developers seek current best practice, releases/upgrades, scaling help, greater expertise, and possible progression from user to contributor. | **Partially supported** | Direct evidence supports professional use, recurring upgrades, performance/async questions, and ongoing learning channels. “Greater expertise” is broad. User-to-contributor progression was not established for experienced backend engineers and is a separate participation job. |
| A mid-to-large-company “marketing executive or technical decision-maker” approves framework standards based on currency, long-term reliance, community/support, security, and hiring. | **Partially supported** | Security/privacy, quality, API, reliability, lifecycle, ecosystem, integration, and developer availability are supported criteria. Developers frequently influence technology choices. A “marketing executive” as framework approver is unsupported here; approval roles vary and are more often technical/managerial review roles in the evidence. |
| Enterprise examples, production architecture, and testimonials influence technical decisions. | **Partially supported** | Detailed production accounts and realistic demonstrations can validate fit. Generic names or testimonials without workload and constraints are not shown to influence experienced engineers. |
| Existing developers are comfortable with ORM, DRF, class-based views, Celery, and deployment. | **Requires further research** | The Django survey shows use of DRF, Celery, databases, cloud, and deployment-related tools, but does not establish competence or comfort. “Existing developer” also spans wide experience levels. |
| Existing Django developers find scaling solutions as their company grows. | **Requires further research** | Scaling/fit investigation is plausible and supported by production accounts, but no representative evidence shows company growth is the usual trigger or that this job applies to most existing users. |
| Claimed channels include docs/release notes, forums/Discord, GitHub/issue tracker, mailing lists, conferences/sprints, podcasts, professional peer networks, and short-form social. | **Partially supported** | Documentation/site, Stack Overflow, public GitHub, forums, YouTube, Reddit, Hacker News, newsletters, podcasts, friends/coworkers, and events have behavioral evidence, though most is not experience-specific. Event and podcast reach is modest in the Django survey. No reviewed evidence validates Discord, mailing lists, sprints, LinkedIn/professional networks, or short-form social as important for this segment. |
| New-developer homepage/social/video behavior also describes experienced backend evaluators. | **Unsupported** | The evidence explicitly shows experience differences in AI trust and YouTube community use. No evidence supports treating early-career discovery behavior as transferable to experienced backend engineers. |

Claims about donors, sponsors, educators, and contributor recognition are outside this audience lens and are not audited here.

## Evidence table

| Finding | Source (title, publisher/author, date, URL) | Evidence type | Direct evidence or inference | Confidence | Research notes |
|---|---|---|---|---|---|
| Experienced practitioners are a large part of the engaged Django respondent base; professional use and team work are common. | *Django Developers Survey 2025 Results*, DSF & JetBrains/PyCharm, fielded Nov 2024–Jan 2025, published 2025, [link](https://lp.jetbrains.com/django-developer-survey-2025/) | Self-selected survey, 4,655 filtered responses | Direct | Medium | 56% had 6+ years professional experience; 82% wrote Django professionally; recruited only through DSF channels, so not a market sample. |
| Django is used across full-stack and API contexts, with varied databases, async tools, queues, cloud, and team settings. | *Django Developers Survey 2025 Results*, DSF & JetBrains/PyCharm, 2025, [link](https://lp.jetbrains.com/django-developer-survey-2025/) | Self-selected survey | Direct | Medium | Supports heterogeneity and concrete use, not comparative superiority or suitability for every workload. |
| Django users follow different stable/LTS upgrade cadences; a minority report unsupported versions. | *Django Developers Survey 2025 Results*, DSF & JetBrains/PyCharm, 2025, [link](https://lp.jetbrains.com/django-developer-survey-2025/) | Self-selected survey | Direct | Medium | 48% every stable release, 27% LTS, 4% unsupported. Motivation inferred. |
| Models, admin, migrations, and auth are valued integrated components among respondents. | *Django Developers Survey 2025 Results*, DSF & JetBrains/PyCharm, 2025, [link](https://lp.jetbrains.com/django-developer-survey-2025/) | Self-selected survey | Direct | Medium | Favorite-component shares support current-user pull, not evaluator conversion. |
| Typing is materially relevant to engaged Django users, but survey design may inflate certainty. | *Django Developers Survey 2025 Results*, DSF & JetBrains/PyCharm, 2025, [link](https://lp.jetbrains.com/django-developer-survey-2025/); *2024 Django Developers Survey* feedback, Django Forum participants, Nov 2024–Jan 2025, [link](https://forum.djangoproject.com/t/2024-django-developers-survey/36657) | Survey plus qualitative forum feedback | Direct signal | Medium-Low | 63% use hints; 84% favored core hints. Forum participants called some questions leading/limited; isolated feedback is not representative. |
| Software selection should begin with the need and usage environment and consider technical, organizational, business, ecosystem, lifecycle, quality, integration, and cost criteria. | *Software selection in large-scale software engineering*, Bjarnason, Åberg & Ali, *Empirical Software Engineering*, 28 Feb 2023, [link](https://link.springer.com/article/10.1007/s10664-023-10288-w) | Peer-reviewed rapid reviews, industry co-design, focus group, case application | Direct; applied to Django by inference | High | Strong method fit; validation centered on one large company and is not framework-specific. |
| Representative prototypes and realistic-context performance tests support better evaluation. | Same Bjarnason et al. study, 28 Feb 2023, [link](https://link.springer.com/article/10.1007/s10664-023-10288-w) | Peer-reviewed empirical/design study | Direct; Django action inferred | High | Study explicitly recommends prototyping and target-context performance assessment. |
| Developers commonly influence technology decisions; work-project endorsement emphasizes API completeness/usability, quality, reliability/latency, and cost, while security/privacy is a top rejection reason. | *Stack Overflow Developer Survey 2025 — Work*, Stack Overflow, 2025, [link](https://survey.stackoverflow.co/2025/work) | Large self-selected developer survey | Direct | Medium | 48% endorsed/influenced a choice; criteria are all-developer results, not backend/experience cross-tabs. |
| Experienced developers use AI but are more cautious about its accuracy, supporting a human/primary-source verification job. | *Stack Overflow Developer Survey 2025*, Stack Overflow, 2025, [link](https://survey.stackoverflow.co/2025/) | Large self-selected developer survey | Direct | Medium | Experienced had lowest high-trust and highest high-distrust rates. Stack Overflow sample and wording can bias results. |
| Stack Overflow, public GitHub, YouTube, Reddit, technical sites, and long-form articles have observable roles in developer information behavior. | *Stack Overflow Developer Survey 2025*, Stack Overflow, 2025, [link](https://survey.stackoverflow.co/2025/) | Large self-selected developer survey | Direct; stage role inferred | Medium | Broad developer evidence, not Django-specific. Platform use does not equal trust or decision influence. |
| Engaged Django users report official technical resources, Stack Overflow, AI, YouTube, blogs, forums, Reddit, newsletters, podcasts, and events at very different rates. | *Django Developers Survey 2025 Results*, DSF & JetBrains/PyCharm, 2025, [link](https://lp.jetbrains.com/django-developer-survey-2025/) | Self-selected survey | Direct | Medium | Useful for ongoing behavior; only 29% had attended any Django-related event. Does not cleanly separate discovery/evaluation. |
| Django can operate at very large scale, but doing so may involve substantial custom infrastructure and codebase tooling. | *Python @ Instagram*, Lisa Guo & Hui Ding, PyCon 2017, 20 May 2017 / posted 7 Jun 2017, [slides/transcript](https://speakerdeck.com/pycon2017/keynote-lisa-guo-and-hui-ding-python-at-instagram); *Python @Scale: An Instagram Story*, Padmarao, Woodruff & Meyer, PyCon US, May 2019, [program](https://us.pycon.org/2019/schedule/presentation/372/) | First-party engineering conference accounts | Direct case evidence | Medium | Strong impossibility counterexample; one exceptional organization, older evidence, not a general cost/performance guarantee. |
| Django has an async request stack under ASGI but sync components can impose adaptation and performance costs. | *Asynchronous support*, Django documentation, current 6.0 docs, accessed 18 Jul 2026, [link](https://docs.djangoproject.com/en/6.0/topics/async/) | Primary project documentation | Direct fact | High | Supports legitimate fit questions; project-controlled source is appropriate for behavior. |
| Production security, performance, and operations still require explicit configuration and review. | *Deployment checklist*, Django documentation, current development docs, accessed 18 Jul 2026, [link](https://docs.djangoproject.com/en/dev/howto/deployment/checklist/) | Primary project documentation | Direct fact | High | Shows responsibility boundary; does not measure ease or comparative security. |
| Release cadence, patch compatibility, and LTS windows are explicit enough to support lifecycle planning. | *Django's release process*, Django documentation 6.0, accessed 18 Jul 2026, [link](https://docs.djangoproject.com/en/6.0/internals/release-process/) | Primary project policy | Direct fact | High | Policy says roughly eight-month feature cadence and typically three-year LTS; actual project capacity perception still unmeasured. |
| Dependency maintenance can complicate upgrades. | *How to upgrade Django to a newer version*, Django documentation, current dev docs, accessed 18 Jul 2026, [link](https://docs.djangoproject.com/en/dev/howto/upgrade-version/) | Primary project guidance | Direct fact | High | Explicitly notes lag from poorly maintained dependencies; frequency/severity unknown. |
| Performance is multidimensional and database work should be profiled rather than assumed. | *Performance and optimization* and *Database access optimization*, Django documentation, accessed 18 Jul 2026, [performance](https://docs.djangoproject.com/en/6.0/topics/performance/), [database](https://docs.djangoproject.com/en/dev/topics/db/optimization/) | Primary technical guidance | Direct fact; job implication inferred | High | Appropriate factual source; does not establish Django's performance relative to alternatives. |
| Documentation clarity, findability, and reliability amplify technical practices and organizational performance. | *Documentation quality*, DORA/Google Cloud, underlying 2021–2022 research, current capability page accessed 18 Jul 2026, [link](https://dora.dev/capabilities/documentation-quality/) | Cross-industry survey/model research summary | Direct general evidence; format implication inferred | Medium-High | About internal documentation and organizational performance, not Django evaluation specifically. |
| Programming-language ecosystem selection depends on application/environment; developer availability and consistent documentation are among relevant criteria. | *A decision model for programming language ecosystem selection: Seven industry case studies*, Farshidi, Jansen & Deldar, *Information and Software Technology* 139, 2021, [repository record](https://dspace.library.uu.nl/handle/1874/420503) | Peer-reviewed seven-company case study | Direct general evidence; Django application inferred | Medium-High | Supports multi-criteria evaluation and team/context fit; not web-framework-specific. |

## Unanswered research questions

1. Which events actually trigger experienced backend engineers to consider Django: greenfield work, inheritance, Python adoption, a framework failure, team change, or client/management request?
2. How do Django-naive experienced engineers describe its category and suitability before exposure, and which beliefs change after a representative proof?
3. Which criteria become decisive for conventional data-centric applications versus API-only, realtime/async, high-throughput, data-intensive, or regulated workloads?
4. What evidence do engineers require before trusting claims about maintainability, security, performance, ecosystem health, and hiring—and what makes a production account transferable?
5. Who actually approves or blocks framework choices across small teams, large organizations, agencies, and regulated environments? How often is the backend engineer the decider versus recommender?
6. What is the observed time and failure pattern for experienced engineers transferring from other backend stacks into Django?
7. Why do current Django teams upgrade every stable release, LTS-to-LTS, or remain unsupported? What costs and anxieties distinguish those groups?
8. How often do typing, async boundaries, ORM behavior, or package maintenance cause rejection, architectural isolation, or migration rather than local mitigation?
9. Which former users left Django, what job had changed, and what evidence would make them re-evaluate? Public migration evidence is especially sparse.
10. How do experienced engineers combine documentation, source, peers, Q&A, conference material, and AI across discovery, evaluation, and validation? Existing surveys measure use more often than trust or causal influence.
11. Which emotional/social jobs—credibility, fear of on-call burden, desire to appear current, or pride in pragmatic stewardship—are real, and which are researcher projections?
12. What outcomes can be measured without reducing framework fit to delivery speed or synthetic throughput—for example onboarding time, upgrade effort, incident load, change failure, and dependency risk?

The highest-priority evidence gap is **direct comparative interviews around recent real decisions**: experienced engineers who adopted Django, rejected it after evaluation, inherited it, stayed with it through a major change, or left it. The present report has strong evidence for the general selection method and current Django-user behavior, but only medium or low evidence for causal motivations among prospective experienced backend engineers.

<!-- RESEARCH PROVENANCE: BEGIN -->
## Research provenance

This section was generated from the recorded Codex session JSONL logs. File attribution uses successful patch events; searches and domains use nested web-tool calls.

### Session `019f7538-5de7-70c0-82a5-cc4a4c888a75`
- Log: `rollout-2026-07-18T14-34-16-019f7538-5de7-70c0-82a5-cc4a4c888a75.jsonl`
- This document: `add, update`
- Search queries:
  - `2025 Django Developers Survey results JetBrains Django REST API backend developers upgrade versions`
  - `Django adoption migration engineering blog why Django backend architecture case study`
  - `Django forum experienced developers concerns async typing 2024 survey`
  - `Django migration away engineering blog async typing performance`
  - `Instagram engineering Django scale PyCon talk database 2017 engineering decision`
  - `Stack Overflow Developer Survey 2025 professional developers learning information sources documentation Stack Overflow AI trust`
  - `backend developer technology selection decision criteria survey 2024`
  - `developer framework selection survey maintainability security performance documentation ecosystem backend engineers`
  - `engineering blog chose Django backend why startup mature framework case study`
  - `site:cloud.google.com devops state 2024 developer experience documentation quality`
  - `site:docs.djangoproject.com Django performance database optimization official`
  - `site:docs.djangoproject.com deployment checklist Django security performance official`
  - `site:docs.djangoproject.com supported versions security release process Django official`
  - `site:dora.dev research documentation quality developer performance 2023`
  - `site:www.djangoproject.com security releases process Django supported versions LTS`
  - `software developers framework selection criteria empirical study maintainability documentation ecosystem security`
- Website domains:
  - `arxiv.org`
  - `blog.algosmiths.com`
  - `blog.jetbrains.com`
  - `bth.diva-portal.org`
  - `cloud.google.com`
  - `cncf.io`
  - `code.djangoproject.com`
  - `computing.co.uk`
  - `conf42.github.io`
  - `creativecommons.org`
  - `cs.cmu.edu`
  - `dam-cdn.atl.orangelogic.com`
  - `digikogu.taltech.ee`
  - `diva-portal.org`
  - `djangoproject.com`
  - `djangostars.com`
  - `docker.com`
  - `docs.djangoproject.com`
  - `doi.org`
  - `dora.dev`
  - `dspace.library.uu.nl`
  - `en.wikipedia.org`
  - `engineering.fb.com`
  - `er.ucu.edu.ua`
  - `escholarship.org`
  - `eurekamag.com`
  - `forum.djangoproject.com`
  - `ideas.repec.org`
  - `itpro.com`
  - `jetbrains.com`
  - `link.springer.com`
  - `lp.jetbrains.com`
  - `openurl.ebsco.com`
  - `papansarkar.com`
  - `pypy.org`
  - `pyvideo.org`
  - `reddit.com`
  - `research.wur.nl`
  - `resourcifi.com`
  - `sciencedirect.com`
  - `scitepress.org`
  - `speakerdeck.com`
  - `stackoverflow.blog`
  - `stackoverflow.co`
  - `survey.stackoverflow.co`
  - `techradar.com`
  - `tore.tuhh.de`
  - `trepo.tuni.fi`
  - `us.pycon.org`
  - `usenix.org`
  - `utupub.fi`
  - `yuriysokolov.ru`

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
