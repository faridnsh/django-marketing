# Former Django users reassessing fit

## Audience definition and boundaries

This audience consists of people and teams that used Django materially but no longer use it for most new work, no longer operate their former Django system, or deliberately moved all or part of a system away. “Former” is a **lifecycle state**, not a role, skill level, organization type, or stable identity. It includes returners actively reconsidering Django.

The boundary matters because stopping Django use does not necessarily mean rejecting Django. Public accounts show at least three distinct mechanisms:

- **Project/context change:** a dynamic application becomes static content, or a service no longer needs templates, persistence, admin, or ORM. Manca removed an over-engineered database/back office from a blog ([November 16, 2019](https://florimond.dev/en/posts/2019/11/starlette-migrate-blog-across-domains)); Mozilla moved MDN content to Git/GitHub while initially retaining reduced Django services for accounts and search ([October 29, 2020](https://hacks.mozilla.org/2020/10/mdn-web-docs-evolves-lowdown-on-the-upcoming-new-platform/)). **Direct evidence; High confidence for the mechanism, not incidence.**
- **Architecture/organization change:** DoorDash credited Django with rapid MVP delivery, then moved toward microservices after growth produced slow tests, longer ramp-up, brittleness, and a need to isolate business lines ([December 2, 2020](https://careersatdoordash.com/blog/how-doordash-transitioned-from-a-monolith-to-microservices/)). **Direct evidence; High confidence for this case, Low confidence for ordinary teams.**
- **Framework or ecosystem dissatisfaction:** some former users object to persistence coupling, non-relational fit, async experience, frontend integration, or the value of bundled conveniences ([Meyvis, January 7, 2026](https://www.natemeyvis.com/on-not-using-django-in-2026/); [Prin, November 19, 2022](https://medium.com/@waprin/why-i-ditched-django-for-nextjs-5ea7dc35779d)). **Direct anecdotes; Medium confidence that concerns recur, Low confidence on prevalence.**

Excluded are current users merely experimenting elsewhere, tutorial-only users, and Django-naive evaluators. People can overlap other role audiences; this lens concerns the job created by prior experience and subsequent distance.

## Important subsegments

- **Context-fit leavers:** Django was appropriate for an earlier application, but the next workload is static, narrowly scoped, non-relational, frontend-centric, or otherwise no longer benefits from its integrated capabilities.
- **Scale and organizational-architecture migrants:** teams decomposing a mature monolith for domain isolation, independent deployment, fault boundaries, or team autonomy. The departure may be from the monolith, Python, or a shared database as much as from Django.
- **Framework-dissatisfied former users:** people who attribute their departure to coupling, abstraction, ORM behavior, async constraints, configuration, testing cost, or difficulty going outside Django’s conventions.
- **Frontend/platform consolidators:** developers who prefer one language and component model across browser, server rendering, and backend boundaries. This is partly an ecosystem/toolchain job rather than a verdict on Django’s backend capabilities.
- **Employment- or client-context switchers:** Django use stopped because the person changed jobs, inherited another stack, followed an organizational standard, or served a different client. Their personal evaluation may never have changed.
- **Partial migrants and maintainers of residual Django:** new capabilities are built elsewhere while Django remains responsible for legacy workflows, data, admin, authentication, or templates. “Former” is gradual and subsystem-specific here.
- **Returners and conditional returners:** former users reconsidering Django because a new project again needs relational CRUD, authentication, migrations, admin, strong conventions, or rapid delivery with a familiar stack.

These are behavioral subsegments, not a maturity ladder. No evidence found supports ranking their size.

## Primary job to be done

> When a new project or changed system makes my previous Django decision relevant again, I want to reassess the current fit using the real workload and what I learned after leaving, so I can choose a productive foundation without repeating old pain or paying an unnecessary switching cost.

This is a **researcher inference; High confidence**. Direct departure and return accounts consistently frame the decision around changed requirements, architecture, accumulated experience, and delivery cost—not simply brand preference.

## Additional jobs to be done

There are six important jobs in total, including the primary job.

1. **Reassess current fit (primary).** When a new project or material change makes prior Django experience relevant again, I want to test today’s project and team needs against Django’s current behavior and my reasons for leaving, so I can choose without treating old experience as current evidence.
2. **Diagnose the real cause of departure.** When I reconsider why Django stopped fitting, I want to separate framework constraints from architecture, outdated versions, packages, team practice, or changed product needs, so I can avoid repeating the wrong diagnosis. DoorDash and MDN describe system/context changes; peers in one migration discussion questioned whether poorly structured code required a new framework ([Reddit r/FastAPI, September 7, 2024](https://www.reddit.com/r/FastAPI/comments/1fau81g/migration_from_django_to_fastapi/)). **Inference; High confidence.**
3. **Recover valuable integrated capabilities.** When separately assembled authentication, persistence, migrations, admin, validation, or structure create recurring work, I want to reassess whether an integrated foundation fits, so I can reduce unnecessary ownership without assuming integration is always better. Return anecdotes describe recreating Django or missing prescribed structure ([Reddit, March 23, 2024](https://www.reddit.com/r/django/comments/1blpjp2/fast_api_or_not/); [Reddit, October 28, 2021](https://www.reddit.com/r/learnpython/comments/qha3hj/flask_or_django_or_both/)). **Direct anecdotes; Medium confidence for the trigger, Low on prevalence.**
4. **Preserve delivery momentum.** When uncertainty and learning in a new stack slow a time-sensitive product, I want to compare that cost with accumulated Django skills and conventions, so I can reach customer feedback sooner without confusing familiarity with fit. Dan Rowden returned after reporting that several weeks of Next.js work were nearly matched by one evening rebuilding in familiar Django ([August 2, 2023](https://danrowden.com/blog/why-ive-gone-back-to-django-for-my-new-thing/)). **Direct anecdote; Medium confidence for this mechanism.**
5. **Manage a reversible transition.** When a system must move away from or back toward Django, I want a bounded seam and incremental migration path, so I can preserve users, data, operations, and rollback while the old and new systems coexist. DramaFever expected years of coexistence ([January 27, 2014](https://blog.gopheracademy.com/moving-to-go/)); DoorDash also staged extraction. **Direct evidence; High confidence for large-system practice.**
6. **Refresh a stale Django mental model.** When my Django knowledge comes from an older version or ecosystem, I want to establish what behavior and practice are current, so I can judge today’s fit rather than a remembered stack. A developer returning after four FastAPI years asked what was now standard for Django APIs ([Reddit, September 26, 2025](https://www.reddit.com/r/django/comments/1nr32uj/back_to_django_after_4_years_with_fastapi_whats/)). **Direct anecdote; Medium confidence.**

## Functional, emotional, and social dimensions

| Job | Core functional job | Emotional job | Social job | Supporting jobs |
|---|---|---|---|---|
| Reassess current fit | Match current workload, team, and lifecycle needs to a technical foundation | **Hypothesis:** avoid both regret and nostalgia-driven choice | **Hypothesis:** be seen as evidence-led rather than trend-chasing or defensive of old expertise | State requirements; inspect current capabilities; prototype; define disqualifiers and exit conditions |
| Diagnose the departure | Attribute prior pain to framework, version, architecture, ecosystem, or practice | Replace a vague negative memory with confidence about the real cause (**inference**) | Explain the prior decision fairly to peers and approvers (**hypothesis**) | Reconstruct timeline; compare alternatives considered; identify bottlenecks and unused features |
| Recover integrated capabilities | Obtain coherent data, auth, admin, migration, and application conventions where valuable | Reduce fatigue from repeatedly assembling infrastructure (**hypothesis**) | Help the team converge on shared conventions (**inference**) | Inventory replacement components; compare maintenance ownership; test extension points |
| Preserve momentum | Deliver a testable product increment quickly | Regain the feeling of fluency and progress (**direct in Rowden’s account; otherwise anecdotal**) | Demonstrate dependable delivery to collaborators or customers (**hypothesis**) | Reuse knowledge; minimize novel decisions; stage optional frontend or service changes |
| Manage transition | Move responsibility without unsafe rewrite or user disruption | Reduce fear of irreversible migration failure (**hypothesis**) | Maintain trust with operators, leadership, and users (**hypothesis**) | Define seams; dual-run; migrate data; observe; roll back; retire old paths |
| Refresh mental model | Replace remembered behavior with current facts and practice | Reduce uncertainty and embarrassment about being out of date (**hypothesis**) | Re-enter technical discussion credibly (**hypothesis**) | Read release/support material; inspect active packages; build a small current example; consult practitioners |

Emotional and social claims are **Low-to-Medium confidence**. The public record contains frustration, fear of breaking code, excitement, and regained momentum, but no representative interview study of former Django users.

## Triggering situations

**Event-triggered**

- A greenfield application resembles a database-backed product the person previously built with Django.
- A replacement stack grows to need authentication, admin workflows, relational models, migrations, permissions, and background work together.
- Delivery stalls because the team is learning too many unfamiliar tools or making too many architectural decisions.
- A new employer, client, acquisition, or internal standard brings Django back into scope.
- An old Django application must be upgraded, revived, extracted from, or replaced.
- A scale, latency, reliability, or organizational incident forces review of the current architecture.
- A release or ecosystem change appears to address a remembered objection, or the replacement creates new integration pain.

**Recurring**

- Maintaining residual Django code while new services use another stack.
- Comparing framework fit for successive projects rather than choosing a permanent personal stack.
- Monitoring whether prior objections remain true and whether critical packages remain healthy.
- Answering colleagues who ask why the team left, stayed, or should reconsider.
- Preserving enough Django literacy to operate an inherited system or keep a return option open.

This trigger set is **inference, Medium-to-High confidence**. Direct accounts support each mechanism, but their frequency is unknown.

## Desired outcomes

- Reduce time from “should we reconsider?” to a decision backed by current facts and a representative vertical slice.
- Identify whether prior pain arose from Django itself, a third-party dependency, code structure, team process, or workload mismatch.
- Reduce components and integration boundaries the team must own when integrated capabilities are valuable.
- Reduce time to the first customer- or user-testable increment.
- Preserve data integrity, URL/API compatibility, availability, and rollback during any staged move.
- Meet workload-specific latency, throughput, concurrency, security, and operability thresholds without assuming a framework label determines them.
- Increase confidence that the selected stack can be maintained, upgraded, staffed, and exited over the expected system lifetime.

These are **directional inferred outcomes; High confidence**. No evidence supports universal numeric targets.

## Current behaviour or status quo

The status quo is usually **not using Django for new work while relying on the replacement’s accumulated knowledge and tooling**. Organizations may still route new domains away from a residual Django system. Knowledge becomes stale, so evaluation often begins with search, blogs, discussions, and “what is standard now?” questions.

Departure is often incremental: DramaFever kept enhancing Django during extraction, DoorDash described staged extraction, and Mozilla reduced Django’s scope. **Direct evidence; High confidence that partial departure exists.**

Aggregate surveys cannot identify former users cleanly. The PSF/JetBrains Python Developers Survey 2024 found Django used by 35% of respondents, FastAPI by 38%, Flask by 34%, and substantial cross-usage; 45% of Django users also reported FastAPI ([survey results, responses collected October–November 2024](https://lp.jetbrains.com/python-developers-survey-2024/)). The Django Developers Survey 2025 similarly found 28% of its Django-engaged sample also used FastAPI and 23% Flask ([fielded November 2024–January 2025](https://lp.jetbrains.com/django-developer-survey-2025/)). These data show multi-framework behavior, **not migration direction or abandonment**. **Direct aggregate evidence; Medium confidence for coexistence, Low confidence for the former-user audience.**

## Pushes

There are two time horizons.

**Pushes that originally moved people away**

- The application stopped needing Django’s integrated capabilities, became frontend-centric, or narrowed to a small service.
- High traffic, slow tests, brittle coupling, long developer ramp-up, shared-database contention, or organizational scaling made domain isolation and independent deployment more important.
- The team wanted async-first execution, non-relational persistence, more explicit data access, or less model/persistence coupling.
- Old runtimes, poor code, missing tests, and outdated dependencies became associated with “Django,” even when attribution was disputed.

**Pushes away from the current non-Django status quo and toward reassessment**

- Replacement-stack assembly grows into an informal framework spanning auth, persistence, admin, validation, migrations, permissions, and tests.
- Learning the replacement consumes scarce early-project momentum.
- A new project matches the relational, user/account, workflow, and internal-operations shape where Django previously accelerated delivery.
- A client, employer, or existing codebase creates a practical need to regain Django fluency.

The first group has **Medium confidence** from varied direct accounts; the second has **Medium confidence** from return anecdotes.

## Pulls

**Pulls of the post-Django status quo** include narrower framework scope, architectural freedom, async-first APIs, a single frontend/backend language, explicit data access, static deployment, independent services, or alignment with an employer’s stack. Their value is conditional on workload; this report does not rank alternatives.

**Pulls that can make Django relevant again** include familiar productivity, a coherent set of conventions, the ORM and schema migrations, authentication, admin, and an established way to structure a database-backed application. Return accounts emphasize reduced decision burden and faster progress; another former Flask user described Django’s prescribed structure and included functionality as freeing once projects became more complex ([Reddit r/learnpython, October 28, 2021](https://www.reddit.com/r/learnpython/comments/qha3hj/flask_or_django_or_both/)). Current-user survey evidence is directionally consistent: in the 2025 Django survey, models (68%), admin (48%), migrations (30%), and authentication (28%) were among favorite core components. **Direct current-user evidence; Medium confidence as a possible return pull, not evidence of former-user conversion.**

A separate pull is **option value**: Django can remain a bounded part of a mixed architecture. Mozilla initially retained it for accounts and search; the 2024 Untangled account retained Django while replacing a Django async process with FastAPI because a full data/admin migration would be costly ([September 28, 2024](https://www.untangled.dev/2024/09/28/two-microservices-into-one/)). **Direct evidence; Medium confidence.**

## Anxieties

- **Repeating old pain with stale assumptions:** returning may recreate coupling, test cost, frontend friction, or performance constraints, while the remembered version may no longer describe current practice.
- **Trend and career risk:** a former user may fear appearing backward-looking or investing in skills with less perceived market momentum. This is a **hypothesis; Low confidence**.
- **Loss of architectural control:** batteries and conventions may feel productive initially but constraining later, especially off the expected path.
- **Replacement regret in the other direction:** returning may sacrifice async-first ergonomics, a unified JavaScript/TypeScript toolchain, non-relational fit, or service independence.
- **Migration cost:** database ownership, authentication, sessions, URLs, templates, and business logic can make either exit or return a multi-year program.
- **Evidence and ecosystem ambiguity:** scale stories and synthetic benchmarks may not predict the workload; critical extensions may lag even when core is healthy.
- **Emotional resistance:** prior frustration can turn a context-specific failure into a durable identity claim (“Django is not for me”). This is plausible but **Low confidence** without interviews.

## Habits and inertia

- Fluency, templates, deployment pipelines, libraries, observability, and peer support now favor the replacement stack.
- Career and employer incentives can keep Django out of consideration even if technical fit changes.
- A successful migration becomes part of team identity and architecture rationale; reopening it has social and coordination cost.
- Residual Django data models, admin workflows, and business logic pull in the opposite direction, making complete removal expensive.
- Former users reuse remembered heuristics—“too heavy,” “fast to ship,” “not async,” “great admin”—because retesting every claim is costly.
- Sunk cost works both ways: prior Django knowledge lowers return cost, while investment in the replacement raises it.
- Incremental coexistence can become permanent because it avoids a risky rewrite, even while duplicate systems increase maintenance.

These are **inferences; High confidence** for the mechanisms, unknown strength by segment.

## Decision criteria

No former-user-specific study ranks criteria. The table states likely importance, not a universal order.

| Criterion | Likely importance | Confidence and evidence |
|---|---|---|
| Fit to application shape: data, workflows, admin, auth, UI/API, realtime and jobs | High | **High confidence.** Manca, Mozilla, and Ironbound show needed capabilities changed the choice. |
| Evidence that the original departure cause is understood and still relevant | High | **High confidence, inference.** Architecture, framework, version, packages, and team practice lead to different remedies. |
| Time to a production-capable increment | High for early products | **Medium confidence.** Rowden is anecdotal; DoorDash credits Django’s early time-to-market. |
| Maintainability, testability, comprehensibility, and upgrades | High for long-lived systems | **High confidence.** DoorDash, DramaFever, and Mozilla cite these concerns. |
| Performance, concurrency, isolation, and resource cost | Context-dependent | **High confidence it matters; Low on outcome without a workload.** Large cases are not general benchmarks. |
| Need for integrated ORM, migrations, auth, admin, forms/validation, and conventions | High when several are needed together; low for narrow/static services | **High confidence.** Direct departure and return accounts show both sides. |
| Frontend and toolchain coherence | High for frontend-centric products, lower elsewhere | **Medium confidence.** Prin’s detailed account is direct but individual. |
| Async-first and non-relational fit | High for relevant workloads | **Medium confidence.** Meyvis identifies both directly; aggregate survey cross-usage supports coexistence but not causation. |
| Team fluency, hiring, standards, and support ownership | High in organizations | **High confidence from DoorDash’s case; incidence unknown.** |
| Migration cost, reversibility, and duration of dual-running | High for existing systems | **High confidence.** DramaFever and DoorDash describe staged multi-year responsibility transfer. |
| Ecosystem health and current practice | Medium to high | **Medium confidence.** Returners explicitly seek current API conventions; current-user surveys show broad cross-framework/package use but are self-selected. |

The 2025 Stack Overflow survey reports that 46.4% of respondents who had done extensive Django work in the prior year wanted to continue using it, versus 55.5% for FastAPI and 41.7% for Flask ([Technology, 2025](https://survey.stackoverflow.co/2025/technology/)). This is an “admired” continuation measure across a broad self-selected sample, **not a former-user return rate, a satisfaction score for all users, or a basis for competitor ranking**.

## Main concerns

**Practical concerns:** how much of the prior code or knowledge is reusable; whether current Django fits the data and request model; package compatibility; deployment; test speed; database behavior; async boundaries; and how to stage data, auth, URL, and API transitions.

**Legitimate limitations:** an integrated database-backed framework can be unnecessary for static content or narrow services; synchronous dependencies can constrain async benefits; the ORM does not fit every persistence model; server-rendered conventions do not automatically solve a frontend-centric component architecture; monolith convenience can create coupling that large organizations later need to unwind.

**Perceived risks:** “Django is old,” “Django cannot scale,” or “all modern applications need an async microservice framework.” These claims are too broad. Current surveys show ongoing use, and large deployments show possibility; neither establishes suitability for a particular system.

**Organizational objections:** approved languages/platforms, security and operations ownership, hiring, service architecture standards, migration budget, and the opportunity cost of reopening a settled decision.

**Emotional resistance (hypothesis):** attachment to the successful replacement, defensiveness about the prior migration, fear that returning admits the earlier decision was wrong, or nostalgia for prior fluency. **Low confidence.** Public technical postmortems rarely investigate these motives directly.

## Objections and perceived risks

- **“We left, so Django failed.” — Often a misattribution risk.** MDN changed its content/contribution model; DoorDash changed its architecture and organization at enormous scale; Manca removed the need for a database. These do not prove framework dissatisfaction.
- **“Django was good before, so it is the fastest route again.” — Familiarity bias.** It may be true for a fitting application, as Rowden’s account illustrates, but current requirements and team constraints must be tested.
- **“The replacement is faster, therefore migration will improve the product.” — Incomplete.** Framework throughput, application bottlenecks, database behavior, development cost, and migration risk are different measures. The 2024 FastAPI migration thread includes peers advising diagnosis/refactoring because the described system also had old Python/Django, weak structure, no tests, and poor documentation.
- **“Django means monolith, and monolith means failure.” — Misconception with a legitimate coupling concern.** Django can participate in a mixed architecture; DoorDash also documents substantial early benefits from its monolith before organization-scale constraints changed.
- **“Batteries included eliminates architecture work.” — Misconception.** Integrated components reduce some choices but do not design domain boundaries, queries, frontend architecture, deployment, or team ownership.
- **“Returning means rewriting everything.” — Usually false as a universal claim.** Staged extraction, coexistence, and bounded services are documented; feasibility depends on data and ownership seams.
- **“A newer API style resolves every prior objection.” — Perceived risk.** Typed schemas or async endpoints may address one concern while leaving persistence coupling, package health, or organizational architecture unchanged.

## Information needed to make progress

- A short, factual record of why Django use stopped: trigger, constraints, version, architecture, packages, evidence available then, and outcomes after switching.
- A classification of each remembered objection as core-framework behavior, third-party behavior, application design, outdated version, team practice, or workload mismatch.
- Current supported-version facts and a concise delta from the last version used.
- Current approaches to the person’s actual sticking points: API schemas/typing, async boundaries, frontend integration, non-relational data, test performance, deployment, and package compatibility.
- A capability/ownership inventory: auth, authorization, admin, persistence, migrations, validation, jobs, API contracts, observability, and who maintains each in either choice.
- Representative migration accounts that disclose workload, team scale, duration, retained Django responsibilities, and negative as well as positive outcomes.
- A bounded proof using the real database shape, one important workflow, one integration, authentication/permissions, tests, and the intended deployment path.
- Explicit disqualifiers, success thresholds, rollback conditions, and the cost of dual-running.
- Evidence that critical packages and operational practices have active ownership.
- Team and organization facts: available expertise, standards, reviewers, staffing, roadmap, and who bears on-call and upgrade consequences.

These are **inferred needs; High confidence**. They prevent a return decision from collapsing into generic framework comparison.

## Trusted content formats

- **First-person migration and return postmortems with dates, architecture, trade-offs, and what remained.** They help former users recognize comparable contexts. DoorDash, Mozilla, DramaFever, Manca, Prin, Meyvis, and Rowden are useful precisely because their motives differ. Isolated accounts remain qualitative.
- **Versioned technical documentation, release notes, upgrade guides, and security/support policy.** These replace stale memory with authoritative facts. Their role is validation, not persuasion.
- **Runnable current examples and representative proofs.** Former users need to test the exact capability that failed or became unnecessary, not repeat a generic tutorial.
- **Architecture diagrams and staged-migration write-ups.** These make boundaries, data ownership, coexistence, and rollback visible.
- **Source, issue, release, and package-maintenance history.** These validate current behavior and ecosystem risk beyond a summary article.
- **Detailed community discussions with multiple experienced viewpoints.** These expose alternative diagnoses, such as refactoring versus framework replacement, but votes and confident tone do not make an anecdote representative.
- **Aggregate surveys with transparent questions and methodology.** These establish ecosystem context and cross-usage, not individual migration causality.

## Discovery, evaluation, validation, and engagement channels

**Discovery:** search, Reddit, Stack Overflow, newsletters, talks, coworkers, and engineering blogs reopen consideration and supply candidate explanations; they do not settle the decision.

**Evaluation:** current documentation establishes supported behavior; source/package histories expose maintenance; postmortems reveal comparable constraints; a local proof asks whether the old reason still applies.

**Validation:** comparable practitioners, relevant reviewers, representative tests, and detailed postmortems challenge the attribution and plan. Logos and isolated social claims are weak validation.

**Ongoing engagement:** security/release notices preserve a return option; issues/forums resolve edge cases; professional channels refresh awareness; residual teams preserve internal operational knowledge.

The 2025 Django survey reports that its current-user respondents preferred djangoproject.com (79%), Stack Overflow (39%), AI tools (38%), YouTube (38%), blogs (33%), books (22%), friends/coworkers (13%), and podcasts (5%) for learning. It also found 71% had never attended a Django-related event. **Direct evidence among a DSF-recruited current-user sample; Medium confidence for format behavior, Low confidence for former users.** GitHub/issue trackers, release notes, forums, and professional peers have strong functional roles in migration evaluation even where this research found no former-user channel-share data.

## Decision-makers and influencers

- **Solo project:** the former user is initiator, evaluator, approver, operator, and consequence bearer.
- **Existing organizational system:** an engineer or incident may initiate; staff engineers/architects evaluate boundaries; engineering managers or CTOs approve time and standards; platform/SRE, database, security, frontend, and data teams influence or block; product leadership weighs feature delay; finance may scrutinize a multi-quarter migration.
- **Residual Django system:** current maintainers and domain experts are critical influencers because they know hidden workflows, data semantics, admin use, and migration hazards.
- **Replacement-stack specialists:** may fairly identify capabilities and costs that a return would forfeit; they should not be treated merely as resistance.
- **Users and consequence bearers:** developers carry learning and maintenance costs; operators carry reliability/on-call costs; internal admin users can lose workflows; customers carry outages, regressions, and delayed delivery.

DoorDash’s migration required engineering-wide alignment, management buy-in, formal program tracking, and representatives across teams. **Direct evidence; High confidence for a large organizational case, Low confidence on governance in smaller teams.**

## Appropriate next actions for Django to encourage

These are progress actions tied to audience jobs, not substitutes for the jobs themselves.

1. **Write a one-page departure diagnosis.** For “diagnose the real cause”: record what changed, hurt, and improved after leaving.
2. **Check the old disqualifier against a supported release.** For “refresh the mental model”: verify one remembered limitation in documentation and code.
3. **Classify the new project before choosing.** For the primary job: identify its application shape and which integrated capabilities create value.
4. **Build one representative vertical slice with explicit pass/fail criteria.** Connects to reassessment and delivery momentum: include data, auth/permission, API/UI, tests, and intended deployment—not a toy benchmark.
5. **Inventory current capabilities and owners.** For recovering integrated capabilities while guarding against familiarity bias.
6. **Choose a bounded coexistence seam.** For reversible transition: define data ownership, contract, observation, rollback, and retirement.
7. **Consult a practitioner with comparable constraints.** For validation of the exact workload, not generic preference.
8. **Keep lightweight awareness after “not now.”** For option value: follow support and changes relevant to the original objection.

## Overlaps with other audiences

- **Existing professional Django developers:** partial migrants may still operate Django; returners become current users again. The former-user lens adds departure memory and comparison experience.
- **Experienced backend engineers:** many former users evaluate workload, architecture, performance, and maintainability as senior individual contributors.
- **Technical leads/software architects and CTOs/engineering managers:** organizational exits and returns require standards, staffing, migration budget, and risk decisions beyond individual preference.
- **Startups and solo builders:** return triggers often center on delivery momentum and obtaining integrated product capabilities quickly.
- **Large organizations:** DoorDash-like cases involve domain isolation, team scaling, platform standards, and multi-year migration governance.
- **Frontend/full-stack developers:** toolchain consolidation and rendering/component architecture can be the primary departure cause.
- **Agencies/consultancies:** stack choice may follow client needs and maintainability across handoff, making “former” engagement-specific.
- **Package maintainers/contributors:** a former user may retain ecosystem involvement, but contribution is not implied by prior use.

## Possible segmentation problems

- **“Former” is not binary.** A person can stop new Django work while maintaining a monolith, using only the ORM/admin, or advising a Django team.
- **Framework departure is confounded with architecture, language, database, frontend, employer, and product changes.** Treating all migration as Django dissatisfaction will produce the wrong job.
- **Public postmortems overrepresent notable migrations and strong opinions.** Quiet employment-driven switching and satisfied non-returners leave less evidence.
- **Individual and organizational decisions differ.** A solo developer can restart in an evening; a large team may need years, management sponsorship, and data-domain redesign.
- **Recency changes meaning.** Someone whose last use was Django 1.x has a different refresh job from someone who left a supported 5.x/6.x project.
- **Success after leaving does not prove the original framework was unsuitable.** The replacement may coincide with a rewrite, new architecture, additional staffing, or a reduced feature set.
- **Returning does not prove Django is generally superior.** Familiarity and a newly fitting application can dominate one decision.
- **Survey categories do not reveal sequence.** Cross-usage and “want to continue” measures cannot identify who migrated, why, or whether they returned.
- **“Former Django user” can be a context, not a targetable audience.** If prior experience has no effect on the present decision, the person is better studied under their current role and workload.

## Existing-analysis claim audit

| Existing-analysis claim | Audit | Rationale |
|---|---|---|
| A mid-to-large-company technical decision-maker approves framework standards based on currency/relevance, long-term reliance, community/support, security, and hiring; enterprise examples, production architecture, and testimonials influence them. | **Partially supported** | DoorDash directly shows architecture, organization scaling, management buy-in, and production evidence matter. This research did not establish a ranked approval model or show that testimonials influence former-user return decisions. Currency, support, security, and hiring are plausible criteria but need former-user decision interviews. |
| Existing professional Django developers seek current best practice, releases/upgrades, scaling help, greater expertise, and possible progression from user to contributor. | **Partially supported** | Returners explicitly seek current API practice, and former operators need releases, upgrades, and scaling evidence. No reviewed source supports contributor progression as a salient job for former users. |
| Companies depending on Django want maintenance continuity to avoid migration costs and may fund it; corporate approval can involve finance and leadership. | **Partially supported** | DramaFever and DoorDash directly show large migration cost, long coexistence, leadership coordination, and business/operational consequences. No reviewed evidence connects former-user migration experience to funding Django. |
| Claimed touchpoints include docs/release notes, forums/Discord, GitHub/issue tracker, mailing lists, conferences/sprints, podcasts, professional peer networks, and short-form social. | **Partially supported** | Documentation/release facts, source/issues, forums, long-form postmortems, and professional peers have clear evaluation/validation roles. Current-user survey evidence supports several channel types but not former-user incidence. Discord, mailing lists, sprints, and short-form social were not directly validated as material former-user decision channels. |

No other existing-analysis hypothesis was sufficiently specific to this lifecycle audience to audit without importing a different audience’s job.

## Evidence table

| Finding | Source (title, publisher/author, date, URL) | Evidence type | Direct evidence or inference | Confidence | Research notes |
|---|---|---|---|---|---|
| Leaving can reflect organization and architecture scale rather than rejection of Django; Django accelerated DoorDash’s MVP before monolith/team constraints grew. | [“Future-proofing: How DoorDash Transitioned from a Code Monolith to a Microservice Architecture,” DoorDash Engineering / Cesare Celozzi, December 2, 2020](https://careersatdoordash.com/blog/how-doordash-transitioned-from-a-monolith-to-microservices/) | First-party organizational migration account | Direct | High for the case; Low for generalization | Details triggers, governance, staged extraction, benefits of original Django architecture, and Kotlin/gRPC direction. Very large-company context. |
| A Django-to-service migration can be deliberately incremental because continuous feature delivery, data, templates, and business risk make a rewrite unsafe. | [“Moving to Go: A Pragmatic Guide,” Gopher Academy / Paddy Foran (DramaFever), January 27, 2014](https://blog.gopheracademy.com/moving-to-go/) | First-party engineering migration account | Direct | High for mechanism; Medium for persistence over time | Old but unusually specific about coexistence, data mirroring, templates, testing, ORM loss, deployment, and cost. |
| A platform can reduce Django because the content/contribution model changed while retaining Django for bounded account/search responsibilities. | [“MDN Web Docs evolves! Lowdown on the upcoming new platform,” Mozilla Hacks / Chris Mills, October 29, 2020](https://hacks.mozilla.org/2020/10/mdn-web-docs-evolves-lowdown-on-the-upcoming-new-platform/) | First-party platform-change account | Direct | High | Strong evidence against equating all Django retirement with framework dissatisfaction. Account describes planned state at publication time. |
| A personal project moved off Django when it no longer needed a database/back office; the new stack cut application code and infrastructure. | [“Using Starlette to migrate my blog across domains,” Florimond Manca, November 16, 2019](https://florimond.dev/en/posts/2019/11/starlette-migrate-blog-across-domains) | First-person technical postmortem with open-source code and LOC comparison | Direct | High for case; Low for broader prevalence | Clear project-fit change. LOC is author-measured and specific to one over-engineered blog. |
| New microservices may not need Django’s templates or ORM even when the original monolith did. | [“Moving from Django to Flask,” Ironbound Software / Nick, June 13, 2016](https://blog.ironboundsoftware.com/2016/06/13/moving-django-to-flask/) | First-person project account | Direct | Medium | Small, anonymous-context account; valuable qualitative signal about workload narrowing. |
| Framework dissatisfaction can center on persistence/model coupling, non-relational database fit, auth boundaries, and reduced value of built-in conveniences. | [“On (not) using Django in 2026,” Nate Meyvis, January 7, 2026](https://www.natemeyvis.com/on-not-using-django-in-2026/) | First-person reflective account | Direct | Medium for recurring concerns; Low for prevalence | Experienced-user perspective, explicitly personal and partly speculative about generative AI. |
| Frontend/platform consolidation can motivate departure because of duplicate rendering logic, toolchains, async ergonomics, and desire for shared components. | [“Why I Ditched Django for NextJS,” Bill Prin, November 19, 2022](https://medium.com/@waprin/why-i-ditched-django-for-nextjs-5ea7dc35779d) | Detailed first-person departure account | Direct | Medium | Strongly opinionated single account; acknowledges Django admin/productivity benefits and existing-stack inertia. |
| Familiarity and early-project momentum can trigger return when a replacement’s learning cost delays delivery. | [“Why I’ve gone back to Django for my new thing,” Dan Rowden, August 2, 2023](https://danrowden.com/blog/why-ive-gone-back-to-django-for-my-new-thing/) | First-person return account | Direct | Medium for mechanism; Low for prevalence | Concrete elapsed-time comparison but self-reported and one small project. |
| A return can occur when a developer realizes they are rebuilding Django-like capabilities and wants Django’s integrated complex-query/admin stack. | [“fast api or not,” Reddit r/django discussion, March 23, 2024](https://www.reddit.com/r/django/comments/1blpjp2/fast_api_or_not/) | Community discussion / individual anecdote | Direct anecdote | Low-to-Medium | Useful return trigger; isolated forum account and unverifiable project details. |
| Prescribed structure and batteries can become attractive again after a former user experiences assembly burden in a lighter framework. | [“Flask or Django or both?”, Reddit r/learnpython discussion, October 28, 2021](https://www.reddit.com/r/learnpython/comments/qha3hj/flask_or_django_or_both/) | Community discussion / individual anecdote | Direct anecdote | Low-to-Medium | Clear return narrative; not representative. |
| Returners need current ecosystem orientation rather than assuming old API practice still applies. | [“Back to Django after 4 years with FastAPI – what’s the standard for APIs today?”, Reddit r/django, September 26, 2025](https://www.reddit.com/r/django/comments/1nr32uj/back_to_django_after_4_years_with_fastapi_whats/) | Community question and discussion | Direct anecdote | Medium for information need; Low for prevalence | Directly names a four-year absence and compares current DRF/Django Ninja practice. |
| Python web developers often use multiple frameworks; aggregate usage does not identify abandonment direction. | [“Python Developers Survey 2024 Results,” Python Software Foundation and JetBrains, responses collected October–November 2024](https://lp.jetbrains.com/python-developers-survey-2024/) | Large ecosystem survey, 25,000+ filtered responses | Direct for reported usage; inference for coexistence implications | Medium | Official PSF channels, self-selected; Django 35%, FastAPI 38%, Flask 34%, and cross-usage. Not a migration cohort. |
| Current Django users frequently also use other frameworks, and value models/admin/migrations/auth; these are potential return pulls, not conversion evidence. | [“Django Developers Survey 2025 Results,” DSF and JetBrains, fielded November 2024–January 2025](https://lp.jetbrains.com/django-developer-survey-2025/) | Django-community survey, about 4,600 responses | Direct for respondents; inference for former-user pulls | Medium for current users; Low for former users | Recruited through Django channels and weighted; strong self-selection. 28% also used FastAPI, 23% Flask. |
| Broad developer continuation intent for Django is mixed and cannot be treated as a former-user return rate. | [“Technology,” Stack Overflow Developer Survey 2025](https://survey.stackoverflow.co/2025/technology/) | Large cross-technology survey | Direct for survey measure; inference for limitation | Medium | “Admired” asks prior-year users whether they want to continue. Self-selected, not Django-specific, and not longitudinal. |

## Unanswered research questions

1. What proportion of former users left because of project/context change, employer change, architecture scale, ecosystem limitations, or dissatisfaction with Django core?
2. At what unit does departure occur: person, new-project default, subsystem, application, organization, language, or architecture?
3. Which remembered objections are most often outdated, and which remain legitimate on current supported Django releases?
4. How long after leaving does prior Django fluency materially reduce return time, and when does stale knowledge become a liability?
5. What concrete events cause reconsideration: new CRUD-heavy product, replacement complexity, staffing change, package improvement, async evolution, or inherited code?
6. Which return triggers lead to actual adoption versus a short proof followed by another rejection?
7. What capabilities do former users miss most after leaving, and what replacement capabilities would they be least willing to give up?
8. How do outcomes differ between full return, bounded Django service, Django retained for admin/ORM, and continued non-use?
9. What are the true costs and durations of migrations away from and back to Django, including dual-running, data migration, feature delay, incidents, and retraining?
10. Who initiates and who can veto reassessment in small teams, agencies, and large organizations?
11. How much do career perception, community identity, sunk-cost defense, or embarrassment affect decisions compared with measurable project fit?
12. Which channels actually change former users’ decisions, rather than merely creating awareness?
13. Are returners more persuaded by current documentation, comparable postmortems, a practitioner conversation, or their own representative prototype?
14. What evidence would convince a satisfied non-returner that Django now fits a particular new project—and what would confirm that it still does not?

<!-- RESEARCH PROVENANCE: BEGIN -->
## Research provenance

This section was generated from the recorded Codex session JSONL logs. File attribution uses successful patch events; searches and domains use nested web-tool calls.

### Session `019f7560-b92e-7202-8ba1-f499786fd8d6`
- Log: `rollout-2026-07-18T15-18-21-019f7560-b92e-7202-8ba1-f499786fd8d6.jsonl`
- This document: `add, update`
- Search queries:
  - `"Why I don't use Django" developer`
  - `"Why I stopped using Django"`
  - `"back to Django" after FastAPI`
  - `"coming back to Django" web framework`
  - `"migrate away from Django" Python`
  - `"moved away from Django" developer blog`
  - `"replaced Django" engineering blog`
  - `"returned to Django" framework`
  - `"went back to Django" Flask`
  - `"why we left Django"`
  - `Django migration firsthand account admin ORM return to Django`
  - `DoorDash Django Kotlin migration 2020 developer frustration`
  - `Gopher Academy "Moving to Go: A Pragmatic Guide" DramaFever date`
  - `JetBrains State of Django 2024 survey other frameworks FastAPI Flask`
  - `Mozilla MDN retiring Django Kuma migration Yari blog 2020`
  - `Python Developers Survey 2024 web frameworks Django FastAPI Flask JetBrains`
  - `Stack Overflow Developer Survey 2025 Django admired desired web frameworks`
  - `company engineering blog migrate Django to Flask`
  - `company engineering blog migrate Django to Go`
  - `engineering "Django" "migration" "FastAPI"`
  - `engineering migration off Django monolith "Django" company`
  - `former Django developer why switched`
  - `postmortem retired Django application architecture`
  - `site:engineering.* "migrating from Django" framework`
  - `site:engineering.* Django monolith migration services`
- Website domains:
  - `abellogin.github.io`
  - `app.readthedocs.org`
  - `arxiv.org`
  - `ashokit.in`
  - `blog.djangogirls.org`
  - `blog.djangowebstudio.com`
  - `blog.gopheracademy.com`
  - `blog.ironboundsoftware.com`
  - `blog.jetbrains.com`
  - `blog.khanacademy.org`
  - `blog.mikihands.com`
  - `blog.mozilla.org`
  - `blog.quastor.org`
  - `builtwithdjango.com`
  - `careersatdoordash.com`
  - `code.djangoproject.com`
  - `cognonative.com`
  - `cosmiclearn.com`
  - `cyces.co`
  - `damianhodgkiss.com`
  - `danrowden.com`
  - `dev.to`
  - `developer.mozilla.org`
  - `developers.googleblog.com`
  - `developersvoice.com`
  - `dimkoug.com`
  - `diposit.ub.edu`
  - `django-authtools.readthedocs.io`
  - `django-cms.org`
  - `django-fluent-contents.readthedocs.io`
  - `django-improved-user.readthedocs.io`
  - `django-orm-cookbook-ko.readthedocs.io`
  - `django-rest-framework.org`
  - `django-reversion.readthedocs.io`
  - `djangocms-blog.readthedocs.io`
  - `djangoproject.com`
  - `docs.djangoproject.com`
  - `docs.python.org`
  - `doordash.engineering`
  - `doordash4.rssing.com`
  - `efe.me`
  - `en.wikipedia.org`
  - `engineering.kraken.tech`
  - `fastapi.tiangolo.com`
  - `firebasestorage.googleapis.com`
  - `florimond.dev`
  - `foxleytalent.com`
  - `fruty.io`
  - `github.com`
  - `go.dev`
  - `gritframework.dev`
  - `hacks.mozilla.org`
  - `holovaty.com`
  - `iangabaraev.com`
  - `ictinstitute.nl`
  - `ijsrem.com`
  - `infoq.cn`
  - `infoworld.com`
  - `instagram-engineering.com`
  - `jetbrains.com`
  - `journals.nipes.org`
  - `justdjango.com`
  - `jyx.jyu.fi`
  - `kth.diva-portal.org`
  - `linkedin.com`
  - `lp.jetbrains.com`
  - `marc-butler.com`
  - `medium.com`
  - `merebtechnology.com`
  - `mgsoftware.nl`
  - `monolithic.dev`
  - `mozilla-django-oidc.readthedocs.io`
  - `natemeyvis.com`
  - `news.pixelbreeders.com`
  - `news.ycombinator.com`
  - `petarmaric.com`
  - `ph.pollub.pl`
  - `puput.readthedocs.io`
  - `pyvideo.org`
  - `redcrowdigital.com.au`
  - `reddit.com`
  - `resources.jetbrains.com`
  - `rippling.com`
  - `roman.pt`
  - `ru.wikipedia.org`
  - `sagarxjadhav.github.io`
  - `simonwillison.net`
  - `sitescdn.wearevennture.co.uk`
  - `skillzpage.com`
  - `stackoverflow.blog`
  - `stackoverflow.co`
  - `stackoverflow.com`
  - `statista.com`
  - `survey.stackoverflow.co`
  - `talentstack.online`
  - `talha-sarwar.com`
  - `tech-insider.org`
  - `test-driven-django-development.readthedocs.io`
  - `thescriptsavant.com`
  - `theseus.fi`
  - `to-go.dev`
  - `training.talkpython.fm`
  - `untangled.dev`
  - `upstaff.com`
  - `uvik.net`
  - `voxire.com`
  - `vskills.in`
  - `vtechworks.lib.vt.edu`
  - `web.fe.up.pt`
  - `webucator.com`

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
