# Django and Python package maintainers

## Audience definition and boundaries

This audience comprises people with continuing responsibility for reusable Python distributions: scope, reviews, supported versions, releases, security, access, and succession. The most Django-relevant members maintain third-party applications, backends, integrations, or tools coupled to Django. A wider Python-package maintainer belongs here only when Django compatibility, Django users, or shared packaging infrastructure creates a real decision context.

This is not synonymous with “Django core contributor.” Package maintainers govern independent projects with their own policies and authority. It also excludes one-time contributors, application teams merely consuming dependencies, PyPI/Warehouse maintainers, and Linux-distribution packagers, though people can move among these roles.

The Django/Python distinction is material:

- **Django-package maintainers** face a two-dimensional compatibility job across Django and Python releases, plus Django-specific deprecations, security coordination, and expectations from downstream web applications. Django's own release notes explicitly call out backwards-incompatible changes and changes needed by third-party database backends ([Django 5.2 release notes, Django Software Foundation, April 2, 2025](https://docs.djangoproject.com/en/dev/releases/5.2/)).
- **Wider Python-package maintainers** face publishing, compatibility, dependency, security, and capacity work but may have no reason to engage with Django. Jazzband's 2026 wind-down points Django projects toward Django Commons while identifying no equivalent for its non-Django projects ([“Sunsetting Jazzband,” Jannis Leidel/Jazzband, March 14, 2026](https://jazzband.co/news/2026/03/14/sunsetting-jazzband)).

The audience is therefore better described as a **maintenance context with concentric relevance**, not one homogeneous persona. **Direct evidence for the different institutional paths; High confidence.** The relative size and needs of each circle have not been measured.

## Important subsegments

- **Solo volunteer maintainers:** authority is simple but time, review, release, security, and succession all concentrate in one person. In Tidelift's self-selected 2023 survey, 44% reported no co-maintainer; this supports the importance of the segment, not a Python- or Django-specific population estimate ([Tidelift report, April 2023](https://tidelift.com/open-source-maintainer-survey-2023)).
- **Small volunteer teams:** responsibility is shared, but access, decisions, and handover may remain informal.
- **Paid and partly paid maintainers:** employer time, consulting, sponsorship, grants, or services shape capacity and obligations. Tidelift found 60% self-described as unpaid hobbyists, 23% semi-professional, and 13% professional among 326 respondents; 77% of unpaid respondents would prefer payment ([April 2023](https://tidelift.com/open-source-maintainer-survey-2023)). **Direct survey evidence; Medium confidence due to self-selection.**
- **Django-extension and reusable-app maintainers:** compatibility with supported Django/Python combinations and visibility among Django users are recurring concerns.
- **Foundational Python-library and tooling maintainers:** their packages may be depended on by Django projects without importing Django. Django is a downstream context, not their governing community.
- **Community-hosted projects:** organizations such as Django Commons provide shared administration, access redundancy, security backup, and transfer processes, but routine maintenance remains the project's responsibility ([governance, accessed July 18, 2026](https://django-commons.org/governance/)).
- **Mature/high-impact versus niche/experimental packages:** popularity can increase issue, compatibility, assurance, and user-support demands, but download counts do not directly measure maintenance burden or criticality.
- **Active, caretaker, and exiting maintainers:** growth, stable care, succession, and archival imply different outcomes.

## Primary job to be done

> **When** people and projects depend on a package I am responsible for, **I want to** keep its compatibility, releases, security, decisions, and human ownership trustworthy within the capacity actually available, **so I can** preserve useful software without making maintenance an indefinite, unsafe personal obligation.

Job hierarchy:

- **Core functional job:** sustain a dependable package and an honest support contract over time.
- **Supporting jobs:** set supported versions; triage, test, review, publish, and document; coordinate vulnerabilities; distribute authority; obtain capacity; and hand over or archive cleanly.
- **Emotional job (partly evidenced):** retain agency, enjoyment, and pride while reducing stress, isolation, guilt, and feeling trapped by having created the project. Tidelift directly measured stress, loneliness, and feeling stuck; the desired emotional state is an inference. **Mixed direct evidence and inference; Medium confidence.**
- **Social job (partly evidenced):** be recognized as a responsible steward and community peer. Tidelift measured recognition; Linux Foundation interviews found belonging and career value. **Direct evidence; Medium confidence, not Django-specific.**

## Additional jobs to be done

1. > **When** Django, Python, or a key dependency changes, **I want to** determine and communicate which combinations my package supports, **so I can** ship compatibility without carrying an unbounded test matrix.
   - **Core functional:** make an explicit version-support decision.
   - **Supporting:** inspect deprecations, test chosen combinations, update metadata, and document breakage.
   - **Emotional hypothesis:** feel permitted to set a boundary rather than satisfy every legacy installation.
   - **Social:** give users a legible contract. A Django Forum maintainer's Python-EOL question demonstrates the decision and lack of consensus ([September 20, 2024](https://forum.djangoproject.com/t/advice-on-python-versions-to-support-for-third-party-packages/34948)). **Direct signal; High confidence in the job, Low in resolutions.**

2. > **When** issues, pull requests, security requirements, and user requests exceed my attention, **I want to** prioritize and automate the work that protects users and project health, **so I can** spend scarce effort where it has the greatest consequence.
   - **Core functional:** turn an open-ended queue into bounded maintenance.
   - **Supporting:** contribution rules, automation, trusted publishing, release checks, security contacts, and non-goals.
   - **Emotional:** reduce overload and unwanted urgency.
   - **Social hypothesis:** decline requests without appearing careless. OpenSSF found demand for best practices and fatigue-reducing automation; Tidelift found 38% disliked requirements they lacked time for. **Direct evidence for burden; Medium confidence.**

3. > **When** the project depends too heavily on me, **I want to** recruit, trust, and retain capable collaborators or transfer it to sound governance, **so I can** remove the single-person failure mode and step back safely when life changes.
   - **Core functional:** replenish maintenance labor and distribute authority.
   - **Supporting:** scoped contributor pathway, access tiers, documentation, check-ins, and succession plan.
   - **Emotional:** be able to take a break without guilt.
   - **Social:** share stewardship safely. Django Commons normalizes stepping back, and its tiered admin model provides a path to trusted PyPI access ([homepage](https://django-commons.org/); [April 21, 2026](https://django-commons.org/blog/2026/04/21/please-welcome-our-new-admins/)). **Direct mechanism; High confidence for hosted projects.**

4. > **When** my package is materially relied upon, **I want to** obtain recognition, funded time, or practical support proportional to the maintenance expected, **so I can** continue necessary work rather than subsidize growing obligations indefinitely.
   - **Core functional:** convert downstream dependence into sustainable capacity.
   - **Supporting:** impact evidence, defined work, employer/sponsor approval, reporting, and non-financial help.
   - **Emotional:** feel the work is valued rather than taken for granted.
   - **Social hypothesis:** show impact without equating popularity with availability. Tidelift found 57% said more income could help them continue, while 64% selected experienced-maintainer help ([April 2023](https://tidelift.com/open-source-maintainer-survey-2023)). **Direct survey evidence; Medium confidence.**

5. > **When** I can no longer responsibly maintain the package, **I want to** hand it over, narrow its promise, deprecate it, or archive it transparently, **so I can** protect users and leave without concealing continuity risk.
   - **Core functional:** end or change the maintenance contract safely.
   - **Supporting:** find a successor/host, rotate access, mark status, document migration, and preserve history.
   - **Emotional:** regain agency and avoid shame around stopping.
   - **Social:** respect users and package-name trust. Jazzband's wind-down and Django Commons' transfer processes demonstrate this job. **Direct case/process evidence; High confidence in existence, Low in prevalence.**

## Functional, emotional, and social dimensions

**Functional (evidenced):** compatibility, triage, publishing, vulnerability response, releases, onboarding, access, funding, and succession. Tidelift found 14% reported succession plans and 63% release/upgrade notes; this shows uneven practice, not ecosystem quality. **Direct evidence; Medium confidence.**

**Emotional (partly evidenced):** meaning and creativity pull maintainers in; stress, loneliness, obligation, and burnout push them out. Tidelift measured all of these; a 2024 interview study frames labor as depletable and highlights work-life balance ([Linåker, Link, and Lumbard, August 13, 2024](https://arxiv.org/abs/2408.06723)). **Direct evidence; Medium across OSS, Low-to-Medium for Django.**

**Social (partly evidenced):** maintainers seek belonging, recognition, career value, and legitimate authority while gatekeeping and mentoring. Linux Foundation interviews found community satisfaction and career benefits but insufficient employer recognition ([August 10, 2023](https://www.linuxfoundation.org/blog/lessons-from-maintainers-of-the-worlds-most-critical-software)). **Direct broad-OSS evidence; Medium confidence.**

## Triggering situations

**Recurring triggers:** releases, queues, dependency/version review, vulnerability alerts, access review, sponsor reporting, onboarding, and health checks.

**Event-triggered triggers:** breaking releases, security reports, blocked users, submission spikes, employer/life changes, co-maintainer departure, lost funding/interest, transfer, or archival.

Established-contributor research found occupational transitions were the most commonly cited disengagement reason and modeled a job transition as associated with 2.48 times the disengagement hazard; respondents also cited lack of time and personal circumstances. This study used 151 survey responses and observational modeling, so it supports life transitions as a trigger, not individual prediction ([Miller et al., “Why do People Give Up FLOSSing?”, 2019](https://www.cs.cmu.edu/~./ckaestne/pdf/oss19.pdf)). **Direct evidence; Medium confidence.**

## Desired outcomes

- Supported Django/Python/platform combinations are explicit, tested, and visible; unexpected compatibility failures trend downward.
- Time from a supported upstream release to a compatible package release is predictable enough for the project's stated promise; no universal target is evidenced.
- Security reports have a private route, named backup, and response/escalation path; publishing no longer relies on unnecessary long-lived secrets.
- Review load stays within chosen bounds, and releases, upgrades, licensing, contribution, and governance do not depend on private knowledge.
- At least two appropriately trusted people or a documented host can perform critical release/access actions where the project's risk warrants it; this is a directional resilience outcome, not an evidence-backed universal minimum.
- Maintainers can pause or exit without silent abandonment; projects have a transfer, deprecation, or archive route.
- Effort matches the support promise; stress and unwanted work trend down while meaningful work and contributor progression remain possible.

These are synthesized from survey, interview, governance, and process evidence. **Mostly inference; Medium-to-High confidence.** No Django-specific benchmarks were found.

## Current behaviour or status quo

Maintainers commonly work from an issue/PR queue, test a chosen matrix in CI, publish to PyPI, and communicate through metadata, documentation, and release notes. These artifacts become a de facto support contract. Django Packages' Readiness view compares compatibility across Django, Python, and Wagtail versions ([accessed July 18, 2026](https://djangopackages.org/readiness/)).

Version policy is decentralized. Django documents its supported Python versions and backwards-incompatible changes, but third-party maintainers decide how much of that matrix they will carry. The 2024 Django Forum thread shows a maintainer seeking “generally accepted wisdom” about whether to retain an EOL Python version that a supported Django LTS still runs on; replies emphasize that the choice remains the maintainer's. **Direct qualitative evidence; High confidence in decentralization, Low confidence in common policy choices.**

PyPI recommends Trusted Publishers, replacing long-lived release credentials with short-lived OIDC tokens, and treats role, deletion, token, and 2FA changes as sensitive ([April 20, 2023](https://blog.pypi.org/posts/2023-04-20-introducing-trusted-publishers/); [PyPI Help, accessed July 18, 2026](https://pypi.org/help/)). Tidelift found paid maintainers more likely than unpaid maintainers to implement every tested security and maintenance practice. **Direct evidence; Medium confidence due to survey selection.**

When ownership becomes untenable, maintainers may add collaborators, transfer, narrow support, or stop. Django Commons supplies administration and security backup but not routine maintenance; Jazzband shows a shared organization can reproduce key-person risk. **Direct case evidence; High confidence about these organizations, Low generalizability.**

## Pushes

- More Django/Python/platform combinations than available CI and review time can cover; deprecations and EOLs can block downstream upgrades.
- Security reports, supply-chain expectations, 2FA/publishing changes, and compliance requests added to unpaid work.
- Growing queues, demanding users, narrowly self-interested changes, and low-quality or automated submissions.
- A solo-maintainer or solo-admin bottleneck around release credentials, permissions, review, and decisions.
- Work and life priorities, employer redeployment, loss of interest, financial pressure, conflict, stress, loneliness, and burnout.
- Unclear governance or a contribution path that makes willing help expensive to absorb.

Tidelift found 58% had quit or considered quitting a project; among that group, life/work priorities (54%), lost interest (51%), and burnout (44%) were the most selected reasons. The survey recruited from Tidelift email lists and social media and analyzed 339 maintainers, so it should not be read as a representative rate for PyPI or Django. **Direct evidence; Medium confidence for the pattern, Low for ecosystem prevalence.**

## Pulls

- Solving a personally or professionally needed problem through meaningful, creative work and learning.
- Positive impact, community belonging, peer relationships, recognition, and career value.
- Competent co-maintainers who share obligation and allow specialization in enjoyable work.
- Automation and clear process that reduce repetitive overhead.
- Employer time, sponsorship, grants, or compensation tied to defined maintenance outcomes.
- Django-specific shared governance that provides administrative redundancy without automatically taking away project-level stewardship.

Broad maintainer research supports the first four pulls; Django-specific pull has not been measured. **Direct broad-OSS evidence plus inference; Medium confidence.**

## Anxieties

- “If I say I support a Django LTS, am I implicitly promising every Python version it ever supported?”
- “Will a new release break downstream applications or expose users to a supply-chain incident?”
- “Can I trust a new collaborator with merge or PyPI authority?”
- “Will collaborators or funding reduce the load, or create more review, coordination, and customer-like expectations?”
- “Can I transfer or step back without violating community trust or harming users?”
- “Will security standards impose work I cannot understand, fund, or complete?”

These anxieties are synthesized from measured burden, governance cases, and maintainer interviews; they were not asked verbatim of Django maintainers. **Inference; Medium confidence for mechanisms, Low-to-Medium for wording/prevalence.**

## Habits and inertia

Repositories, CI workflows, build backends, release scripts, PyPI ownership, changelog conventions, support matrices, communication norms, and personal expertise are accumulated operating systems. Changing them consumes the same scarce maintenance capacity the change is meant to save. A long-lived API or broad support promise also creates user expectations and compatibility inertia.

Identity compounds inertia: a creator may feel uniquely responsible, while users route every question to the person whose name is historically attached. Tidelift directly included “feel like I'm stuck maintaining something simply because I created it” among reported dislikes. **Direct evidence that the feeling exists; Medium confidence; prevalence is not clearly extractable from the report text.**

Governance inertia can be legitimate. PyPI release authority and security response require earned trust; immediate open access can be unsafe. Jazzband's 2026 account says open membership and shared push access became untenable amid low-quality automated submissions, while Django Commons separates ordinary admin from higher-trust PyPI and sensitive controls. **Direct case evidence; High confidence about the trade-off, not a universal governance prescription.**

## Decision criteria

No evidence supports a universal ranking. Importance below describes likely decision weight for the stated maintenance job; “Critical” means a potential gate, not first place.

| Criterion | Importance | Confidence | Evidence or question |
|---|---|---:|---|
| Compatibility and support-boundary clarity | Critical for Django-coupled packages | High | Which Django/Python/platform combinations are promised, tested, and encoded in package metadata? |
| Security response and release integrity | Critical for depended-on packages | High | Private reporting, backup contact, 2FA, trusted publishing, dependency response, and recovery path |
| Available maintainer capacity | Critical | High | Paid/volunteer time, queue size, release work, life/employer constraints, realistic support promise |
| Co-maintainer and succession resilience | High; Critical for high-impact packages | High | Trusted collaborators, access redundancy, documentation, transfer/archive path |
| Governance and control fit | High when joining/transferring | High | Decision rights, administrator duties, maintainer autonomy, security intervention, exit process |
| Automation and operational overhead | High | Medium-to-High | CI matrix cost, release automation, repetitive triage, credential burden, false-positive/noise rate |
| Contributor pathway and mentoring cost | High when growth is a goal | Medium | Bounded tasks, contribution guide, review capacity, mentorship, recognition, progression to trust |
| Funding/support fit | High where labor is under-resourced | Medium | Source, duration, conditions, reporting, user expectations, ability to fund necessary rather than only novel work |
| Meaning, interest, recognition, and community | High for retention | Medium | Whether the work remains valuable and enjoyable and whether invisible labor is acknowledged |
| User impact and downstream criticality | Variable to Critical | Medium | Actual dependents, consequences of failure, security exposure, not downloads alone |
| Django-community relevance | Critical for whether Django should engage | High | Direct Django integration/users versus a general Python dependency with no Django-specific job |

The set is directly supported by maintainer surveys, interviews, Django/Python release processes, and the Jazzband/Django Commons cases. Weighting remains project-specific. **Direct synthesis; High confidence in the set, Low confidence in universal weights.**

## Main concerns

**Practical concerns:** compatibility, testing, releases, security, triage, documentation, packaging, access, contributor review, funding, and handover.

**Legitimate limitations:** Django cannot staff or govern every independent package. A host distributes administration but cannot create unlimited labor; contributors initially add review cost; broad compatibility and funding both carry overhead. **Directly supported mechanisms; High confidence.**

**Perceived risks:** shared governance will take control; accepting a co-maintainer creates supply-chain risk; dropping old versions will alienate users; accepting funding converts a hobby into customer support; admitting a pause will damage reputation.

**Misconceptions:** publishing code creates a permanent duty; downloads prove adequate resources; “community maintained” means someone else owns routine maintenance; every supported Django/Python combination must be supported by every package; a contribution automatically reduces maintainer load; recognition alone resolves burnout.

**Organizational objections:** employers may not fund non-product work; legal/security may limit contribution or release access; sponsors and hosts may impose deliverable or governance conditions; downstream companies may request assurance without allocating time.

**Emotional resistance (partly evidenced):** reluctance to relinquish control, guilt about saying no or stopping, fear of unsafe delegation, resentment at entitlement, and exhaustion with administrative rather than creative work. Broad evidence supports stress and unwanted obligation, but Django-specific emotional research is missing. **Mixed evidence and inference; Medium confidence.**

## Objections and perceived risks

- **“Package maintainers mainly want recognition and influence.”** Incomplete. Recognition, meaningful work, learning, community, career value, money, experienced help, and work-life fit all appear in evidence. Governance influence was not shown to be a universal primary job.
- **“Just add more contributors.”** Misleading. Onboarding, review, mentoring, trust, and retention require labor. A 2024 systematic review of 39 OSS mentoring studies found social, process, and technical challenges, alongside sustainability benefits ([Balali et al., July 2024](https://www.sciencedirect.com/science/article/abs/pii/S0950584924000752)).
- **“Transfer the package to a community organization and the burden disappears.”** Contradicted by Django Commons' scope: maintainers retain routine project responsibility. Jazzband shows the host layer can itself become a bottleneck.
- **“Payment solves burnout.”** Partially supported but too simple. More income was a leading requested support, while experienced maintainer help was selected even more broadly in Tidelift's survey; interest, life changes, conflict, and user demands also matter.
- **“Volunteer means the maintainer does not want payment.”** Contradicted within Tidelift's sample: 77% of unpaid maintainers said they would prefer payment. Generalization beyond the recruited sample remains uncertain.
- **“Django's support policy dictates a third-party package's policy.”** Contradicted. It supplies upstream facts and constraints; independent maintainers still choose their contract.
- **“A popular package is safe to highlight if it works today.”** Risky. Compatibility, security response, governance, and succession are separate from popularity. Django-specific evidence does not provide a validated universal endorsement rule.
- **“Wider Python maintainers are a Django community audience.”** Usually unsupported unless they have Django-specific users, compatibility work, dependencies, or community ties. Treating all PyPI maintainers as one addressable audience would misclassify their job.

## Information needed to make progress

Maintainers need information that changes a decision or removes work:

- Exact Django and Python support timelines, deprecations, backwards-incompatible changes, and third-party API implications.
- A compatibility view separating “tested,” “declared,” “known broken,” and “unknown,” plus reproducible CI for a bounded matrix.
- Private security-reporting and coordination routes, including when a popular third-party vulnerability should involve Django's security team. Django policy says such reports should come from package maintainers ([Django security policies, accessed July 18, 2026](https://docs.djangoproject.com/en/5.2/internals/security/)).
- Release-integrity guidance and concrete governance terms: ownership, publishing, intervention, decisions, and exit.
- Honest estimates of non-coding work and paths to experienced co-maintainers, funding, or employer time.
- Succession, pause, deprecation, and archive practices, plus defensible impact evidence for approvers.

**Direct synthesis from observed decisions and process sources; High confidence.** The best delivery and level of detail remain untested with Django maintainers.

## Trusted content formats

- **Versioned release notes and deprecation timelines:** trusted for upstream facts because maintainers can map a concrete API change to tests and code.
- **Executable compatibility matrices and minimal test repositories:** trusted for evaluation because results are reproducible across selected Django/Python combinations.
- **Checklists and reference workflows:** useful for recurring release, security, transfer, and archive work when linked to authoritative detail.
- **Governance documents and transfer playbooks:** trusted for high-consequence access and succession decisions because roles, intervention powers, and exit terms are inspectable.
- **Security advisories and incident postmortems:** useful for urgent action and for validating how a project or host responds under pressure.
- **Maintainer retrospectives and transparent studies:** explain mechanisms and validate patterns when methods and limitations are visible; neither makes a single case representative.
- **Bounded live working sessions or sprints:** useful when trust and tacit project knowledge must transfer; not a scalable substitute for durable documentation.

The 32-maintainer Linux Foundation study reported unanimous emphasis on better documentation and recommended streamlined contribution processes; the mentoring review describes code review itself as informal mentoring. **Direct broad-OSS evidence; Medium confidence.** No source ranks formats specifically for Django-package maintainers.

## Discovery, evaluation, validation, and engagement channels

- **Discovery:** release announcements, directories, talks, peers, Forum discussions, and social alerts can surface a change, project needing help, or host; they are not sufficient decision evidence.
- **Evaluation:** official documentation, metadata, release notes, governance, and transfer terms establish whether a policy or host fits; the Forum supports peer interpretation.
- **Validation:** the package's GitHub/GitLab repository, issue and PR history, CI results, TestPyPI/PyPI releases, security workflow, and compatibility directories validate claims through inspectable behavior. GitHub is also a stress-bearing work queue: research identifies toxic issue discussions as particularly stressful to maintainers ([Raman et al., ICSE-NIER, May 2020](https://www.cs.cmu.edu/~ckaestne/pdf/icsenier20.pdf)).
- **Ongoing engagement:** issue/PR review, check-ins, community discussion, host meetings, conferences, and sprints maintain relationships and transfer tacit knowledge.

**Claimed-channel caveat:** docs/release notes, GitHub/issue trackers, Forum, conferences/sprints, and professional peers have a defensible behavioral role. This research found insufficient evidence that Discord, mailing lists, podcasts, or short-form social are consistently important specifically to package-maintenance decisions. They may matter in individual communities; they should not be assumed. **Mixed direct evidence and inference; Medium confidence.**

## Decision-makers and influencers

- **Solo owner/maintainer:** decides support, scope, access, releases, transfer, and exit unless constrained by employer or host.
- **Co-maintainers/project leads:** share technical and governance decisions and may approve new maintainers.
- **PyPI owners and maintainers:** hold distinct release/access capabilities; credential and role changes are consequential.
- **Community-host administrators:** approve membership and transfer, manage organization settings and sensitive backup controls, but may not maintain code.
- **Employer engineering manager, OSPO, security, and legal staff:** can approve paid time, contribution, disclosure, licensing, release infrastructure, or sponsorship; they can also block it.
- **Sponsors, foundations, fiscal hosts, downstream users, and security reporters:** provide resources, evidence, or urgency but do not automatically control the roadmap.
- **Django core/security/release teams:** set upstream facts and may coordinate a popular third-party vulnerability, but do not govern independent packages.
- **Experienced contributors and peer maintainers:** are a plausible successor pool and validate choices.

For a volunteer solo project, initiator, evaluator, approver, user, and consequence-bearer may collapse into one person. In an employer-backed or hosted project, these roles separate. **Inference grounded in documented role structures; High confidence.**

## Appropriate next actions for Django to encourage

These are audience actions tied to jobs, not proposed campaigns or assets:

- **Inspect the relevant Django release notes and declare a bounded support matrix** — advances the compatibility job by replacing ambiguous obligation with a testable contract.
- **Run compatibility tests and report precise incompatibilities** — advances early risk detection without promising untested support.
- **Adopt PyPI 2FA and Trusted Publishers and add an appropriate backup owner** — advances safe publishing and continuity.
- **Update release/upgrade, contribution, security, and support information** — advances user trust and reduces repeated explanation.
- **Offer one bounded maintenance contribution—triage, reproducer, documentation, test, release help, or review—rather than an unsolicited feature** — advances capacity while respecting maintainer priorities.
- **Join, contribute to, or evaluate transfer to Django Commons where Django-specific shared administration fits** — advances governance and succession; it should not be framed as automatic maintenance outsourcing.
- **Create an explicit co-maintainer, pause, transfer, deprecation, or archive plan** — advances safe exit and removes permanent-personal-obligation assumptions.
- **Ask an employer or dependent organization for defined paid maintenance time or funding tied to compatibility, security, releases, or mentoring** — advances capacity and makes downstream reliance visible.
- **Use Django's private security route when coordinating a vulnerability in a popular third-party package is appropriate** — advances harm reduction.

## Overlaps with other audiences

- **Django core and ecosystem contributors:** shared contribution, governance, recognition, and burnout concerns, but authority and release responsibility differ.
- **Existing professional Django developers:** many maintainers are also application developers seeking upgrades and best practice; this report concerns their package-stewardship job.
- **Technical leads, engineering managers, and companies depending on Django:** can allocate employee time, approve security processes, or fund critical packages; maintainers bear the actual work and community consequences.
- **Donors and corporate funders:** funding may support maintenance capacity, but the maintainer's job is not donating or producing sponsor ROI.
- **Security and platform stakeholders:** influence release integrity, vulnerability handling, SBOM/compliance expectations, and access controls.
- **Educators, early-career contributors, and package users:** can supply future maintainers and impact evidence, while also creating mentoring or support demand.

## Possible segmentation problems

- “Django and Python package maintainers” is too broad if treated as one addressable audience. Most Python packages are not Django-specific.
- “Maintainer” can mean creator, merger, release owner, triager, community lead, security contact, or distribution packager; authority and burden differ.
- Download count, GitHub stars, and dependent count do not reliably distinguish criticality, labor, financial need, or willingness to grow.
- Paid/volunteer and solo/team are not clean binaries: funding sources coexist, and a nominal team can still have one active release owner.
- Django Commons membership, Django core contribution, DSF membership, Jazzband history, and independent PyPI ownership are different governance states.
- Growth, caretaking, security-only, transfer, and archival should not be placed in one journey.
- Geography, language, gender, disability, and access to paid time likely affect participation and recognition. Tidelift's 2023 sample was 83% men and 83% Europe/North America, limiting generalization.
- AI-generated issue/PR load is a salient 2026 Jazzband trigger, but its prevalence and effects across Django/Python projects are not yet established by the reviewed evidence.
- Active-maintainer research risks survivor bias because quiet leavers are harder to survey.

## Existing-analysis claim audit

| Existing-analysis claim | Audit | Evidence and qualification |
|---|---|---|
| Ecosystem/core contributors seek recognition, governance understanding and influence, co-maintainers, less burnout, and a clear participation pathway. | **Partially supported** | Recognition, co-maintainers/experienced help, burnout reduction, governance structure, and participation/mentoring pathways are supported by Tidelift, Linux Foundation research, mentoring research, Jazzband, and Django Commons. “Influence” was not established as a general maintainer job, and package maintainers should not be merged with Django core contributors. |
| Companies depending on Django want maintenance continuity to avoid migration costs and may fund it; corporate approval can involve finance and leadership. | **Requires further research** | Broad OSS evidence shows employer payment and maintainer demand for funding; Django Commons seeks funding support. This research did not find Django-package-specific company studies demonstrating continuity motives, migration-cost calculations, or approval chains. Plausible, not validated here. |
| Existing professional Django developers seek current best practice, releases/upgrades, scaling help, greater expertise, and possible progression from user to contributor. | **Partially supported for the overlap only** | Release/upgrade and progression concerns are supported, but scaling help is not a central package-maintainer job. Maintainers may also be professional developers; the roles should remain distinct. |
| Docs/release notes are a maintainer touchpoint. | **Supported** | They carry upstream compatibility, deprecation, security, and upgrade facts and are part of recurring release work. |
| GitHub/issue tracker is a maintainer touchpoint. | **Supported** | It is a work, validation, review, mentoring, and sometimes stress channel; it is not merely discovery. |
| Forums are a maintainer touchpoint. | **Supported, qualitatively** | The 2024 Django Forum thread shows peer interpretation of third-party support policy. Prevalence is unknown. |
| Conferences/sprints and professional peers are touchpoints. | **Partially supported** | Maintainer interviews support personal engagement and community relationships; Django Commons and Jazzband histories include conference-based engagement. The specific effect on package decisions is not quantified. |
| Discord, mailing lists, podcasts, and short-form social are maintainer touchpoints. | **Requires further research** | They may surface alerts or support individual communities, but this research found no maintainer-specific evidence sufficient to assign a stable behavioral role across Django/Python package maintainers. |

## Evidence table

| Finding | Source (title, publisher/author, date, URL) | Evidence type | Direct evidence or inference | Confidence | Research notes |
|---|---|---|---|---|---|
| Maintainer work is often unpaid; payment and experienced co-maintainer help are both desired. | [“The 2023 State of the Open Source Maintainer Report,” Tidelift, April 2023](https://tidelift.com/open-source-maintainer-survey-2023) | Survey, n=339 after screening | Direct | Medium | Recruited through Tidelift lists/social; not representative of PyPI/Django. Exact item n varies. |
| Stress, loneliness, inadequate compensation, user demands, and burnout are maintenance pressures. | [Tidelift report, April 2023](https://tidelift.com/open-source-maintainer-survey-2023) | Survey | Direct | Medium | Strong pattern evidence; ecosystem prevalence uncertain. |
| Meaningful work, impact, learning, recognition, and community are important pulls. | [Tidelift report, April 2023](https://tidelift.com/open-source-maintainer-survey-2023); [“Lessons from Maintainers of the World's Most Critical Software,” Linux Foundation, August 10, 2023](https://www.linuxfoundation.org/blog/lessons-from-maintainers-of-the-worlds-most-critical-software) | Survey plus 32 maintainer interviews | Direct | Medium | LF interviewees skew to critical/high-profile projects and often full-time roles. |
| Maintenance labor is depletable; work-life balance, social pressure, governance/culture, and funding shape sustainability. | [“Sustaining Maintenance Labor for Healthy Open Source Software Projects through Human Infrastructure,” Linåker, Link, and Lumbard, August 13, 2024](https://arxiv.org/abs/2408.06723) | Qualitative study, 10 maintainers/9 projects | Direct | Medium | Small sample; not Django/Python-specific. |
| Life and job transitions are important disengagement triggers. | [“Why do People Give Up FLOSSing?”, Miller et al., 2019](https://www.cs.cmu.edu/~./ckaestne/pdf/oss19.pdf) | Survey (151 responses) plus survival model | Direct | Medium | Association, not individual prediction; established contributors rather than maintainers only. |
| Toxic/urgent issue interactions can make GitHub a stress channel. | [“Stress and Burnout in Open Source,” Raman et al., ICSE-NIER, May 2020](https://www.cs.cmu.edu/~ckaestne/pdf/icsenier20.pdf) | Computational exploratory study | Direct with authors' caveats | Low-to-Medium | Classifier had precision/recall limitations and covers GitHub issues, not all channels. |
| Mentoring supports skills, norms, networks, and sustainability but costs time and faces social/process/technical challenges. | [“Guiding the way,” Balali et al., Information and Software Technology 171, July 2024](https://www.sciencedirect.com/science/article/abs/pii/S0950584924000752) | Systematic literature review of 39 studies | Direct synthesis | High for general OSS | Not Django-specific; implementation effectiveness varies. |
| Django-package support requires explicit choices across Django and Python versions. | [“Advice on python versions to support for third-party packages,” Django Forum, September 20, 2024](https://forum.djangoproject.com/t/advice-on-python-versions-to-support-for-third-party-packages/34948); [Django 5.2 release notes, April 2, 2025](https://docs.djangoproject.com/en/dev/releases/5.2/) | First-person discussion plus authoritative documentation | Direct job signal; inference on prevalence | High for job, Low for prevalence | A single thread is qualitative; official notes establish upstream constraints. |
| Compatibility status is a distinct ecosystem information need. | [“Readiness,” Django Packages, accessed July 18, 2026](https://djangopackages.org/readiness/) | Live ecosystem directory | Direct | High for existence, Low for usage | Does not establish completeness, accuracy, or maintainer adoption. |
| Django Commons exists to reduce maintainer overhead/barriers, support stepping back, contributors, practice, and funding. | [Django Commons homepage, accessed July 18, 2026](https://django-commons.org/); [“Django Commons — A home for community-maintained Django packages,” Tim Schilling, May 22, 2024](https://www.better-simple.com/django/2024/05/22/looking-for-help-django-commons/) | Organization policy plus founder first-person account | Direct | High about intent/model | Outcomes and population reach are not independently evaluated. |
| A community host can provide security backup while routine maintenance remains with project maintainers. | [“Django Commons Governance,” accessed July 18, 2026](https://django-commons.org/governance/) | Governance document | Direct | High | Describes formal responsibility, not observed performance across all projects. |
| Shared-maintenance governance can itself become a key-person bottleneck; Django and wider Python projects now have different host options. | [“Sunsetting Jazzband,” Jannis Leidel/Jazzband, March 14, 2026](https://jazzband.co/news/2026/03/14/sunsetting-jazzband) | First-person 10-year retrospective/wind-down | Direct case evidence | High for Jazzband, Low generalizability | Salient current case; author's causal account, not independent evaluation. |
| Tiered access can create a path to higher trust while reducing sensitive-access risk. | [“Please welcome our new admins,” Django Commons, April 21, 2026](https://django-commons.org/blog/2026/04/21/please-welcome-our-new-admins/) | Organization operational account | Direct | High for mechanism | Too new for long-term outcome evidence. |
| Trusted Publishing removes long-lived PyPI credentials from automated release workflows. | [“Introducing ‘Trusted Publishers’,” Dustin Ingram/PyPI, April 20, 2023](https://blog.pypi.org/posts/2023-04-20-introducing-trusted-publishers/) | Authoritative platform documentation | Direct | High | Supports release-integrity job; does not prove adoption or eliminate all compromise paths. |
| Maintainers want security best practices and automation that reduces fatigue; many still lack universal baseline practices. | [“Maintainer Motivations, Challenges, and Best Practices on OSS Security,” OpenSSF/Linux Foundation, January 31, 2024](https://openssf.org/blog/2024/01/31/maintainer-motivations-challenges-and-best-practices-on-open-source-software-security/) | Survey report summary | Direct | Medium | Broad OSS; methodology and Python/Django subsamples not exposed in the summary. |
| Django recognizes third-party ecosystem sustainability as a project concern, but this does not establish maintainer needs by itself. | [“2024 Annual Impact Report,” Django Software Foundation, 2024](https://www.djangoproject.com/foundation/reports/2024/) | Foundation report | Direct about DSF priorities; inference about audience | Medium | Django-controlled source, used only for project context and triangulated externally. |

## Unanswered research questions

- How many actively used Django packages are solo-maintained, employer-supported, security-only, seeking help, or effectively unmaintained?
- Which maintenance tasks consume the most time for Django-package maintainers: compatibility, issue support, review, releases, security, documentation, or governance?
- How do maintainers actually choose Django/Python support matrices, and what would reduce the matrix without blocking downstream LTS upgrades?
- What does “successful support” look like by package phase and criticality? Which directional metrics are useful without encouraging unhealthy responsiveness?
- How often do downstream companies fund or allocate employee time to the Django packages they depend on, who approves it, and what evidence unlocks approval?
- What forms of compensation change retention or security outcomes without creating unwanted service expectations?
- Do Django Commons transfers measurably improve release continuity, security response, contributor progression, and maintainer wellbeing? What new administrative burden appears?
- After Jazzband's 2026 wind-down, what governance paths will non-Django Python projects use, and which lessons transfer to Django Commons?
- Which channels do Django/Python maintainers use for discovery, peer validation, security coordination, and ongoing relationships, segmented by geography and language?
- How have AI-generated issues and pull requests changed review load, trust, openness, and contributor onboarding across Django/Python projects?
- What prevents occasional contributors from becoming co-maintainers: skill, time, unclear tasks, review latency, identity, trust, compensation, or lack of desire?
- How do underrepresented maintainers experience recognition, mentoring, toxicity, and access to paid time? Current survey samples are not adequate.
- How do former maintainers describe the point at which a pause, transfer, deprecation, or archive intervention would have helped?
- Which wider Python-package maintainers see Django as a meaningful downstream community, and which would regard Django outreach as irrelevant noise?
