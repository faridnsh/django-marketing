# Agencies and consultancies delivering client software

## Audience definition and boundaries

This is a **client-delivery context occupied by several people**, not a persona. It includes agency owners, technical directors, architects, consultants, developers, project managers, and commercial staff. Client product owners, technical authorities, buyers, procurement, reviewers, users, and future maintainers shape whether the supplier can responsibly use Django.

The boundary is commercial responsibility for somebody else's outcome. An in-house engineer belongs primarily to developer/lead audiences; a freelancer enters when scope, handover, liability, or client approval changes the job. Hosted-site configuration is outside the core unless custom delivery is considered.

Agency is too broad unless delivery and business model are named. Promethean separates revenue generation, delivery, support, and leadership. Its 2025 report compiles mostly North American owner/manager surveys, interviews, and company/public data ([2025 Digital Agency Industry Report](https://prometheanresearch.com/wp-content/uploads/2025/05/2025-Promethean-Research-Digital-Agency-Industry-Report-V1.02.pdf), April 2025). Owners commonly span sales, production, and leadership below 10 FTE; larger firms separate duties. **Direct industry evidence; Medium confidence outside this sample.**

The main conclusion is that Django is rarely the end job. It is one component in a joint client-supplier system. **Inference; High confidence**, triangulated by operating data, outsourcing research, procurement guidance, and consultancy accounts.

## Important subsegments

- **Owner-led Django studio or specialist consultancy.** The owner may initiate positioning, qualify and close work, choose standards, architect, deliver, and bear margin and reputation consequences. Specialization can make accumulated Django knowledge, templates, and peer reputation economically important.
- **Larger development/digital agency.** Sales wins the account; technical leadership sets guardrails and evaluates fit; delivery manages scope; engineers operate; commercial, security, and legal review risk. Approval is distributed.
- **Generalist agency choosing per project.** Django competes with internal stacks, client mandates, packaged platforms, and buying rather than building. The job is to avoid an ill-fitting custom build.
- **Product/discovery or transformation consultancy.** Work may end at discovery, prototype, advice, rescue, or capability building. Recommendation independence matters more than house-stack reuse.
- **Staff augmentation or embedded delivery.** The client normally owns architecture and product priority; the consultant's job is to become productive, align with the client's standards, and transfer knowledge. Framework advocacy may be inappropriate.
- **Build-and-handover engagement.** The supplier must create code, deployment, documentation, access, and capability that a client or replacement supplier can operate. Exit and knowledge transfer are part of the product.
- **Build-operate/managed service or retainer.** The agency retains operations and recurring revenue; upgrades, security, incidents, and dependencies must remain serviceable.
- **Fixed-bid, time-and-materials, or outcome/value engagement.** Fixed price puts scoping error largely on the agency; T&M places more overage risk on the client; outcome models demand agreed measures. Most sampled agencies mix methods. **Direct evidence; Medium confidence.**
- **Public-sector, regulated, or enterprise client.** Formal procurement, accessibility, security, privacy, architecture, open-source policy, supplier assurance, financial viability, and exit terms can outweigh developer preference.
- **Rescue, upgrade, or inherited Django system.** The trigger is an existing dependency, failed delivery, performance or stability issue, end-of-support version, or missing client capability—not greenfield framework selection.

These dimensions intersect; they should not be treated as a maturity ladder.

## Primary job to be done

> When a client entrusts us with a software outcome under budget, time, assurance, and ownership constraints, I want to deliver a supportable solution our joint teams can sustain, so I can create client value while protecting delivery credibility and engagement economics.

This is a **researcher inference; High confidence in the functional job, Medium in its wording**. Evidence establishes commercial risk, collaboration, outcome clarity, knowledge transfer, and delivery economics; no reviewed study asks this audience to formulate a JTBD.

## Additional jobs to be done

There are six important jobs in total, including the primary job.

1. **Deliver a supportable client outcome (primary).** When a client brings an uncertain software need under commercial and ownership constraints, I want to turn it into working, secure, operable software, so I can create client value without confusing framework adoption with the outcome.
2. **Make uncertainty commercially governable.** When discovery and change make delivery uncertain, I want scope, evidence, roles, pricing, acceptance, and risk to remain explicit, so I can keep learning from becoming either an unbounded client bill or an agency-margin surprise.
3. **Turn expertise into repeatable delivery capacity.** When recurring delivery work can be reused safely, I want to apply proven judgment, conventions, components, automation, training, and partner knowledge, so I can reduce lead time and defects while preserving project-specific discovery.
4. **Earn and preserve multi-party trust.** When client sponsors, technical reviewers, procurement, security/legal, users, and future operators bear different consequences, I want to give each role proportionate evidence, so I can earn trust without asking one stakeholder’s proof to stand in for another’s.
5. **Transfer or retain operational ownership deliberately.** When an engagement approaches operation, renewal, or exit, I want code, environments, credentials, decisions, and know-how controlled by the agreed party, so I can avoid ambiguous ownership and an unsafe handover.
6. **Keep the service and the relationship viable after launch.** When a launched service needs upgrades, security work, observation, support, evolution, or handover, I want a cost and cadence compatible with client value and the supplier’s business model, so I can sustain the service without an uneconomic or misleading commitment.

## Functional, emotional, and social dimensions

| Job | Core functional job | Emotional job | Social job | Supporting jobs |
|---|---|---|---|---|
| Deliver a supportable outcome | Discover, build, deploy, and evidence the intended client result | Reduce fear of a visible failure outside the team's control (**hypothesis**) | Be trusted as a responsible adviser, not merely a pair of hands (**inference**) | User research; architecture; delivery; security; testing; operations |
| Govern uncertainty | Match contract, scope, cadence, and acceptance to what is knowable | Feel able to discuss uncertainty without appearing evasive (**hypothesis**) | Demonstrate commercial maturity to client and leadership (**hypothesis**) | Discovery; backlog; assumptions; estimates; change control; metrics |
| Create repeatable capacity | Reduce avoidable variation and relearning across engagements | Reduce overload from every project being bespoke (**hypothesis**) | Be recognized internally as a force multiplier (**hypothesis**) | Standards; reusable apps; CI/CD; playbooks; code review; training |
| Preserve trust | Make claims inspectable by every decision role | Avoid reputational shame and escalation (**hypothesis**) | Maintain peer, client, and procurement credibility (**inference**) | References; demos; risk register; reporting; assurance evidence |
| Transfer/retain ownership | Put access, knowledge, and decision rights where contracted | Reduce anxiety about dependency on one person or supplier (**inference**) | Be seen as a partner who does not manufacture lock-in (**hypothesis**) | Repository control; runbooks; ADRs; training; exit rehearsal |
| Sustain service/relationship | Maintain supported, secure, useful software and service economics | Reduce dread associated with neglected legacy work (**hypothesis**) | Preserve client confidence and professional pride (**hypothesis**) | Monitoring; support; patching; upgrades; roadmap; account review |

Functional and supporting dimensions are **Medium-to-High confidence**. Emotional and most social jobs are **Low-confidence hypotheses** requiring interviews with owners, consultants, client buyers, and teams after unsuccessful engagements.

## Triggering situations

**Event-triggered**

- A prospect issues an RFP, asks for a proposal, or requests technical discovery before approving spend.
- A client need moves beyond a hosted product, no-code tool, CMS configuration, or manual process and may justify custom software.
- An agency wins unfamiliar work, enters a regulated sector, changes its specialization, or considers a new house standard.
- A prototype must become a production service with authentication, workflows, integrations, administration, accessibility, security, or service levels.
- A supplier inherits an old Django system, a failed build, poor tests, weak deployment, performance problems, or an unsupported version.
- A fixed-price scope starts diverging from reality, acceptance is disputed, or delivery evidence fails to reassure a sponsor.
- A client hires an internal team, changes supplier, brings work in-house, or invokes an exit/knowledge-transfer plan.
- A security release, dependency failure, incident, audit, key-person departure, or client procurement review exposes latent lifecycle risk.

**Recurring**

- Qualifying opportunities against capability, capacity, commercial model, and reputation risk.
- Allocating specialists and contractors while protecting utilization, continuity, and learning.
- Re-estimating and reprioritizing with the client as evidence changes.
- Demonstrating progress and maintaining alignment among users, product owners, commercial staff, and technical reviewers.
- Monitoring service health, support demand, version status, dependencies, margin, and renewal/retainer viability.
- Onboarding staff and transferring client/domain knowledge in both directions.

The distinction is **inference; High confidence**; prevalence is unmeasured.

## Desired outcomes

- Reduce elapsed time from qualified client need to a usable, production-shaped increment.
- Increase the proportion of work accepted against observable user/service outcomes rather than ambiguous activity.
- Reduce estimation variance, unplanned rework, and margin erosion while keeping change possible.
- Reduce time for an agency or client engineer to set up, understand, test, deploy, and safely change the system.
- Increase the share of common capabilities delivered through tested, maintained patterns without forcing inappropriate reuse.
- Reduce defects, security exposure, unsupported-version time, incidents, and recovery time over the contracted lifecycle.
- Make repository, environment, data, credentials, IP/license, runbook, and decision ownership explicit and testable.
- Reduce key-person and single-supplier dependence to the level the client has consciously contracted for.
- Produce procurement, security, architecture, accessibility, and operational evidence without disruptive last-minute reconstruction.
- Sustain client value and relationship continuity while keeping each engagement economically viable for the supplier.

These are **directionally measurable inferences; Medium-to-High confidence**. No universal targets are supported; context and service level determine them.

## Current behaviour or status quo

Agencies commonly start from prior capability, client mandate, or an existing platform. Promethean reports 84% of sampled agencies identified as specialists in 2024, 95% offered projects, 91% retainers, and 88% both; most leads still came through referrals. **Direct evidence; Medium confidence for digital agencies, Low for management consultancies.** Accumulated expertise is commercially useful, but the easiest stack to sell and staff is not necessarily the smallest adequate solution.

Six Feet Up described changing a small Flask extension to Django after discovering SQL, auth, user-management, and admin needs; it reports an hour-long switch and days saved ([“Django Saves the Day,”](https://sixfeetup.com/blog/django-saves-the-day) 29 September 2021). Torchbox abandoned Drupal for Django-based Wagtail despite 60% revenue exposure, citing client value, overruns/losses, and developer frustration ([“We’ve dropped Drupal,”](https://torchbox.com/wagtail-cms-services/blog/torchbox-has-dropped-drupal/) 17 October 2018). These are **direct supplier retrospectives; Medium confidence as existence proofs, Low for prevalence/causality** because they are interested sources.

REVSYS sells twice-yearly Django/package upgrades and emphasizes tests; Torchbox turned client staff-augmentation training into reusable internal/external training. These show maintenance and capability transfer as service models, not universal demand.

## Pushes

- Custom workflows, integrations, data models, permissions, or service evolution can exceed commodity products.
- Weak discovery and ambiguous acceptance turn uncertainty into rework, dispute, or margin loss. Government guidance warns against commitments based on uncertainty and bidder risk pricing.
- Thin margins make delivery leverage material: Promethean reports 14% average net margin in 2024 and says fixed-fee scoping inaccuracies can erode margin.
- Siloed teams, missing CI/CD, weak onboarding, and undocumented systems create client and supplier bottlenecks; a Six Feet Up client case reported these issues across more than 30 sub-organizations ([“Could Your Software Project Be Running Better?”](https://sixfeetup.com/company/news/could-your-software-project-be-running-more-smoothly), Six Feet Up, 21 October 2024).
- Unsupported Django/Python/package versions, security findings, incidents, or inherited technical debt make deferred lifecycle work unavoidable.
- Client procurement, security, accessibility, privacy, or open-source requirements can block an otherwise feasible proposal.
- Client concern about supplier dependence pushes explicit ownership, documentation, transferable skill, and exit planning.

## Pulls

- Django's integrated data modeling, auth, migrations, forms, admin, and security features can reduce assembly work for data/workflow-heavy services. Six Feet Up's case supports this in one bounded project.
- Python packages can let a specialist focus on client logic. Lincoln Loop says this supported its Django-focused model since 2007 ([“Python provides the tools and flexibility our clients need to thrive,”](https://lincolnloop.com/blog/python-website-development-success-story/) 25 May 2023). **Direct supplier account; Medium-Low confidence.**
- Modular Django apps can support internal reuse and clearer testing/documentation, but package selection adds maintenance and supply-chain responsibility. **Direct framework capability plus inference; Medium confidence.**
- A BSD license, public source, support roadmap, and security process enable legal/lifecycle review. Policy provides roughly eight-month feature releases and typically three-year LTS security/data-loss support ([Django download/support roadmap](https://www.djangoproject.com/download/), accessed 18 July 2026). **Direct project fact; High confidence.**
- An established specialist community can supply peers, staff, subcontractors, upgrade services, and references. The 2025 Django survey includes employed developers, owners, team leads, architects, and executives, but its official-channel recruitment cannot establish total labor supply.
- Public-sector policies can positively value open source, openness, standards, reuse, flexibility, and reduced supplier lock-in. This pull is sector-specific, not universal.

## Anxieties

- **Owner/partner:** under-scoped fixed bids, bench time, client concentration, inability to staff promises, or delivery failure damaging referrals.
- **Technical lead/architect:** choosing from familiarity, overlooking a non-functional constraint, inheriting fragile third-party packages, or being accountable for a standard across dissimilar projects.
- **Consultant/delivery lead:** unclear client goals, rights, availability, or definition of done preventing predictable delivery.
- **Engineer/operator:** being handed bespoke legacy code without tests, access, domain context, supported dependencies, or time for maintenance.
- **Client buyer:** paying for activity without outcomes; overrun; supplier failure; inability to change direction or supplier.
- **Client technical/security reviewer:** insecure configuration, weak supply-chain controls, unsupported versions, poor recovery, privacy violations, or standards mismatch.
- **Procurement/legal:** uncertain scope, financial viability, IP/open-source warranties, liability, compliance, subcontracting, lock-in, and exit.
- **Future maintainer/user:** ownership in name but not in practice.
- **Emotional hypothesis:** Django being perceived as old, monolithic, or less fashionable can threaten consultant status even when task fit is good; conversely, specialist attachment can make rejection feel like a loss of identity. **Low confidence.**

## Habits and inertia

- Reuse of a house stack, boilerplate, cloud account pattern, vendor relationship, and trained team reduces immediate sales and delivery friction.
- Specialist positioning, references, hiring, internal training, and reusable components compound around the chosen ecosystem. Torchbox's high-cost platform shift directly illustrates that standards are business-model commitments.
- Client data, integrations, infrastructure, contracts, and knowledge favor incremental rescue or upgrade over replacement.
- Referral-led selling favors work similar to the agency's existing network and portfolio; Promethean directly notes that referrals can constrain expansion into new work and scopes.
- Fixed procurement categories and mandatory client standards can settle the technology decision before the delivery team begins.
- Retainers create continuity and inertia; suppliers may benefit from ongoing complexity while clients prefer autonomy. **Inference; Medium confidence**, not a general accusation.

## Decision criteria

No reviewed evidence supports one universal ranking. Importance depends on engagement, client, delivery phase, business model, and who bears failure.

| Criterion | Contextual importance | Confidence |
|---|---|---|
| Fit to client user/service outcome and build-versus-buy boundary | First-order gate in every context | High |
| Joint team capability, availability, and ownership | High; may override theoretical framework fit | High |
| Security, privacy, accessibility, reliability, recovery, and regulatory fit | Showstopper in high-consequence/regulated work; baseline responsibility elsewhere | High |
| Time to a production-shaped increment | High in discovery, prototype, fixed runway, and iterative delivery | Medium-High |
| Maintainability, testability, documentation, and onboarding | High for handover, multi-team, or long-lived services | High |
| Supported lifecycle, dependency health, and upgrade effort | High for managed services and client reliance | High |
| Integration/data-model fit and representative performance | Workload-specific gate; test rather than infer from labels | High |
| Delivery repeatability without inappropriate standardization | High for agency capacity and quality | Medium-High |
| Contract/pricing fit, estimate uncertainty, acceptance, and liability | High because risk allocation changes with the commercial model | High |
| Client control, IP/license compatibility, portability, and exit | High for procurement and build-handover | High |
| Talent/subcontractor availability in relevant market and seniority | Potential gate; public aggregate popularity is insufficient | Medium |
| Credible comparable references and operational evidence | Important for validation, not a substitute for project testing | Medium-High |

An interactive rapid-review study with practitioners organized large-scale software selection across market strength, strategy/culture, productivity, quality, integration, cost, legal, ethics, and sense of control; it also notes performance, compatibility, reliability, security, maintainability, and portability ([Bjarnason, Åberg & bin Ali, *Empirical Software Engineering*](https://link.springer.com/article/10.1007/s10664-023-10288-w), 2023). **Direct selection-framework evidence; Medium confidence for agency web-framework choices** because the case concerned engineering software in one large company.

## Main concerns

**Practical concerns:** discovery; client availability; scope/acceptance; staffing; data/integrations; permissions; admin/content workflow; APIs/front end; testing; CI/CD; deployment; observability/recovery; accessibility; performance/cost; documentation; versions/packages; upgrade/support ownership.

**Legitimate limitations:** Django does not perform research, define outcomes, supply operations, guarantee accessibility, audit custom code, provide a vendor SLA, or transfer knowledge. Defaults do not eliminate architecture, security, supply-chain, performance, or lifecycle judgment. Realtime, CPU-intensive, unusual-database, edge/client-heavy, or platform-constrained work needs representative evaluation.

**Organizational objections:** a client may mandate another stack; its team may lack Django skill; procurement may require supplier assurance; sales may promise before discovery; delivery may resist a commercially convenient standard; the sponsor may not empower a product owner.

**Misconceptions:** open source means zero lifecycle cost; built-ins make an app secure; specialization guarantees fit; famous deployments prove every workload; fixed bids remove uncertainty; source ownership equals operational control.

**Emotional resistance hypotheses:** fear of losing expert identity, embarrassment about legacy systems, distrust produced by prior suppliers, and reluctance to expose uncertainty to the client. **Low confidence.**

## Objections and perceived risks

- **“Django is too monolithic/heavy for client work.”** Unsupported as a universal claim. It may be unnecessary for a commodity site or narrow service; integrated capabilities may reduce total delivery work for data-rich workflows. Prototype the actual slice.
- **“Django lets us deliver faster, therefore it protects margin.”** Isolated accounts partially support speed, but it does not correct unclear goals, rework, operations, or poor estimates.
- **“Standardizing on Django makes every project repeatable.”** Project requirements contradict this. Standards reduce variation but can bias build-versus-buy and hide mismatch.
- **“Open source prevents vendor lock-in.”** Only partially supported. It removes some license/source constraints, but bespoke architecture, undocumented operations, agency-owned accounts, and concentrated knowledge can still create supplier dependence.
- **“Repository ownership solves handover.”** Unsupported. Control also requires environments, credentials, documentation, recovery practice, domain knowledge, and capable people.
- **“Django is secure by default.”** Misleading. Django documents many protections, but says real-world security is multi-layered and the deployment checklist requires production-specific configuration ([Django security overview](https://docs.djangoproject.com/en/dev/topics/security/) and [deployment checklist](https://docs.djangoproject.com/en/dev/howto/deployment/checklist/), accessed 18 July 2026).
- **“An LTS removes maintenance work.”** Unsupported. LTS defines a fix window, not application/package compatibility, deployment, testing, or automatic upgrades.
- **“A specialist consultancy supplies long-term framework support.”** Contractually false unless purchased. Django community maintenance, agency service, and client application responsibility are separate.

## Information needed to make progress

Before proposing: user/service outcome; current alternative; buy/configure/build boundary; data/integrations; consequence/regulatory profile; budget/procurement; decision map; ownership/exit; joint capability/capacity; commercial model.

During evaluation: a production-shaped slice; functional/non-functional requirements; assumptions; representative data/load/cost; permission/accessibility/security review; deploy, observe, rollback, restore; version/package evidence; license/IP/subcontractor terms; estimate/change process; definition of ready/done.

Before operation/handover: repository/account ownership; reproducible setup; secrets; tests/CI; architecture decisions; migration/recovery exercise; monitoring/on-call boundaries; upgrade roadmap; known debt; training; acceptance; exit rehearsal.

## Trusted content formats

- **Client discovery artefacts and outcome/backlog maps** expose the actual job and uncertainty before technology detail.
- **Production-shaped prototypes and working increments** let product, technical, and commercial roles validate different risks.
- **Comparable case studies with scope, team, constraints, metrics, adaptations, failures, and lifecycle** are stronger than logo lists. Supplier cases remain interested evidence.
- **Primary documentation, release/security policy, source and issue history, package metadata, and license text** support technical and procurement diligence.
- **Short architecture decision records, threat models, dependency inventories, test results, and runbooks** make claims inspectable and transferable.
- **Reference calls and peer review** validate supplier behavior, collaboration, and long-term ownership better than framework popularity alone.
- **Upgrade, restore, handover, and onboarding exercises** validate lifecycle claims through behavior.
- **Interactive workshops, code review, and paired delivery** support bidirectional knowledge transfer better than passive documentation alone.

Format trust is **inferred; Medium-to-High confidence**; no reviewed research ranks it for Django agencies.

## Discovery, evaluation, validation, and engagement channels

**Discovery:** owners and consultants encounter options through prior delivery, staff and subcontractor expertise, client mandates, referrals, professional peer networks, searches, conferences, partner ecosystems, and comparable project accounts. Promethean directly supports referrals as a major agency business channel; it does not prove referrals select frameworks. Short-form social or podcasts may surface an option, but decisiveness is unproven.

**Evaluation:** technical leads use documentation, source/releases, packages, GitHub/issues, Forum, Stack Overflow, engineering accounts, spikes, and peers. Delivery/commercial assess capacity, scope, acceptance, and risk; procurement and security/legal use tenders, policy, contracts, references, assurance, and supplier data. These roles need different evidence.

**Validation:** working increments with client users, representative performance/cost tests, security/accessibility review, deploy/restore/upgrade exercises, code review by future maintainers, reference calls, and discovery/pilot contracts convert claims into evidence. UK agile-contract guidance explicitly suggests an MVP and even parallel paid discovery contracts as de-risking options.

**Ongoing engagement:** releases/advisories support maintenance; Forum, Stack Overflow, and peers support troubleshooting; GitHub/issues support investigation/contribution; training, conferences, and sprints deepen capability; account reviews connect lifecycle work to outcomes. Mailing lists, Discord, podcasts, and social remain unvalidated.

## Decision-makers and influencers

| Context | Initiator | Researcher/evaluator | Influencer/recommender | Approver/economic buyer | Blockers/reviewers | Users and consequence bearers |
|---|---|---|---|---|---|---|
| Owner-led studio, greenfield | Client sponsor or owner/partner | Owner/technical lead, senior developer | Account/delivery lead, client product contact, specialist peers | Client sponsor controls budget; agency owner accepts commercial risk | Client IT/security/legal/procurement; buy/no-build alternative | Client users and future maintainers; owner bears margin/reputation |
| Larger agency | Sales/account or client product lead | Solution architect, technical lead, delivery team | Practice lead, delivery manager, security/ops, client architects | Client budget owner; agency leadership approves bid/risk and internal standard exceptions | Procurement, legal, security, architecture, accessibility, finance | Delivery/on-call teams, client service owner and users |
| Staff augmentation | Client engineering/product lead | Client architect/lead; consultant validates local fit | Embedded engineer and agency practice lead | Client manager/procurement | Existing standards, security, supplier terms | Client team owns system consequences; consultant bears delivery credibility |
| Fixed-bid custom build | Client sponsor, procurement, or agency sales | Agency architect and delivery lead with client product owner | Engineers, users, domain experts | Client buyer approves spend; agency owner/finance accepts estimate and liability | Definition/acceptance, legal/IP, security, capacity | Agency margin and team workload; client users/operations |
| Managed service/retainer | Service owner, incident, roadmap need, or account review | Agency service/technical lead and client owner | Support, security, finance, users | Client service/budget owner; agency account/operations leadership | SLA, renewal, security, version support, exit terms | Users, on-call staff, both organizations' reputations |
| Public-sector/regulated | Commissioning/product owner | Multidisciplinary digital/technical team and supplier | User research, architecture, security/privacy/accessibility, commercial | Authorized budget holder under procurement governance | Procurement/commercial, legal, security, policy, service assessment, audit | Citizens/customers, service team, accountable officials and supplier |
| Rescue/upgrade/handover | Incident, audit, new lead, client insourcing, or supplier change | Incoming technical lead plus specialist consultant | Operators, original developers, security, procurement | Client service/budget owner | Data/access gaps, unsupported dependencies, IP/contract, unavailable knowledge | Future maintainers, on-call, users; client bears continuity risk |

This allocation is **inference; High confidence at role-category level, Medium confidence for any specific organization**. UK guidance directly identifies the client product owner, delivery manager, development team, commercial capability, supplier relationship, and multidisciplinary decision roles. Promethean directly supports owner role compression in small agencies and separation as agencies grow.

## Appropriate next actions for Django to encourage

These are progress actions tied to jobs, not proposed campaigns or assets.

- **Name the client outcome, consequence bearer, and build-versus-buy decision before selecting a framework** → supports the primary delivery job.
- **Map initiator, evaluator, influencer, approver, veto holders, users, and future owner** → supports multi-party trust and avoids treating “the client” as one chooser.
- **Run a paid, time-boxed discovery or production-shaped slice with explicit gates** → makes uncertainty governable and validates fit.
- **Record adaptations, critical dependencies, owners, assumptions, and revisit triggers** → supports repeatable but responsible delivery.
- **Test deploy, security configuration, observability, rollback, restore, upgrade, and representative load** → supports lifecycle and assurance jobs.
- **Agree source/account/IP control, knowledge-transfer evidence, maintenance responsibility, and exit conditions in the engagement** → supports deliberate ownership.
- **Invite future client maintainers and relevant procurement/security/accessibility reviewers before commitment** → supports trust and reduces late vetoes.
- **Follow supported-version/security information and budget upgrades as recurring service work** → supports post-launch viability.
- **Contribute fixes or sustained funding when repeated client delivery depends on shared Django infrastructure** → supports continuity, but only after dependency and business value are explicit.

## Overlaps with other audiences

- **Technical leads/software architects:** often the framework evaluator; this lens adds bid, utilization, client, handover, and liability constraints.
- **CTOs/engineering managers:** agency technical directors set standards while client CTOs or service owners approve exceptions and bear long-term consequences.
- **Experienced backend/full-stack developers:** implement and operate projects; their developer-experience job is only one input to client delivery.
- **Start-up decision-makers:** non-technical founders often delegate research to an agency, creating incentive and ownership risks.
- **Existing professional Django developers:** rescue, upgrades, performance, security, and best practice become consultancy services.
- **Companies depending on Django:** a client or agency with repeated reliance may care about upstream continuity; using, buying support, contributing, and funding are distinct jobs.
- **Contributors/funders:** specialist agencies can gain expertise and recognition through contribution, but evidence here does not show that contribution is a primary agency job.

## Possible segmentation problems

“Agencies and consultancies” combines business models, sizes, disciplines, buyer types, and decision rights that materially change the job. Owner, technical lead, consultant, procurement specialist, client sponsor, and future maintainer should never be collapsed into a fictional agency decision-maker. Nor should public-sector procurement be generalized to small private clients.

Recruit by decision episode, delivery model, risk allocation, agency size, assurance level, client skill, and post-launch operator. Include specialists, generalists, rejecters, replaced suppliers, failed fixed bids, and successful handovers. Evidence is heavily supplier-authored and English-speaking/North American or UK public-sector; client and post-handover views are thin.

## Existing-analysis claim audit

| Existing-analysis claim | Audit | Evidence and qualification |
|---|---|---|
| A mid-to-large-company “marketing executive or technical decision-maker” approves framework standards based on currency/relevance, long-term reliance, community/support, security, hiring; enterprise examples and testimonials influence them. | **Partially supported** | Technical leadership, client architecture/security, procurement, and economic buyers have distinct roles. Lifecycle, security, team capability, references, and comparable evidence matter. A marketing executive as normal framework approver is unsupported; testimonials aid validation but do not replace project evidence. |
| Existing professional Django developers seek current best practice, releases/upgrades, scaling help, greater expertise, and possible progression from user to contributor. | **Partially supported** | Upgrade, testing, performance, rescue, operations, and training are directly offered and discussed by Django consultancies. Contributor progression is plausible for specialists but not established as a general job. |
| Companies depending on Django want maintenance continuity to avoid migration costs and may fund it; corporate approval can involve finance and leadership. | **Partially supported** | Managed upgrade services, long-lived client systems, and Torchbox's costly platform specialization shift support continuity and switching-cost concerns. Promethean supports owner/leadership and support/finance role separation by size. Client or agency willingness to fund upstream Django is not directly evidenced. |
| Touchpoints include docs/release notes, forums/Discord, GitHub/issue tracker, mailing lists, conferences/sprints, podcasts, professional peers, and short-form social. | **Partially supported** | Docs/policy, source/issues, peers, consultancy accounts, training, and conferences have clear evaluation or engagement roles. Forum and Stack Overflow plausibly support evaluation/troubleshooting. Evidence does not establish Discord, mailing lists, podcasts, or short-form social as influential in agency decisions; listing them without behavioral purpose would overclaim. |

Donor, early-career learner, and contributor-recognition hypotheses are not central to this context and are not audited.

## Evidence table

| Finding | Source (title, publisher/author, date, URL) | Evidence type | Direct evidence or inference | Confidence | Research notes |
|---|---|---|---|---|---|
| Small agency owners often combine revenue, production, and leadership; roles separate with size. | [2025 Digital Agency Industry Report](https://prometheanresearch.com/wp-content/uploads/2025/05/2025-Promethean-Research-Digital-Agency-Industry-Report-V1.02.pdf), Promethean Research/Nicholas Petroski, April 2025 | Multi-year owner/manager surveys, interviews, company/public data | Direct | Medium | Mostly North American digital agencies; not Django- or consultancy-specific. |
| Agencies mix commercial models; fixed fee shifts scoping risk toward the agency, T&M toward the client; average 2024 net margin was 14%. | Same Promethean report, April 2025 | Industry survey/report | Direct | Medium | Useful for incentives, not universal benchmarks; methodology aggregates several surveys. |
| Projects and retainers commonly coexist; referrals remain a major but unpredictable lead source; specialization is prevalent. | Same Promethean report, April 2025 | Industry survey/report | Direct | Medium | Supports business-model context, not framework causality. |
| Agile digital contracts require client collaboration, an empowered product owner, commercial capability, outcome focus, explicit roles/definition of done, and risk-aware pricing. | [Contracting for Agile Guidance Note](https://www.gov.uk/government/publications/the-digital-data-and-technology-playbook/contracting-for-agile-guidance-note-html), UK Cabinet Office, updated 20 June 2023 | Authoritative procurement guidance | Direct | High for UK central-government guidance; Medium elsewhere | Normative guidance, not outcome evaluation. Strong role/process detail. |
| Open source, open standards, security, accessibility, purchasing strategy, and sustainability can be formal procurement criteria. | [Technology Code of Practice](https://www.gov.uk/guidance/the-technology-code-of-practice), GDS/CDDO, published 14 July 2021, updated 7 July 2025 | Authoritative public-sector policy | Direct | High in stated UK scope; Low-Medium elsewhere | Sector-specific; should not be generalized to all buyers. |
| Sustainable outside-supplier delivery requires a multidisciplinary team and accountable decision-makers inside the team. | [Service Standard: Have a multidisciplinary team](https://www.gov.uk/service-manual/service-standard/point-6-have-a-multidisciplinary-team), GOV.UK, published 8 May 2019, updated 29 January 2026 | Authoritative service guidance | Direct | High in stated scope; Medium as broader principle | Normative; does not measure supplier outcomes. |
| Goal clarity/alignment and requirements certainty affected outsourced-software project performance in a 214-client-person survey. | [“Vendor or client: What are the important factors for SDO project success?”](https://scholarworks.gnu.ac.kr/handle/sw.gnu/21764), Cho & Sung, 2013 | Empirical survey study | Direct | Medium | Older and context-limited; abstract reports vendor/client knowledge itself was not significant. |
| Knowledge transfer is difficult but central in offshore client-vendor work. | [“Client-vendor knowledge transfer in IS offshore outsourcing”](https://doi.org/10.1111/j.1365-2575.2010.00354.x), Williams, *Information Systems Journal*, 2011 | Survey of vendor engineers | Direct | Medium | Offshore India-to-Europe/US context; supports role of transfer, not Django choice. |
| Credibility and coordination positively affected knowledge transfer and outsourcing-team success in sampled teams. | [“Vendors’ team performance in software outsourcing projects”](https://doi.org/10.1108/NBRI-02-2014-0013), Nankai Business Review International, 2014 | Interviews plus survey of 124 teams | Direct | Medium | China/context and age limit generalization. |
| A consultancy selected Django when project needs expanded to SQL, auth, user management, and admin, reporting days saved. | [“Django Saves the Day”](https://sixfeetup.com/blog/django-saves-the-day), Six Feet Up/Shane Hathaway, 29 September 2021 | Direct supplier project account | Direct | Medium-Low | Self-authored commercial account; no independent client data; strong bounded context. |
| A client with 30+ sub-organizations and disparate software teams showed siloed teams, absent CI/CD, and inefficient onboarding as recurring SDLC pain points. | [“Could Your Software Project Be Running Better?”](https://sixfeetup.com/company/news/could-your-software-project-be-running-more-smoothly), Six Feet Up, 21 October 2024 | Direct supplier case-study account | Direct | Medium-Low | Self-authored commercial account describing one client engagement; not Django-specific or prevalence evidence. |
| A specialist agency changed platform despite 60% revenue exposure, citing client value, overruns/losses, and developer frustration. | [“We’ve dropped Drupal”](https://torchbox.com/wagtail-cms-services/blog/torchbox-has-dropped-drupal/), Torchbox/Paul Vetch, 17 October 2018 | Direct organizational retrospective | Direct | Medium-Low | Interested source and older; unusually candid business-model evidence. |
| Client staff-augmentation training became repeatable internal/external Django/Wagtail training. | [“The evolution of our developer training programme”](https://torchbox.com/wagtail-cms-services/blog/the-evolution-of-our-developer-training-programme/), Torchbox/Emily Topp-Mugglestone, 29 January 2024 | Direct practitioner account | Direct | Medium-Low | Shows capability-transfer model, not market prevalence. |
| Rescue and recurring upgrade services make testing, dependencies, and lifecycle work sellable consultancy jobs. | [Django Upgrade Service](https://www.revsys.com/django-upgrades/), REVSYS, accessed 18 July 2026; [“REVSYS is 16 Years Old Today”](https://www.revsys.com/tidbits/revsys-is-16-years-old-today/), Frank Wiles, 5 May 2023 | Current service description and founder retrospective | Direct | Medium-Low | Commercial offering proves availability, not buyer demand or outcome. |
| Django has a public BSD license, supported-version roadmap, LTS policy, security process, and production checklist. | [Download/support roadmap](https://www.djangoproject.com/download/), [security overview](https://docs.djangoproject.com/en/dev/topics/security/), [deployment checklist](https://docs.djangoproject.com/en/dev/howto/deployment/checklist/), Django/DSF, accessed 18 July 2026 | Primary project policy/documentation | Direct | High | Establishes inspectable process/capabilities, not application security or agency support. |
| The 2025 engaged Django sample spans employees, owners, leads, architects, and executives and uses diverse hosting/operations. | [Django Developers Survey 2025](https://lp.jetbrains.com/django-developer-survey-2025/), DSF and JetBrains; fielded November 2024–January 2025, results 2025 | Self-selected survey, 4,600+ respondents | Direct | Medium for respondents; Low for agency market | Recruited through official Django channels; no agency/client role cross-tabs. |
| Software selection is multi-criteria, including quality, integration, cost, legal, strategy/culture, ethics, and control—not popularity alone. | [“Software selection in large-scale software engineering”](https://link.springer.com/article/10.1007/s10664-023-10288-w), Bjarnason, Åberg & bin Ali, *Empirical Software Engineering*, 2023 | Interactive rapid reviews and practitioner co-design/evaluation | Direct model; inferred agency applicability | Medium | One industrial engineering-tool context; useful taxonomy, not Django ranking. |
| Open-source security practice matters in adoption, while staying current and complying with security policies remains difficult for organizations. | [Open Source Survey 2024](https://opensourcesurvey.org/), GitHub, 2024; [2024 State of Open Source press summary](https://www.perforce.com/press-releases/openlogic-perforce-release-2024-state-of-open-source-report), OpenLogic/OSI/Eclipse Foundation, 1 February 2024 | Participant and organizational surveys | Direct | Medium | Vendor involvement and broad OSS scope; supports concern, not Django-specific risk. |
| Agency framework choice must jointly satisfy client outcome, delivery capability, lifecycle/ownership, and engagement economics. | Synthesis of evidence above | Researcher synthesis | Inference | High | Exact relative weights require role- and episode-specific interviews. |

## Unanswered research questions

- In actual framework decisions, who initiates, recommends, vetoes, approves spend, operates, and bears failure—and how does this differ by agency size and engagement model?
- What proportion of Django agency work is greenfield, rescue/upgrade, staff augmentation, managed service, CMS, or capability transfer?
- Which requirements most often disqualify Django before a proposal, and which concerns are merely perceived?
- How do Django specialists test build-versus-buy honestly when their revenue and identity favor custom Django delivery?
- What delivery metrics differ between Django and the same agency's other stacks after controlling for team experience and project type?
- How much do reusable apps, templates, infrastructure, and training improve lead time or quality, and how often do they create inappropriate coupling?
- What are the actual costs of Django upgrades, package replacement, security response, and client handover across project sizes and ages?
- Which evidence persuades each client role: working slice, reference call, case study, architecture note, security evidence, procurement certification, or specialist reputation?
- How do clients evaluate practical ownership six to twelve months after handover or supplier change?
- How do fixed bid, T&M, retainer, outcome-based, and public framework contracts change technical choices and maintenance quality?
- Is Django/Python talent genuinely hard or easy to source by geography, seniority, domain, clearance, and employment/contract model?
- What do agencies and clients that rejected or replaced Django report, including successful non-adoption and failed Django engagements?
- Do contribution and DSF funding produce measurable delivery, hiring, reputation, or dependency-risk value for specialist agencies, and who approves that spend?

<!-- RESEARCH PROVENANCE: BEGIN -->
## Research provenance

This section was generated from the recorded Codex session JSONL logs. File attribution uses successful patch events; searches and domains use nested web-tool calls.

### Session `019f7553-5611-72d2-a272-d58d5c9eeb69`
- Log: `rollout-2026-07-18T15-03-43-019f7553-5611-72d2-a272-d58d5c9eeb69.jsonl`
- This document: `add, update`
- Search queries:
  - `2024 Django developers survey results framework professional use clients agency`
  - `2025 digital agency industry report profitability utilization fixed fee retainer client acquisition Promethean Research`
  - `Django Developers Survey 2025 official results JetBrains agency freelance`
  - `Django consultancy case study agency handover client team open source`
  - `Django survey 2025 using Django at work professional developer percentage`
  - `UK government Digital Data Technology sourcing playbook outcomes agile procurement supplier guidance`
  - `client agency software handover source code ownership maintainability procurement guidance`
  - `digital agency survey 2024 client relationships project based retainer report`
  - `open source software selection criteria enterprise survey support community security 2024 report`
  - `outsourced software development client vendor selection criteria study communication trust competence`
  - `professional services client buying survey consulting firm referrals expertise case studies`
  - `site:blog.jetbrains.com/pycharm 2025 Django Developers Survey results 4600`
  - `site:caktusgroup.com/blog Django agency why Django client project maintainability`
  - `site:docs.djangoproject.com security Django overview vulnerabilities deployment checklist`
  - `site:docs.djangoproject.com/en/5.2/releases/5.2 LTS support April 2028`
  - `site:gov.uk service standard multidisciplinary team supplier digital service`
  - `site:gov.uk spend controls technology choose open source software`
  - `site:gov.uk technology code of practice open source avoid vendor lock-in procurement`
  - `site:gov.uk/government/publications/contracting-for-agile-guidance-note agile contract supplier delivery outcomes 2023`
  - `site:lincolnloop.com case study Django agency long term maintenance client`
  - `site:lincolnloop.com/blog Django agency project architecture client`
  - `site:lp.jetbrains.com/django-developer-survey-2025 results deployment cloud databases team size`
  - `site:revsys.com/tidbits consulting Django client upgrade project`
  - `site:sixfeetup.com/blog Django client project case study maintainability`
  - `site:torchbox.com client Wagtail Django procurement accessibility case study technical decision`
  - `site:torchbox.com/blog Django why we use Django agency client`
  - `site:www.djangoproject.com/download/ supported versions Django LTS security`
  - `site:www.djangoproject.com/foundation/corporate-members membership corporate Django support`
  - `software consultancy framework selection client requirements maintainability case study Django agency`
  - `software framework selection criteria practitioners study community documentation maintainability security web framework`
  - `software outsourcing success factors client vendor communication knowledge transfer empirical study`
  - `survey buyers choose software development agency referrals case studies technical expertise 2024`
- Website domains:
  - `5qgroup.com`
  - `agilemanifesto.org`
  - `artefacts-discovery.researcher.life`
  - `arxiv.org`
  - `assets.applytosupply.digitalmarketplace.service.gov.uk`
  - `assets.publishing.service.gov.uk`
  - `axios.com`
  - `bitkom.org`
  - `blog.jetbrains.com`
  - `caktusgroup.com`
  - `citeseerx.ist.psu.edu`
  - `clickmasterssoftwaredevelopmentcompany.co.uk`
  - `cognitiveconvergence.com`
  - `committees.parliament.uk`
  - `companyname`
  - `comum.rcaap.pt`
  - `cuh.staging.torchbox.com`
  - `digiqt.com`
  - `digital-handbook.cabinetoffice.gov.uk`
  - `digitalcommons.memphis.edu`
  - `digitalmarketplace.service.gov.uk`
  - `diva-portal.org`
  - `djangoproject.com`
  - `docs.djangoproject.com`
  - `docs.italia.it`
  - `doi.org`
  - `en.wikipedia.org`
  - `engineering.fb.com`
  - `engineering.homeoffice.gov.uk`
  - `england.nhs.uk`
  - `forrester.com`
  - `gca.gov.uk`
  - `github.com`
  - `gov.uk`
  - `hackerrank.com`
  - `iadisportal.org`
  - `itpro.com`
  - `jetbrains.com`
  - `khub.net`
  - `kiplinger.com`
  - `koder.ai`
  - `learn.caktusgroup.com`
  - `lincolnloop.com`
  - `link.springer.com`
  - `linuxfoundation.org`
  - `lp.jetbrains.com`
  - `nao.org.uk`
  - `opensourcesurvey.org`
  - `oulurepo.oulu.fi`
  - `perforce.com`
  - `pmc.ncbi.nlm.nih.gov`
  - `promethean-research.com`
  - `prometheanresearch.com`
  - `prweb.com`
  - `pure.tudelft.nl`
  - `reddit.com`
  - `reports.sourceglobalresearch.com`
  - `research.prometheanresearch.com`
  - `researchgate.net`
  - `resources.jetbrains.com`
  - `revsys.com`
  - `romisatriawahono.net`
  - `routiine.io`
  - `scholarworks.gnu.ac.kr`
  - `sciencedirect.com`
  - `security.gov.uk`
  - `sixfeetup.com`
  - `sixfeetup.com.\n\n`
  - `squ.elsevierpure.com`
  - `stepto.net`
  - `surveys.jetbrains.com`
  - `swfconsults.co.uk`
  - `talkthinkdo.com`
  - `tandfonline.com`
  - `tech-radar.justice.gov.uk`
  - `technology.blog.gov.uk`
  - `techradar.com`
  - `thedrum.com`
  - `torchbox.com`
  - `uhra.herts.ac.uk`
  - `virtuoustechlogic.com`
  - `whitehouse.gov`
  - `cite38†agilemanifesto.org`

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
