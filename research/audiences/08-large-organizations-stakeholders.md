# Large-organization technology stakeholders

## Audience definition and boundaries

“Large organization” is not a persona. It is a decision context in which authority, expertise, budget, implementation, and consequences are distributed. The relevant audience is the set of people who must get a consequential web service adopted, governed, delivered, and sustained: initiators and business/service owners; researchers and evaluators; enterprise, solution, and security architects; delivery developers and operators; platform and open-source-program-office (OSPO) staff; privacy, legal, compliance, risk, procurement, and finance reviewers; accountable executives; and users or customers who bear failure.

The unit of decision is usually not a framework license purchase—Django is open source—but a service architecture and operating commitment that contains Django and third-party dependencies. Open-source components can still enter formal inventory, security review, standards approval, and supplier-risk processes. UK government guidance explicitly puts open-source products into third-party product review, while NIST says acquisition teams should combine program, technical, security, supply, and procurement expertise ([UK Government Security, updated December 31, 2025](https://www.security.gov.uk/policy-and-guidance/secure-by-design/activities/managing-third-party-product-security-risks/); [NIST SP 800-161r1, May 2022](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-161r1-upd1.pdf)). **Direct evidence; High confidence** for formal public-sector and regulated processes; **Medium confidence** for how consistently private enterprises apply them.

Included: greenfield adoption, an exception to a technology standard, expansion of an existing Django estate, a “stay/upgrade/contain/migrate” review, acquisition integration, and funding or contributing to Django because the organization depends on it. Excluded: a developer's personal framework choice, generic “enterprise buyers” shopping for a SaaS product, and senior leaders with no stake in the service. Technical leads, architects, executives, contributors, and funders overlap other audience reports; this report focuses on how their jobs interact inside a large organization.

## Important subsegments

- **Regulated and public-sector services:** formal business cases, risk owners, procurement schedules, audit evidence, privacy, accessibility, and sector controls create explicit gates.
- **Large technology/product companies:** strong internal platforms and staff expertise may enable team autonomy, but production scale, privacy, efficiency, and custom infrastructure raise the evidence bar.
- **Non-technology enterprises digitizing operations:** internal skills, vendor/consultancy dependence, integration with packaged and legacy systems, and supportability may matter more than frontier scale.
- **Existing Django estates:** continuity, patching, upgrades, shared tooling, and migration cost dominate; the decision differs from greenfield comparison.
- **Greenfield or exception-seeking teams:** must establish fit and often explain why an approved stack does not suffice.
- **Centralized versus federated governance:** a central architecture/security body may approve a reusable paved road, while federated organizations delegate decisions within guardrails.
- **Commercial software manufacturers serving the EU:** when in scope, the Cyber Resilience Act (CRA) adds lifecycle risk assessment, third-party-component due diligence, support-period, vulnerability-handling, documentation, and reporting obligations. This is not a requirement for every internal Django service ([European Commission CRA summary, updated 2026](https://digital-strategy.ec.europa.eu/en/policies/cra-summary)). **Direct evidence; High confidence on the law's stated scope, Medium confidence pending organization-specific legal analysis.**

## Primary job to be done

> **When** a consequential service needs a web application foundation or an existing foundation must be revisited, **I want to** assemble enough shared evidence and ownership for the organization to approve, deliver, secure, operate, and evolve the system, **so I can** meet the service need without creating unacceptable lifecycle, compliance, continuity, or switching risk.

Job hierarchy:

- **Core functional job:** turn a proposed or inherited technical choice into an organizationally operable and governable service decision.
- **Supporting jobs:** define requirements and risk appetite; map the estate and dependencies; prototype critical paths; document architecture and ownership; estimate total lifecycle cost; establish patch, upgrade, incident, support, and exit plans; secure required approvals.
- **Emotional job (hypothesis):** reduce fear of an avoidable incident, audit failure, stalled delivery, or costly reversal without pretending uncertainty is zero.
- **Social job (hypothesis):** build credible consensus across people with different incentives and demonstrate responsible stewardship to leadership, reviewers, delivery teams, customers, and regulators. The cross-functional job is directly evidenced; emotional and reputational dimensions were not directly measured for Django decisions. **Inference; Medium confidence for emotional, Low-to-Medium for social.**

## Additional jobs to be done

1. > **When** a team proposes Django or a Django-based architecture, **I want to** test the riskiest functional, integration, security, and operational assumptions in our environment, **so I can** replace popularity claims with decision evidence.
   - **Core functional:** prototype and measure the critical paths.
   - **Supporting:** representative data/load, identity, deployment, observability, failure/recovery, dependency inventory, and acceptance thresholds.
   - **Emotional (hypothesis):** feel able to defend the decision without overclaiming.
   - **Social:** give architecture, security, operations, and service owners a shared artifact. GOV.UK explicitly recommends prototypes for security, compliance, integration, and technical constraints. **Direct evidence; High confidence.**

2. > **When** many teams need a repeatable technology choice, **I want to** create a governed default and a proportionate exception path, **so I can** reduce duplicate review while preserving fit and accountable variation.
   - **Core functional:** establish reusable guardrails, supported versions, and ownership.
   - **Supporting:** reference architecture, approved components, decision record, review cadence, and exception criteria.
   - **Emotional (hypothesis):** avoid becoming either a bottleneck or an absentee governor.
   - **Social:** align central reviewers and delivery teams. NIST and UK guidance support proportional, contextual review and reuse of prior assessments. **Direct evidence for supporting work; Medium-to-High confidence for this synthesized job.**

3. > **When** the service depends on Django and its ecosystem, **I want to** keep versions, dependencies, skills, and response processes healthy, **so I can** avoid preventable exposure and emergency migration.
   - **Core functional:** manage adoption as a lifecycle, not a one-time approval.
   - **Supporting:** inventory/SBOM, advisories, patch ownership, upgrade rehearsals, maintainer and license review, training, succession, and incident playbooks.
   - **Emotional (hypothesis):** avoid surprise from an unsupported release or abandoned dependency.
   - **Social:** show due care to risk owners and service users. OpenSSF treats unmaintained dependencies as security risks and recommends checking activity, maintainer diversity, releases, LTS, security response, tests, license, and practical behavior ([OpenSSF, March 28, 2025](https://best.openssf.org/Concise-Guide-for-Evaluating-Open-Source-Software.html)). **Direct evidence; High confidence.**

4. > **When** an established Django estate no longer cleanly fits, **I want to** choose among upgrade, containment, decomposition, platform investment, or migration, **so I can** improve outcomes without paying unnecessary rewrite or continuity cost.
   - **Core functional:** identify the smallest safe change that meets the target state.
   - **Supporting:** estate map, coupling/data analysis, incident and delivery data, skills, incremental exit route, and migration rehearsal.
   - **Emotional (hypothesis):** resist both sunk-cost denial and rewrite enthusiasm.
   - **Social:** make consequences legible to product, finance, operators, and customers. **Inference from technology-evolution guidance and switching-cost logic; Medium confidence; Django-estate interviews are missing.**

5. > **When** Django becomes materially important to the organization, **I want to** decide whether employee contribution, upstream collaboration, or funding reduces our dependency risk or advances our goals, **so I can** support continuity rather than only consume value.
   - **Core functional:** connect contribution/funding to dependency stewardship and business goals.
   - **Supporting:** dependency criticality, internal contribution policy, legal approval, budget owner, expected outcome, and impact reporting.
   - **Emotional (hypothesis):** feel the organization is not passively relying on an under-resourced commons.
   - **Social:** demonstrate responsible open-source citizenship. A 2024 LF/GitHub/Harvard survey estimates organizations invest $7.7B annually in OSS, mainly labor, but notes that many respondents could not quantify hours or budget; this establishes real organizational funding and measurement difficulty, not Django-specific ROI ([2024 Open Source Software Funding Report](https://www.linuxfoundation.org/research/open-source-funding-2024)). **Direct evidence; Medium confidence due to survey/extrapolation limits.**

## Functional, emotional, and social dimensions

**Functional (evidenced):** satisfy user and business needs; integrate with the estate; meet security, privacy, availability, performance, accessibility, and regulatory requirements; enable delivery; control total cost; preserve data/control and reversibility; and sustain dependencies. Government technology guidance explicitly emphasizes user need, security risk, total ownership, existing systems, prototypes, and ability to change direction. **Direct evidence; High confidence.**

**Emotional (hypotheses):** confidence that material unknowns are visible; fear of blame for a breach or outage; frustration with slow gates; relief from a supported organizational default; anxiety about relying on volunteer-maintained infrastructure. These are plausible consequences of accountability but were not isolated in the reviewed evidence. **Inference; Low-to-Medium confidence.**

**Social (partly evidenced hypotheses):** architects and security reviewers need to be credible stewards; delivery teams need autonomy and fair review; executives need defensible risk acceptance; procurement and finance need comparable evidence; contributors need internal permission and recognition. Cross-functional responsibility is direct evidence; prestige, identity, and reputation effects remain hypotheses. **Mixed direct evidence and inference; Medium confidence.**

## Triggering situations

**Recurring triggers:** architecture and portfolio review; budget planning; security/advisory review; dependency and license scan; supported-version change; audit; capacity/cost review; workforce planning; incident exercises; and annual standards renewal.

**Event-triggered triggers:** new service or major feature; prototype moving to production; exception request; acquisition or supplier change; security incident or new vulnerability; end of support; inability to hire or retain expertise; traffic or data growth; platform/cloud migration; new regulation or customer assurance request; executive cost mandate; or a proposal to rewrite.

The incumbent can itself be a pull: Meta reused Instagram's Django backend, data models, business logic, security features, and server infrastructure to build Threads quickly, with infrastructure, foundation, production, and engineering teams carrying much of the scaling work ([Meta Engineering, September 7, 2023](https://engineering.fb.com/2023/09/07/culture/threads-inside-story-metas-newest-social-app/)). **Direct case evidence; High confidence about Meta, Low generalizability.**

## Desired outcomes

- Critical user journeys and non-functional requirements meet agreed thresholds under representative load and failure modes.
- Time from proposal to a clear approve/condition/reject decision decreases without bypassing material risk.
- Change lead time and deployment friction improve while change failure, unplanned rework, and recovery time do not worsen; these are established DORA measures, not Django benchmarks ([DORA metrics, updated January 2, 2026](https://dora.dev/insights/dora-metrics-history/)).
- Supported-version coverage, dependency freshness, patch latency, vulnerability ownership, and exception age are visible and trend in the intended direction.
- Total cost includes delivery, infrastructure, operations, assurance, upgrades, skills, support, and exit—not only a zero license price.
- Review evidence is reusable across teams, while exceptions remain traceable and time-bounded.
- No critical service depends on one internal expert; onboarding and succession time improve.
- Risk acceptance has a named owner, expiry/review trigger, and consequences for users and operators.

**Direct evidence supports these measurement categories; High confidence.** No evidence supports universal targets or a claim that Django alone causes them.

## Current behaviour or status quo

Organizations commonly begin with approved languages, platforms, identity, observability, data stores, supplier lists, and prior decisions. A delivery lead or architect develops a business/technical case; reviewers request architecture, dependency, security, data, license, and cost evidence; teams prototype uncertain areas; an architecture or risk owner approves, conditions, or rejects; operational teams then inherit patching and incident obligations. NIST describes due-diligence questionnaires, supplier profiles, risk-tailored requirements, and continuing contract/performance monitoring. **Direct evidence for formal acquisition; High confidence.** How often an unpurchased framework itself goes through each procurement step is unmeasured.

Open source often arrives transitively through applications rather than through a central purchase. A 2024 HBS working paper uses usage data from millions of firms and estimates firms would spend 3.5 times more on software absent widely used OSS, demonstrating material organizational dependence but not the value of Django specifically ([Hoffmann, Nagle, and Zhou, January 2024](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4693148)). **Direct empirical estimate; Medium confidence given model/data assumptions.**

## Pushes

- Delivery delay from fragmented foundations, excessive handoffs, or an incumbent stack that no longer fits.
- Recurring incidents, security findings, unsupported versions, stale dependencies, or unclear ownership.
- Cost pressure across licenses, cloud resources, consultancy, duplication, assurance, and migration.
- Integration friction with identity, data, cloud/platform, observability, API, or frontend standards.
- Audit, customer, insurer, or regulator requirements that the current process cannot evidence.
- Hiring/onboarding difficulty, consultant dependence, or key-person risk.
- A need to preserve data/control, reduce supplier lock-in, or standardize reusable components.

The 2024 OpenLogic/OSI/Eclipse survey found security/compliance and keeping current with patches persistent challenges (79% and 70% of responding organizations respectively). It is a self-selected, vendor-linked OSS survey and does not isolate Django or large firms, so it supports the existence—not the ranking—of these pressures ([February 1, 2024](https://www.perforce.com/press-releases/openlogic-perforce-release-2024-state-of-open-source-report)). **Direct survey evidence; Medium confidence.**

## Pulls

- Reuse of installed Python/Django expertise, models, business logic, deployment patterns, and training.
- An integrated application foundation that may reduce assembly for common data-backed web-service needs.
- Open source inspectability, adaptability, and avoidance of per-seat/runtime licensing, with the important caveat that operation is not free.
- A public release, deprecation, security-disclosure, and LTS process that can be incorporated into lifecycle planning. Django feature releases occur roughly every eight months and LTS releases typically receive security/data-loss fixes for three years ([Django release process, current for 6.0](https://docs.djangoproject.com/en/6.0/internals/release-process/)). **Direct factual evidence; High confidence.**
- Visible professional use and workforce familiarity. In the 2025 Django survey, 25% of respondents worked at organizations above 1,000 employees (6% at 1,001–5,000 and 19% above 5,000); 82% of all respondents wrote Django professionally. This proves participation in large organizations, not organization-wide adoption or local hiring supply ([DSF/JetBrains survey, responses November 2024–January 2025](https://lp.jetbrains.com/django-developer-survey-2025/)). **Direct survey evidence; Medium confidence.**
- Production precedent can reduce novelty anxiety. Meta proves Django can be part of a very large deployment, but its custom infrastructure and Python optimization mean “Meta uses it” is not a workload-fit argument.

## Anxieties

- “Who is accountable if an open-source component has no vendor SLA or indemnity?”
- “Will core and third-party packages be patched within our required window?”
- “Can it meet our target latency, concurrency, availability, data, and deployment constraints without disproportionate customization?”
- “Are we approving Django core, or an unbounded package ecosystem with different maintainers and licenses?”
- “Can we recruit, train, and retain enough maintainers in our markets?”
- “Will the framework's release cadence create upgrade churn, or will an LTS become an excuse to defer upgrades?”
- “Can evidence satisfy security, privacy, customer, and regulatory reviewers?”
- “Will a standard create leverage across teams or lock unsuitable workloads into one answer?”
- “Will I be blamed for delay if I require evidence, or for harm if I approve too quickly?” **Emotional hypothesis; Low confidence.**

## Habits and inertia

Approved technology catalogs, golden paths, cloud contracts, identity, databases, CI/CD, monitoring, security tools, hiring pipelines, outsourcing relationships, and prior architecture decisions constrain the feasible set. These are often rational controls: reusing a prior proportional assessment saves time. They can also hide drift when an old approval no longer matches a service's data sensitivity, dependencies, or threat model.

An installed Django estate accumulates models, migrations, admin workflows, APIs, tests, runbooks, packages, and expertise. This produces real switching cost and makes incremental evolution attractive. Conversely, an organization standardized on another runtime may reject Django because the exception cost exceeds expected product benefit. **Inference from authoritative evolution/TCO guidance; High confidence for the mechanism, Low confidence on its magnitude.**

## Decision criteria

No reviewed evidence supports one universal ranking. “Critical/High/Variable” indicates a context-dependent gate, not an ordinal market score.

| Criterion | Importance | Confidence | Evidence the stakeholder system needs |
|---|---|---:|---|
| Service and workload fit | Critical | High | User needs, data model, integrations, latency/concurrency, accessibility, privacy, roadmap, prototype results |
| Security and supply-chain governance | Critical | High | Secure-use guidance, disclosure/patch process, dependency inventory/provenance, vulnerability history, control ownership |
| Operability and reliability | Critical for production | High | Deployment, health, telemetry, capacity, backup/recovery, incident/on-call and database-change practice |
| Organizational/platform compatibility | High | High | Approved runtime/cloud, identity, data, CI/CD, observability, network, architecture and support model |
| Lifecycle support and maintainability | High | High | Release/LTS/deprecation path, upgrade rehearsal, package health, maintainer diversity, succession |
| Total cost and reversibility | High | High | Delivery, infrastructure, assurance, operations, upgrades, skills, support, migration/exit and opportunity cost |
| Team capability and talent | High where growth/turnover matters | Medium | Current skills, onboarding evidence, local labor market, training/consultancy and key-person exposure |
| Legal, license, privacy and regulatory fit | Critical where applicable | High | License review, data flows/residency, records, contractual responsibility, sector and market obligations |
| Performance efficiency/scalability | Variable to Critical | High | Representative load/cost results and known mitigation complexity, not adopter logos |
| Project/ecosystem sustainability | High for critical dependency | High | Governance, activity, releases, bus factor, security response, funding/contribution options |
| Standardization leverage versus exception cost | Variable | Medium | Reuse across teams, duplicated controls removed, unsuitable workloads excluded, exception lead time |

The criterion set is directly supported by GOV.UK's open-source buying questions (function, users, cost, training, maturity, support, maintenance, reliability, performance, scale, security patches, flexibility, interoperability, license, warranty), OpenSSF's dependency guide, and NIST's risk-based acquisition guidance ([GOV.UK, March 31, 2021](https://www.gov.uk/guidance/be-open-and-use-open-source)). **Direct synthesis; High confidence in the set, Low confidence in any universal weighting.**

## Main concerns

**Practical concerns:** production architecture; dependency boundaries; upgrade/patch mechanics; identity/data integration; deployment and rollback; observability; testing; capacity and cloud cost; skills; documentation; support; and ownership.

**Legitimate limitations:** Django is an application framework, not a complete enterprise support contract, platform, compliance certification, or assurance package. Third-party package quality varies; LTS still requires upgrades; extreme scale may require specialized infrastructure and optimization. Meta's millions-of-lines Python estate uses custom analysis and runtime work, illustrating both achievable scale and the investment behind it ([Meta Pysa account, August 7, 2020](https://engineering.fb.com/2020/08/07/security/pysa/); [Meta Immortal Objects, August 15, 2023](https://engineering.fb.com/2023/08/15/developer-tools/immortal-objects-for-python-instagram-meta/)). **Direct case evidence; High confidence about Meta, Low generalizability.**

**Perceived risks/misconceptions:** open source means “unsupported”; no license fee means no cost; a famous adopter proves fit; old means obsolete; LTS means no maintenance; built-in security controls make an application compliant; or procurement has no role because Django is not purchased.

**Organizational objections:** unapproved runtime, no accountable owner, insufficient evidence, platform divergence, unclear residual risk, unacceptable support window, weak package governance, or no budget for ongoing stewardship.

**Emotional resistance (hypotheses):** fear of novelty, fear of appearing conservative, preference for a vendor “throat to choke,” sunk-cost attachment, and review fatigue. **Low confidence; requires interviews.**

## Objections and perceived risks

- **“Django cannot scale.”** Contradicted as an absolute by Meta; not contradicted for every latency, concurrency, cost, or organization. Validate the target workload.
- **“Django is enterprise-ready.”** Too vague. Framework maturity does not supply a production topology, SLA, dependency governance, compliance evidence, or operating team.
- **“Open source cannot pass procurement.”** Contradicted as an absolute: authoritative procurement guidance explicitly covers OSS. Some organizations may still require paid support or contractual accountability.
- **“There is no vendor, so nobody supports it.”** Partially misconceived. Django has public maintainers, paid Fellows, a security team, releases, and LTS; the DSF explicitly does **not** provide technical support or consulting to corporate members ([DSF corporate membership, current](https://www.djangoproject.com/foundation/corporate-membership/)). The adopting organization still needs operational ownership.
- **“A corporate membership buys influence or support.”** Contradicted by DSF policy: membership funds priorities and provides recognition/impact reporting, but no technical services or preferential development input.
- **“Large company adoption proves our risk case.”** Unsupported. OpenSSF explicitly warns against choosing software merely because large companies use it.
- **“A zero-cost dependency should not need finance attention.”** Misleading. Finance may not approve Django itself, but does approve staff, infrastructure, assurance, support, upgrades, migration, and optional upstream funding.

## Information needed to make progress

1. Service outcomes, users, criticality, data sensitivity, regulatory scope, risk appetite, and decision owner.
2. Existing standards and estate constraints; why prior decisions were made; approved/exception routes.
3. Workload and non-functional thresholds, plus a production-like prototype of the highest-risk paths.
4. Reference architecture: boundaries, identity, data, API/frontend, queue/cache, infrastructure, telemetry, resilience, recovery, and on-call.
5. Django core and third-party inventory: versions, licenses, provenance, maintainers, vulnerabilities, support windows, and upgrade plan.
6. Secure-development and assurance evidence mapped to the organization's controls; NIST SSDF gives a common outcome language and helps acquirers understand supplier practices ([NIST SP 800-218, February 2022](https://nvlpubs.nist.gov/nistpubs/specialpublications/nist.sp.800-218.pdf)).
7. Team model: owners, capability, onboarding, succession, local hiring, consultants/support, and contribution policy.
8. Lifecycle economics and alternatives, including exit/transition; explicit residual risks, approver, expiry, and revisit triggers.

## Trusted content formats

- **Executable prototype, benchmark, threat model, and failure/recovery exercise:** validates fit against the organization's thresholds.
- **Architecture diagram and decision record:** lets reviewers see context, interfaces, owners, trade-offs, consequences, and revisit conditions.
- **Versioned documentation, support/deprecation policy, security advisories, upgrade guides, checksums and release history:** lifecycle evidence.
- **Dependency inventory/SBOM, license record, repository history, tests/CI, maintainer and OpenSSF-style assessment:** supply-chain review.
- **Control mapping and concise risk report:** translates project facts for security, audit, legal, procurement, and risk owners.
- **Detailed production account or postmortem with constraints and numbers:** analogous validation; a logo/testimonial alone is weak.
- **TCO and staffing model with sensitivity ranges:** supports finance and accountable leadership without false precision.

These preferences are inferred from the artifacts authoritative guidance asks decision teams to produce. **Inference; High confidence for formal evaluation, Medium for less regulated enterprises.**

## Discovery, evaluation, validation, and engagement channels

- **Discovery:** internal developer portals/approved catalogs, peers, architecture communities, search, engineering blogs, conferences, podcasts, and short-form social expand the option set. They signal relevance but do not establish approval.
- **Evaluation:** official documentation, release/security/support policies, repositories/issues, dependency metadata, standards, practitioner forums, and internal ADRs answer fit and lifecycle questions.
- **Validation:** prototypes, load/failure/security tests, architecture and threat-model review, detailed peer references, due-diligence questionnaires, and production accounts test claims in context.
- **Ongoing engagement:** security/release notices, documentation, GitHub/issues, Forum/Discord, mailing lists, internal communities, conferences/sprints, consultants, and OSPO processes support operation, escalation, contribution, and horizon scanning.

The 2025 Django survey provides behavioral but non-enterprise-specific evidence: respondents used djangoproject.com (60%), YouTube (22%), Stack Overflow (18%), Reddit (18%), Django Forum (15%), newsletter (12%), podcasts (7%), Discord (6%), and other channels to follow development; 18% did not follow it. This supports different ongoing/discovery roles, not an enterprise trust ranking. GitHub/issues and mailing lists are plausible evaluation/engagement channels but were not reported in that survey question. Professional peer networks and short-form social remain weakly measured. **Direct survey evidence plus inference; Medium confidence.**

## Decision-makers and influencers

| Decision role | Typical actors | Authority / blocker | Consequences carried |
|---|---|---|---|
| Initiator | Product/service owner, senior engineer, technical lead, business sponsor, platform team | Frames new need, reuse, exception, or modernization | Delivery opportunity and delay |
| Researcher/evaluator | Solution/software architect, lead/staff developer, platform/SRE, security architect | Produces prototype, architecture, dependency, risk, skills, and TCO evidence | Technical debt and implementation feasibility |
| Influencer | Delivery developers, data/frontend leads, operations, peer architects, consultants, OSPO | Supplies tacit experience; may condition feasibility | Daily productivity, maintainability, on-call load |
| Approver/economic buyer | Accountable service owner, CTO/CIO/VP, architecture authority, budget/risk owner | Accepts investment, standard/exception, and residual risk | Business continuity, cost, reputation, regulatory exposure |
| Blocker/reviewer | Security, privacy/DPO, legal/license, compliance/audit, enterprise architecture, platform governance, procurement, finance | Can reject or condition when evidence, control, ownership, contract, or funding is inadequate | Assurance failure within their mandate |
| User | Developers, testers, DevOps/SRE, support staff, administrators | Builds, deploys, upgrades, troubleshoots, and operates | Workflow friction and incident toil |
| Consequence bearer | End users/data subjects, customers, on-call staff, business operations, service owner, organization/public | Often little framework-choice power | Outage, breach, exclusion, delay, migration, financial and reputation harm |

NIST directly supports multidisciplinary acquisition teams; UK Secure by Design names senior responsible owner, service owner, programme manager, delivery/development teams, security professionals, legal, and procurement. Exact titles and vetoes vary. **Direct evidence for role distribution; High confidence.** A “marketing executive” is not evidenced as a normal framework-standard approver; a business/product executive may sponsor outcomes or budget without evaluating the framework.

## Appropriate next actions for Django to encourage

These are job-progress actions, not campaign or site recommendations:

- **Move from interest to contextual test:** define requirements and run a bounded production-like prototype; serves the validation job.
- **Move from prototype to shared decision:** record architecture, dependencies, ownership, risks, TCO, and revisit triggers; serves consensus and approval.
- **Move from approval to stewardship:** nominate service/dependency owners, choose supported versions, subscribe to security/release information, inventory packages, and rehearse upgrades; serves continuity.
- **Move from local success to reusable governance:** contribute a reference pattern and proportional assessment to the internal platform/catalog, with an exception path; serves organizational scale.
- **Move from dependence to resilience:** assess whether upstream issues, employee contribution, security work, or DSF funding aligns with dependency criticality and organizational goals; serves sustainability.
- **Move from inherited risk to an explicit plan:** baseline the estate and choose upgrade, containment, decomposition, or migration milestones; serves modernization.

## Overlaps with other audiences

- **Technical leads/software architects:** usually lead technical evaluation; this report adds the organizational system around them.
- **CTOs/engineering managers:** may sponsor, approve budget, set risk appetite, and bear portfolio consequences.
- **Existing professional Django developers:** users and internal experts who surface maintenance and delivery realities.
- **Security, platform/SRE, privacy, legal, procurement, and finance specialists:** reviewers or blockers whose jobs extend beyond Django.
- **Contributors/maintainers:** employees may contribute upstream when policy allows; maintainers are external dependency stakeholders.
- **Corporate funders:** dependency-owning organizations may fund continuity, but funding has a separate proposal/impact job.
- **End users and data subjects:** consequence bearers, not framework evaluators.

## Possible segmentation problems

Organization size alone is a poor predictor. Segmenting by **service criticality, regulatory burden, data sensitivity, installed Django depth, greenfield versus inherited estate, centralization of governance, platform maturity, internal expertise, sourcing model, geography, and product-versus-internal-service status** is more actionable. A 10,000-person technology firm may give teams more autonomy than a 500-person regulated organization. A single large organization may contain both tightly governed systems and low-risk experiments.

“Enterprise” also risks conflating a framework, a commercial support offering, a deployment platform, and organizational assurance. “Decision-maker” hides vetoes and consequence bearers. “Technology stakeholder” should therefore be modeled per decision, not assigned permanently by title. **Inference from role and risk guidance; High confidence.**

## Existing-analysis claim audit

| Existing claim | Audit | Evidence basis | Confidence and gap |
|---|---|---|---|
| A mid-to-large-company “marketing executive or technical decision-maker” approves framework standards based on currency, long-term reliance, community/support, security, and hiring; enterprise examples, production architecture, and testimonials influence them. | **Partially supported** | **Direct:** authoritative guidance supports currency/support, security, maintainability, maturity, skills, fit, and contextual production evidence. **Inference:** those criteria apply to Django review. Authority is distributed; marketing executives are not evidenced as routine framework approvers, and OpenSSF warns against large-company imitation. | **High** for criteria and distributed roles; **Low** for a marketing-executive role or testimonial influence. Gap: private-enterprise decision interviews. |
| Companies depending on Django want maintenance continuity to avoid migration costs and may fund it; corporate approval can involve finance and leadership. | **Partially supported** | **Direct:** general OSS dependence, transition-cost guidance, organizational OSS funding, and DSF corporate funding. **Inference:** Django-dependent firms fund specifically to avoid migration and route approval through finance/leadership. | **Medium.** Gap: Django-dependent firms' stated motives, avoided-cost estimates, and approval paths. |
| Corporate funders need visible impact and internal ROI/proposal support. | **Partially supported** | **Direct:** DSF corporate membership includes an annual impact report; the OSS funding study documents organizational measurement difficulty. **Inference:** Django funders require a particular ROI case. | **Medium.** Gap: interviews with sponsors, budget owners, and declined prospects. |
| Existing professional Django developers seek releases/upgrades, scaling help, and best practice. | **Partially supported** | **Direct:** users inside large organizations carry upgrade, scaling, and operations work; Django publishes lifecycle channels and the survey establishes professional use. **Inference:** large-organization respondents share all stated motivations. | **Medium.** Gap: employer-size cross-tabs and job interviews. |
| Docs/release notes, forums/Discord, GitHub/issues, mailing lists, conferences/sprints, podcasts, professional peers, and short-form social are touchpoints. | **Partially supported** | **Direct:** the Django survey supports the official site, Forum, Discord, podcasts, newsletter, and some social/friend channels for following development. **Inference:** repositories/issues, releases, and other channels fill the assigned enterprise-stage roles. | **Medium** overall; **Low** for enterprise-specific ordering. Gap: behavioral channel data by role and decision stage. |

## Evidence table

| Finding | Source (title, publisher/author, date, URL) | Evidence type | Direct evidence or inference | Confidence | Research notes |
|---|---|---|---|---|---|
| Large-organization technology decisions should preserve reversibility, manage security risk/TCO, account for the existing landscape, prototype, map, and evolve. | [“Choosing technology: an introduction,” GOV.UK Service Manual, published May 23, 2016; updated October 15, 2024](https://www.gov.uk/service-manual/technology/choosing-technology-an-introduction) | Authoritative public-sector guidance | Direct | High | Strong for public services; principles likely transfer, exact governance may not. |
| OSS evaluation criteria include need, cost, training, maturity, support, maintenance, reliability, performance, scale, security patches, interoperability, license, and warranty. | [“Be open and use open source,” GOV.UK, published November 6, 2017; updated March 31, 2021](https://www.gov.uk/guidance/be-open-and-use-open-source) | Authoritative procurement/technology guidance | Direct | High | Criteria, not ranked weights. Explicitly says OSS is not cost-free and includes exit/transition cost. |
| Formal software acquisition combines program, technical, security, supply, and procurement roles and tailors review to criticality, data, and environment. | [NIST SP 800-161r1, NIST, May 2022](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-161r1-upd1.pdf) | Government standard/guidance | Direct | High | Federal origin; useful model, not proof every enterprise follows it. |
| Open-source and other third-party products should be inventoried, proportionately security-reviewed, documented, and monitored through the lifecycle. | [“Managing third-party product security risks,” UK Government Security, updated December 31, 2025](https://www.security.gov.uk/policy-and-guidance/secure-by-design/activities/managing-third-party-product-security-risks/) | Authoritative security-governance guidance | Direct | High | Names SRO, service owner, programme, delivery, security, legal, and procurement roles. |
| Secure development practices need integration across the SDLC; SSDF provides an outcome language usable by acquirers. | [“Secure Software Development Framework 1.1,” NIST SP 800-218, February 2022](https://nvlpubs.nist.gov/nistpubs/specialpublications/nist.sp.800-218.pdf) | Government standard/guidance | Direct | High | Framework-neutral; not an assurance certificate for Django. |
| OSS dependency due diligence should cover necessity, authenticity, maintenance, maintainer diversity, releases/LTS, security response, tests, license, adoption, and practical testing. | [“Concise Guide for Evaluating Open Source Software,” OpenSSF Best Practices WG, March 28, 2025](https://best.openssf.org/Concise-Guide-for-Evaluating-Open-Source-Software.html) | Cross-industry foundation guidance | Direct | High | Explicitly warns against choosing because large companies use it. |
| Security/compliance and patch currency are recurring OSS-operations challenges. | [“2024 State of Open Source Report” release, OpenLogic/Perforce with OSI and Eclipse Foundation, February 1, 2024](https://www.perforce.com/press-releases/openlogic-perforce-release-2024-state-of-open-source-report) | Industry survey | Direct | Medium | Self-selected/vendor-linked; all organization sizes; not Django-specific. |
| Widely used OSS creates large firm value and dependence. | [“The Value of Open Source Software,” Hoffmann, Nagle, Zhou, HBS Working Paper 24-038, January 1, 2024](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4693148) | Empirical working paper | Direct | Medium | Millions-of-firms data and modeled replacement value; not Django-specific. |
| Organizations fund OSS mainly through labor, but measurement and internal visibility are difficult. | [“2024 Open Source Software Funding Report,” LF Research/GitHub/Harvard, 2024](https://www.linuxfoundation.org/research/open-source-funding-2024) | Survey and extrapolation | Direct | Medium | Respondents include OSPO, engineering/product heads, and executives; quantification gaps are explicit. |
| Django has time-based releases, patch releases, and typically three-year LTS security/data-loss support. | [“Django's release process,” Django documentation 6.0, current in July 2026](https://docs.djangoproject.com/en/6.0/internals/release-process/) | Project policy | Direct | High | Django-controlled source appropriate for factual policy. |
| Corporate membership funds DSF priorities but buys neither technical support nor preferential development influence. | [“Corporate membership,” Django Software Foundation, current in July 2026](https://www.djangoproject.com/foundation/corporate-membership/) | Project/foundation policy | Direct | High | Annual impact report supports visible-impact claim; motivations listed are self-reported by program. |
| Django is used professionally by respondents in large organizations; official site, forums, newsletters, video, Q&A, podcasts, and social have observable following/learning use. | [“Django Developers Survey 2025,” DSF/JetBrains, responses November 2024–January 2025](https://lp.jetbrains.com/django-developer-survey-2025/) | Community survey | Direct | Medium | Self-selected users/enthusiasts; employer-size response is not organization adoption; no enterprise cross-tabs reviewed. |
| Reuse of an installed Django estate and internal infrastructure accelerated Threads, while multiple specialist teams enabled scale. | [“Threads: The inside story of Meta's newest social app,” Meta Engineering, September 7, 2023](https://engineering.fb.com/2023/09/07/culture/threads-inside-story-metas-newest-social-app/) | Direct production account | Direct | High for Meta; Low generalizability | Shows consequences of installed capability and organizational collaboration, not greenfield fit. |
| Very large Django/Python operation can require specialized security analysis and runtime/efficiency work. | [“Pysa,” Meta Engineering, August 7, 2020](https://engineering.fb.com/2020/08/07/security/pysa/); [“Immortal Objects,” Meta Engineering, August 15, 2023](https://engineering.fb.com/2023/08/15/developer-tools/immortal-objects-for-python-instagram-meta/) | Direct production accounts | Direct | High for Meta; Low generalizability | Counters both “cannot scale” and “scales without investment.” |
| EU commercial software manufacturers in scope of the CRA must manage lifecycle cyber risk and third-party component due diligence; reporting starts September 11, 2026 and main provisions December 11, 2027. | [“Cyber Resilience Act: summary,” European Commission, updated 2026](https://digital-strategy.ec.europa.eu/en/policies/cra-summary) | Official legal summary | Direct | High | Applies by legal scope, not simply because an organization uses Django. Obtain counsel for classification. |
| Delivery outcomes can be tracked through change lead time, deployment frequency, failed-deployment recovery, change failure, and rework. | [“A history of DORA's software delivery metrics,” DORA, updated January 2, 2026](https://dora.dev/insights/dora-metrics-history/) | Long-running industry research synthesis | Direct | High for constructs | Framework-neutral and not a Django causal claim. |

## Unanswered research questions

1. In private enterprises, when does a zero-license-cost framework trigger procurement review versus architecture/security review only?
2. Which roles actually hold veto power for Django adoption by industry, geography, service criticality, and governance model?
3. What evidence has caused large organizations to approve, condition, or reject Django specifically?
4. How do approved Django estates measure patch latency, upgrade cost, dependency risk, incident load, and developer onboarding?
5. What support model do regulated adopters require: internal ownership, consultancy, managed platform, commercial package support, or some combination?
6. How deep is Django hiring supply in the actual regions and domains where large adopters recruit, and how transferable are general Python skills?
7. What organizational costs arise from Django's core release cadence and third-party compatibility across several teams?
8. What prevents employee contribution or funding when a company materially depends on Django, and which impact measures unlock approval?
9. Do architecture accounts, security/process evidence, peer references, or prototypes change decisions most—and for which reviewer?
10. How are end-user, data-subject, operator, accessibility, and business-continuity consequences represented in framework decisions?
