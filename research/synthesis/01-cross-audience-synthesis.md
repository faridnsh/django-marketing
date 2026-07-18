# Cross-audience synthesis

## Method and confidence

This synthesis treats the 17 supplied reports as lenses, not mutually exclusive market segments. It normalizes their jobs, decision roles, and contexts, then looks for repeated progress patterns and material exceptions. A statement marked **direct pattern** is supported across multiple reports by the evidence those reports cite; it does not imply independent triangulation when reports reuse the same survey, guidance, or incumbent sample. The normalized cross-audience wording remains synthesis inference unless a source directly elicited that wording. A statement marked **synthesis inference** is a cross-report interpretation that still needs primary research. Confidence describes the bounded pattern and must not exceed the diversity, directness, or external validity of its underlying evidence.

The strongest evidence describes current, engaged Django users; general software-selection, education, open-source, and regulatory practice; and a limited set of public adoption, migration, and maintenance episodes. It is much weaker on unaware prospects, serious rejecters, quiet former users, non-English-language participants, and the internal sequence of real decisions. Consequently, this document supports research architecture, not audience priority or causal claims about adoption.

## Audience architecture

The reports become coherent when arranged on seven composable dimensions rather than one persona list.

| Dimension | Categories visible in the reports | What it changes |
|---|---|---|
| Experience/readiness | First programming steps; Python-capable/web-new; web-capable/Django-new; experienced cross-stack; Django incumbent/expert | Prerequisites, mental models, evaluation ability, help needed, and consequence of errors |
| Adoption role | Initiator; researcher/evaluator; recommender; approver/economic buyer; blocker/reviewer; implementer/operator; consequence bearer | Authority, evidence threshold, language of risk, and whose outcome counts |
| Organization/context | Independent; classroom/workshop; startup; product team; agency/client system; multi-team organization; institution | Time horizon, resource scarcity, handoffs, governance, and switching cost |
| Industry/risk overlay | Ordinary data-centric service; regulated/high-assurance; public service; education; healthcare; finance; media; other jurisdictional contexts | Controls, accessibility, resilience, procurement, evidence retention, and harm model |
| Django lifecycle | Unaware; considering; proving; adopting; operating; upgrading/deepening; reconsidering; leaving; former/returning | Trigger, comparison baseline, sunk knowledge, and relevant next decision |
| Ecosystem participation | Consumer; helper; first-time contributor; recurring contributor/reviewer; package maintainer; governance participant | Type of contribution, legitimacy, feedback, authority, and sustainability burden |
| Funding relationship | Beneficiary/non-funder; individual donor; organizational sponsor/member; direct maintainer supporter; employee-time contributor; grant/in-kind supporter | Motivation, approval path, expected accountability, and rights boundaries |

This architecture reconciles several apparent contradictions. “Beginner” can mean no programming model, solid Python with no web model, or an experienced web developer new only to Django; these require different paths and should not be pooled ([first-time programmers](../audiences/01-first-time-programmers.md), [Python developers new to web](../audiences/02-python-developers-new-to-web.md)). “Decision-maker” may be a solo implementer, a technical recommender, a risk veto holder, or a budget approver; title does not settle authority ([technical leads](../audiences/05-technical-leads-software-architects.md), [engineering leaders](../audiences/06-ctos-engineering-managers.md)). “Industry” changes constraints but does not itself explain motivation or role ([industry contexts](../audiences/09-industry-contexts-government-education-media-healthcare-finance.md)). “Former” and “existing” are lifecycle states whose meaning depends on current responsibility and workload ([existing users](../audiences/13-existing-django-users.md), [former users](../audiences/14-former-django-users.md)). **Synthesis inference; High confidence.**

## Shared job clusters

### 1. Create a useful outcome and shorten the learning/delivery loop

**Normalized progress:** When an uncertain need must become observable, I want to produce the smallest understandable, usable result, so I can learn, deliver value, or decide what to do next.

Participants include first-time programmers, Python developers entering web work, full-stack developers, startups, agencies, educators, and institutions. For a first-time programmer the outcome is a mastery experience; for a startup it is validated customer learning under runway constraints; for an agency it is a supportable client outcome; for an educator it is authentic practice that reveals understanding. The shared mechanism is a bounded result plus feedback, not simply speed or “use Django” ([01](../audiences/01-first-time-programmers.md), [02](../audiences/02-python-developers-new-to-web.md), [04](../audiences/04-full-stack-developers.md), [07](../audiences/07-startups-technical-decision-makers.md), [10](../audiences/10-agencies-consultancies.md), [12](../audiences/12-individual-educators-instructors-bootcamp-teachers.md)).

**Evidence strength:** Medium-High direct pattern. **Exception:** high-assurance contexts may rationally accept a slower initial loop to generate reviewable evidence, and package maintainers may need to reduce work rather than ship more.

### 2. Build an accurate mental model and become independently effective

**Normalized progress:** When a system or workflow is unfamiliar, I want to understand cause, boundaries, and failure modes well enough to act and debug independently, so I can make safe progress without permanent reliance on a guide or specialist.

This is central for beginners, Python-to-web entrants, full-stack developers learning another layer, engineers inheriting systems, educators diagnosing misconceptions, and clients receiving a handover. It also appears as governance literacy for contributors and dependency understanding for funders. The content differs—request/response, inherited architecture, assessment validity, contribution process, or funding rights—but the progress is from opaque dependence to informed agency ([01](../audiences/01-first-time-programmers.md), [02](../audiences/02-python-developers-new-to-web.md), [03](../audiences/03-experienced-backend-engineers.md), [10](../audiences/10-agencies-consultancies.md), [15](../audiences/15-prospective-existing-django-contributors.md), [16](../audiences/16-donors-sponsors-corporate-members.md)).

**Evidence strength:** High for the functional need; Medium for emotional and social effects. **Exception:** an approver may need trustworthy delegated evidence, not practitioner-level mastery.

### 3. Make a fit-for-context, defensible commitment

**Normalized progress:** When a consequential choice or review arises, I want evidence against the actual workload, people, controls, costs, and lifecycle, so I can commit, reject, or defer with known trade-offs.

This spans experienced engineers, technical leads, engineering leaders, startups, large organizations, industry contexts, agencies, former users, and curriculum decision-makers. The common evidence is multi-criteria and contextual; there is no supported universal ranking. Practitioners emphasize workload behavior and daily changeability; leaders translate technical evidence into organizational consequences; reviewers test controls; former users diagnose whether prior pain still applies; institutions add learning outcomes and delivery economics ([03](../audiences/03-experienced-backend-engineers.md), [05](../audiences/05-technical-leads-software-architects.md), [06](../audiences/06-ctos-engineering-managers.md), [08](../audiences/08-large-organizations-stakeholders.md), [14](../audiences/14-former-django-users.md), [17](../audiences/17-educational-institutions-training-curriculum-decision-makers.md)).

**Evidence strength:** High as a general selection job; Medium for Django-specific weighting. **Exception:** learners in assigned curricula and delivery developers in standardized environments may not choose the foundation at all; their decision is whether and how to persist or request an exception.

### 4. Ship, operate, recover, and change safely

**Normalized progress:** When software becomes consequential, I want reproducible delivery, observable behavior, controlled change, and recovery paths, so failures are bounded and users are protected.

This cluster joins full-stack delivery, backend engineering, incumbent use, agency handover, organizational assurance, and regulated continuity. Beginners encounter its first cliff at deployment, but should not be assigned enterprise operating jobs. Reliability and security are legitimate constraints; their acceptable evidence and cost vary enormously by service consequence ([02](../audiences/02-python-developers-new-to-web.md), [04](../audiences/04-full-stack-developers.md), [08](../audiences/08-large-organizations-stakeholders.md), [09](../audiences/09-industry-contexts-government-education-media-healthcare-finance.md), [10](../audiences/10-agencies-consultancies.md), [13](../audiences/13-existing-django-users.md)).

**Evidence strength:** High for the job; Low-Medium for typical Django-specific friction and relative weighting. **Exception:** prototypes with no users or sensitive data can use proportionate assurance rather than production-grade process.

### 5. Preserve changeability, supportability, and a bounded exit

**Normalized progress:** When requirements, dependencies, teams, or personal capacity change, I want an affordable path to upgrade, adapt, transfer, contain, migrate, or stop, so today’s commitment does not become an unsafe indefinite obligation.

This connects full-stack developers, architects, leaders, startups, organizations, agencies, existing/former users, maintainers, educators, and institutions. Apparent conflict between “integrated conventions accelerate work” and “integration creates lock-in” is resolved by context: integration can reduce coordination now while increasing coupled change later. The relevant question is whether ownership, boundaries, upgrade cadence, and exit costs fit the expected life—not whether integration is categorically good or bad ([04](../audiences/04-full-stack-developers.md), [05](../audiences/05-technical-leads-software-architects.md), [07](../audiences/07-startups-technical-decision-makers.md), [11](../audiences/11-django-python-package-maintainers.md), [13](../audiences/13-existing-django-users.md), [14](../audiences/14-former-django-users.md)).

**Evidence strength:** Medium-High direct pattern; causal estimates of upgrade and migration cost are weak. **Exception:** a maintainer’s legitimate exit may be archive/deprecation, while an operator’s exit must preserve service and data continuity.

### 6. Sustain human capability and distribute ownership

**Normalized progress:** When valuable work depends on scarce people, I want knowledge, authority, and capacity distributed appropriately, so delivery or stewardship does not fail when one person leaves or cannot continue.

Leaders frame this as hiring, onboarding, autonomy, and key-person risk; agencies as knowledge transfer; educators as teachable, repeatable delivery; contributors and maintainers as timely feedback, trust, co-maintainers, and succession; funders as converting dependence into capacity. These jobs are structurally related but not interchangeable: paying a maintainer, training a team, recruiting a contributor, and approving a curriculum solve different bottlenecks ([06](../audiences/06-ctos-engineering-managers.md), [10](../audiences/10-agencies-consultancies.md), [11](../audiences/11-django-python-package-maintainers.md), [12](../audiences/12-individual-educators-instructors-bootcamp-teachers.md), [15](../audiences/15-prospective-existing-django-contributors.md), [16](../audiences/16-donors-sponsors-corporate-members.md)).

**Evidence strength:** Medium-High; weakest at quantifying which intervention relieves which bottleneck. **Exception:** adding newcomers can initially increase review burden, and nominal teams can retain a single release or security owner.

### 7. Establish trust, legitimacy, and accountable influence

**Normalized progress:** When other people bear consequences or must cooperate, I want evidence, roles, and decisions to be legible, so they can trust the work and grant only the authority warranted.

Practitioners want a defensible recommendation; agencies need multi-party trust; large organizations need shared decision records; educators and institutions need assessment/credential credibility; contributors need legitimate participation; funders need accountability without purchasing technical control. Recognition appears across learners, maintainers, contributors, institutions, and sponsors, but it is not uniformly desired and is often only hypothesized ([03](../audiences/03-experienced-backend-engineers.md), [08](../audiences/08-large-organizations-stakeholders.md), [12](../audiences/12-individual-educators-instructors-bootcamp-teachers.md), [15](../audiences/15-prospective-existing-django-contributors.md), [16](../audiences/16-donors-sponsors-corporate-members.md), [17](../audiences/17-educational-institutions-training-curriculum-decision-makers.md)).

**Evidence strength:** Medium for functional trust/accountability; Low-Medium for reputation, belonging, status, or identity effects. **Exception:** anonymous donors may avoid recognition; technical legitimacy does not imply governance authority; sponsorship must not imply roadmap control.

## Audience-specific jobs that distinguish a lens

| Lens | Distinguishing job, beyond shared clusters | Confidence |
|---|---|---|
| First-time programmer | Test whether programming is for me through a mastery experience I can explain and modify | Medium-High |
| Python developer new to web | Translate existing Python competence into a transferable browser/server/deployment model | High functional, Medium wording |
| Experienced backend engineer | Resolve representative workload and architecture-fit uncertainty | High |
| Full-stack developer | Reduce cross-layer seams while retaining end-to-end control | Medium-High |
| Technical lead/architect | Establish an enabling default and proportionate exception path across teams | Medium-High |
| Engineering leader | Translate a foundation choice into business, staffing, ownership, and residual-risk commitments | High inference |
| Startup technical actor | Maximize validated learning per unit of runway while preserving stage-fit reversibility | High functional |
| Large-organization stakeholder | Turn a technical option into an organizationally approvable and operable service decision | High functional |
| Industry/risk context | Protect the particular affected population and statutory/institutional duty; this is an overlay, not one audience | High structural |
| Agency/consultancy | Make uncertainty commercially governable and transfer operational ownership deliberately | High functional |
| Package maintainer | Sustain an honest support contract within available human capacity, including safe handoff or closure | High |
| Individual educator | Observe learner understanding and intervene within cohort/time constraints | High |
| Existing Django user | Make the next production change while keeping the dependency stack supportable | High |
| Former Django user | Diagnose the actual cause of departure and reassess it against today’s context | High inference, weak prevalence |
| Contributor | Convert intent into an accepted contribution with legitimate feedback and bounded commitment | Medium-High |
| Donor/sponsor/member | Convert appreciation or dependence into accountable resources without buying technical control | High functional |
| Institution/curriculum decision-maker | Balance learning outcomes, demand, delivery capacity, governance, and program economics | High functional |

## Overlap, duplication, and reconciliation

- **Merge conceptually, retain as recruitment variants:** reports 03, 05, 06, 08, and part of 09 share the consequential technology-decision job. Keep their role and context differences in sampling; do not maintain five disconnected “decision-maker personas.”
- **Split:** “CTOs and engineering managers” must become hands-on early technical leader, growth/multi-team approver, and manager/recommender-steward. Their authority and consequences differ ([06](../audiences/06-ctos-engineering-managers.md)).
- **Rename:** “first-time programmers” to “people seeking a first programming mastery experience”; “Python developers new to web” to “Python-capable, web-system-new builders”; “existing users” to “people responsible for changing or operating an existing Django system.” These names encode progress/readiness rather than identity.
- **Treat as context:** startups, large organizations, the five industries, and former-Django status. Each changes constraints or priors, but does not supply a stable role by itself.
- **Keep distinct but link:** individual educator and institution/curriculum decision-maker; learner and educator; contributor and package maintainer; technical reliance and funding. They influence one another but have different success criteria and authority.
- **Do not merge full-stack and experienced backend developers:** responsibility span and front/back-end seams distinguish the former; workload/architecture depth distinguishes the latter, though one person may occupy both.

**Synthesis inference; High confidence in the dimensional correction, Medium in the exact labels.**

## Apparent contradictions reconciled

| Apparent contradiction | Reconciliation | Confidence |
|---|---|---|
| Django can enable a first web success / Django assumes prior Python and web concepts | A coached end-to-end experience can temporarily supply setup, sequencing, and debugging support; that is not evidence that an unsupported R0 learner has the mental model to work independently | High boundary, Medium transition |
| Integrated capabilities accelerate delivery / an integrated framework can feel complex or constraining | Built-ins reduce component selection and seams for fitting work, while increasing initial vocabulary and coupled behavior; readiness and workload determine the net effect | Medium-High |
| Startups prioritize speed / high-assurance organizations prioritize governance | Both seek the smallest sufficient evidence for their consequence and uncertainty. The acceptable assurance threshold, reversibility, and people involved differ; neither context rationally seeks speed or process in isolation | High synthesis inference |
| Technical experts choose the stack / executives are “decision-makers” | Experts often evaluate and recommend; leaders accept resources and residual risk; reviewers can veto. In solo settings roles collapse, while in larger settings no one title represents the decision | High |
| Mature Django reduces lifecycle risk / mature Django is perceived as stale | The first is a functional inference from release, security, governance, and installed practice; the second is a weakly evidenced social/career perception. They can coexist for different people and should not be averaged into one sentiment | Medium |
| Existing users may become contributors / most users primarily need to operate software | Contribution is an optional lifecycle branch, not the expected next step or proof of deeper user value. Stated willingness and event attendance are not observed participation | High |
| Organizational dependence creates a reason to fund / most dependent organizations do not visibly fund | Dependence can create the underlying stewardship job, but action also requires a champion, fundable target, budget/legal route, and acceptable accountability. Use is not funding intent | Medium |
| Recognition motivates contributors, maintainers, and sponsors / some participants avoid visibility | Recognition is context-dependent and can be a pull, an obligation, or a deterrent. Anonymous giving, bounded contribution, and quiet maintenance are legitimate paths | Medium |
| A former user left because Django did not fit / departure accounts show successful replacements | Framework, architecture, product, employer, staffing, and scope often change together. Departure proves a transition occurred, not that Django alone caused it or that return is preferable | High causal caution |

Claims from the supplied analysis that a “marketing executive” normally approves framework standards, or that homepage/social/video exposure drives early-career progression, remain unsubstantiated. The reports support technical, service-owner, leadership, finance/procurement, educator, and peer influence in context; they do not establish those proposed roles or channels as general causal paths. **Direct cross-report audit; High confidence in the evidence limitation.**

## Journey and lifecycle transition hypotheses

### Evidenced transitions

- Coached beginners can complete and deploy a first web artifact; this does not establish independent competence or continued use ([01](../audiences/01-first-time-programmers.md)).
- Existing users repeatedly upgrade, operate, and deepen expertise; some move into contribution, but stated willingness or attendance is not observed contribution ([13](../audiences/13-existing-django-users.md)).
- Contributors can move from bounded tasks to review, mentoring, formal teams, voting, and governance; programs provide evidence of this path but have selection effects ([15](../audiences/15-prospective-existing-django-contributors.md)).
- Maintainers may recruit co-maintainers, transfer governance, narrow support, or archive; these are observed mechanisms, not a single linear maturity ladder ([11](../audiences/11-django-python-package-maintainers.md)).
- Organizations may evolve from greenfield adoption to installed-estate stewardship and later choose upgrade, containment, decomposition, or migration ([05](../audiences/05-technical-leads-software-architects.md), [14](../audiences/14-former-django-users.md)).

### Hypothesized transitions requiring research

- First mastery experience → Python/web learner → independent builder. The transition likely depends more on explanation, debugging, and support than artifact completion alone. **Low-Medium confidence.**
- Evaluator → adopter → operator. A representative proof and an explicit ownership handoff may be the critical bridge. **Medium confidence.**
- Practitioner concern → leader decision → reviewer approval. Evidence is likely translated and compressed at each handoff, creating attribution errors. **Medium confidence.**
- Existing user → helper/contributor → maintainer/governance participant. Timely feedback, tractable scope, relationships, paid time, and legitimacy may matter at different stages; the path is not inevitable or always desirable. **Medium confidence.**
- Organizational dependence → employee contribution or funding. Dependence alone is insufficient; an internal champion, budget fit, legal route, and accountable outcome may mediate action. **Medium confidence.**
- Former user → returner. Return is likely triggered by a newly fitting workload plus retained familiarity, not persuasion in isolation. **Low-Medium confidence due to public-anecdote bias.**

## Decision-system map

```text
Affected users / learners / clients
       | needs, outcomes, harm, acceptance
       v
Practitioners and operators <----> educators / peers / maintainers
       | feasibility, proof, daily friction       | skills, support, ecosystem capacity
       v                                           v
Evaluators / technical leads ---- recommendation and evidence ----+
       |                                                          |
       v                                                          |
Leaders / service owners / economic approvers                     |
       | budget, ownership, residual risk                          |
       v                                                          |
Security / privacy / legal / procurement / assurance reviewers ---+
       | conditions, vetoes, evidence requirements
       v
Adoption, exception, delay, buy, migration, or no-build decision
       |
       v
Production outcomes, maintenance load, learning, and dependence
       |                              |
       +--> contributors/maintainers -+--> funders / employee-time sponsors
                    capacity, continuity, accountability
```

In solo projects several boxes collapse into one person. In institutions and regulated organizations they separate and may conflict. Practitioners supply feasibility evidence but may underweight procurement or continuity; reviewers can veto without bearing daily implementation cost; leaders approve resources but often rely on translated evidence; educators shape the future practitioner pool; maintainers create ecosystem continuity but cannot infer organizational willingness to fund; funders can add capacity but should not receive technical authority by default. **Synthesis inference; Medium-High confidence.**

## Evidence gaps and primary-research implications

The evidence base has six systemic weaknesses: incumbent/survivorship bias; self-selection through Django and technology channels; English-language and Europe/North America concentration; weak role attribution; public success/postmortem selection; and weak causal or longitudinal evidence. Channel evidence usually shows reported use, not what moved a person from discovery to evaluation, approval, adoption, retention, contribution, or funding.

Primary research should therefore begin with recent decision episodes, not attitudes. Sample matched adopters, serious rejecters, no-build/buy decisions, quiet former users, and retained incumbents across authority, lifecycle, and risk contexts. Reconstruct who initiated, supplied evidence, vetoed, approved, used, and bore consequences; capture artifacts such as decision records, proof criteria, review requests, upgrade plans, course proposals, contribution threads, and funding proposals. Separately observe beginner and contributor attempts because retrospective interviews underreport setup, vocabulary, and feedback failures. Details and sequencing appear in [the primary-research plan](05-primary-research-plan.md); gaps are audited in [the evidence-gaps matrix](04-evidence-gaps.md).
