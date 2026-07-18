# Existing Django users maintaining, extending, and operating real systems

## Audience definition and boundaries

This audience consists of people who already use Django and must keep a codebase useful, safe, understandable, operable, and changeable. The defining boundary is **consequence-bearing responsibility for an existing Django system or repeated Django work**. It includes individual developers, maintainers of inherited applications, production/on-call engineers, senior practitioners, technical leads, consultants, and experienced users moving toward teaching or contribution.

It is not one homogeneous “professional Django developer” persona. A developer adding a feature to a current project, an engineer carrying an unsupported inherited system, and an operator diagnosing a latency regression have different jobs even if one person performs all three. The 2025 Django Developers Survey also cuts across work and personal contexts: 70% of respondents used Django for both, 16% only for work, and 14% only for personal, educational, or side projects. **[Direct evidence; High confidence for survey respondents, with self-selection limits.]**

This report focuses on the person doing or coordinating the technical work. Framework-standard approval, organizational funding, hiring strategy, and economic buying belong primarily to technical-lead, executive, organization, or funder audiences. Core/ecosystem maintainers belong here only while doing a user’s job; contribution itself is an adjacent audience and possible transition, not the primary definition. **[Boundary inference; High confidence.]**

## Important subsegments

- **Active application builders:** extend a supported codebase, integrate packages and frontends, improve tests, and choose patterns that teammates can maintain. Their recurring job is safe delivery. **[Direct survey evidence plus inference; High confidence.]**
- **Production operators and performance owners:** deploy, observe, debug, secure, scale, and recover Django services. Rippling’s 17-million-line monolith and Clubhouse’s growth from under 10,000 to over one million requests per minute illustrate that bottlenecks emerge in application/process architecture, infrastructure, dependencies, and workload—not as a single generic “does Django scale?” question. **[Direct organizational accounts; High confidence that these situations occur, Low on prevalence.]**
- **Upgrade owners of maintained systems:** keep Python, Django, database, infrastructure, and packages within support while preserving behavior. Most surveyed users upgrade frequently, but a long tail does not: 48% reported every stable release, 27% LTS-only, 11% every monthly point release, and 4% an unsupported version. **[Direct evidence; High confidence for respondents.]**
- **Legacy inheritors and rescue maintainers:** receive an old system after original authors leave, often with weak tests, stale packages, undocumented behavior, and simultaneous Python/Django changes. Repeated forum threads directly express uncertainty about the least-risk path. **[Direct qualitative evidence; Medium confidence on pattern, not prevalence.]**
- **Technical leads, architects, and internal enablers:** set conventions, review changes, make upgrade work legible to management, unblock teammates, and balance maintenance with product commitments. The survey included team leads (16%), architects (15%), and CTO/CIO/CEOs (13%); roles were multi-select. **[Direct evidence; High confidence for respondent composition.]**
- **Independent consultants and multi-project specialists:** move between codebases and need fast diagnosis, reusable practices, and credible recommendations. Fifty-two percent of survey respondents reported many different projects; only 12% reported one project. **[Direct evidence plus inference; Medium-High confidence.]**
- **Expertise-to-community users:** seek deeper mastery, peer recognition, teaching opportunities, or a first contribution after solving user problems. Interest is visible but action should not be assumed: 45% said they would contribute to a proposed typing effort, while 71% had never attended a Django event or meetup. **[Direct evidence; Medium confidence because hypothetical intent is not behavior.]**

Lifecycle stage, system condition, responsibility, and consequence are more useful segmentation axes than seniority alone.

## Primary job to be done

> **When an existing Django system must continue changing under real user, team, and operational constraints, I want to make the next change with evidence that compatibility, behavior, security, and performance remain acceptable, so I can deliver value without creating an incident or an unaffordable maintenance burden.**

**[Inference synthesized from survey behavior, upgrade accounts, and production engineering reports; High confidence in the functional job, Medium confidence in the exact wording.]**

## Additional jobs to be done

| Job | Core functional job | Emotional job | Social job | Supporting jobs | Evidence assessment |
|---|---|---|---|---|---|
| **Change safely** | Add or modify behavior while preserving contracts and controlling regressions | Feel confident enough to ship, not merely hopeful | Be trusted as a reliable teammate *(hypothesis)* | Find current patterns; test; review; stage; observe; roll back | **Direct production evidence plus inference; High.** |
| **Keep the dependency stack supportable** | Upgrade Django, Python, packages, databases, and infrastructure before support or compatibility becomes critical | Replace dread with a bounded plan | Demonstrate responsible stewardship *(hypothesis)* | Inventory dependencies; read release notes; surface deprecations; automate edits; sequence and validate changes | **Direct evidence; High.** |
| **Operate and improve a production service** | Diagnose incidents and bottlenecks, preserve reliability, and meet changing load/cost needs | Regain control during ambiguity | Be credible to users, support staff, and peers | Instrument; benchmark; capacity-plan; deploy progressively; communicate; recover | **Direct organizational accounts; High that job exists, Low on typical scale.** |
| **Understand an inherited or unfamiliar system** | Build an accurate mental model before changing poorly documented code | Reduce fear of causing hidden breakage | Become a legitimate steward rather than “the person stuck with it” *(hypothesis)* | Map code and data; recover intent; establish tests; identify unsupported packages and owners | **Direct qualitative signals plus inference; Medium-High.** |
| **Raise team capability and consistency** | Turn personal solutions into reviewable conventions, automation, and shared knowledge | Reduce repeated firefighting | Be recognized as an effective technical guide *(hypothesis)* | Document decisions; mentor; create examples/checklists; align practices | **Inference supported by large-team accounts; Medium-High.** |
| **Deepen expertise and optionally participate** | Solve harder Django problems, understand framework evolution, teach peers, or make a bounded contribution | Feel continuing growth rather than stagnation *(hypothesis)* | Belong to and earn standing in a professional community *(hypothesis)* | Follow internals selectively; reproduce issues; discuss proposals; contribute docs/tests/code | **Survey intent plus community-process evidence; Medium.** |

In full audience-progress form:

1. **Change safely:** When an existing system needs new or changed behavior, I want evidence that contracts and critical behavior remain acceptable, so I can ship without avoidable regressions.
2. **Keep the dependency stack supportable:** When Django, Python, packages, databases, or infrastructure approach a compatibility or support change, I want a bounded upgrade plan and regression evidence, so I can avoid unsupported accumulation and emergency migration.
3. **Operate and improve a production service:** When incidents, bottlenecks, load, or cost threaten service outcomes, I want observable evidence and controlled interventions, so I can restore control and improve reliability without speculative changes.
4. **Understand an inherited or unfamiliar system:** When I become responsible for poorly understood Django code, I want an accurate model of its code, data, dependencies, contracts, and owners, so I can change it without triggering hidden breakage.
5. **Raise team capability and consistency:** When recurring problems depend on individual memory or inconsistent practices, I want shared, reviewable conventions, automation, and knowledge, so I can reduce repeated firefighting and key-person risk.
6. **Deepen expertise and optionally participate:** When harder Django problems or framework changes exceed my current understanding, I want to deepen the relevant expertise and, where useful, make a bounded contribution, so I can solve the immediate problem and choose whether broader participation serves me.

## Functional, emotional, and social dimensions

- **Functional:** shorten time to a correct, observable change; keep support status current; control regressions, downtime, latency, resource cost, and future change cost; make knowledge transferable. **[Direct evidence plus inference; High confidence.]**
- **Emotional—evidenced:** legacy maintainers express danger, uncertainty, and lack of experience with large upgrades. Production accounts emphasize protecting customers and the ability to roll back. These indicate a need for control and reassurance through evidence. **[Direct qualitative evidence; Medium confidence on generality.]**
- **Emotional—hypothesis:** experienced users want to feel current and capable, and may experience embarrassment when a familiar stack becomes obsolete or an incident exposes a blind spot. **[Inference; Low-Medium confidence.]**
- **Social—hypothesis:** practitioners want peers and decision-makers to see them as sound stewards who can explain trade-offs, not framework loyalists. Internal upgrade communication at Shippo and the survey’s coworker/peer learning signals make this plausible, but no Django-specific motivation study was found. **[Inference; Medium-Low confidence.]**

## Triggering situations

**Recurring triggers**

- A feature, bug, integration, query, migration, permission rule, or deployment must change.
- A point/security release, stable release, LTS transition, Python release, or package update appears.
- Tests, CI, observability, or a code review reveal a compatibility, correctness, security, or performance problem.
- A teammate asks for a pattern, explanation, review, or help diagnosing an unfamiliar part of the stack.
- Growth changes query volume, worker memory, cache behavior, latency, or infrastructure cost.

These are **[directly evidenced across surveys and production accounts; High confidence]**.

**Event-triggered situations**

- Ownership changes and the developer inherits an unsupported or undocumented application.
- A security scanner, end-of-support date, customer requirement, audit, or incident forces deferred maintenance into priority.
- A large version jump couples Django, Python, packages, database, and infrastructure changes.
- Traffic growth, cost pressure, or a production regression invalidates previous scaling assumptions.
- A difficult user problem leads to a reproducible framework issue, documentation improvement, talk, package, or first contribution.

The first four are **[direct evidence; High confidence that they occur]**. The contribution transition is **[inference; Medium confidence]**.

## Desired outcomes

- Reduce lead time from required change to safely deployed change without increasing change-failure or rollback rate.
- Keep deployed Django/Python/package versions inside declared support windows; reduce the size and number of skipped upgrade steps.
- Detect incompatibilities and deprecations before production; increase relevant test coverage and staging fidelity.
- Hold or improve correctness, latency, throughput, availability, memory/CPU cost, and security findings appropriate to the service.
- Reduce time to diagnose incidents and unfamiliar code; improve the proportion of changes another teammate can review and operate.
- Continue delivering product work during maintenance instead of freezing all other development.
- Convert repeated fixes into automation, documented decisions, or shared patterns.
- For users who want community participation, shorten the path from a real problem to a well-scoped discussion or contribution.

These are directional, not universal targets. Shippo reported about 20% performance improvement and more than 600 security fixes; Rippling reported over 70% memory savings and 30% cost reduction. Those are case-specific outcomes, not Django benchmarks. **[Direct case evidence plus inference; High confidence in directions, Low in transferable magnitudes.]**

## Current behaviour or status quo

Current users combine official documentation with a mixed operating stack. In the 2025 survey, 79% preferred djangoproject.com to learn Django, while Stack Overflow (39%), AI tools (38%), YouTube (38%), blogs (33%), books (22%), and friends/coworkers (13%) remained meaningful. For staying current rather than learning, djangoproject.com led at 60%; 18% said they did not follow Django development. **[Direct evidence; High confidence for respondents.]**

Projects are heterogeneous: 77% named Django as their most-used web framework, yet 29% also used React, 28% FastAPI, 23% Flask, and 18% each jQuery and Vue. Seventy-six percent used PostgreSQL, 52% Redis, 57% containers in development, and 44% containers in production. Operations advice therefore has to account for surrounding systems and cannot treat “a Django app” as one deployment shape. **[Direct evidence; High confidence.]**

Upgrade practice ranges from continuous to deferred. Mature teams may automate migration, benchmark, run unit/integration/functional tests, use staged traffic, monitor, communicate, and preserve rollback, as Shippo did. Open edX’s deferred path required 14 production services, 62+ repositories, about five months, and 14 staff/contractors who worked full-time for at least a month. Forum users with inherited systems commonly ask whether to jump directly or move incrementally; responses emphasize release notes, tests, deprecation warnings, and third-party-package viability. **[Direct case and qualitative evidence; High confidence that effort varies with system condition.]**

## Pushes

- Unsupported versions turn optional housekeeping into security and continuity risk. **[Direct evidence; High.]**
- Deferred upgrades compound: Open edX had to finish prior upgrade work, modernize dependencies/tests, and clean authentication code to reach the next supported release. **[Direct evidence; High for case, Medium generality.]**
- Product delivery slows when an aged stack blocks newer libraries or capabilities; Shippo explicitly reports this push. **[Direct evidence; High for case.]**
- Production load and cost expose hidden process, connection, caching, database, and worker assumptions. **[Direct evidence; High that this occurs.]**
- Repeated local fixes and tribal knowledge create review, onboarding, and on-call burden. **[Inference supported by developer-experience research; Medium-High.]**
- Users want modern practices such as stronger typing and simpler frontend interactions, but integration and migration cost constrain adoption. **[Survey evidence plus inference; Medium.]**

## Pulls

- A predictable deprecation/release process, current reference documentation, and compatible packages make maintenance tractable. **[Direct process evidence plus inference; High.]**
- Django’s integrated models, migrations, admin, and authentication remain heavily used/favored; they preserve accumulated system knowledge and reduce incentives for wholesale replacement. **[Direct survey evidence plus inference; Medium-High.]**
- Incremental improvement can preserve customer behavior while unlocking performance, observability, security, and newer libraries. **[Direct Shippo evidence; High for feasibility, Low for typical gains.]**
- Peer accounts with code, metrics, failure modes, and trade-offs help practitioners validate that a path works under production constraints. **[Inference from evidence-seeking behavior; High.]**
- Automation that turns deprecations into reviewable edits reduces upgrade toil; the 2025 Steering Council discussion about integrating `django-upgrade` into deprecation work is evidence that this need is recognized, not proof the proposal is implemented. **[Direct proposal evidence; High on status.]**

## Anxieties

- **Legitimate risk:** Django, Python, database, infrastructure, and third-party upgrades can interact in obscure production-only ways. Shippo encountered ORM/PostgreSQL, Celery, and memcached-client failures. **[Direct evidence; High.]**
- **Legitimate risk:** incomplete tests and unknown data paths make “it starts” an inadequate acceptance criterion. The 2025 survey reports 24% using no listed testing framework. **[Direct evidence; High for respondents; response does not prove no tests of any kind.]**
- **Practical concern:** maintenance competes with features and may require coordination across dozens of teams or repositories. **[Direct evidence; High.]**
- **Perceived risk:** Django itself will be the limiting factor at scale. Real cases show both large Django deployments and genuine bottlenecks, but bottlenecks were workload/architecture-specific; a universal scale ceiling is unsupported. **[Direct cases plus inference; Medium-High.]**
- **Misconception:** an LTS upgrade alone resolves all maintenance debt. Open edX and Shippo contradict this; packages, Python, databases, tests, infrastructure, and application code move together. **[Direct evidence; High.]**
- **Emotional resistance—hypothesis:** touching stable legacy code feels less rewarding and more blame-exposed than feature work, encouraging delay. **[Inference; Medium-Low.]**
- **AI concern:** current users increasingly use AI to learn or develop, but generated advice may ignore project version and local constraints. The Django survey establishes use, not correctness or trust. **[Direct use evidence plus inference; Medium.]**

## Habits and inertia

- Stay on an LTS because organizational cadence and known behavior feel safer; 27% reported LTS-only upgrades. **[Direct evidence plus inference; Medium-High.]**
- Postpone upgrades while the system still serves users, allowing skipped releases and package abandonment to accumulate. **[Direct case evidence; High that pattern occurs, unknown prevalence.]**
- Reuse familiar architecture, deployment, debugging, and project templates. Fifty-nine percent still start new projects from scratch, while smaller groups use Cookiecutter or internal tooling. **[Direct evidence; Medium.]**
- Diagnose via logs/print statements: 80% reported doing so, and 29% said they only use log statements for remote/container debugging. This can be entirely appropriate, but also indicates the importance of operational context over IDE-only guidance. **[Direct evidence; High.]**
- Seek help only when an upgrade or incident becomes urgent; isolated forum threads show this reactive pattern but cannot establish prevalence. **[Qualitative signal; Low-Medium.]**
- Follow official updates selectively or not at all; 18% reported not following Django development. **[Direct evidence; High for respondents.]**

## Decision criteria

No source supports a universal ranking. Importance changes by lifecycle and responsibility.

| Criterion | Likely importance | Confidence | What progress requires |
|---|---|---|---|
| Behavioral compatibility and rollback | Very high for production changes | High | Known contracts, migration behavior, staged rollout, monitoring, reversible steps |
| Security and support status | Very high for maintainers | High | Version/support matrix, security implications, package/database compatibility |
| Testability and observable evidence | Very high | High | Deprecation output, targeted/unit/integration/functional tests, benchmarks, production signals |
| Third-party ecosystem viability | High | High | Maintained packages, version classifiers, alternatives, upgrade sequencing |
| Delivery continuity | High | High | Ability to ship priority work during maintenance; coordination and ownership plan |
| Operational performance and cost | High for operators; variable elsewhere | High on conditionality | Workload-specific profiling, capacity, memory/CPU/latency and cost evidence |
| Maintainability and team comprehension | High | Medium-High | Clear conventions, documented decisions, reviewability, type/tool support |
| Recency and version specificity of guidance | High | High | Advice matched to installed/target versions and deployment environment |
| Time/effort and organizational approval | Context-dependent, often high | Medium-High | Scoped work, risk of delay, staffing, milestones, customer impact |
| Community participation opportunity | Low to high by motivation | Medium | Bounded task, process clarity, feedback and recognition; never assume it is desired |

## Main concerns

The central concern is not abstract framework preference; it is **whether the next necessary change can be made with controlled consequences**. Compatibility, security, test evidence, dependencies, production behavior, delivery commitments, and team comprehension converge on that question. **[Inference; High confidence.]**

For active builders, “current best practice” matters only when it improves a real change. For operators, scaling help must begin with symptoms, workload, architecture, and measurements. For legacy inheritors, the immediate need is a credible sequence and risk map. For experts, deeper learning or contribution is optional progress after—not a substitute for—solving the system’s job. **[Inference; High confidence.]**

## Objections and perceived risks

- “Upgrading will consume months and still create regressions.” Legitimate for large deferred systems; smaller/current applications may be much easier. **[Direct contrasting evidence; High.]**
- “The business will not pause feature delivery.” Legitimate constraint; Shippo made continued feature shipping an explicit rule. **[Direct evidence; High.]**
- “Our unmaintained package or old database blocks the route.” Legitimate dependency risk. **[Direct evidence; High.]**
- “Rewriting is cleaner than understanding this system.” Often an emotional/architectural reaction; evidence here supports incremental modernization feasibility but does not prove it is always cheaper than replacement. **[Inference; Medium.]**
- “Django is too slow/old for our scale.” A perceived risk containing legitimate workload-specific concerns. Large deployments disprove a simple universal ceiling, not every performance objection. **[Direct case evidence plus inference; Medium-High.]**
- “Official guidance is too generic for our architecture.” Legitimate limitation: reference and upgrade guidance cannot know local data, contracts, packages, and infrastructure. **[Inference; High.]**
- “Community participation is extra unpaid work.” Legitimate objection; interest in improvements should not be translated into an obligation to contribute. **[Inference grounded in intent/action gap; Medium-High.]**

## Information needed to make progress

- Exact current and target Django/Python versions, support dates, required intermediate versions, deprecations, and backward-incompatible changes.
- A compatibility map for database, cache, task queue, ASGI/WSGI server, deployment platform, and every consequential third-party package.
- Version-specific examples showing the old pattern, target pattern, automated fixer availability, and validation method.
- A system inventory: critical paths, data migrations, external contracts, ownership, test gaps, production signals, and rollback boundaries.
- Effort/risk evidence suitable for leads: skipped releases, unsupported components, security exposure, milestones, staffing, customer impact, and cost of further delay.
- Production accounts that include scale, starting condition, architecture, failed approaches, measurements, and trade-offs—not only success claims.
- Clear routes for usage questions, suspected bugs, design discussions, security reports, and bounded contributions.

**[Inference strongly supported by cases and forum questions; High confidence.]**

## Trusted content formats

- **Versioned reference documentation, release notes, deprecation timelines, and compatibility tables** for authoritative implementation facts. **[Direct behavior/process evidence; High.]**
- **Runnable minimal reproductions, tests, diffs, codemods, checklists, and commands** for applying and verifying a change. **[Direct community/process evidence plus inference; High.]**
- **Production engineering reports with metrics and failures** for validating operational feasibility and trade-offs. **[Direct observed format; High.]**
- **Long-form forum answers and peer reviews** for architecture-dependent diagnosis where context changes the answer. **[Direct qualitative behavior; Medium-High.]**
- **Talks, books, blogs, and podcasts** for synthesis and expertise development; survey use is lower than official docs and varies by role. Reported use is direct, while the synthesis/expertise role is inferred. **[Direct evidence plus inference; Medium.]**
- **AI-assisted answers** for fast exploration, followed by versioned primary documentation, tests, and local evidence. The validation requirement is an inference; the 38% learning use is direct. **[Direct plus inference; High on use, Medium on actual validation behavior.]**

## Discovery, evaluation, validation, and engagement channels

- **Discovery:** djangoproject.com announcements, newsletters, blogs, YouTube, podcasts, Reddit/Hacker News, short-form social, and coworkers can surface releases, techniques, and incidents. In the survey, djangoproject.com dominated following (60%); YouTube 22%, Stack Overflow and Reddit 18%, Forum 15%, newsletter 12%, friends 9%, Hacker News 8%, podcasts and X 7%, Discord 6%, Fediverse 5%, Google Groups and RSS 4%. The proportions are direct respondent behavior; assigning “discovery” is an inference because the survey did not observe episode sequence or causal influence. **[Direct evidence plus inference; Medium.]**
- **Evaluation:** versioned documentation/release notes establish official behavior; substantive blog posts, talks, Stack Overflow/Forum threads, and professional peers help interpret fit for a particular codebase. Team leads in [the 2024 analysis](https://blog.jetbrains.com/pycharm/2024/06/the-state-of-django/) used newsletters, Hacker News, Reddit, X, and friends more than average, suggesting role-specific channel mixes. **[Direct evidence plus inference; Medium-High.]**
- **Validation:** a project’s tests, staging, benchmarks, observability, dependency metadata, minimal reproductions, and source/issues are stronger evidence than any channel claim. Shippo’s staged traffic, monitoring, and rollback show this behavior. GitHub/issue trackers are most relevant when inspecting package activity, source behavior, or a suspected bug—not necessarily as broad discovery channels. **[Direct case evidence plus inference; High.]**
- **Ongoing engagement:** the Forum/Discord support discussion and peer contact; conferences, local meetups, sprints, and contributor systems can enable deeper relationships. Yet 71% reported no event/meetup participation, so events cannot be treated as the default reach channel. Mailing lists are now primarily announcement/update mechanisms; the official Forum is the preferred usage and internals venue. Channel participation and policy are direct; relationship depth is inferred. **[Direct evidence plus inference; Medium.]**

## Decision-makers and influencers

For a routine code change, the implementer may decide, while reviewers, code owners, QA, SRE/platform staff, security, and product owners influence acceptance. For a major upgrade, the initiator is often a maintainer or scanner; the researcher/evaluator is a senior developer or architect; approval may come from an engineering manager, product leadership, or finance; platform, security, database, support, partner, and customer-facing teams can block or bear consequences. Shippo explicitly involved engineers, quality engineering, stakeholders, customer support, partner managers, and protected customer cohorts. **[Direct evidence plus role inference; High confidence.]**

In small teams one person may hold all roles. In large systems, ownership distribution—not framework knowledge alone—determines progress. Users need evidence they can translate into another actor’s language: customer risk, delivery interruption, support status, cost, or reliability. **[Inference; High confidence.]**

## Appropriate next actions for Django to encourage

These are user-progress actions, not marketing asset prescriptions:

- **Inventory the current system and verify support status**—advances the job of keeping the stack supportable.
- **Read the exact intervening release notes and surface all deprecation warnings**—advances a bounded upgrade plan.
- **Add or strengthen a test around one critical behavior before changing it**—advances safe change and inherited-system understanding.
- **Reproduce and measure one production symptom before selecting a scaling remedy**—advances the operator’s job.
- **Stage, observe, and define rollback for consequential upgrades**—advances controlled delivery.
- **Ask a context-rich Forum question or produce a minimal reproduction**—advances diagnosis when local investigation stalls.
- **Share a verified pattern internally through a test, decision record, or example**—advances team capability.
- **Optionally turn a solved problem into a docs correction, issue, talk, package support, or bounded contribution**—advances expertise/community participation only for users who want it.

**[Inference; High confidence that actions map to jobs, not a claim of current conversion effectiveness.]**

## Overlaps with other audiences

- **Technical leads/software architects and CTOs/engineering managers:** overlap when practitioners set standards, negotiate maintenance priority, or approve risk.
- **Companies depending on Django:** the organization bears continuity and migration costs; this report covers the human implementers/advocates.
- **Agencies/consultancies:** multi-project experts add estimation, client communication, and reputation jobs.
- **Ecosystem/core contributors:** overlap begins when a user’s problem becomes upstream work; contributor sustainability and governance are separate jobs.
- **Educators and professional learners:** experts may teach peers; users returning after a long gap may temporarily have learner needs.
- **Security, platform, and SRE audiences:** production responsibility may be shared with people who do not identify primarily as Django users.

## Possible segmentation problems

- “Existing” hides a range from one completed tutorial to a decade operating critical services; responsibility and consequence are better boundaries than elapsed time.
- “Professional developer” hides builders, operators, inherited-system maintainers, consultants, leads, and contributor-adjacent users.
- Survey recruitment through official Django channels likely overrepresents engaged enthusiasts; it should not estimate the silent legacy population or all production deployments.
- Company size is a poor proxy for system complexity, criticality, traffic, regulation, team topology, or upgrade debt.
- Version choice alone does not distinguish responsible LTS strategy from abandonment; support status, patch cadence, and constraints matter.
- Desire for a feature or willingness to contribute is not observed contribution. Event attendance is not a proxy for expertise or belonging.
- Scaling should be segmented by workload and bottleneck rather than a single traffic threshold.
- Geographic representation is uneven (41% Europe, 25% North America, 20% Asia, 8% Africa in the survey), and evidence here is predominantly English-language and organization-visible. **[Direct survey limitations plus inference; High confidence.]**

## Existing-analysis claim audit

| Existing hypothesis | Audit | Assessment |
|---|---|---|
| Existing professional Django developers seek current best practice, releases/upgrades, scaling help, greater expertise, and possible progression from user to contributor. | **Partially supported** | Upgrade behavior, version-specific learning, production scaling cases, and hypothetical contribution interest are supported. “Current best practice” and “greater expertise” are reasonable inferred jobs, but no evidence ranks them across all users. Progression to contributor is possible, not a standard funnel: 45% expressed willingness for one proposed effort, while 71% had never attended a Django event. |
| Touchpoints include docs/release notes. | **Supported with qualification** | djangoproject.com is the leading reported learning (79%) and following (60%) resource. Release notes are repeatedly used/recommended in upgrade practice, but were not separately measured in the survey. Their behavioral role is authoritative evaluation/implementation. |
| Touchpoints include forums/Discord. | **Supported with qualification** | Forum was used by 15% to follow development and directly hosts contextual upgrade/help discussions; Discord was 6%. They are support and ongoing-engagement channels, not universal reach. |
| Touchpoints include GitHub/issue tracker. | **Partially supported** | These are appropriate for source/package activity, reproduction, bugs, and contribution validation. The survey evidence reviewed does not establish them as common general discovery channels for existing users. |
| Touchpoints include mailing lists. | **Partially supported** | Google Groups was 4%; official guidance now routes usage and internals discussions to the Forum while retaining announcement/update lists. Mailing lists are specialized/legacy or announcement channels, not a broad default. |
| Touchpoints include conferences/sprints. | **Partially supported** | Events offer deep engagement, but only 8% reported DjangoCon/similar participation and 21% a smaller event; 71% reported none. No survey measure isolated sprints. |
| Touchpoints include podcasts. | **Supported with qualification** | Seven percent followed Django development via podcasts and 5% preferred them for learning. Useful for synthesis/ongoing engagement, low reported reach. |
| Touchpoints include professional peer networks. | **Supported with qualification** | Friends were 9% for following and friends/coworkers 13% for learning; the 2024 analysis found team leads learned from friends more than average. Evidence does not map all professional networks. |
| Touchpoints include short-form social. | **Supported with qualification** | X (7%) and Fediverse (5%) surface updates. They are discovery channels, not strong evidence for technical validation. |

## Evidence table

| Finding | Source (title, publisher/author, date, URL) | Evidence type | Direct evidence or inference | Confidence | Research notes |
|---|---|---|---|---|---|
| Existing users span work/personal contexts, roles, company sizes, team modes, and experience levels. | [Django Developers Survey 2025 Results](https://lp.jetbrains.com/django-developer-survey-2025/), DSF/JetBrains, survey fielded Nov. 2024–Jan. 2025; results published Oct. 2025 | ~4,600-person self-selected survey | Direct | High for respondents; Medium external validity | Recruitment used official DSF channels; enthusiasts and followers may be overrepresented. |
| Upgrade cadences differ: 48% every stable release, 27% LTS-only, 11% monthly point release, 4% unsupported. | [Django Developers Survey 2025 Results](https://lp.jetbrains.com/django-developer-survey-2025/), DSF/JetBrains, Oct. 2025 | Survey | Direct | High for respondents | Wording/categories may overlap conceptually; does not explain why projects use each cadence. |
| Official Django web resources dominate learning/following, with substantial secondary use of Q&A, AI, video, blogs, and communities. | [Django Developers Survey 2025 Results](https://lp.jetbrains.com/django-developer-survey-2025/), DSF/JetBrains, Oct. 2025 | Survey | Direct | High for respondents | Multi-select channel use; not trust, effectiveness, or causal influence. |
| Django retains meaningful continuation intent outside its own survey: 50.7% admired and 11.3% desired in Stack Overflow’s 2024 web-framework chart. | [Technology — 2024 Developer Survey](https://survey.stackoverflow.co/2024/technology), Stack Overflow, July 24, 2024 | Broad developer survey | Direct | Medium | Independent triangulation; Stack Overflow respondents are self-selected and “admired/desired” is not adoption or job demand. |
| Large upgrades couple application code, packages, database/infrastructure, tests, staged rollout, monitoring, rollback, and stakeholder communication. | [Modernizing Tech Stack at Shippo—Upgrade Python and Django Version](https://goshippo.com/blog/modernizing-tech-stack-at-shippo-upgrade-python-and-django-version), Manoj Pahuja/Shippo, Sept. 22, 2023 | First-party production migration account | Direct | High for case; Medium generality | Detailed 1.1M-line migration; contains a likely version typo (“Django 1.22”), so report does not repeat that starting-version claim. |
| Deferred maintenance can make reaching one supported Django release a multi-repository, multi-month program. | [Django 2.2 upgrade: statistics and lessons learned](https://discuss.openedx.org/t/django-2-2-upgrade-statistics-and-lessons-learned/2391), Jeremy Bowman/Open edX, June 10, 2020 | Direct project retrospective | Direct | High for case; Medium generality | Older but unusually concrete: 14 services, 62+ repos, ~5 months, 14 substantial contributors. |
| Legacy inheritors need tests, release-note review, incremental sequencing, and third-party-package assessment. | [Upgrading from Django 2.0.1 to latest](https://forum.djangoproject.com/t/upgrading-from-django-2-0-1-to-latest/8600), Django Forum participants, July 2, 2021; [Django Upgrade: 3.1 to 4](https://forum.djangoproject.com/t/django-upgrade-3-1-to-4-steps-and-or-advice/25179), Django Forum, Nov. 9, 2023 | Community discussions | Direct qualitative signal | Medium | The first thread's replies directly cover incremental sequencing, tests, release notes, and third-party-package risk. The second thread only shows the same inherited-legacy trigger recurring; its single reply defers to an external conference talk rather than repeating that advice itself. Forum answers are expert advice, not representative outcome research. |
| Django systems can reach very large scale, while performance bottlenecks remain architecture/workload-specific. | [Rippling’s Gunicorn pre-fork journey](https://www.rippling.com/blog/rippling-gunicorn-pre-fork-journey-memory-savings-and-cost-reduction), Xiayang Wu/Rippling, Oct. 28, 2025; [Reining in the thundering herd](https://joinclubhouse.ghost.io/reining-in-the-thundering-herd-with-django-and-gunicorn/), Clubhouse engineering, 2021 | First-party production engineering accounts | Direct cases; inference on segmentation | Medium-High | Exceptional-scale cases disprove a simple ceiling but do not predict ordinary workloads or comparative efficiency. |
| Very large Django organizations may invest years in maintainability tooling such as static typing. | [Static typing Python at scale—Our journey with mypy and Django](https://engineering.kraken.tech/news/2026/02/16/static-typing-python-at-scale.html), Kraken Engineering, Feb. 16, 2026 | First-party engineering account | Direct | High for case; Low prevalence | 2,000+ models and 2.5-year effort; useful evidence of expert/team-enablement job, not a default prescription. |
| Developers need workload- and user-centered delivery practices; technical debt hinders productivity. | [2024 Accelerate State of DevOps Report](https://dora.dev/research/2024/dora-report/), DORA/Google Cloud, 2024 | Cross-industry research report | Direct general evidence; inference to Django | Medium-High | Not Django-specific; supports consequence and developer-experience dimensions rather than framework claims. |
| Automation of Django deprecation changes is a recognized current need, but integration into core process remained exploratory. | [Making django-upgrade part of deprecation policy and release cycle](https://forum.djangoproject.com/t/making-django-upgrade-part-of-deprecation-policy-and-release-cycle/43377), Django Steering Council discussion, Nov. 10, 2025–Jan. 29, 2026 | Governance/community proposal | Direct | High on proposal status | Do not present as shipped policy or guaranteed roadmap. |
| Event attendance and contribution intent do not justify treating all existing users as community participants. | [Django Developers Survey 2025 Results](https://lp.jetbrains.com/django-developer-survey-2025/), DSF/JetBrains, Oct. 2025 | Survey | Direct data; inference | Medium-High | 71% no event; typing question measured hypothetical willingness for a specific effort, not actual contributions. |
| Team leads reported using the Django News newsletter, Hacker News, Reddit, and X more than average respondents, and cited friends as a learning source more often (16% vs. 11% average). | [The State of Django 2024](https://blog.jetbrains.com/pycharm/2024/06/the-state-of-django/), JetBrains PyCharm Blog, June 2024 | Secondary analysis of the 2024 Django Developers Survey | Direct | Medium | Role breakdown from the prior survey year, not re-measured in the 2025 results; single secondary write-up, not the raw dataset. |

## Unanswered research questions

- What proportion of production Django applications are inside support, and how does this differ by organization size, criticality, region, and regulated industry?
- Which upgrade barriers most often dominate: application APIs, Python, packages, data migrations, database/infrastructure, tests, ownership, or budget?
- How do upgrade time and failure rate differ between every-release, LTS-to-LTS, and long-deferred strategies after controlling for codebase age and size?
- Which information do active builders seek most often after introductory learning, and where do official docs fail to resolve version- or architecture-specific tasks?
- How do practitioners actually validate AI-generated Django advice, and what errors arise from version mismatch?
- What are the most common production Django bottlenecks by workload, and which symptoms lead teams to change architecture versus tune the application/infrastructure?
- What distinguishes users who want deeper expertise but not contribution from those who contribute once, become repeat contributors, teach, maintain packages, or sponsor work?
- How much uncompensated maintenance/on-call labor falls on individual Django specialists, and what emotional/burnout effects follow?
- How do consultants, public-sector maintainers, nonprofits, and teams outside English-language channels differ from visible software-company accounts?
- Which channels cause action—successful upgrade, resolved incident, adopted practice, or first contribution—rather than merely awareness?

<!-- RESEARCH PROVENANCE: BEGIN -->
## Research provenance

This section was generated from the recorded Codex session JSONL logs. File attribution uses successful patch events; searches and domains use nested web-tool calls.

### Session `019f7560-0549-7052-a5c7-3158bbfbc62d`
- Log: `rollout-2026-07-18T15-17-34-019f7560-0549-7052-a5c7-3158bbfbc62d.jsonl`
- This document: `add`
- Search queries:
  - `DORA 2024 developer experience documentation technical debt productivity report`
  - `Django Developers Survey 2024 results upgrade versions deployment testing official`
  - `Django Developers Survey 2025 results JetBrains Django Foundation`
  - `Django at scale operations engineering blog Instagram Disqus Zulip`
  - `Django monolith scaling production engineering case study`
  - `Django operations production incident postmortem engineering`
  - `Django production operations scaling postmortem upgrade case study`
  - `Django upgrade case study large codebase production engineering blog`
  - `Django upgrade discussion legacy code production forum`
  - `Django upgrade experience survey technical debt discussion`
  - `GitHub Octoverse Django adoption Python framework`
  - `Stack Overflow Developer Survey 2024 Django professional developers official`
  - `Stack Overflow Developer Survey 2025 Django web frameworks results official`
  - `site:blog.sentry.io Django production scaling performance engineering`
  - `site:engineering.* Django upgrade production case study Django 4 5`
  - `site:engineeringblog.yelp.com Django performance scaling production`
- Website domains:
  - `arxiv.org`
  - `aws.amazon.com`
  - `blog.jetbrains.com`
  - `cloud.google.com`
  - `code.djangoproject.com`
  - `computersciencejournals.com`
  - `d-nb.info`
  - `d1.awsstatic.com`
  - `dam-cdn.atl.orangelogic.com`
  - `dev.to`
  - `devecosystem-2025.jetbrains.com`
  - `discuss.openedx.org`
  - `diva-portal.org`
  - `django-deployments.readthedocs.io`
  - `django-polymorphic.readthedocs.io`
  - `django-upgrade.readthedocs.io`
  - `django.readthedocs.io`
  - `djangoproject.com`
  - `djangostars.com`
  - `docs.djangoproject.com`
  - `dora.dev`
  - `dspace.ut.ee`
  - `em-tools.io`
  - `en.wikipedia.org`
  - `engineering.fb.com`
  - `engineering.kraken.tech`
  - `files01.core.ac.uk`
  - `forum.djangoproject.com`
  - `github.blog`
  - `github.com`
  - `goshippo.com`
  - `homepages.dcc.ufmg.br`
  - `ijeret.org`
  - `itpro.com`
  - `jetbrains.com`
  - `jetbrains.com.cn`
  - `joinclubhouse.ghost.io`
  - `leaddev.com`
  - `linkedin.com`
  - `linuxuzmani.com`
  - `lp.jetbrains.com`
  - `meta.stackoverflow.com`
  - `objectstorage.ap-dcc-gazipur-1.oraclecloud15.com`
  - `offline-pixel.github.io`
  - `openedx.atlassian.net`
  - `pure.rug.nl`
  - `pure.tudelft.nl`
  - `reddit.com`
  - `repo.pw.edu.pl`
  - `rippling.com`
  - `ru.wikipedia.org`
  - `sanketsaurav.github.io`
  - `security.snyk.io`
  - `stackoverflow.blog`
  - `stackoverflow.co`
  - `subscription.packtpub.com`
  - `survey.stackoverflow.co`
  - `surveys.jetbrains.com`
  - `tanujgarg.com`
  - `techradar.com`
  - `thegarywilson.com`
  - `typing.readthedocs.io`
  - `usenix.org`
  - `webbyfox.co.uk`
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
