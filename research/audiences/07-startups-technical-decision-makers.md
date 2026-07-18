# Technical decision-makers in software start-ups and scale-ups

## Audience definition and boundaries

This is a **decision context occupied by people**, not a single persona and not an organization that can think or act. It comprises the people who initiate, evaluate, approve, implement, review, or bear consequences from a backend-framework decision while a young software-intensive company is searching for, validating, or scaling a business model. Depending on stage, those people may be a technical co-founder, founder-CTO, first engineer, non-technical CEO working through an adviser or contractor, lead engineer, Head/VP of Engineering, security or platform specialist, product leader, investor adviser, enterprise customer reviewer, or board member.

The distinctive context is uncertainty plus constrained people, time, and cash. A 2021 survey of 140 developers in Brazilian start-ups found initial/validation-stage practices and tools selected ad hoc and from team prior knowledge; growth-stage respondents recognized that earlier choices could have better supported scaling ([Souza, Cico & Machado](https://arxiv.org/abs/2108.00343), 1 August 2021). A study of 86 start-up cases describes scarce resources, shortcuts, and technical debt, especially in testing ([Klotins et al.](https://oulurepo.oulu.fi/handle/10024/25796), 27 May 2018). These are **direct findings; Medium confidence** across software start-ups because both samples are geographically/contextually limited and neither concerns framework selection specifically.

Boundaries matter. A profitable small business is not necessarily still operating under start-up uncertainty; a funded company may retain the label after leaving that context. “Early-stage,” “growth,” and “scale-up” are operating contexts, not funding-round definitions. Pure implementers belong primarily to developer audiences; mature-company leaders belong to the leadership audience.

## Important subsegments

- **Idea/prototype: technical co-founder, fractional CTO, adviser, or contractor.** One person may assess feasibility, constrain the first experiment, choose build-versus-buy, code, deploy, and explain risk to a non-technical co-founder. No framework choice may be necessary if a no-code prototype or manual service tests the riskiest assumption better.
- **Pre-product-market-fit: hands-on founder-CTO and first engineers.** Their technical choice is subordinate to learning from users and runway. A practitioner stage account assigns the CTO feasibility and effort at idea stage, the minimum customer-testable feature set, stack/cloud choice, architecture, coding, and investor explanation at MVP stage ([Antler/Chris Brooke](https://www.antler.co/blog/how-cto-role-evolves-as-startup-grows), 5 September 2019). **Direct qualitative account; Medium-Low confidence for prevalence.**
- **Post-validation/growth: founder-CTO, lead engineer, Head or VP Engineering.** Stabilization, deployability, maintainability, hiring, code quality, and scaling become more salient; investigation may move to senior engineers while approval moves toward an engineering leader and CEO/budget owner.
- **Scale-up/multi-team: CTO/VP Engineering, staff engineers, platform/SRE/security, and service owners.** Team topology, operational isolation, upgrade policy, standards, and exceptional workloads matter. This is no longer a single-founder decision.
- **Regulated, enterprise-selling, or high-consequence start-up at any stage.** Customer security reviews, privacy, data residency, audit evidence, availability commitments, and software-supply-chain controls can be early showstoppers. Customer and legal/security reviewers gain decision power before internal headcount suggests they would.
- **Non-technical founding team outsourcing development.** A CEO may approve spend but need an agency, contractor, adviser, prospective hire, or investor technologist to evaluate. Incentives and IP/knowledge-transfer risks differ from a founder-engineer’s.
- **Incumbent Django team after a pivot, funding round, incident, or leadership change.** The job is usually to decide what to retain, repair, isolate, or incrementally evolve—not to rerun a greenfield popularity contest.

These segments should not be ranked. Public Django survey data shows relevant people exist—13% of respondents selected CTO/CIO/CEO, 20% worked in 2–10-person companies, and 21% in 11–50-person companies—but roles were multi-select, stages were not asked, and recruitment was through official Django channels ([Django Developers Survey 2025](https://lp.jetbrains.com/django-developer-survey-2025/), fielded November 2024–January 2025). **Direct respondent evidence; Low confidence about the wider start-up market.**

## Primary job to be done

> When we need to turn an uncertain product hypothesis into a dependable customer outcome with limited runway, I want to choose the smallest technical foundation that the people available can ship, learn from, and responsibly operate, so I can increase validated learning without creating risks that prevent the next stage.

This is a **researcher inference; High confidence in the functional job, Medium confidence in its wording**. The studies connect engineering decisions to customer learning, scarce resources, prior knowledge, and scaling consequences. Choosing Django, or even writing software, is not assumed to be the correct next action.

## Additional jobs to be done

There are six important jobs in total, including the primary job.

1. **Create a reliable learning loop (primary).** When a product assumption needs testing, I want the smallest production-capable path from idea to observed user behaviour, so I can learn before runway or attention is consumed.
2. **Make a reversible, stage-fit commitment.** When a technical foundation is unavoidable, I want to distinguish near-term showstoppers from speculative future needs and preserve reasonable exit options, so I can avoid both paralysis and premature architecture under uncertainty.
3. **Keep scarce engineering attention on differentiated value.** When common web capabilities and operations compete with product work, I want useful conventions and integrated capabilities, so I can keep the team’s attention on differentiated value rather than undifferentiated plumbing. **Inference; Medium-High confidence.**
4. **Earn trust from the next stakeholder.** When a co-founder, first hire, customer, investor, or diligence reviewer examines the product, I want inspectable evidence of feasibility, security, ownership, reliability, and known trade-offs, so I can help the company sell, hire, fundraise, or contract without unsupported claims. **Direct context, inferred job; Medium confidence.**
5. **Grow delivery capacity without losing control of the system.** When hires and teams are added, I want newcomers to understand, test, deploy, and own changes safely, so I can turn added headcount into useful throughput rather than magnified coordination and debt.
6. **Adapt the product and architecture as evidence changes.** When customer needs, workload, regulation, or team structure changes, I want to evolve boundaries and replace exceptional components incrementally, so I can support a pivot or growth phase without a business-threatening rewrite.

## Functional, emotional, and social dimensions

| Job | Core functional job | Emotional job | Social job | Supporting jobs |
|---|---|---|---|---|
| Create a learning loop | Deliver a testable customer outcome and capture evidence | Reduce fear of spending runway without learning (**hypothesis**) | Demonstrate focus to co-founders/investors (**hypothesis**) | Identify riskiest assumption; scope vertical slice; instrument behaviour; review evidence |
| Make a stage-fit commitment | Test requirements, constraints, options, and reversibility | Feel able to commit despite uncertainty (**hypothesis**) | Be seen as pragmatic rather than fashionable or reckless (**hypothesis**) | Record assumptions; prototype; set gates; define revisit triggers and exit path |
| Protect scarce attention | Reduce integration, decision, deployment, and maintenance work | Avoid overwhelm from owning too many systems (**hypothesis**) | Signal disciplined use of capital (**inference**) | Prefer defaults; automate; buy commodities where appropriate; count lifecycle work |
| Earn stakeholder trust | Produce evidence proportionate to customer/funding risk | Reduce fear of a diligence surprise (**hypothesis**) | Maintain credibility as a competent steward (**inference**) | Architecture note; dependency/IP inventory; security review; recovery and load evidence |
| Grow capacity | Make knowledge, conventions, tests, and ownership transferable | Reduce founder key-person anxiety (**hypothesis**) | Attract and retain credible technical peers (**hypothesis**) | Document; onboard; delegate; clarify domains; measure delivery and reliability |
| Adapt safely | Change boundaries/components without interrupting the business | Avoid feeling trapped by the MVP (**hypothesis**) | Avoid a visible rewrite narrative (**hypothesis**) | Observe bottlenecks; isolate domains; upgrade; migrate incrementally |

Functional dimensions are **Medium-to-High confidence**. Emotional and social statements are **Low confidence hypotheses** pending interviews with founders, first engineers, and framework rejecters.

## Triggering situations

**Event-triggered**

- A founder must test technical feasibility or turn a validated problem into an MVP.
- A first paying customer requires authentication, administration, integrations, auditability, privacy, or availability beyond a prototype.
- A pivot changes the domain model, workflow, interface, or economics.
- Funding permits hiring, or a first/next technical hire challenges founder-made choices.
- Product-market fit or traffic growth exposes slow delivery, database/load constraints, brittle tests, poor deployment, or on-call pain.
- An incident, vulnerability, unsupported dependency, failed upgrade, or key-person departure makes latent risk visible.
- Enterprise procurement, regulated customers, an investment round, or acquisition starts technical/security/IP diligence.
- A new CTO/VP Engineering, platform lead, or board adviser reopens architecture and standards.

**Recurring**

- Trading product experiments against testing, security, reliability, upgrades, and debt reduction.
- Reassessing assumptions as user evidence changes.
- Hiring, onboarding, reviewing ownership, and reducing dependence on founders or contractors.
- Watching cloud cost, delivery lead time, incidents, support demand, version/package status, and customer commitments.
- Explaining technical trade-offs to non-technical founders, investors, customers, and staff.

This distinction is **inference; High confidence**. Thresholds and frequency require direct research.

## Desired outcomes

- Reduce elapsed time and engineering effort from a product question to trustworthy user evidence.
- Increase the proportion of early work that is reversible, instrumented, and connected to a stated assumption.
- Reduce time from a new engineer starting to making and deploying a safe change.
- Keep deployment, rollback, backup/restore, patching, and incident response feasible for the actual team—not an imagined future platform group.
- Reduce duplicated infrastructure and glue while keeping exceptional workloads separable.
- Keep critical test, security, upgrade, and architecture debt visible and within consciously accepted limits.
- Meet customer-specific latency, availability, privacy, compliance, and cost constraints under representative conditions.
- Reduce founder/contractor key-person dependence and increase shared ownership.
- Preserve the ability to pivot the domain and incrementally change components without stopping product learning.
- Produce proportionate, inspectable technical evidence quickly for customers, hires, investors, and reviewers.

These are **directionally measurable inferred outcomes; Medium-to-High confidence**. No evidence supports universal target numbers; stage, runway, consequence severity, and business model determine acceptable thresholds.

## Current behaviour or status quo

Early teams commonly begin from the technical founder’s or contractor’s known language, framework, hosting, and tools. The Brazilian survey directly found prior knowledge and ad hoc selection in initial/validation phases, plus preference for tools that integrate and automate operations. The 88-report study found requirements engineering and software design and quality most discussed, and concluded many engineering challenges stemmed from requirements inadequacies ([Klotins, Unterkalmsteiner & Gorschek](https://arxiv.org/abs/2311.12139), 20 November 2023). This means a framework evaluation can be misframed when the real uncertainty is the customer problem or requirements.

Direct Django experience shows a plausible stage-fit path, not a universal template. DoorDash reports that a small team chose a single Django application to build an MVP quickly, iterate changing business logic, reuse patterns, and contain pipeline/cloud-component overhead. With business and engineering growth, coupling, slow/brittle tests, onboarding, reliability, database constraints, and an aging Python/Django stack contributed to a multi-year rearchitecture ([DoorDash Engineering](https://careersatdoordash.com/blog/how-doordash-transitioned-from-a-monolith-to-microservices/), 2 December 2020). **Direct retrospective case; Medium confidence as an existence proof, Low confidence for typical thresholds or causality.**

## Pushes

- Runway and opportunity cost make long integration projects and speculative infrastructure unattractive.
- Repeated implementation of accounts, permissions, forms, data administration, migrations, APIs, and internal workflows consumes capacity that could test the product.
- A fragile prototype, manual deployment, poor tests, security gaps, or contractor-only knowledge prevents confident customer delivery.
- Growth increases the cost of coupling, slow feedback, unclear ownership, and inconsistent patterns. The 86-case study found larger teams faced more difficulty controlling debt and warned that adding people can amplify resource, communication, and practice problems.
- Enterprise customers or investors require evidence the team did not previously maintain.
- End-of-life versions, incidents, cloud cost, or scaling bottlenecks turn deferred maintenance into urgent work.

## Pulls

- A coherent, integrated foundation can reduce the number of early architectural and integration decisions. DoorDash’s early case directly reports one codebase/language, shared infrastructure, one pipeline, and lower operational complexity.
- Python familiarity and access to libraries can fit teams already using Python for data, automation, or product work. This is contextual, not proof of an easier labor market.
- Built-in conventions can make the first system more legible to later hires, provided the team follows and documents them. **Inference; Medium confidence.**
- Open source provides inspectable code, no framework license fee, and the possibility of incremental adaptation; it does not supply a support SLA or eliminate lifecycle cost.
- A public release, deprecation, and security process makes maintenance planning possible. Django documents time-based releases, backwards-compatible patch releases, and extended support for LTS releases ([Django release process](https://docs.djangoproject.com/en/6.0/internals/release-process/), current 6.0 documentation, accessed 18 July 2026). **Direct project fact; High confidence.**
- Credible production histories can answer “is this trajectory possible?” DoorDash validates early leverage and later evolution cost simultaneously; it cannot guarantee fit.

## Anxieties

- **Runway:** spending too long selecting or building before learning whether users care. **Hypothesis; Medium confidence.**
- **Premature commitment:** choosing for imagined hyperscale, or choosing a shortcut that blocks the next customer, hire, or round.
- **Personal familiarity bias:** whether the founder chose what they know rather than what the product and future team need; prior-knowledge selection is directly evidenced.
- **Founder/contractor key-person risk:** whether anyone else can debug, deploy, secure, or evolve the product.
- **Diligence and credibility:** hidden security, licensing/IP, dependency, testing, architecture, or documentation issues surfacing before a customer or financing event.
- **Hiring and onboarding:** whether people with relevant Django/Python and production judgment are available at the salary, location, and stage required. Public evidence does not establish supply.
- **Scaling:** whether framework, database, architecture, and team topology can meet a specific growth path at acceptable people/cloud cost.
- **Being labelled outdated or unserious:** concern that a mature framework or monolith will be judged aesthetically rather than against constraints. **Low-confidence hypothesis.**

## Habits and inertia

- Founder and first-engineer expertise strongly favors familiar stacks because it reduces immediate learning/debugging time.
- Existing prototypes, domain models, data, integrations, tests, CI/CD, and cloud configuration accumulate switching cost before a formal decision occurs.
- Contractor or agency templates can become the default even when the internal team did not choose or fully understand them.
- Once customers depend on behavior and data, incremental repair often dominates replacement even if the original decision was informal.

Application to framework choice is **inference; High confidence**, supported by direct evidence of prior-knowledge selection and later-stage debt. Relative strength is unmeasured.

## Decision criteria

No start-up-specific study supports a universal ranking. Criteria are therefore marked by likely stage importance and confidence, not scored.

| Criterion | Stage-sensitive importance | Confidence |
|---|---|---|
| Fit to the riskiest product assumption and core workflow | Potential showstopper at every stage; avoid solving the wrong problem efficiently | High |
| Time to a trustworthy production learning loop | Very high pre-PMF; remains important after validation | High |
| Team fit and prior knowledge | Very high when one or two people must ship and operate; reassess when hiring | High |
| Security, privacy, data ownership, reliability, and recovery | Potential showstopper for high-consequence/enterprise/regulated products; minimum responsibility always applies | High |
| Operational simplicity for the actual team | High early; includes deploy, observe, patch, restore, and support—not only code generation | High |
| Adaptability and boundary quality | High where pivots are likely; modularity does not require premature distributed systems | Medium-High |
| Testing and change safety | Increasingly high with customers, hires, and revenue; start-up debt evidence is direct | High |
| Ecosystem/lifecycle health | High for a product expected to outlive its first team; inspect critical packages separately | High |
| Hiring, onboarding, and knowledge transfer | Becomes high as the team grows; location and compensation are decisive contexts | Medium-High |
| Representative performance and cloud cost | A workload-specific gate, not a framework reputation contest | High |
| Customer/investor diligence fit | High when selling to enterprises, fundraising, or acquiring; low for an idea test | Medium |
| Exit/switching cost | Important but should be proportionate to evidence and stage | Medium-High |

For broad developer work projects, Stack Overflow’s 2025 respondents ranked robust/complete API first, reputation for quality second, easy-to-use API third, reliability/low latency fourth, and manageable cost fifth ([2025 Developer Survey, Work](https://survey.stackoverflow.co/2025/work)). This is the only cited ordering and is **direct broad-developer evidence; Low-to-Medium confidence for start-up framework approval** because it is neither stage- nor role-specific.

## Main concerns

**Practical concerns:** time to deploy a real vertical slice; authentication and permissions; product/admin workflows; API/client fit; integration; data migrations; async/background work; observability; recovery; cloud cost; testing; upgrades; package compatibility; hiring and documentation.

**Legitimate limitations:** Django does not supply product discovery, deployment architecture, SRE, dependency governance, customer compliance, or a vendor SLA. A batteries-included framework can reduce integration work but does not make a coupled domain model modular. Workloads dominated by CPU-intensive processing, extreme concurrency/latency, realtime interaction, or non-relational data require representative testing and may merit separate components. DoorDash explicitly moved a CPU-intensive logistics service out of Python early; this supports workload separation, not a claim that Django broadly fails at scale.

**Organizational objections:** a non-technical CEO may not trust a founder-only choice; a first senior hire may inherit undocumented assumptions; customer security/legal teams may block deployment; investors may question IP ownership or key-person risk; engineers may resist a standard that ignores their experience.

**Emotional resistance hypotheses:** shame about prototype debt, attachment to founder-written code, fear that admitting limits weakens investor confidence, and status pressure toward fashionable architectures. **Low confidence.**

## Objections and perceived risks

- **“Django is too heavyweight for an experiment.”** Sometimes legitimate if the riskiest assumption needs no custom backend. Otherwise “heavyweight” requires task evidence: integrated capabilities may reduce total decisions and glue.
- **“Django is old, so investors or hires will reject it.”** Requires further research. Age is not fit; current release/security policy demonstrates active maintenance, while local labor-market and package evidence must be checked.
- **“Django lets a tiny team ship, so architecture can wait until scale.”** Partially supported but dangerously absolute. DoorDash shows early leverage; the start-up debt study shows testing debt and team growth can compound. Minimal boundaries, tests, ownership, and upgrade discipline may be cheaper early.
- **“We must design for millions of users before launch.”** Unsupported as a general rule. Representative next-stage constraints matter; speculative distributed architecture can slow learning and add operating burden.
- **“Django cannot scale.”** Contradicted as a universal claim by DoorDash’s production history. The legitimate question is whether a particular architecture/team can meet a defined workload and organizational scale economically.
- **“A monolith inevitably becomes a rewrite.”** Unsupported. DoorDash is one coordinated migration case, not destiny; lack of domain isolation and accumulated constraints were material. Public negative and no-rewrite cases are sparse.
- **“Open source means free and supported.”** Unsupported. License cost is one component; the team still owns operations, upgrades, dependencies, and support unless it contracts separately.
- **“Python popularity guarantees easy hiring.”** Requires further research by geography, compensation, seniority, domain, and on-call needs.

## Information needed to make progress

Before evaluation: the product assumption being tested; why custom software is needed; user and consequence profile; core data/workflows; actual team skill; runway/timebox; regulatory/customer constraints; expected next-stage workload; build-versus-buy boundaries; and who can veto or bear failure.

During evaluation: a deployed vertical slice; setup-to-change and change-to-production effort; authentication/permission/admin/API fit; representative latency/load/cost where material; deployment, logs, rollback and restore; dependency/license inventory; supported-version path; critical package health; test strategy; security responsibility boundaries; and an explicit list of adaptations or missing capabilities.

For growth or an incumbent system: current bottlenecks and incident data; onboarding time; test/build/deploy feedback; version/upgrade lag; coupling and ownership map; cloud/support cost; key-person concentration; customer commitments; and incremental isolation/migration options.

For a non-technical founder: independent technical review, IP assignment and repository control, deploy/recovery documentation, scope/change terms, knowledge-transfer plan, and evidence that the evaluator’s incentives are disclosed.

## Trusted content formats

- A **time-boxed, production-shaped vertical slice** against stated success/failure criteria validates learning speed and operational fit.
- **Primary documentation and policy** for releases, security, supported versions, deployment, and APIs answers current factual questions.
- A **short architecture/decision record** stating stage, assumptions, workload, alternatives, owner, risks, and revisit triggers supports co-founder, hire, customer, and investor review.
- **Detailed founder/engineering retrospectives** that expose team size, stage, workload, benefits, adaptations, failures, and costs are useful existence proofs. DoorDash’s account is strong because it documents both early benefit and later pain.
- **Peer review and pair evaluation** by the people who will implement and operate the system reduces founder or agency blind spots.
- **Upgrade, restore, security, and representative load exercises** validate claims where consequences justify the work.
- **Inspectable repositories, issue/release histories, package metadata, and dependency inventories** support lifecycle and diligence checks.

Format trust is **inferred; Medium-to-High confidence**. No reviewed evidence ranks formats for this exact audience.

## Discovery, evaluation, validation, and engagement channels

**Discovery:** prior experience, co-founders, first engineers, advisers, agencies, investor/accelerator networks, peers, search, GitHub, engineering accounts, and developer communities surface options. Prior knowledge is directly evidenced as an early-stage driver. Short-form social, podcasts, or famous-company mentions may create awareness, but no evidence shows they decide adoption.

**Evaluation:** official docs, package/source/release history, issue trackers, Stack Overflow, Django Forum, GitHub discussions, engineering blogs, and internal prototypes answer capability, lifecycle, and implementation questions. Future hires/operators and product/security peers help uncover consequence-bearing requirements.

**Validation:** a deployed user-facing slice, customer feedback, load/cost tests, threat/security review, restore/upgrade exercises, and references with comparable stage/workload convert awareness into evidence. Enterprise customers, investor technologists, or external advisers may validate later-stage risk.

**Ongoing engagement:** release notes and security advisories support maintenance; Forum/Stack Overflow/peer groups support problem solving; GitHub and the issue tracker support source-level investigation; conferences/sprints deepen expertise and contribution. Among current engaged Django respondents, 60% used djangoproject.com to follow development, 22% YouTube, 18% each Stack Overflow and Reddit, 15% Django Forum, and 12% the newsletter; 18% did not follow development. These are **direct current-user figures with Medium-Low confidence for start-up decision-makers** because role/stage cross-tabs are absent.

## Decision-makers and influencers

| Context | Initiator | Researcher/evaluator | Influencers | Approver/economic buyer | Blockers/reviewers | Users and consequence bearers |
|---|---|---|---|---|---|---|
| Idea/prototype | Technical or non-technical founder, customer problem | Technical co-founder, adviser, contractor, or founder using a template | Co-founder, prospective users, accelerator/peer | Founders; spend may be implicit | No-code/manual alternative, feasibility, runway, unavailable skill | Founders and test users; founders bear wasted runway |
| Pre-PMF product | Founder-CTO, first engineer, product evidence | Founder-CTO and first engineers | CEO/product founder, users, design/data expertise | Founder-CTO jointly with CEO where cost/commitment matters | Customer requirements, runway, security/privacy, contractor incentives | Builder-operators, early users; company bears outages and lost learning |
| Growth/post-validation | Lead/staff engineer, founder-CTO, Head Engineering | Senior engineers and future service owners | Product, support, SRE/security, experienced hires, customers | Founder-CTO/VP Engineering; CEO/finance for material spend or rewrite | Customer contracts, security/legal, delivery capacity, incumbent data | Engineers/on-call, support, customers; leadership bears delivery and funding consequences |
| Scale-up/multi-team | Service owner, platform/architecture lead, incident or program | Cross-functional technical team | Engineering managers, product, data, SRE, internal Django experts | CTO/VP Engineering or delegated architecture owner; CEO/board for existential investment | Platform standards, security/compliance/legal, key customers | Multiple teams and downstream services; customers and business bear systemic risk |
| Outsourced build | Non-technical founder or product lead | Agency/contractor plus ideally independent reviewer | Prospective internal hire, adviser, investor technologist | CEO/founders control spend; technical approval may be delegated | IP ownership, repository/control, maintainability, vendor incentives | Founder, future maintainers, customers; founder bears lock-in and knowledge risk |

This map is **inference; High confidence at role-category level, Medium confidence for allocation**. Antler’s direct account supports the founder-CTO’s evolving role. It does not justify “the start-up decides,” nor the assumption that the CTO always approves alone.

## Appropriate next actions for Django to encourage

These are audience progress actions, not campaign or asset recommendations.

- **State the riskiest product assumption and whether a backend is needed** → supports the learning-loop job.
- **Time-box a production-shaped vertical slice with explicit gates** → supports stage-fit commitment and reduces abstract framework debate.
- **Record current-stage assumptions, adaptations, owners, and revisit triggers** → supports reversibility and future handover.
- **Test deploy, log, rollback, backup/restore, and patch responsibilities** → supports responsible operation, not merely demo completion.
- **Invite the next engineer/operator and relevant customer/security reviewer into evaluation** → supports trust and reveals consequence-bearing constraints.
- **Inventory critical dependencies, licenses, supported versions, and ownership** → supports diligence and lifecycle stewardship.
- **Measure onboarding/change feedback and isolate demonstrated bottlenecks incrementally** → supports growing capacity and adaptation.
- **Follow release/security information and budget recurring maintenance** → supports ongoing production responsibility.

## Overlaps with other audiences

- **CTOs and engineering managers:** the same titles appear, but start-up stage compresses roles and ties choices more tightly to runway and product uncertainty.
- **Technical leads/software architects:** growth-stage evaluators may be leads or staff engineers, especially when the founder delegates investigation.
- **Experienced backend/full-stack developers:** first engineers often research, prototype, implement, and operate; their personal developer job differs from the organizational decision job.
- **Python developers new to web:** a data/ML-oriented founder may value Python continuity but need web-production evidence.
- **Existing professional Django developers:** incumbent teams need upgrades, scaling, and best practice rather than a greenfield choice.
- **Companies depending on Django/funders:** a successful start-up may later fund maintenance to reduce dependency risk, but adoption and funding are separate jobs.

## Possible segmentation problems

“Start-ups” is too coarse and anthropomorphic. Stage, product risk, technicality of founders, team size, business model, customer assurance, funding model, and incumbent status change both the job and the decision system. “Technical decision-maker” also falsely implies one final chooser: the researcher, approver, veto holder, user, and consequence bearer may differ.

Funding round and headcount are weak proxies: a bootstrapped team can have mature revenue and enterprise controls, while a two-person fintech may face more review than a larger low-consequence product. Do not collapse non-technical founders, founder-CTOs, first engineers, and growth VPs into a fictional founder persona. Interviews should recruit by decision episode and stage, including Django rejecters and teams that chose not to build.

## Existing-analysis claim audit

| Existing-analysis claim | Audit | Evidence and qualification |
|---|---|---|
| A mid-to-large-company technical decision-maker approves framework standards based on currency, long-term reliance, community/support, security, hiring, and enterprise examples. | **Partially supported, mostly outside this lens** | These are relevant in scale-ups and enterprise-selling start-ups, but stage changes their weight and approval is distributed. “Marketing executive” is unsupported as a normal approver. Production cases are validation inputs, not transferable proof. |
| Existing professional Django developers seek current best practice, releases/upgrades, scaling help, greater expertise, and possible progression from user to contributor. | **Partially supported** | Release/upgrade/scaling needs are supported for incumbent start-up teams; expertise progression and contributor intent are not evidenced for this segment. |
| Companies depending on Django want maintenance continuity to avoid migration costs and may fund it; corporate approval can involve finance and leadership. | **Partially supported** | DoorDash demonstrates substantial migration/architecture cost and Django policy establishes lifecycle relevance. Start-up funding intent and finance involvement are not directly evidenced; early decisions often have no separate finance role. |
| Docs/release notes, forums/Discord, GitHub/issue tracker, mailing lists, conferences/sprints, podcasts, professional peers, and short-form social are touchpoints. | **Partially supported** | Official Django survey supports use of the site, Stack Overflow, Reddit, Forum, newsletter, GitHub-adjacent investigation and smaller podcast/Discord use among current users. Behavioral roles are inferred; no start-up-role cross-tabs establish decisiveness. Professional peers/prior knowledge have stronger discovery support. |

The donor, learner, and contributor-specific hypotheses are irrelevant to this decision context and are not audited here.

## Evidence table

| Finding | Source (title, publisher/author, date, URL) | Evidence type | Direct evidence or inference | Confidence | Research notes |
|---|---|---|---|---|---|
| Early/validation teams select practices/tools ad hoc and from prior knowledge; growth teams see earlier maturity gaps | [A Survey on Software Engineering Practices in Brazilian Startups, Souza, Cico & Machado, 1 Aug 2021](https://arxiv.org/abs/2108.00343) | Survey of 140 start-up developers | Direct | Medium | Single-country cohort; concerns practices/tools, not Django selection |
| Start-ups accumulate notable testing debt; team size/experience and adding people affect debt control | [Exploration of technical debt in start-ups, Klotins et al./ACM, 27 May 2018](https://oulurepo.oulu.fi/handle/10024/25796) | Case survey, 86 start-up cases | Direct | Medium-High | Strongly relevant to growth; older and not framework-specific |
| Requirements inadequacy connects engineering and business challenges | [Software engineering in start-up companies: analysis of 88 experience reports, Klotins et al., 20 Nov 2023](https://arxiv.org/abs/2311.12139) | Multivocal analysis of 88 reports | Direct | Medium | Experience reports can overrepresent salient problems |
| Founder-CTO work shifts from feasibility/MVP/stack/coding toward stability, hiring and management | [How the Role of a CTO Evolves as a Startup Grows, Chris Brooke/Antler, 5 Sep 2019](https://www.antler.co/blog/how-cto-role-evolves-as-startup-grows) | First-person practitioner stage account | Direct qualitative | Medium-Low | One experienced CTO/adviser; useful role map, not prevalence data |
| A small Django monolith supported DoorDash MVP speed and low operational complexity, then growth exposed coupling, tests, onboarding, reliability and data constraints | [How DoorDash transitioned from a code monolith to microservices, DoorDash Engineering, 2 Dec 2020](https://careersatdoordash.com/blog/how-doordash-transitioned-from-a-monolith-to-microservices/) | Direct adoption/migration retrospective | Direct | Medium | Rich single success case; retrospective and non-comparative |
| Broad developers value API completeness/usability, quality, reliability and manageable cost in work technology | [2025 Developer Survey: Work, Stack Overflow, 2025](https://survey.stackoverflow.co/2025/work) | Large self-selected developer survey | Direct; application inferred | Medium for developers, Low-Medium for start-up approvers | Only evidence-backed ordering used; not role/stage/framework-specific |
| Current Django users include leadership and small-company respondents; most teams are small | [Django Developers Survey 2025, DSF/JetBrains, fielded Nov 2024–Jan 2025](https://lp.jetbrains.com/django-developer-survey-2025/) | ~4,600-user self-selected survey | Direct | Medium for sample, Low for market incidence | Official-channel recruitment; no stage/role cross-tabs |
| Current Django followers use official site, YouTube, Stack Overflow, Reddit, Forum and newsletter in differing proportions | [Django Developers Survey 2025, DSF/JetBrains, fielded Nov 2024–Jan 2025](https://lp.jetbrains.com/django-developer-survey-2025/) | User channel survey | Direct usage; roles inferred | Medium-Low | Does not prove discovery or decision influence for start-up leaders |
| Time-based releases, patch compatibility and LTS support make lifecycle planning possible | [Django release process, Django documentation, accessed 18 Jul 2026](https://docs.djangoproject.com/en/6.0/internals/release-process/) | Primary project policy | Direct | High | Policy is not a support SLA or evidence of third-party package health |
| Product/user focus, delivery performance, stability and well-being can trade off; simplistic velocity claims are unsafe | [Accelerate State of DevOps Report 2024, DORA/Google Cloud, 2024](https://dora.dev/research/2024/dora-report/) | Multi-organization industry research | Direct general; start-up application inferred | Medium | Not start-up- or Django-specific; used only for measurement caution |

## Unanswered research questions

- What concrete decision episode led technical founders/first engineers to choose, reject, retain, or leave Django, and what alternative—including not building—won?
- At which stage and consequence level does a framework choice receive explicit CEO, investor, customer-security, or board review?
- Which Django capabilities measurably shorten a production learning loop for different start-up products, and which create unused complexity?
- What minimum tests, boundaries, documentation, and deployment practices best prevent early Django speed from becoming growth-stage debt?
- How do non-technical founders assess agency/contractor framework recommendations, incentives, IP ownership, and handover risk?
- What are actual Django hiring supply, compensation, onboarding time, and key-person risks by geography and start-up stage?
- Which workload or architecture constraints most often cause start-ups to isolate components, add services, or migrate, and at what observed cost?
- How do enterprise customer reviews treat Django/Python specifically, separate from the start-up’s overall security and operational maturity?
- Which discovery and validation channels actually changed a start-up framework decision rather than merely being used by existing Django users?
- What emotional or status concerns—maturity, fashion, founder identity, investor credibility—meaningfully affect decisions?
- How do bootstrapped, venture-funded, agency-built, regulated, and AI-native start-ups differ enough to require separate jobs research?
- What can be learned from failed, stalled, or quietly maintained Django start-ups, which are largely absent from public success retrospectives?

<!-- RESEARCH PROVENANCE: BEGIN -->
## Research provenance

This section was generated from the recorded Codex session JSONL logs. File attribution uses successful patch events; searches and domains use nested web-tool calls.

### Session `019f754b-c5b8-7691-9c36-954ea81e4ea1`
- Log: `rollout-2026-07-18T14-55-28-019f754b-c5b8-7691-9c36-954ea81e4ea1.jsonl`
- This document: `add, update`
- Search queries:
  - `2025 Stack Overflow survey technology choice robust complete API security privacy rejection`
  - `DORA 2024 report platform engineering developer productivity documentation`
  - `Django Developers Survey 2025 company size role startup`
  - `site:blog.sentry.io Django monolith startup architecture scaling engineering`
  - `site:careersatdoordash.com/blog Django monolith time to market microservices December 2020`
  - `site:engineering.instagram.com Django scaling architecture Instagram engineering`
  - `site:stackoverflow.co 2025 survey work technology choice security privacy rejection`
  - `site:survey.stackoverflow.co/2025 technology admired desired Python Django`
  - `site:survey.stackoverflow.co/2025 work technology endorsement security privacy rejection criteria`
  - `site:ycombinator.com startup technical founders launch quickly users advice`
  - `software engineering startups technical debt study 86 startups Klotins 2018`
  - `startup CTO role evolves technical founder product market fit interview`
  - `startup software engineering practices 88 experience reports Paternoster 2014`
  - `startup technical due diligence founders engineering primary research survey`
  - `venture capital technical due diligence startup software security architecture checklist`
- Website domains:
  - `administraciondesistemas.com`
  - `ai-infra-link.com`
  - `antler.co`
  - `arxiv.org`
  - `assets.ctfassets.net`
  - `axios.com`
  - `bairesdev.com`
  - `bear-images.sfo2.cdn.digitaloceanspaces.com`
  - `blackduck.com`
  - `careersatdoordash.com`
  - `celaeno.cloud`
  - `cincodias.elpais.com`
  - `cleveroad.com`
  - `cora.ucc.ie`
  - `corp.tied-inc.com`
  - `datadrivendaily.com`
  - `dextralabs.com`
  - `dipankar.org`
  - `djangoproject.com`
  - `doi.org`
  - `dora.dev`
  - `dx.doi.org`
  - `eliftech.com`
  - `en.wikipedia.org`
  - `firebasestorage.googleapis.com`
  - `fortiumpartners.com`
  - `foundersled.studio`
  - `gainhq.com`
  - `gartner.com`
  - `github.com`
  - `glencoyne.com`
  - `hapy.co`
  - `images.template.net`
  - `itpro.com`
  - `lp.jetbrains.com`
  - `meta.stackoverflow.com`
  - `oulurepo.oulu.fi`
  - `peruma.me`
  - `reddit.com`
  - `rightsstatements.org`
  - `roamingpigs.com`
  - `run.unl.pt`
  - `scispace.com`
  - `seedforge.com`
  - `semasoftware.com`
  - `sphereinc.com`
  - `stackoverflow.blog`
  - `stackoverflow.co`
  - `startupbuddy.net`
  - `startups.com`
  - `startupscience.io`
  - `storage.googleapis.com`
  - `survey.stackoverflow.co`
  - `teamusec.de`
  - `techcrunch.com`
  - `techradar.com`
  - `traceable.ai`
  - `trio.dev`
  - `trustshoring.com`
  - `urn.fi`
  - `zaitsevartem.com`

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
