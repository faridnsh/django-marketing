# Full-stack web developers responsible for end-to-end delivery

## Audience definition and boundaries

This audience consists of developers expected to move a web feature across browser interface, server behavior, data, testing, and often deployment or production diagnosis. “Full-stack” is therefore a **work context and responsibility boundary**, not evidence that one person is equally expert in every layer. In Stack Overflow’s 2025 survey, 27% selected full-stack, its largest developer-role category, with experience ranging from 1–5 years (28.2%) and 6–10 years (24.4%) to much longer careers ([Stack Overflow Developer Survey, 2025](https://survey.stackoverflow.co/2025/developers)). (Direct evidence; confidence: High for that self-selected survey population, Medium externally.)

The audience includes people evaluating a framework and those inheriting or extending an existing stack. It excludes presentation-only, API-only, and operations-only developers unless they bear cross-layer delivery consequences, and excludes non-technical economic buyers. A senior full-stack developer may still research, recommend, or veto a framework.

The Django label is not the boundary. The 2025 Django Developers Survey found 80% of respondents used Django for full-stack development and 51% for REST APIs; 82% said they wrote Django professionally. It also found a multi-technology reality: 70% used JavaScript in addition to Python, 64% HTML/CSS, 44% SQL, and 27% TypeScript ([Django Developers Survey 2025](https://lp.jetbrains.com/django-developer-survey-2025/), results published October 31, 2025; responses collected November 2024–January 2025). This directly supports treating full-stack Django work as cross-technology work rather than “Python developers who also make pages.” Confidence: High for engaged Django users; the survey was distributed through official Django channels and cannot describe unaware or rejecting evaluators.

## Important subsegments

- **Solo builders, founders, and freelancers:** one person may initiate, evaluate, approve, implement, deploy, and support the stack. Breadth, cost, time-to-working-product, and recoverability dominate.
- **Small product-team generalists:** developers share end-to-end ownership in teams where handoffs are limited. The Django survey’s largest team band was 2–7 people (59%), a useful direct signal for current Django users, not a universal full-stack distribution.
- **Cross-functional product developers in larger organizations:** they implement across layers but framework choice may be constrained by architecture, security, platform, procurement, or hiring standards. They are influential evaluators, not necessarily approvers.
- **Front-end-leaning and back-end-leaning full-stack developers:** both accept cross-layer responsibility, but their learning burden and perceived seams differ. A React/TypeScript specialist approaching Django has a different job from a Python/Django developer adding richer interaction.
- **Early-career portfolio and employability builders:** they need end-to-end proof of competence and transferable mental models; they should not be merged with first-time programmers, who are not yet equipped to judge a production framework.
- **Maintainers of established applications:** switching cost, upgrade safety, production diagnosis, and incremental modernization matter more than first-project speed.
- **Regulated, security-sensitive, or high-scale contexts:** evidence, reviewability, supported versions, integration constraints, and operational behavior may outweigh convenience.

Segments overlap. Evidence is strongest for engaged Django users and Stack Overflow respondents, and weak for Django rejecters, developers outside English-language channels, and organization-specific approval contexts. (Inference; confidence: Medium.)

## Primary job to be done

> **When I am responsible for taking a web feature from interface through server behavior, data, and release, I want a coherent stack and workflow that lets me build, understand, test, ship, and change it without unnecessary seams, so I can deliver user value reliably while retaining control of the system.**

The core progress is dependable end-to-end delivery. Server-side frameworks reduce repeated work around requests, data, sessions, authorization, responses, and common security concerns; selection remains contextual ([MDN, “Server-side web frameworks,” Mozilla contributors, 2026](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Server-side/First_steps/Web_frameworks)). Current use—80% full-stack, 83% Django templates, with admin and auth widely valued—directly shows integrated-layer work; the JTBD synthesis is inference. Confidence: Medium-High.

**Job hierarchy:** functional core (complete and evolve an end-to-end feature); emotional support (feel in control rather than exposed by unknown seams); social support (be seen as a dependable product engineer, a hypothesis); supporting jobs (select components, learn unfamiliar layers, integrate front end and deployment, test, observe, secure, and maintain).

## Additional jobs to be done

1. **Reduce integration and coordination work:** When a feature crosses UI, server, data, authentication, and deployment, I want compatible conventions and clear interfaces, so I can spend more effort on product behavior than glue. **Dimensions:** functional core; emotional support through lower cognitive load. Integration is a directly evidenced selection category; Django priority is inferred. Confidence: Medium-High.
2. **Make a fit-for-context stack decision:** When starting or changing an application, I want to test realistic use cases against technical, organizational, cost, and ecosystem constraints, so I can recommend a defensible choice. **Dimensions:** functional core; hypothesized social credibility. Industry studies find selection multi-criteria and often ad hoc ([Farshidi, Jansen & Deldar, 2021](https://research-portal.uu.nl/en/publications/a-decision-model-for-programming-language-ecosystem-selection-sev/); [Bjarnason, Åberg & bin Ali, 2023](https://link.springer.com/article/10.1007/s10664-023-10288-w)). Confidence: High functionally.
3. **Learn the next layer without losing momentum:** When the feature requires an unfamiliar framework feature, browser technique, deployment system, or operational practice, I want trustworthy, searchable guidance and quick feedback, so I can become independently effective. **Dimensions:** functional core; emotional support. In Stack Overflow’s 2025 survey, 69.1% said they had learned a new coding technique or language in the prior year; technical documentation was the most-used learning resource (67.8%). Confidence: High for continuous learning, Medium for its exact full-stack form.
4. **Protect changeability:** When the application changes substantially, I want understandable conventions, tests, upgrades, and boundaries, so I can keep today’s speed from becoming tomorrow’s maintenance trap. **Dimensions:** functional core; emotional confidence. Broader research connects understanding, feedback, and documentation with perceived productivity and technical debt ([Kalliamvakou & GitHub, 2024](https://github.blog/news-insights/research/good-devex-increases-productivity/)). Confidence: Medium-High.
5. **Ship and recover safely:** When code leaves my laptop, I want a reproducible path to configure, deploy, observe, debug, patch, and roll it back, so I can protect users and bound incidents. **Dimensions:** functional core; emotional support through reduced fear of production. DORA emphasizes robust testing and delivery stability even where AI raises individual productivity ([2024 Accelerate State of DevOps](https://dora.dev/research/2024/dora-report/)); Django survey behavior spans containers, CI, VMs, PaaS, and log/debug workflows. Confidence: High for the general job, Medium for Django-specific friction.
6. **Demonstrate end-to-end capability:** When seeking a role, responsibility, or client trust, I want a working application I can explain and operate, so I can give others credible evidence of my ability beyond isolated exercises. **Dimensions:** functional and social core; emotional support through confidence. This is plausible for the early-career subsegment, but the reviewed sources do not directly measure Django portfolio-to-employment outcomes. Confidence: Low-Medium; hypothesis requiring research.

## Functional, emotional, and social dimensions

- **Functional:** implement user-facing flows; model and query data; manage identity and permissions; connect browser and server; test across seams; deploy; diagnose; update dependencies; evaluate trade-offs. Directly supported by observed Django full-stack technologies and general framework-selection research; confidence: High.
- **Emotional:** maintain a sense of control, avoid the anxiety of “unknown unknowns” across layers, reduce frustration from fragmented setup, and feel safe changing production code. **Hypothesis**, supported indirectly by developer-experience findings on cognitive load, flow, feedback, understanding, and job satisfaction; confidence: Medium.
- **Social:** be trusted as a developer who can own an outcome, give a defensible recommendation, collaborate with specialists, and avoid appearing attached to an unfashionable or unsuitable stack. **Hypothesis**; evidence specific to Django full-stack developers is weak. Confidence: Low-Medium.
- **Supporting:** search and verify information, create a prototype, estimate operational burden, coordinate reviews, explain architecture, and keep current. Direct/inferred mixed; confidence: Medium-High.

## Triggering situations

**Recurring triggers** are a new feature crossing multiple layers; routine defects whose cause might lie in browser, server, data, or deployment; dependency and security updates; performance work; and onboarding into an unfamiliar codebase. Continuous learning is normal rather than exceptional: 69.1% of Stack Overflow’s 2025 respondents learned a new technique or language during the year. (Direct evidence for learning; trigger mapping is inference; confidence: Medium-High.)

**Event-triggered situations** include a greenfield product or client brief; a prototype becoming production-bound; a team standardization decision; a framework reaching end of support; a serious incident; a scale or compliance threshold; a front-end modernization; inheriting a legacy Django application; and entering the job market. Django 5.2’s April 2, 2025 release notes, for example, designate it LTS and state at least three years of security updates, while the April 7, 2026 security release announced Django 4.2’s end of extended support—concrete events that force maintainers to reassess ([Django 5.2 release notes](https://docs.djangoproject.com/en/dev/releases/5.2/); [Django security release, April 7, 2026](https://www.djangoproject.com/weblog/2026/apr/07/security-releases/)). Direct evidence; confidence: High.

## Desired outcomes

- Shorten the elapsed time from a defined user need to a tested, deployable end-to-end slice.
- Reduce the number and fragility of integration seams, duplicate models, and hand-maintained contracts.
- Make local setup, test, deployment, and rollback reproducible for another developer.
- Keep changes understandable: a developer can trace request, authorization, state change, response, and visible result.
- Detect failures before users do where practical; reduce change failure and recovery time.
- Meet security, accessibility, performance, data, and compliance constraints appropriate to the application.
- Upgrade supported components with bounded effort and known compatibility effects.
- Allow a developer to become productive in an unfamiliar layer without prolonged dependency on a specialist.
- Preserve the option to add richer client interaction, APIs, async behavior, or operational tooling when the actual product requires it.

These are directional, not universal numeric targets. DORA delivery measures and DevEx constructs offer measurement families; no reviewed evidence establishes Django-specific targets. Confidence: Medium.

## Current behaviour or status quo

Full-stack developers assemble technology portfolios. Stack Overflow’s 2025 respondents report server frameworks, client tools, databases, containers, clouds, and build tooling ([Technology, Stack Overflow Developer Survey 2025](https://survey.stackoverflow.co/2025/technology/)). Among engaged Django users, 29% also used React, 28% FastAPI, 23% Flask, and 18% Vue; 77% named Django their most-used web framework. They commonly add databases, caches, queues, containers, and CI. (Direct evidence; confidence: High for respondents.)

Evaluation is often informal: prior experience, peers, documentation, tutorials, and prototypes. Industry research reports ad hoc selection and weak uptake of systematic criteria; the 2023 Ericsson study instead combines documentation, reviews, experience reports, hands-on prototypes, and stakeholder impact analysis. Confidence: High in the studied context, Medium externally.

In the Django survey, respondents used AI for completion (56%), generation (51%), boilerplate (44%), tests (36%), explanations (35%), and questions (34%). This is behavior, not proof of correctness. DORA cautions that individual AI productivity gains can coincide with worse stability and throughput. Confidence: High for the tension, not its Django magnitude.

## Pushes

- Repeating authentication, data-management, validation, administration, or CRUD plumbing delays the actual product behavior.
- Separate front-end/back-end systems can create duplicated schemas, build steps, contracts, repositories, deployments, and debugging boundaries when the product does not need that separation.
- Conversely, a server-rendered setup can become strained when the required interaction model genuinely needs complex client state, offline behavior, or a specialist front-end workflow.
- Inconsistent documentation, slow feedback, and low code understanding increase cognitive load and make change feel risky; GitHub/DX’s multi-company study directly links these DevEx factors with perceived productivity and innovation.
- A prototype must become secure, tested, observable, and maintainable in production.
- End-of-support, security advisories, dependency conflicts, scaling needs, or a production incident make inertia more costly.
- Hiring, team skill, platform, or regulatory constraints invalidate a stack that worked for one developer locally.

The first three are contextual inferences; the remainder have broader direct support. Confidence: Medium-High.

## Pulls

- One coherent path through routing, models, migrations, forms, templates, authentication, and administration can make common product flows fast to build and easier to trace.
- “Batteries included” components reduce component search and integration, while documented conventions give collaborators a shared default.
- Python familiarity and the ability to use Django as a rendered full-stack system or as an API backend widen the number of plausible project shapes.
- Mature documentation, a time-based release process, an LTS option, and a public security process make maintenance obligations more legible.
- A large body of real usage, packages, Q&A, peers, and employment experience lowers uncertainty and offers recovery routes.
- Server-rendered templates plus selective JavaScript/HTMX/Alpine can avoid an extra application boundary for suitable interaction models; a separate rich client remains available when justified.

Actual behavior supports the integrated pull: 80% full-stack use, 83% templates, and strong reported usefulness of models, admin, migrations, and auth. Whether it outweighs flexibility costs is project-specific inference; confidence: Medium-High.

## Anxieties

- “I can build the happy path, but will I know how to deploy, secure, observe, and recover it?”
- “The framework will hide too much, and I will be stuck when its conventions stop fitting.”
- “I will need to maintain two worlds—Python/Django and a JavaScript toolchain—with unclear ownership at the seam.”
- “The UI will look dated or become difficult to make highly interactive.”
- “Python or Django performance/async constraints will appear only after commitment.”
- “A mature stack will be perceived as stale, reducing career value or peer credibility.”
- “A smaller ecosystem package will become abandoned or block an upgrade.”
- “AI-generated code will look complete while introducing bugs I cannot trace across layers.”

The Django Forum thread asking how to embed React while keeping a monolith identifies build-process and front-/back-end communication uncertainty directly ([February 15, 2024](https://forum.djangoproject.com/t/can-we-use-reactjs-components-inside-django-to-make-a-monolithic-app/28095)). Deployment threads similarly surface staging, media serving, proxy, SSL, containers, and environment questions. These are qualitative signals, never prevalence evidence. Emotional wording and ordering are hypotheses; confidence: Medium for the categories, Low for relative importance.

## Habits and inertia

- Existing fluency makes the familiar stack faster and safer initially; MDN explicitly notes that teams have reason to retain a framework/language they know.
- Starter repositories, standards, CI, monitoring, deployment automation, reusable components, and internal expertise embed prior choices.
- Popularity or trusted-peer advice becomes a shortcut because multi-criteria evaluation is costly.
- Tutorial success can be mistaken for production fit; one painful project can become an overbroad veto.
- Maintainers may postpone upgrades until support or dependency deadlines force action.

These are inferences from selection studies and switching-cost logic; their Django-specific strength is unquantified. Confidence: Medium.

## Decision criteria

No universal ranking is evidenced. These tiers synthesize selection research, MDN guidance, DevEx research, and Django practice.

**Usually high importance / Medium-High confidence:**

- Fit to the application’s real user scenarios and interaction model.
- Time and cognitive effort to build, test, debug, and change an end-to-end feature—not only scaffold it.
- Maintainability: understandable conventions, code quality, testability, upgrade/deprecation path, and documentation quality.
- Integration with the team’s required browser stack, data stores, authentication, APIs, background work, deployment platform, and observability.
- Security behavior and update process appropriate to the risk context.
- Team skills, onboarding burden, and availability of help.

**Often important / Medium confidence:**

- Operational reliability, performance, scaling, async/realtime suitability, and resource cost under a representative workload.
- Ecosystem maturity, package health, release continuity, governance, and developer availability.
- Ability to prototype quickly without creating an unacceptable production gap.
- Architecture flexibility: monolith, selectively interactive server rendering, API plus separate client, or gradual transitions.
- Licensing, legal, privacy, accessibility, and organizational standards.

**Context-dependent / Low-Medium confidence:**

- Market visibility, résumé signaling, perceived modernity, enterprise references, and personal enjoyment. These may influence adoption, but reviewed sources do not establish their rank for this audience.

Farshidi et al. identified 164 ecosystem criteria whose priority depends on project requirements; Bjarnason et al. cover market strength, strategy/culture, productivity, quality, integration, cost, legal, ethical, and control concerns. This argues against a generic popularity ranking. Confidence: High.

## Main concerns

**Practical concerns:** local setup; front-end asset pipeline; API or template architecture; schema and validation duplication; testing across layers; static/media handling; configuration and secrets; deployment; logs and debugging; dependency compatibility; upgrades; accessibility and performance.

**Legitimate limitations:** an integrated framework cannot eliminate the need to understand HTTP, browser behavior, databases, security, and operations. Django’s synchronous heritage and server-rendering defaults may add complexity for highly async, realtime, offline-first, or client-state-heavy products. A rich separate client can add an additional architecture and toolchain. Which cost is legitimate depends on the product.

**Perceived risks:** “Django cannot make a modern interface,” “monolith means unscalable,” “batteries included means inflexible,” or “API plus React is always the professional architecture.” These absolutes are unsupported. The 2025 survey shows actual Django developers using templates, React, Vue, HTMX, APIs, containers, and multiple clouds; diversity disproves a single mandatory shape, not the existence of trade-offs.

**Misconceptions:** full-stack means one person must master every specialty; fast prototype means production-ready; framework security eliminates application security work; an LTS eliminates upgrade work; package popularity guarantees maintenance.

**Organizational objections:** approved languages/platforms, security review, staffing, procurement, support expectations, architecture standards, and migration cost can block an individual preference. Directly supported as selection categories in industry research; confidence: High.

**Emotional resistance:** fear of looking obsolete, loss of autonomy under strong conventions, or reluctance to admit an unfamiliar layer. Hypotheses; confidence: Low-Medium.

## Objections and perceived risks

- **“Django is primarily back end.”** Partly a category mismatch: Django covers server-rendered UI and application services but not CSS, design, browser knowledge, or every rich-client need.
- **“Modern front-end integration is awkward.”** Legitimate in some architectures. A 2024 Forum thread asks about embedded React, builds, and communication; survey coexistence does not measure integration effort.
- **“Deployment has too many choices.”** Legitimate cross-stack burden. Varied cloud/runtime use and isolated forum confusion do not prove Django is worse than alternatives.
- **“It will not handle scale, async, or realtime.”** Requires workload evidence. ASGI/async adoption shows use, not adequacy; runtime must be weighed against learning and maintenance.
- **“The ecosystem is old or career-irrelevant.”** Unestablished. Surveyed use and professional incumbency do not answer local job demand or learning returns.
- **“Included security makes the app secure.”** Misconception: configuration, application logic, dependencies, infrastructure, and timely upgrades remain developer responsibilities.
- **“AI makes framework learning unnecessary.”** Unsupported in production. DORA finds productivity gains with stability trade-offs; understanding, testing, and feedback remain necessary.

## Information needed to make progress

- A task map from representative user flow through URL, view, authorization, model/query, template or API, browser update, test, deploy, and observability.
- Clear architecture choices and consequences: Django templates alone, selective interaction, hybrid embedded components, or separate API/client.
- A realistic vertical-slice example that includes validation, permissions, errors, tests, configuration, assets, database migration, and deployment—not only CRUD scaffolding.
- Compatibility information for Python, Django, database, packages, client tooling, deployment target, and supported-version horizon.
- Evidence for security policy, disclosure/update path, deprecations, and upgrade effort.
- Workload-relevant performance and async behavior, with assumptions and measurement method.
- Ecosystem-package health: maintainer activity, release compatibility, issue responsiveness, alternatives, and exit plan.
- Operational path: secrets, static/media, processes, queues, migrations, health checks, logs, monitoring, backup, rollback, and incident recovery.
- Team-fit evidence: who learns what, specialist collaboration boundaries, code ownership, onboarding exercise, and local hiring constraints.
- A prototype scorecard tied to requirements, recording failures and trade-offs as well as time-to-first-success.

This is a mixed direct/inferred synthesis; confidence: Medium-High.

## Trusted content formats

- **Versioned reference documentation and release/security notes** support implementation, upgrades, and validation because they are searchable and tied to supported behavior.
- **End-to-end sample repositories with tests and deployment configuration** let evaluators inspect seams and run a realistic spike; trust depends on visible versions, maintenance, and explained trade-offs.
- **Architecture guides and decision records** help choose between templates, selective interaction, and a separate client by scenario.
- **Short runnable tutorials** are useful for initial evaluation; they are weak production evidence unless they expose security, failure, testing, and operations.
- **Benchmarks and production case studies with workload and architecture detail** validate a particular risk better than unqualified scale claims.
- **Migration/upgrade reports and compatibility matrices** reduce maintainers’ uncertainty.
- **Forum answers, issue threads, and peer code review** resolve edge cases and expose failure modes, but isolated posts are qualitative.
- **Video talks and live demonstrations** build mental models and aid discovery; written artifacts remain easier to search during implementation.

Use is directly supported: 79% of Django respondents preferred djangoproject.com for learning, 39% Stack Overflow, 38% AI, 38% YouTube, 33% blogs, 22% books, and 13% friends/coworkers. These are neither trust scores nor full-stack-only. Format mapping is inferred; confidence: Medium-High.

## Discovery, evaluation, validation, and engagement channels

- **Discovery:** search, YouTube, blogs/podcasts, public GitHub, community platforms, colleagues, and prior Python exposure make a stack visible. Stack Overflow’s broader 2025 data supports documentation, online resources, Q&A, video, AI, blogs/podcasts, and colleagues as learning routes. The evidence does not establish short-form social or the Django homepage as the first discovery source for full-stack evaluators.
- **Evaluation:** official documentation, a representative prototype, source/package repositories, architecture discussions, peer advice, and implementation-focused articles answer fit and effort questions. Industry research directly supports reading documentation/reviews/experience reports and prototyping against scenarios.
- **Validation:** tests, security/release policy, issue history, realistic benchmarks, production references with detail, platform/security review, and experienced peer review reduce adoption risk. Enterprise testimonials alone are insufficient evidence; no reviewed source measures their influence on full-stack developers.
- **Ongoing engagement:** versioned docs, release and security announcements, djangoproject.com, Django Forum, Stack Overflow, newsletters/RSS, Discord, code/issue workflows, local meetups, conferences, and podcasts serve different maintenance and learning needs. The Django survey directly reports following behavior: djangoproject.com 60%, YouTube 22%, Stack Overflow and Reddit 18% each, Django Forum 15%, newsletter 12%, podcasts and X 7% each, Discord 6%, and 18% not following development. Only 29% had attended a Django event or meetup, so conferences cannot be treated as a broad default channel.

The survey validates these behaviors among current users, but neither isolates full-stack respondents nor distinguishes discovery from ongoing use. GitHub/issue-tracker and professional-network behavior remain unvalidated here. Confidence: High for use, Medium-Low for stage assignment.

## Decision-makers and influencers

- **Solo project:** the developer may be initiator, researcher/evaluator, approver, user, operator, and bearer of time, outage, and migration consequences. A client or co-founder can still constrain deadline and budget.
- **Small product team:** developer or lead initiates and prototypes; peers influence through maintainability and skill fit; product/founder approves time and risk; users and on-call developers bear quality consequences.
- **Larger organization:** a senior developer or architect may research and recommend; engineering leadership owns standardization and staffing; platform/operations assesses deployability; security, privacy, accessibility, legal, and procurement review; finance or product leadership approves material cost; delivery teams and users bear consequences.
- **Early-career learner:** the developer usually chooses a learning project, while employers, job listings, instructors, peers, and portfolio reviewers influence perceived career value.
- **Established application:** maintainers and on-call engineers surface need; technical lead/architect assesses migration or upgrade; product owners control interruption; security can force timing; users bear regression risk.

The organization-role mapping is supported at a category level by Bjarnason et al.’s cross-stakeholder selection model, which explicitly includes decision makers, managers, legal/financial departments, technical experts, and affected stakeholders. Django-specific authority patterns remain unmeasured. Confidence: Medium.

## Appropriate next actions for Django to encourage

These are actions for the developer, tied to jobs, not campaign or site recommendations.

1. **Write one representative end-to-end user scenario and its constraints** — serves the fit-for-context selection job.
2. **Build a small vertical slice through UI, permissions, data, tests, and production-like deployment** — serves end-to-end delivery and reveals seams.
3. **Compare template, selective-interaction, hybrid, and separate-client shapes against that scenario** — serves integration reduction without assuming one architecture.
4. **Run the deployment and security checks, then exercise a failure and rollback** — serves safe shipping and recovery.
5. **Inspect supported versions, deprecations, package compatibility, and an upgrade path** — serves changeability.
6. **Measure one realistic workflow or workload and record assumptions** — serves evidence-based performance and productivity evaluation.
7. **Ask an experienced peer to review the prototype and decision record** — serves validation and professional credibility.
8. **Subscribe to the release/security channel appropriate to a maintained application** — serves ongoing maintenance.
9. **Choose a bounded next-layer learning task and verify AI-assisted answers against docs/tests** — serves independent learning while preserving understanding.

Appropriateness is inferred from the job hierarchy and evidence; confidence: Medium-High.

## Overlaps with other audiences

- **Python developers new to web:** overlap when Python fluency exists but browser, HTTP, deployment, or production web concepts are new; their immediate job is acquiring web capability rather than optimizing end-to-end ownership.
- **Experienced back-end engineers:** overlap strongly in server, data, security, and operations; full-stack responsibility adds interaction design, browser behavior, assets, and cross-layer integration.
- **Front-end developers:** overlap for rich-client work; a front-end specialist may value separate ownership while the full-stack developer bears both sides of the seam.
- **Early-career/self-taught/bootcamp/CS/career-changing developers:** overlap in portfolio and career learning; experience level must remain a separate axis.
- **Existing professional Django developers:** large overlap, but not all are full-stack; their jobs may center on upgrades, scale, best practice, or contribution.
- **Technical decision-makers/architects:** overlap when a full-stack developer recommends or standardizes a stack; approval authority is not inherent in the role.
- **DevOps/platform/security specialists:** influence and constrain delivery, while full-stack developers often consume their paths rather than own organizational infrastructure.

## Possible segmentation problems

“Full-stack developer” is unusually prone to false unity. It conflates role title with actual task breadth, mixes solo owners with developers inside specialist organizations, and says nothing about seniority, front-/back-end leaning, product complexity, regulatory context, or decision authority. It can also conceal an exploitative expectation that one person perform several specialties without time or support.

The Django survey’s “full-stack development” response describes a use case, whereas Stack Overflow’s “developer, full-stack” describes a role. They should not be treated as the same denominator. The Django sample is also incumbency-biased: distribution through official Django channels overrepresents engaged users and cannot reveal the anxieties, criteria, or channels of non-users and rejecters. Recommended future segmentation uses at least four axes: **responsibility span, current stack relationship (unaware/evaluating/new/incumbent/migrating), experience, and decision authority**. Contextual axes—team size, interaction complexity, operational risk, and front-/back-end leaning—should be added when evidence permits. Confidence: High for measurement caution; Medium for the proposed axes.

## Existing-analysis claim audit

| Existing-analysis hypothesis | Audit | Evidence and limits |
|---|---|---|
| A mid-to-large-company technical decision-maker approves framework standards based on currency/relevance, long-term reliance, community/support, security, and hiring; enterprise examples, production architecture, and testimonials influence them. | **Partially supported** | Industry selection research directly supports multi-stakeholder decisions and technical, business, organizational, ecosystem, developer-availability, documentation, quality, integration, cost, legal, and control criteria. Django’s release/security process supplies evidence relevant to continuity. The full-stack developer may influence or prototype but is not necessarily the approver. No reviewed evidence establishes the claimed importance of enterprise examples or testimonials. Confidence: High on criteria/roles, Low on those content influences. |
| Early-career/self-taught/bootcamp/CS/career-changing developers evaluate a framework as a career investment, portfolio tool, modern-app tool, and route to a welcoming community; homepage/social/video/community discovery is claimed. | **Requires further research** | Stack Overflow directly shows continuous learning and high video/community use, and Django’s survey shows learning via official site, Q&A, AI, YouTube, and blogs. The sources do not isolate early-career full-stack evaluators, connect Django portfolios to employment, or distinguish first discovery from ongoing learning. Homepage and short-form-social claims are unvalidated. Confidence: High in the gap assessment. |
| Existing professional Django developers seek current best practice, releases/upgrades, scaling help, greater expertise, and possible progression from user to contributor. | **Partially supported** | Current developers directly use official channels, Q&A, forum, newsletter, Discord, and other resources; supported-version transitions and security releases create concrete upgrade jobs. The survey shows 84% favoring core type hints and 45% willing to contribute to that effort, indicating a possible user-to-contributor path. It does not directly measure “best practice,” scaling-help demand, progression motives, or full-stack-only behavior. Confidence: Medium-High. |
| Claimed touchpoints include docs/release notes, forums/Discord, GitHub/issue tracker, mailing lists, conferences/sprints, podcasts, professional peer networks, and short-form social. | **Partially supported** | The 2025 Django survey directly validates djangoproject.com, Stack Overflow, Forum, newsletter, Discord, podcasts, friends, X, Fediverse/RSS, and event attendance among current users. The security process validates release announcement channels. It does not behaviorally validate GitHub/issue tracker, sprints, or professional networks in a full-stack-specific journey, and attendance was a minority behavior. Channel roles must not be collapsed. Confidence: High. |

## Evidence table

| Finding | Source (title, publisher/author, date, URL) | Evidence type | Direct evidence or inference | Confidence | Research notes |
|---|---|---|---|---|---|
| Full-stack was the largest developer-role response (27%), with a broad experience distribution. | [2025 Developer Survey: Developers, Stack Overflow, 2025](https://survey.stackoverflow.co/2025/developers) | Large self-selected industry survey | Direct | High for sample; Medium external validity | 49,000+ overall responses; role and years questions have their own response counts. Stack Overflow participation bias applies. |
| Engaged Django users predominantly report full-stack use (80%) and professional Django work (82%). | [Django Developers Survey 2025 Results, DSF/JetBrains, published 2025; collected Nov. 2024–Jan. 2025](https://lp.jetbrains.com/django-developer-survey-2025/) | Django-user survey, 4,655 filtered responses | Direct | High for respondents; Medium external validity | Recruited only via official Django channels; not representative of unaware/rejecting developers. |
| Django full-stack practice is cross-language and multi-framework, not Python-only. | [Django Developers Survey 2025 Results, DSF/JetBrains, 2025](https://lp.jetbrains.com/django-developer-survey-2025/) | Survey | Direct | High for respondents | 70% JavaScript, 64% HTML/CSS, 44% SQL, 27% TypeScript; many also use other web frameworks. Multi-select questions. |
| Full-stack developers’ core job is coherent end-to-end delivery rather than framework adoption. | Django survey plus [Server-side web frameworks, MDN/Mozilla contributors, 2026](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Server-side/First_steps/Web_frameworks) | Cross-source JTBD synthesis | Inference | Medium-High | Needs direct switch interviews with developers to validate wording and job hierarchy. |
| Framework/ecosystem choice is context-dependent and multi-criteria; developer availability and consistent documentation matter. | [A decision model for programming language ecosystem selection: Seven industry case studies, Farshidi, Jansen & Deldar, Nov. 2021](https://research-portal.uu.nl/en/publications/a-decision-model-for-programming-language-ecosystem-selection-sev/) | Peer-reviewed expert study and seven industry case studies | Direct | High | 164 criteria/47 alternatives in the full model; not web-framework- or Django-specific. |
| Industrial software selection should cover technical, business, organizational, integration, quality, cost, legal, ethical, and control factors and use prototypes plus stakeholder impact analysis. | [Software selection in large-scale software engineering, Bjarnason, Åberg & bin Ali, Feb. 28, 2023](https://link.springer.com/article/10.1007/s10664-023-10288-w) | Peer-reviewed co-designed model, focus group, practical Ericsson use | Direct | High in studied context; Medium generalization | One company; authors explicitly call for further validation. |
| Documentation, online resources, Q&A, video, AI, and colleagues are substantial learning behaviors; learning is recurring. | [2025 Developer Survey: Developers, Stack Overflow, 2025](https://survey.stackoverflow.co/2025/developers) | Large self-selected survey | Direct | High for sample; Medium external validity | 69.1% learned a new technique/language; 67.8% used technical documentation. Not full-stack-only. |
| Lower cognitive load, stronger understanding, and faster feedback relate to perceived developer productivity and innovation. | [Yes, good DevEx increases productivity, Kalliamvakou/GitHub, Jan. 23; updated May 14, 2024](https://github.blog/news-insights/research/good-devex-increases-productivity/) | Multi-company DevEx survey with statistical analysis | Direct | Medium-High | More than 20 companies; largely self-reported outcomes; vendor-published summary links underlying study. |
| AI can raise individual productivity while harming delivery stability and throughput; robust testing remains important. | [2024 Accelerate State of DevOps Report, DORA/Google Cloud, 2024](https://dora.dev/research/2024/dora-report/) | Large industry research program/report | Direct | High for general direction; Medium Django transfer | Organization/team-level evidence, not a Django-specific comparison. |
| Current Django users learn and follow development through different channels with different prevalence. | [Django Developers Survey 2025 Results, DSF/JetBrains, 2025](https://lp.jetbrains.com/django-developer-survey-2025/) | Survey | Direct use; stage mapping is inference | High use / Medium-Low stage mapping | Learning preferences are not trust ratings; no full-stack cross-tab. |
| Front-end integration and production deployment create concrete uncertainty for some Django developers. | [Can We Use ReactJS Components Inside Django to Make a Monolithic App?, Django Forum, Feb. 15, 2024](https://forum.djangoproject.com/t/can-we-use-reactjs-components-inside-django-to-make-a-monolithic-app/28095); [CI/CD Django—Dev & Prod Environments, Django Forum, Mar. 13, 2024](https://forum.djangoproject.com/t/ci-cd-django-dev-prod-environments/29024) | First-person community discussions | Direct qualitative signal | Medium for issue existence; Low prevalence | Isolated threads identify vocabulary and situations only; cannot support ranking or market-wide claims. |
| Supported-version transitions and public security releases create recurring maintenance jobs. | [Django 5.2 release notes, Django, Apr. 2, 2025](https://docs.djangoproject.com/en/dev/releases/5.2/); [Django security releases 6.0.4/5.2.13/4.2.30, Django, Apr. 7, 2026](https://www.djangoproject.com/weblog/2026/apr/07/security-releases/) | Official project process/release records | Direct | High | Django-controlled sources are appropriate for factual support and security lifecycle, not motivation. |
| A templates/selective-interaction approach may reduce seams for some products, while separate clients remain valid for others. | Django survey, MDN selection guidance, and forum integration signal | Cross-source architectural synthesis | Inference | Medium | No controlled comparison of developer time, maintainability, or user outcomes across Django architecture shapes. |
| Career/portfolio value and social identity are plausible for an early-career subsegment but not established. | Stack Overflow 2025 learning/role evidence; no direct outcome study found | Evidence-gap assessment | Inference | Low-Medium | Requires job-posting analysis and longitudinal interviews/outcomes; avoid employability promises. |

## Unanswered research questions

1. What situations cause full-stack developers to put Django on an initial shortlist, and what causes them to reject it before prototyping?
2. How do evaluators define “full-stack” in practice: responsibility, skill identity, team title, or ownership of production outcomes?
3. Which job wording survives interviews with solo builders, small-team generalists, and enterprise product developers, and where should the audience split?
4. How do developers compare Django templates, HTMX/Alpine-style selective interaction, embedded rich-client components, and a separate API/client on delivery time, comprehension, test burden, accessibility, and changeability?
5. Which deployment steps create Django-specific friction versus general web-operations learning, and at what experience levels?
6. What evidence do front-end-leaning full-stack developers need before they trust Django’s browser-facing workflow? What do back-end-leaning developers need to trust their own UI output?
7. How do current Django users discover the framework originally, as distinct from the channels through which they later learn or follow it?
8. Which sources are trusted for architecture and production validation, and how are AI answers verified in real workflows?
9. How important are local hiring demand, résumé signaling, perceived modernity, community welcome, and peer identity relative to project fit—and for which subsegments?
10. Who actually has framework approval, veto, and consequence-bearing roles in small, mid-size, and regulated organizations?
11. What are the upgrade, package-compatibility, and migration costs experienced across different ages and shapes of Django applications?
12. What do developers who migrated away from Django, or returned to it, say the underlying job and decisive switching forces were?
13. How do geography, language, disability, connectivity, gender, race, and economic access change the full-stack evaluation and learning job?
14. Can raw Django survey cross-tabs isolate full-stack respondents by experience, team size, front-end approach, deployment, learning channel, and contribution intent without creating misleading precision?

<!-- RESEARCH PROVENANCE: BEGIN -->
## Research provenance

This section was generated from the recorded Codex session JSONL logs. File attribution uses successful patch events; searches and domains use nested web-tool calls.

### Session `019f7541-49ec-76d3-bcfc-06de3323224d`
- Log: `rollout-2026-07-18T14-44-00-019f7541-49ec-76d3-bcfc-06de3323224d.jsonl`
- This document: `add, update`
- Search queries:
  - None recorded.
- Website domains:
  - `artefacts-discovery.researcher.life`
  - `arxiv.org`
  - `blog.jetbrains.com`
  - `bth.diva-portal.org`
  - `code.djangoproject.com`
  - `coursera-assessments.s3.amazonaws.com`
  - `creativecommons.org`
  - `d-nb.info`
  - `dam-cdn.atl.orangelogic.com`
  - `data.mendeley.com`
  - `developer.mozilla.org`
  - `developers.ucdavis.edu`
  - `django-deployments.readthedocs.io`
  - `django-report-tools.readthedocs.io`
  - `django.readthedocs.io`
  - `djangoproject.com`
  - `docs.djangoproject.com`
  - `doi.org`
  - `dora.dev`
  - `dspace.library.uu.nl`
  - `dspace.ut.ee`
  - `en.wikipedia.org`
  - `form.jotform.com`
  - `forum.djangoproject.com`
  - `frontiersin.org`
  - `github.blog`
  - `ijrpr.com`
  - `infoq.com`
  - `itpro.com`
  - `jetbrains.com`
  - `jetir.org`
  - `link.springer.com`
  - `linkedin.com`
  - `lp.jetbrains.com`
  - `mail-archive.com`
  - `mdpi.com`
  - `mobileworldcapital.com`
  - `objectstorage.ap-dcc-gazipur-1.oraclecloud15.com`
  - `pages.hackerrank.com`
  - `peps.python.org`
  - `pmc.ncbi.nlm.nih.gov`
  - `preprints.org`
  - `project-archive.inf.ed.ac.uk`
  - `queue.acm.org`
  - `queue.org.cn`
  - `reddit.com`
  - `research-portal.uu.nl`
  - `research.google`
  - `researchgate.net`
  - `researchr.org`
  - `resources.jetbrains.com`
  - `sciencedirect.com`
  - `siamakfarshidi.nl`
  - `stackoverflow.blog`
  - `stormvirux.github.io`
  - `survey.stackoverflow.co`
  - `symfony.com`
  - `techguide.org`
  - `techradar.com`
  - `theseus.fi`

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
