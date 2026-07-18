# Prospective and existing Django contributors

## Audience definition and boundaries

This audience comprises people considering, attempting, repeating, or governing contributions to Django itself and the Django Software Foundation (DSF): code, tests, documentation, localization, issue reporting, triage, review, technical discussion, community support, events, working groups, releases, infrastructure, security, and elected leadership. The underlying job is to turn knowledge, concern, or available effort into useful participation with enough feedback, legitimacy, and human connection to make the effort worthwhile—not simply to “contribute to Django.”

It excludes people who only use Django, donate money, attend a tutorial, or consume community content. DSF membership explicitly distinguishes use and one-off small contributions from substantial or sustained contribution ([DSF Individual Membership FAQ, accessed July 18, 2026](https://www.djangoproject.com/foundation/individual-members/faq/)). It also excludes **third-party package maintainers as a primary audience**: they own an independent package's releases, compatibility, security, and succession, while Django contributors participate in Django/DSF processes. A person can be both; the Steering Council's own contribution-persona discussion lists “Django Library Maintainer” separately from frequent Django subject-matter experts and Fellows ([Lily Foote, March 17, 2025](https://forum.djangoproject.com/t/django-contribution-personas-steering-council/39652)).

This is a participation lifecycle, not one persona. Prospective, first-time, occasional, sustained, and governance participants have different jobs and costs. **Direct evidence for the role boundaries and pathways; High confidence.** Django has not published a representative contributor census or stage-to-stage conversion analysis, so segment sizes and prevalence of particular motives are unknown.

## Important subsegments

- **Prospective contributors:** interested but not yet publicly participating. Some are experienced Django users rather than junior programmers: Djangonaut Space reports a median five years of programming experience among applicants, while many had not found a route into contribution ([“Launching Contributors,” Rachell Calhoun and Tim Schilling, 2026; accessed July 18, 2026](https://djangonaut.space/launching-contributors/)). This is program-applicant evidence, not a profile of all prospects.
- **First-time contributors:** learning the social and technical workflow while attempting a first useful act—reproducing a bug, improving documentation, commenting, reviewing, or submitting a patch. Django's newcomer guidance acknowledges frustration, fear of public judgment, and uncertain review waits ([Django contributor advice, accessed July 18, 2026](https://docs.djangoproject.com/en/dev/internals/contributing/new-contributors/)).
- **Occasional or episodic contributors:** solve one “itch,” contribute around a sprint/release/program, or return irregularly. A contribution may be valuable without becoming sustained participation. Broad OSS research notes that half of newcomers contribute only once, while a 2026 matched study found organic contributors commonly had intermittent engagement ([Ouf and Guizani, April 23, 2026](https://arxiv.org/abs/2604.22120)). **Direct broad-OSS evidence; Medium confidence for Django.**
- **Sustained contributors and subject-matter experts:** repeatedly triage, review, patch, document, translate, support users, organize, or serve on teams. Their job shifts from learning the process to protecting quality, transferring knowledge, and keeping effort sustainable.
- **Mentored/program contributors:** Djangonaut Space and Google Summer of Code participants have structured tasks, peers, mentors, and a time box. This scaffolding is materially different from organic entry and needs a post-program transition.
- **Elevated operational roles:** Triage & Review, Mergers, Releasers, security, ops, and other teams carry differentiated authority and responsibility. Most are volunteers; Django Fellows are paid contractors ([DSF teams, accessed July 18, 2026](https://www.djangoproject.com/foundation/teams/)).
- **Community/organizational contributors:** moderators, event organizers, educators, accessibility advocates, and working-group members contribute to the mission without necessarily changing `django/django`.
- **Governance participants:** DSF Individual Members vote for the Board and Steering Council; Board members govern the foundation; the Steering Council safeguards fundamental technical decisions and future direction. Eligibility, workload, and influence differ from ordinary contribution.

## Primary job to be done

> **When** I see a problem, learning opportunity, community need, or future direction where my effort could matter, **I want to** find a tractable, legitimate contribution and carry it through with timely human feedback, **so I can** improve something people rely on while building competence, belonging, and an appropriate level of influence without wasting or overcommitting my time.

Job hierarchy:

- **Core functional job:** convert intent and relevant knowledge into an accepted, useful outcome.
- **Supporting jobs:** choose a suitable task; understand scope, authority, and quality rules; set up tools; locate context; coordinate publicly; obtain review; respond; and know what happens next.
- **Emotional job (partly evidenced):** move from intimidation and self-doubt toward confidence, agency, and permission to participate. Djangonaut Space measured confidence rising from 2.3 to 4.3/5 among its surveyed alumni, but the follow-up had only 24 of 104 alumni respondents. **Direct program evidence; Medium confidence, limited generalizability.**
- **Social job (evidenced):** become a trusted peer whose work is recognized and who can help shape a community they value. DSF membership formalizes recognition and voting; motivation research finds learning, kinship, reputation, career, and later altruism. **Direct evidence; Medium-to-High confidence.**

## Additional jobs to be done

1. > **When** I want to make my first contribution but the project looks large and unfamiliar, **I want to** identify a task matched to my skills and receive enough context and feedback to finish it, **so I can** prove to myself that I can participate and learn the real workflow.
   - **Core functional:** complete one bounded contribution.
   - **Supporting:** first-contribution tutorial, environment setup, task selection, tests/docs, public communication, review.
   - **Emotional:** reduce fear of doing it wrong or being judged.
   - **Social hypothesis:** be treated as a legitimate newcomer, not as review overhead. Newcomer-barrier research and Django guidance support the mechanism; wording is inference. **Medium-to-High confidence.**

2. > **When** Django behavior or documentation blocks work I care about, **I want to** move the problem from private workaround to an accepted fix or informed decision, **so I can** resolve the immediate need and improve the shared framework.
   - **Core functional:** scratch an itch through bug reproduction, report, patch, documentation, or feature process.
   - **Supporting:** establish whether the issue is valid, recover ticket history, confirm support before large work, and satisfy compatibility, test, and documentation standards.
   - **Emotional hypothesis:** replace frustration with agency.
   - **Social:** avoid duplicating work and respect downstream stability. Django's Steering Council independently identified the “particular itch” contributor ([March 17, 2025](https://forum.djangoproject.com/t/django-contribution-personas-steering-council/39652)). **Direct Django evidence; High confidence in existence, Low in prevalence.**

3. > **When** I have contributed once or episodically, **I want to** find a next responsibility, relationship, or subject area that fits my changing time and motivation, **so I can** deepen expertise without needing to promise permanent availability.
   - **Core functional:** progress from isolated output to repeatable participation.
   - **Supporting:** follow-up task, review/triage, feedback, subject-area ownership, peer relationships, breaks and re-entry.
   - **Emotional:** sustain enjoyment and avoid guilt about irregularity.
   - **Social:** become known and trusted through reliable interaction. A 2026 matched study found steady early engagement associated with longer retention, but also a post-program mentor-dependency risk. **Direct broad-OSS evidence; Medium confidence for Django.**

4. > **When** my experience lets me unblock others or protect Django's quality, **I want to** review, mentor, triage, document decisions, or take a bounded team role, **so I can** multiply useful contributions and reduce concentration on Fellows and a few experts.
   - **Core functional:** convert expertise into project capacity.
   - **Supporting:** appropriate tasks, review queues, role expectations, mentor support, recognition, and authority boundaries.
   - **Emotional hypothesis:** feel useful without becoming permanently on call.
   - **Social:** earn trust and help others belong. Mentor research found task matching, process, personal, technical, and interpersonal challenges; unpaid and under-one-year contributors were less likely to mentor in its Apache sample ([Trinkenreich et al., June 1, 2021](https://link.springer.com/article/10.1186/s13174-021-00140-z)). **Direct broad-OSS evidence; Medium confidence.**

5. > **When** consequential technical or organizational choices need direction, **I want to** understand how decisions and eligibility work and participate at the level I have earned, **so I can** help keep Django stable, relevant, accountable, and viable.
   - **Core functional:** exercise informed influence through discussion, proposals, voting, teams, Steering Council, or Board service.
   - **Supporting:** legible governance, public rationale, eligibility, nomination, elections, meeting records, conflict resolution.
   - **Emotional hypothesis:** trust that effort can lead to meaningful voice rather than opaque gatekeeping.
   - **Social:** represent a constituency while retaining peer legitimacy. The 2024 governance reset directly described an impactful but demanding role and frustration with unclear direction ([DSF Board, November 14, 2024](https://www.djangoproject.com/weblog/2024/nov/14/technical-governance-challenges-and-opportunities/)). **High confidence.**

## Functional, emotional, and social dimensions

**Functional (evidenced):** task discovery, environment setup, issue reproduction, history recovery, tests, documentation, pull requests, review loops, triage state, releases, team work, and governance. Django's code path requires coordination across Trac and GitHub for most non-trivial changes and tests/docs as part of a complete fix ([submitting contributions, accessed July 18, 2026](https://docs.djangoproject.com/en/dev/internals/contributing/writing-code/submitting-patches/)). **High confidence.**

**Emotional (partly evidenced):** confidence, enjoyment, intellectual stimulation, agency, pride, belonging, fear of public error, frustration while waiting, and overload. Djangonaut Space exit/follow-up data directly measures confidence and welcome; Django guidance explicitly names fear and frustration; broader motivation research finds learning, fun, kinship, career, and altruism change with tenure ([Gerosa et al., January 25, 2021](https://arxiv.org/abs/2101.10291)). **Medium confidence; no representative Django survey.**

**Social (evidenced):** peer relationships, recognition, reputation, reciprocal help, trust, membership, influence, and mentoring. Half of GitHub's 2017 random-sample respondents said open-source work mattered to obtaining their current role, while negative behavior caused 21% of those who experienced or witnessed it to stop contributing to a project ([GitHub Open Source Survey, 2017](https://opensourcesurvey.org/2017/)). **Medium confidence for broad OSS, High that social climate matters.**

## Triggering situations

**Recurring triggers:** encountering a bug or unclear documentation; reviewing a release or regression; seeing an actionable ticket or pull request; answering a community question; a sprint, scheduled working-group meeting, mentorship check-in, release cycle, or election.

**Event-triggered triggers:** a work problem needing an upstream fix; a first successful PR; invitation or nomination; Djangonaut/GSoC applications; a conference sprint; a security issue; governance breakdown; a colleague or mentor asking for help; job or life transition; contributor departure.

Entry is often problem-led or relationship-led, while exit is often capacity-led. Established-contributor research found work/academic transitions the most commonly cited disengagement reason, and its model associated job transition with 2.48 times the disengagement hazard ([Miller et al., May 2019](https://dl.ifip.org/IFIP-AICT-556/hal-02305702)). **Direct broad-OSS evidence; Medium confidence for Django.**

## Desired outcomes

- Time from intent to a suitable, unblocked first task decreases; fewer people abandon setup or task selection.
- Contributors can state what system holds the authoritative issue, proposal, review, and decision at each stage.
- A first contribution gets clear acknowledgment and actionable feedback; abandoned review loops trend down.
- Occasional contributors can stop, resume, or change contribution type without losing all context or social connection.
- Sustained contributors spend more time on meaningful work and less on repetitive coordination; review and mentoring load is distributed without lowering quality.
- Non-code work is visible and can progress toward recognition and decision rights.
- Mentored contributors maintain self-directed activity and relationships after program scaffolding ends.
- Governance participants can explain eligibility, authority, workload, decisions, and routes for community input.
- Contributor composition and leadership become more representative of Django's user community.

These are directional measures synthesized from Django process evidence and contributor studies; no universal service-level target or conversion benchmark is supported. **Inference; Medium-to-High confidence in direction, Low in target values.**

## Current behaviour or status quo

Prospects may start from a work problem, Django documentation, community discussion, a GitHub/Trac item, a conference sprint, or a structured program. Django presents multiple valid first acts: triage, review, documentation, localization, code, forum/Discord help, and ecosystem work. The code contribution path commonly means: establish or locate a Trac ticket, confirm acceptance for non-trivial work, create a GitHub pull request, include tests and documentation, update Trac flags, wait for community review, and receive final merger review. Anyone may triage, fix, or review; only Mergers merge ([triage workflow, accessed July 18, 2026](https://docs.djangoproject.com/en/dev/internals/contributing/triaging-tickets/)).

This openness coexists with complexity. Django's newcomer page says ticket history depends on context, warns against large work without support, and acknowledges review waits. Steering Council candidates called feature contribution daunting, bureaucratic, and costly in time and mental energy ([candidate statements, December 10, 2024](https://www.djangoproject.com/weblog/2024/dec/10/django-6x-steering-council-candidates/)). **Direct qualitative evidence; High confidence that friction exists, Low in prevalence or dominant step.**

Structured mentorship changes this for a selected minority. Djangonaut Space reports 104 participants across six sessions and a 24-person alumni follow-up in which 83% had opened PRs after the program, 62% reported long-term motivation, and 42% mentored others. Its 2024 activity included 46 participants and 80 merged PRs ([DSF 2024 Impact Report](https://www.djangoproject.com/foundation/reports/2024/)). Program selection, self-report, low follow-up response, and no control group prevent causal or population claims. **Direct program evidence; Medium confidence.**

Sustained work can lead to Triage & Review, merger/releaser or team roles, DSF Individual Membership, voting, and elected governance. The boundary is not automatic: membership recognizes substantial or sustained work and is lifetime recognition; operational authority requires separate trust and selection. **Direct evidence; High confidence.**

## Pushes

- A concrete bug, documentation gap, accessibility need, missing feature, or recurring workaround.
- Desire to learn internals, improve collaboration skills, gain work experience, demonstrate capability, or give back.
- Seeing peers with similar backgrounds participate; personal invitation, mentoring, or a bounded sprint lowers social uncertainty.
- Concern about Django's quality, technical direction, contributor concentration, or long-term viability.
- Recognition that review, triage, mentoring, and community work can have more leverage than another isolated patch.
- Governance frustration can push experienced contributors toward reform or candidacy.

Learning, career, fun, kinship, reputation, and altruism are supported across OSS, with motivation changing by tenure; the ordering for Django is unknown. **Direct broad-OSS evidence plus Django program signals; Medium confidence.**

## Pulls

- A task tied to a real interest and clearly within current skill/time.
- A successful first feedback loop: acknowledgment, specific review, visible progress, and credit.
- Relationships with a peer, mentor, Fellow, or subject-matter expert who supplies missing context.
- Work whose impact is legible: a merged fix, clearer docs, resolved ticket, supported contributor, shipped release, or recorded decision.
- Multiple contribution modes and permission to start small, pause, or move from code to review/community work.
- A visible progression from participant to trusted reviewer, member, team role, mentor, or voter—without implying everyone should pursue governance.
- A respectful environment with enforceable conduct norms.

Djangonaut Space's follow-up found confidence, welcome, network growth, continued PRs, and mentoring, while GitHub's survey linked process/conduct documentation and social climate to accessibility. **Direct evidence; Medium confidence.**

## Anxieties

- “Do I know enough Django internals, Git, testing, and project history to be useful?”
- “Which of Trac, GitHub, Forum, Discord, or a DEP is authoritative, and have I skipped a required step?”
- “Will I spend days on a change that lacks support or duplicates old work?”
- “Will public feedback expose that I do not belong, or will silence mean rejection?”
- “How long will review take, and must I keep rebasing an aging patch?”
- “Does using AI assistance make my contribution suspect?” Django now requires disclosure and human understanding because of inaccurate or fictitious generated submissions ([submitting contributions, accessed July 18, 2026](https://docs.djangoproject.com/en/dev/internals/contributing/writing-code/submitting-patches/)).
- “If I become reliable, will every gap become my unpaid obligation?”
- “Can I influence direction, or are informal status and opaque history more important than the written process?”

The first five are supported by Django guidance and newcomer studies; the latter wording is inference from workload and governance evidence. **Medium confidence.**

## Habits and inertia

Prospects often keep workarounds private, ask familiar colleagues, or choose a repository whose workflow they know. Public participation means switching from product delivery to community coordination, often outside paid time. GitHub found 65% of employed contributors contributed as part of work duties while employer IP policies were often unclear, making permission and time real inertia.

Insiders accumulate Trac queries, notifications, contacts, test commands, and knowledge of decision-makers, making repeat work cheaper but entry less legible. Breaks also erode context: across 18 GitHub organizations, all studied core developers took breaks and about 45% disengaged for at least a year ([Calefato et al., November 24, 2021](https://link.springer.com/article/10.1007/s10664-021-10012-6)). **Direct broad-OSS evidence; Medium confidence; not a Django rate.**

## Decision criteria

No evidence supports a universal ranking; importance varies by lifecycle stage.

| Criterion | Importance | Confidence | Evidence or practical question |
|---|---|---:|---|
| Task relevance and tractability | Critical for first/occasional contribution | High | Is the task meaningful, supported, bounded, and matched to skill/time? |
| Process and authority clarity | Critical | High | Where are issue state, code review, feature approval, and final decision recorded? |
| Feedback quality and timeliness | Critical for continuation | High | Is there acknowledgment, actionable review, and a way to recover stalled work? |
| Setup and test feasibility | High for code | High | Can the contributor reproduce, run focused tests, and satisfy checks on available hardware/OS? |
| Social safety and belonging | High; potentially gating | Medium-to-High | Are questions safe, conduct enforced, language accessible, and mistakes treated constructively? |
| Learning and impact | High | Medium | Will the effort build valued skill and improve something real? |
| Time, employer permission, and flexibility | Critical for sustained work | High | Is work paid or voluntary, allowed under IP policy, and compatible with life transitions? |
| Recognition and progression | Medium-to-High, stage-dependent | Medium | Is code and non-code work credited, and are membership/team/governance paths legible? |
| Maintainer/reviewer capacity | Critical system constraint | High | Is someone able to review and mentor without displacing release/security duties? |
| Governance legitimacy and transparency | High for influential roles | High | Are eligibility, authority, records, and accountability understandable? |

## Main concerns

**Practical concerns:** task fit, setup, history, testing, quality rules, Trac/GitHub navigation, review latency, English fluency, employer permission, time, and re-entry.

**Legitimate limitations:** Django's maturity and stability promise make large changes expensive. Review and mentorship consume expert time; sensitive authority requires earned trust; episodic participation is not necessarily failure.

**Perceived risks:** rejection is personal; only code counts; small work is pointless; governance is a fixed inner circle; a task creates indefinite duty; one must already be an expert.

**Misconceptions:** professional use is contribution; a PR needs no issue context; “easy pickings” needs no learning; every idea belongs in core; membership grants merge rights; mentorship guarantees retention.

**Organizational objections:** IP policy, unpaid time, confidentiality, CLA/legal review, unclear employer return, timezone, and travel.

**Emotional resistance:** intimidation, fear of public mistakes, prior negative interactions, impostor feelings, guilt after inactivity, and aversion to open-ended unpaid responsibility. **Mixed direct evidence and inference; Medium confidence.**

## Objections and perceived risks

- **“The workflow is bureaucratic.”** Legitimate for changes spanning proposal, Trac, GitHub, tests, docs, and review; stability explains some checks but not all navigation cost.
- **“No one will review my work.”** Review delay is acknowledged; whether silence is a dominant dropout cause is unmeasured.
- **“Core contribution is only for experts.”** Contradicted as an absolute: anyone can triage, fix, or review, and newcomer programs produce merged work. Expertise still matters for complex areas and elevated authority.
- **“Only commits count.”** Contradicted by DSF criteria recognizing docs, review, support, events, content, and working groups.
- **“Contribution will improve my career.”** Plausible, not guaranteed. Broad survey and GSoC research support career/work-experience motives; Djangonaut Space reports 21% of 24 alumni respondents gained professional opportunities, but selection and response bias are substantial.
- **“Mentorship solves retention.”** Partially contradicted: it can improve early activity, but scaffolding may create dependency and does not always yield sustained contributors.
- **“Governance gives real influence.”** Supported but gated: members vote and elected bodies have authority; 2024 shows formal structure can still fail operationally.
- **“If I become trusted, I will burn out.”** Burnout and capacity strain are legitimate broad-OSS risks, but no Django contributor prevalence estimate exists. Fellows and distributed teams reduce some volunteer concentration, not all.

## Information needed to make progress

Prospective and first-time contributors need contribution types, prerequisites, a system map, task examples, tests/docs expectations, setup help, review norms, conduct routes, CLA/employer implications, and a place to ask.

Occasional contributors need current state, changed context, a bounded next step, and permission to pause or unclaim.

Sustained contributors need priority, review queues, constraints, rationale, team boundaries, capacity support, recognition, and hand-off norms.

Governance participants need: eligibility, nomination and election mechanics, role workload and authority, conflicts, meeting/decision records, current reform status, and routes for community input. This is especially salient because proposed DEP 19 aimed for July 1, 2026 adoption but its official pull request remained open on July 18, 2026 ([django/deps PR #107, opened April 16, 2026](https://github.com/django/deps/pull/107)). **Direct current-state evidence; High confidence.**

## Trusted content formats

- **Executable tutorial and focused setup commands:** first action can be verified locally.
- **Checklist, triage definitions, and worked ticket/PR examples:** expose acceptance criteria and handoffs.
- **Reference documentation and role charters:** authoritative for rules and permissions.
- **Public issue, review, meeting, and decision records:** validate rules in context.
- **Mentored practice and sprint pairing:** transfer tacit context but consume expert time.
- **Contributor retrospectives and program outcomes:** validate pathways if selection, denominators, and response rates are disclosed.
- **Release/Fellow/Steering Council reports:** useful for ongoing engagement and locating current work, not necessarily sufficient first-contribution instruction.

Evidence supports the behavioral fit of these formats, not a universal preference order. **Direct process evidence plus inference; Medium confidence.**

## Discovery, evaluation, validation, and engagement channels

| Stage | Channel | Behavioral role and caveat |
|---|---|---|
| Discovery | Work problems, docs, search, community peers, conference talks/sprints, Djangonaut/GSoC announcements, podcasts and social posts | Exposes a need or makes contribution seem possible. No evidence establishes homepage, video, podcast, or short-form social as a dominant acquisition channel. |
| Evaluation | Contributor docs/tutorial, “easy pickings,” Trac reports/dashboard, team/program descriptions | Lets a prospect judge prerequisites, task fit, effort, and accepted contribution types. Labels alone cannot supply missing context or mentorship. |
| Validation | Trac history and flags, GitHub PR/checks, `django/new-features`, Forum Internals, public governance records | Confirms that a problem is supported, a patch meets standards, or a proposal has authority. Fragmentation across systems is itself a cost. |
| Ongoing engagement | GitHub/Trac notifications, Forum, Discord, working groups, Fellow/Steering Council reports, conferences and sprints | Maintains relationships, context, review loops, and role participation. Discord is useful for low-friction help but less durable than public archived records. |
| Governance | DSF member communications, candidate statements, election mail, Forum, meeting notes, DEPs | Supports informed voting, candidacy, reform, and accountability; eligibility is narrower than open discussion. |

Mailing lists remain relevant for announcements, updates, some team calls, and member/election communication, but the Steering Council moved new-feature proposals away from Forum/mailing lists to `django/new-features` in 2025 to reduce Fellow workload ([Steering Council year in review, February 11, 2026](https://www.djangoproject.com/weblog/2026/feb/11/steering-council-2025-year-in-review/)). **Direct evidence; High confidence that channel function changes over time.**

## Decision-makers and influencers

The individual decides whether effort, exposure, and learning justify participation. Employers/managers and legal or open-source program offices can approve paid time, public disclosure, and IP terms; family/care obligations can be practical blockers even without formal authority.

For contribution outcomes, triagers and community reviewers validate tickets and patches; Fellows perform substantial triage/review/merge/release/security work; Mergers decide whether code enters the repository; subject-matter experts influence technical consensus; the Steering Council decides major technical questions and selects/removes certain elevated roles. Program Navigators, Captains, peers, and event sprint leaders strongly influence whether newcomers persist.

For organizational governance, DSF Individual Members elect the Board and Steering Council. In the 2024 Steering Council election, 215 of 400 eligible voters participated (54%) ([results, December 18, 2024](https://www.djangoproject.com/weblog/2024/dec/18/django-6x-steering-council-election-results/)). The DSF Board governs the foundation and intervened in the 2024 technical-governance crisis. **Direct evidence; High confidence.**

## Appropriate next actions for Django to encourage

- **Prospect → choose one contribution context:** connect the first-contribution job to a real interest—bug reproduction, docs, triage, review, localization, community help, or code—rather than assuming a PR is the only success.
- **First-timer → complete one verified loop:** reproduce/setup, state the intended task publicly, submit the smallest complete change, and obtain actionable review. This serves competence and confidence.
- **One-time contributor → select a self-directed next step:** review a neighboring patch, continue in one subject area, or join a recurring discussion; this serves continuity without demanding permanence.
- **Mentored contributor → transition beyond the cohort:** maintain peer/mentor connections while choosing work not dependent on program scheduling; this serves autonomous retention.
- **Sustained contributor → multiply capacity:** perform review/triage, document tacit context, mentor within a bounded commitment, or join a relevant team; this serves leverage and sustainability.
- **Substantial contributor → seek recognition and voice:** apply or accept nomination for DSF membership if criteria fit, then vote or contribute to governance discussion; this serves recognition and legitimate influence.
- **Experienced governance prospect → assess a defined role:** review authority, workload, eligibility, records, and support before candidacy; this serves direction without romanticizing leadership burden.
- **Paused contributor → re-enter safely or hand off:** update status, unclaim stale work, ask for current context, or choose a smaller mode; this serves continuity without guilt.

These are participation outcomes tied to jobs, not recommendations for marketing assets. **Inference grounded in direct pathway and retention evidence; Medium-to-High confidence.**

## Overlaps with other audiences

- **Existing professional Django developers:** frequent source of itch-driven or mentorship applicants, but professional use is not contribution.
- **Early-career/self-taught developers:** career, learning, and confidence overlap, but many contribution newcomers are experienced programmers.
- **Django/Python package maintainers:** may contribute compatibility findings, features, and reviews upstream; their primary maintenance job remains independent.
- **Educators/content creators:** documentation, teaching, talks, and learning resources can qualify as community contribution.
- **Companies relying on Django:** may allow time or funding; contributor and company-continuity jobs differ.
- **Donors/DSF members:** financial support does not qualify for Individual Membership, while contributors may also donate.
- **Event organizers and moderators:** contribute under the DSF's broad mission without core code activity.

## Possible segmentation problems

- “Contributor” is often reduced to code, hiding review, triage, docs, translation, support, governance, and organizing.
- “Core contributor” is historically ambiguous; current Django uses named roles and teams.
- First-time does not mean junior, and occasional does not mean failed retention.
- Stage, motive, authority, and payment are separate; Fellow, Merger, package maintainer, program participant, and DSF member roles can overlap.
- Selected, scaffolded program participants cannot represent organic newcomers.
- Open discussion, voting, elected leadership, and operational roles are different kinds of “influence.”
- Django-core and ecosystem contribution connect but have separate governance.
- GitHub activity misses Trac, Forum, Discord, events, working groups, sensitive work, and offline mentoring.

## Existing-analysis claim audit

| Existing-analysis claim | Audit | Evidence and qualification |
|---|---|---|
| Early-career/self-taught/bootcamp/CS/career-changing developers evaluate a framework as a career investment, portfolio tool, modern-app tool, and route to a welcoming community; homepage/social/video/community discovery is claimed. | **Partially supported** | Broad OSS and [GSoC research (Silva et al., 2020)](https://arxiv.org/abs/1910.05798) support career, learning, work-experience, reputation, and belonging motives, and Djangonaut data includes professional outcomes. This does not validate framework-selection motives, “modern-app” needs, or homepage/social/video acquisition for Django contributors. |
| Existing professional Django developers seek current best practice, releases/upgrades, scaling help, greater expertise, and possible progression from user to contributor. | **Partially supported** | This report directly supports the progression possibility: Django explicitly wants users to become contributors, and Djangonaut applicants often have years of programming/Django experience. It does not establish the relative importance of best practice, upgrades, or scaling for the contributor audience. |
| Ecosystem/core contributors seek recognition, governance understanding and influence, co-maintainers, less burnout, and a clear participation pathway. | **Partially supported** | Recognition is formalized by DSF membership; voting/roles create influence; Django documents pathways and acknowledges friction; [Linux Foundation maintainer interviews (August 10, 2023)](https://www.linuxfoundation.org/blog/lessons-from-maintainers-of-the-worlds-most-critical-software) support capacity and burnout risk. Co-maintainers primarily belong to package maintenance, and no representative Django data ranks these needs or measures burnout. |
| Companies depending on Django want maintenance continuity to avoid migration costs and may fund it; corporate approval can involve finance and leadership. | **Requires further research** | Relevant only when employer time/funding enables contributors. This audience research does not establish company buying motives or approval chains. |
| Docs/release notes are contributor touchpoints. | **Supported** | Docs are evaluation/reference; release notes and reports help ongoing contributors track change. No evidence shows they are dominant discovery channels. |
| Forums/Discord are contributor touchpoints. | **Supported** | Django directs questions/disagreement and relationship-building to these spaces; Forum supplies durable validation and Discord lower-friction help/engagement. |
| GitHub/issue tracker are contributor touchpoints. | **Supported** | They are operationally required for most code contributions and review state; fragmentation creates navigation cost. |
| Mailing lists are contributor touchpoints. | **Partially supported** | Relevant for announcements, member/election communication, and occasional team calls; feature proposal work moved elsewhere and their current behavioral importance is unmeasured. |
| Conferences/sprints are contributor touchpoints. | **Supported** | They create event-triggered discovery, pairing, and bounded participation; retention after events is not guaranteed. |
| Podcasts, professional peer networks, and short-form social are contributor touchpoints. | **Partially supported** | Peers and public contributor stories plausibly drive discovery/validation, and Djangonaut alumni report network growth/content creation. No Django attribution data establishes podcast or short-form social behavior or importance. |

## Evidence table

| Finding | Source (title, publisher/author, date, URL) | Evidence type | Direct evidence or inference | Confidence | Research notes |
|---|---|---|---|---|---|
| Django contribution includes code and multiple non-code modes; project work is conversational and volunteer-dependent. | [“Contributing to Django,” Django documentation, accessed July 18, 2026](https://docs.djangoproject.com/en/dev/internals/contributing/) | Official process documentation | Direct | High | Authoritative scope; not audience-prevalence evidence. |
| First-time contributors face frustration, public-feedback fear, context/history ambiguity, and review waits. | [“Advice for new contributors,” Django documentation, accessed July 18, 2026](https://docs.djangoproject.com/en/dev/internals/contributing/new-contributors/) | Official guidance | Direct | High | The project explicitly anticipates these problems; frequency unknown. |
| Most non-trivial code contributions span Trac and GitHub and require accepted scope, tests, docs, and review-state management. | [“Submitting contributions,” Django documentation, accessed July 18, 2026](https://docs.djangoproject.com/en/dev/internals/contributing/writing-code/submitting-patches/) | Official workflow | Direct | High | Strong evidence for functional cost and information needs. |
| Anyone can triage, fix, and review; merger authority is restricted. | [“Triaging tickets,” Django documentation, accessed July 18, 2026](https://docs.djangoproject.com/en/dev/internals/contributing/triaging-tickets/) | Official workflow/governance | Direct | High | Distinguishes open participation from elevated authority. |
| Contribution roles include paid Fellows, volunteer teams, Mergers, Releasers, Steering Council, and working groups. | [“Teams,” Django Software Foundation, accessed July 18, 2026](https://www.djangoproject.com/foundation/teams/) | Official organizational record | Direct | High | Current roster can change; accessed date supplied. |
| Substantial/sustained code and non-code contribution can earn recognition and election voting; use or a small one-off act does not ordinarily qualify. | [“DSF Individual Membership FAQ,” Django Software Foundation, accessed July 18, 2026](https://www.djangoproject.com/foundation/individual-members/faq/) | Official membership criteria | Direct | High | Recognition is lifetime; operational authority is separate. |
| Django's 2024 technical-governance model produced contributor frustration and lacked forward-looking direction. | [“Django’s technical governance challenges, and opportunities,” DSF Board, November 14, 2024](https://www.djangoproject.com/weblog/2024/nov/14/technical-governance-challenges-and-opportunities/) | Official governance postmortem | Direct | High | Institution-authored admission; supports governance job and risk. |
| Contributors described feature contribution as high-effort and intimidating. | [“Django 6.x Steering Council Candidates,” Django Software Foundation, December 10, 2024](https://www.djangoproject.com/weblog/2024/dec/10/django-6x-steering-council-candidates/) | Candidate statements | Direct qualitative evidence | Medium | Multiple experienced voices, but advocacy statements are not a survey. |
| 2024 Steering Council election had 400 eligible voters and 215 votes. | [“Django 6.x Steering Council Election Results,” Django Software Foundation, December 18, 2024](https://www.djangoproject.com/weblog/2024/dec/18/django-6x-steering-council-election-results/) | Administrative data | Direct | High | Exact event count, not general participation rate. |
| Governance simplification remained unfinished after its target adoption date. | [“DEP 0019 - Technical governance,” django/deps PR #107, opened April 16, 2026; status checked July 18, 2026](https://github.com/django/deps/pull/107) | Current official repository state | Direct | High | PR was open on access date; current governance must not be inferred from the proposal. |
| Djangonaut Space reports higher confidence, welcome, continued PRs, mentoring, and leadership among participants. | [“Launching Contributors,” Rachell Calhoun and Tim Schilling/Djangonaut Space, 2026; accessed July 18, 2026](https://djangonaut.space/launching-contributors/) | Program records, exit surveys, alumni follow-up | Direct | Medium | 104 participants; alumni survey n=24 (~23%); self-selection, self-report, no control group. |
| Djangonaut Space produced 80 merged PRs from 46 participants in 2024. | [“2024 Annual Impact Report,” Django Software Foundation, accessed July 18, 2026](https://www.djangoproject.com/foundation/reports/2024/) | Program/administrative reporting | Direct | Medium-to-High | Counts outputs, not attribution or long-term retention. |
| Learning, intellectual stimulation, social/reputation motives remain important; novice and experienced motives differ. | [“The Shifting Sands of Motivation,” Gerosa et al., January 25, 2021](https://arxiv.org/abs/2101.10291) | Survey of 242 OSS contributors | Direct, broad OSS | Medium | Not Django-specific; self-reported motivation. |
| Newcomer barriers are social as well as technical/organizational. | [“Social Barriers Faced by Newcomers Placing Their First Contribution,” Steinmacher et al., March 2015](https://doi.org/10.1145/2675133.2675215) | Interviews and triangulated qualitative research | Direct, broad OSS | High for mechanisms; Medium for Django | Used interviews with 36 developers across 14 projects plus other sources. |
| Mentoring transfers technical, social, and organizational knowledge but burdens mentors, especially in task matching. | [“Being a Mentor in Open Source Projects,” Trinkenreich et al., June 1, 2021](https://link.springer.com/article/10.1186/s13174-021-00140-z) | Apache survey (n=624) and 18 interviews | Direct, broad OSS | Medium-to-High | Mature foundation context; mentor capacity is not free. |
| Structured events correlate with higher core transition and longer retention, while post-program dependency is a risk. | [“Same Project, Different Start,” Ouf and Guizani, April 23, 2026](https://arxiv.org/abs/2604.22120) | Matched observational study, 4,002 contributors/330 projects | Direct association, broad OSS | Medium-to-High | Not causal; event-hosting projects may be unusually structured. |
| Process documentation, social climate, employer policy, career value, and language accessibility affect contribution. | [“Open Source Survey,” GitHub and collaborators, 2017](https://opensourcesurvey.org/2017/) | Random sample of 5,500 GitHub respondents | Direct, broad OSS | High for sample; Medium for Django | Older but unusually rigorous/open data; platform population differs from Django. |
| Established contributors most often cited transitions in disengagement. | [“Why Do People Give Up FLOSSing?”, Miller et al., May 2019](https://dl.ifip.org/IFIP-AICT-556/hal-02305702) | Mixed survey and survival modeling | Direct, broad OSS | Medium | Supports capacity/life triggers, not individual prediction. |

## Unanswered research questions

- How many people enter each Django contribution mode annually, and what proportion make a second contribution after 1, 3, 6, and 12 months?
- Where do prospects abandon the path: task search, environment setup, Trac account/history, proposal acceptance, PR creation, review wait, or revision?
- Which motives and desired outcomes differ among first-time, episodic, sustained, paid, and governance contributors to Django specifically?
- How long do first acknowledgment and substantive review take by task type, contributor stage, and system?
- What share of contributor work occurs on employer time, and which employer policies enable or block it?
- How do non-code contributions and private work become visible enough for recognition without exposing sensitive activity?
- Which groups are underrepresented among prospects, successful first contributors, sustained contributors, team members, DSF members, and elected leaders?
- What produces durable self-directed participation after Djangonaut Space or GSoC, and what support can end without creating mentor dependency?
- What does mentoring cost Fellows and volunteers, and which task/mentor matching approaches improve outcomes without shifting overload?
- How often do occasional contributors return, what prompts return, and how should intentional episodic participation be distinguished from dropout?
- Do contributors understand the current division among Trac, GitHub, `django/new-features`, Forum, Discord, DEPs, teams, Board, and Steering Council?
- What is the final status and practical effect of DEP 19 after missing its stated July 1, 2026 adoption goal?
- Why do eligible DSF members vote or abstain, and which governance information changes participation?
- How prevalent are burnout, guilt, harassment, review fatigue, and life-transition exits among Django contributors specifically?
- Which channels actually originate first contributions? Current evidence validates channel roles but not attribution or relative volume.

<!-- RESEARCH PROVENANCE: BEGIN -->
## Research provenance

This section was generated from the recorded Codex session JSONL logs. File attribution uses successful patch events; searches and domains use nested web-tool calls.

### Session `019f7563-9575-71e1-bc40-bae5e09f57e1`
- Log: `rollout-2026-07-18T15-21-28-019f7563-9575-71e1-bc40-bae5e09f57e1.jsonl`
- This document: `add, update`
- Search queries:
  - None recorded.
- Website domains:
  - `2024.djangocon.eu`
  - `alphaxiv.org`
  - `apache.org`
  - `api.github.com`
  - `app.readthedocs.org`
  - `archive.fosdem.org`
  - `arxiv.org`
  - `aserebre.win.tue.nl`
  - `assets-eu.researchsquare.com`
  - `biancatrink.github.io`
  - `cdnc.heyzine.com`
  - `citeseerx.ist.psu.edu`
  - `cmustrudel.github.io`
  - `code.djangoproject.com`
  - `community.kde.org`
  - `conf.researchr.org`
  - `conservancy.umn.edu`
  - `cs.cmu.edu`
  - `debian.org`
  - `developer.mozilla.org`
  - `devolution.go.ke`
  - `digitalcommons.wayne.edu`
  - `django.readthedocs.io`
  - `djangonaut.space`
  - `djangoproject.com`
  - `dl.ifip.org`
  - `docs.django-cms.org`
  - `docs.djangoproject.com`
  - `documents1.worldbank.org`
  - `doi.org`
  - `en.wikipedia.org`
  - `fedoraproject.org`
  - `forum.djangoproject.com`
  - `fr.wikipedia.org`
  - `github.com`
  - `github.github.com`
  - `hacktoberfest.com†hacktoberfest.com`
  - `igor.pro.br`
  - `inria.hal.science`
  - `journals.aom.org`
  - `journals.plos.org`
  - `jstage.jst.go.jp`
  - `link.springer.com`
  - `linuxfoundation.org`
  - `lp.jetbrains.com`
  - `media.oralhealthgroup.com`
  - `minevaganti.org`
  - `opencollective.com`
  - `opengovpartnership.org`
  - `opensource.com`
  - `opensource.google`
  - `opensourcesurvey.org`
  - `pdfs.semanticscholar.org`
  - `pure.tudelft.nl`
  - `raw.githubusercontent.com`
  - `reddit.com`
  - `repositorio.usp.br`
  - `research.tue.nl`
  - `researchgate.net`
  - `s3-eu-west-1.amazonaws.com`
  - `sciencedirect.com`
  - `ugspace.ug.edu.gh`
  - `wiki.gnome.org`
  - `wiki.mozilla.org`
  - `wiki.ubuntu-women.org`
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
