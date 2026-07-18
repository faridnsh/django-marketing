# Individual educators teaching web development with Python

## Audience definition and boundaries

This audience is the person who plans, explains, demonstrates, facilitates, assesses, and improves learning experiences in which Django could be one means of teaching web development. It includes school teachers, university lecturers and teaching assistants, bootcamp instructors and mentors, independent trainers, workshop coaches, and creators who personally teach a cohort or individual learners.

The defining consequence is **student learning**: the educator bears the day-to-day cost when setup fails, an abstraction is introduced too early, examples do not transfer, feedback arrives too late, or students leave able to imitate a tutorial but unable to reason about a web application. This audience may recommend or select a framework, but its underlying job is not “get students to use Django.”

It excludes institutional curriculum leaders, accreditors, procurement teams, bootcamp owners, and department economic buyers when their primary concern is standards coverage, portfolio strategy, staffing, revenue, or return on investment. Those actors can constrain the educator. It also excludes self-directed learners except when an educator is designing for them. A working developer who occasionally mentors belongs only while performing the teaching job.

Evidence is uneven by setting. K–12 teacher research is strongest on preparation and constraints; computing-education research is strongest on introductory programming; direct evidence about individual instructors choosing Django is sparse. Current Django curricula establish feasibility and practice, not comparative learning effectiveness. **[Direct evidence plus boundary inference; High confidence in the boundary, Medium confidence across all subsegments.]**

## Important subsegments

- **K–12 computing teachers:** often teach mixed-readiness groups under short periods, standards, device policies, and limited preparation. The 2025 CS Teacher Landscape survey of 2,882 U.S. PK–12 teachers reports limited preparation, heavy workloads, time restrictions, and inconsistent support; only 17% could participate in professional development as needed. **[Direct evidence; High confidence for U.S. PK–12, Low outside it.]**
- **Higher-education instructors and teaching assistants:** teach web development inside CS, information systems, software engineering, or continuing education. They may have more curricular autonomy, but larger cohorts intensify feedback, grading, academic-integrity, and environment-support work. **[Inference supported by computing-at-scale and GenAI evidence; Medium-High confidence.]**
- **Bootcamp and career-training instructors:** teach compressed, employment-oriented cohorts in which instructor quality, mentors/TAs, curriculum rigor, pedagogy, technology, and career support jointly shape the experience. A 2022 qualitative analysis of bootcamp reviews identified all of these as satisfaction factors, while cautioning that its data came from one review platform and the proposed model still needed quantitative testing. **[Direct evidence; Medium confidence.]**
- **Independent instructors and course creators:** personally choose scope, sequence, format, examples, and support model, but may lack assistants, learner analytics, or time to maintain versioned material. Evidence specific to this segment is thin. **[Inference; Low-Medium confidence.]**
- **Short-workshop coaches and volunteer educators:** optimize for a motivating success in hours or a day, not semester-long mastery. Django Girls explicitly separates a one-day core tutorial from extensions and pairs it with a coaching manual and pre-workshop installation. **[Direct practice evidence; High confidence that this model exists, Low on comparative effectiveness.]**
- **Developer-educators teaching professional peers:** emphasize authentic practice, debugging, reference use, and transfer to work. Software Carpentry's training model targets usable mental models, misconception diagnosis, formative assessment, and immediate application. **[Direct program-practice evidence; Medium confidence beyond that program.]**

These segments should not be collapsed. Learner age and prerequisites, course duration, educator autonomy, cohort size, assessment stakes, employment promises, and access to assistants materially change the job.

## Primary job to be done

> **When I must help a varied group learn to build real web applications within limited time and support, I want a coherent, teachable progression from visible result to underlying concepts and independent practice, so I can help students understand, complete, explain, and extend their work rather than merely copy it.**

**[Inference synthesized from teacher surveys, pedagogy research, bootcamp evidence, and deployed curricula; High confidence in the functional job, Medium confidence in the exact wording.]**

## Additional jobs to be done

| Job | Core functional job | Emotional job | Social job | Supporting jobs | Evidence assessment |
|---|---|---|---|---|---|
| **Design a learnable progression** | Sequence Python, HTTP, data modelling, URLs, views, templates, forms, authentication, testing, security, and deployment without overwhelming novices | Feel prepared rather than exposed | Be regarded as a clear, competent teacher *(hypothesis)* | Diagnose prerequisites; select examples; scaffold; fade support | **Direct general evidence plus inference; High confidence.** |
| **Create authentic, motivating practice** | Let students build something recognizably useful while practicing transferable concepts | Sustain energy and avoid watching students disengage | Help students see themselves as capable builders | Use meaningful contexts; incremental features; choice; collaboration | **Direct evidence; High confidence generally, Medium for Django specifically.** |
| **See understanding and intervene in time** | Detect misconceptions, stalled progress, and superficial copying before high-stakes assessment | Reduce helplessness when many learners are stuck | Demonstrate attentive, fair support | Formative checks; code reading; targeted feedback; progress signals | **Direct evidence; High confidence.** |
| **Assess individual learning credibly** | Determine what a student can reason about, debug, and produce, including when AI or peers assisted | Trust the grade and preserve fairness | Maintain legitimacy with students and colleagues | Rubrics; process evidence; oral explanation; tests; AI policy | **Direct current evidence; High confidence that the job exists, Medium on best method.** |
| **Keep the course runnable and current** | Prevent version, dependency, OS, editor, hosting, and stale-instruction failures | Avoid class-time embarrassment and firefighting | Be a reliable guide | Pin/test environments; monitor releases; maintain starter code; fallback plans | **Direct practice facts plus inference; High confidence.** |
| **Support diverse starting points and belonging** | Give novices access without leaving experienced students idle or reinforcing stereotypes | Help learners feel safe asking for help | Build an inclusive learning community | Low-floor/high-ceiling tasks; structured collaboration; relevant contexts; accessible materials | **Direct general CS-education evidence; High confidence, with implementation effects context-dependent.** |

In full audience-progress form:

1. **Design a learnable progression:** When learners must move from varied prerequisites to independent web work, I want to sequence concepts, examples, and fading support, so I can help them progress without avoidable overload.
2. **Create authentic, motivating practice:** When abstract exercises do not reveal why the work matters, I want learners to build something recognizably useful while practicing transferable concepts, so I can sustain engagement and make capability visible.
3. **See understanding and intervene in time:** When a cohort may be copying, stalled, or carrying misconceptions, I want timely evidence of each learner’s understanding, so I can intervene before the problem reaches high-stakes assessment.
4. **Assess individual learning credibly:** When AI, peers, and scaffolds may have contributed to an artifact, I want evidence of what each learner can reason about, debug, and produce, so I can assess learning fairly.
5. **Keep the course runnable and current:** When versions, dependencies, operating systems, editors, or hosting change, I want tested environments and fallback paths, so I can preserve learning time and repeatable delivery.
6. **Support diverse starting points and belonging:** When learners enter with different preparation, access, and confidence, I want low-floor, high-ceiling and inclusive participation structures, so I can support progress without reinforcing exclusion or leaving experienced learners idle.

Developing teaching-specific expertise is supporting work across course design, timely intervention, and course currentness rather than a separate important job. It includes rehearsing lessons, learning likely misconceptions, sharing materials, observing learners, and seeking professional-development peers. **Direct teacher evidence; High confidence.**

## Functional, emotional, and social dimensions

- **Functional:** produce observable learning and transfer while controlling cognitive load, setup risk, feedback latency, grading burden, and content maintenance. **[Direct evidence plus inference; High confidence.]**
- **Emotional — evidenced:** educators want confidence in teaching actual students, not only more subject knowledge. A small 2022 study of seven first-time CS teachers found post-teaching perceptions of their preparation were lower and concluded that confidence and classroom-ready materials deserved more attention. Its sample is too small to estimate prevalence. **[Direct evidence; Low-Medium confidence on generality.]**
- **Emotional — hypothesis:** avoid the guilt and loss of control associated with a cohort failing after too little scaffolding. A 2025 instructor discussion describes exactly this experience, but it is an isolated qualitative signal. **[Direct qualitative signal; Low confidence on prevalence.]**
- **Social — hypothesis:** be seen by learners as technically current, pedagogically fair, and able to connect coursework to authentic practice. Bootcamp review analysis and CS teacher-identity research make this plausible, but Django-specific evidence is absent. **[Inference; Medium-Low confidence.]**
- **Belonging and identity:** inclusive context, community, confidence, and professional identity are learning concerns, not optional atmosphere. NCWIT's research-backed framework organizes engagement around relevance, inclusive community, and confidence/professional identity. **[Direct synthesized guidance; Medium-High confidence.]**

## Triggering situations

**Recurring triggers**

- Planning the next lesson, lab, assignment, code-along, or assessment.
- Observing the same setup error or misconception across several students.
- Supporting a group with widely different prior programming and web knowledge.
- Updating examples after Python, Django, packages, browsers, editors, or hosting change.
- Grading projects and deciding whether the code demonstrates understanding.
- Answering a learner who can reproduce steps but cannot explain the request-to-response flow.

The first four are **[directly evidenced across teacher practice and curricula; High confidence]**. The final two are **[inferences strongly supported by misconception and GenAI evidence; High confidence].**

**Event-triggered situations**

- Being assigned a new CS/web course or asked to add a server-side unit.
- Replacing stale or poorly paced material after a difficult cohort.
- A new course format: bootcamp, short workshop, remote class, large enrollment, or self-paced product.
- A policy change involving AI assistance, academic integrity, privacy, accessibility, or assessment.
- A framework or Python release makes the current environment unsupported.
- Student goals shift toward deployable portfolio work or APIs.

The assignment and reform trigger is **[direct evidence; High confidence in K–12]**. AI is a current trigger: the February 2026 ACM task-force report found 64% of 469 responding computing instructors had changed teaching approaches and 68% of 459 had changed assessments because of GenAI. **[Direct survey evidence; High confidence for respondents, unknown representativeness.]** The remaining triggers are **[inference; Medium-High confidence].**

## Desired outcomes

Directionally measurable outcomes include:

- More learners complete a first working, database-backed application feature within the available course time.
- More learners can predict, trace, explain, test, debug, and modify the code without step-by-step prompts.
- Fewer learners lose lab time to installation, version mismatch, hidden state, or deployment setup.
- Misconceptions become visible earlier; time from a learner becoming stuck to an appropriate intervention falls.
- Assignment completion, pass, retention, and continuation improve without lowering the intended conceptual standard.
- Differences in outcomes by prior experience or learner group narrow; more learners report belonging and confidence.
- Educator preparation, grading, and repetitive support time falls or becomes predictable.
- Student work remains assessable when peers and AI are allowed; learners can disclose assistance and defend decisions.
- Course examples remain runnable across the declared support window.

**[Inference; High confidence as progress directions, Low confidence on numeric benchmarks.]** No evidence found isolates Django's causal effect on these outcomes against another framework.

## Current behaviour or status quo

Educators commonly assemble or adapt a course from official documentation, open curricula, videos, books, prior course repositories, their own professional experience, and peer recommendations. Actual Django paths show several patterns: CS50 Web places Django after HTML/CSS, Git, and Python, then follows it with SQL/models/migrations and later testing, scalability, and security; MDN uses a multi-part Local Library project ending in testing and deployment plus an independent mini-blog assessment; Django Girls uses a guided personal blog, pre-installation, coaches, deployment, and optional extensions. **[Direct evidence of current practice; High confidence that these paths exist, no comparative efficacy claim.]**

Many educators rehearse or modify “canned” material rather than teach it unchanged. In a 2020 CS educator discussion, instructors described running through curriculum, coping with stale links and tool changes, and wanting training about how to teach rather than merely completing student projects. This is a useful practice signal, not representative evidence. **[Direct qualitative evidence; Low-Medium confidence.]**

During class, common mechanisms include short explanation or live coding, worked or partially worked examples, individual or paired practice, projects, formative questions, debugging support, and office hours/mentoring. Pair programming has evidence across 3,308 higher-education students: a 2017 meta-analysis found positive results in assignments, exams, and passing rates but not affective measures. That supports considering structured collaboration, not assuming every pairing works. **[Direct meta-analytic evidence; High confidence within studied settings.]**

## Pushes

- **Setup and toolchain friction consumes teaching time.** Django Girls schedules installation before the workshop specifically to preserve coding time. **[Direct practice evidence; High confidence that the concern is real.]**
- **Existing material becomes stale.** Django's 5.2 tutorial is explicitly versioned, and the 5.2 LTS notes describe compatibility, deprecations, and at least three years of security updates. **[Direct factual evidence; High confidence.]**
- **Students arrive with entrenched misconceptions and uneven prior knowledge.** Targeted-feedback research and prior-experience studies directly document both. **[Direct evidence; High confidence generally.]**
- **A lecture/code-along alone does not reveal whether learners can transfer.** Computing pedagogy emphasizes formative checks, dialogue, projects, and independent assessment. **[Direct synthesized evidence; Medium-High confidence.]**
- **Compressed programs create pressure for visible, job-relevant outcomes.** Bootcamp reviews connect satisfaction to rigor, pedagogy, instructor/mentor support, technology, and career support. **[Direct qualitative evidence; Medium confidence.]**
- **GenAI weakens product-only assessment.** In the ACM task-force survey, instructor concerns included dependency (87%), cheating/plagiarism (72%), and misinformation (53%). **[Direct evidence; High confidence for respondents.]**

## Pulls

- A coherent, integrated stack can support an end-to-end project without requiring the educator to select a router, ORM, form system, administration interface, authentication system, and test integration separately. **[Inference from Django capabilities; High confidence factually, Medium for instructional benefit.]**
- Staying in Python can let a cohort reuse prior language knowledge while learning HTTP, persistence, templates, and deployment. CS50 Web's ordering demonstrates this curriculum choice. **[Direct practice plus inference; Medium confidence.]**
- Generated project structure, migrations, ORM, admin, forms, and authentication can make consequential web concepts visible within a bounded course. They can also hide mechanisms or add vocabulary, so the pull is conditional. **[Inference; High confidence on the tradeoff.]**
- A versioned official tutorial, MDN module, CS50 course, and Django Girls tutorial provide multiple reusable starting points and formats. **[Direct factual evidence; High confidence.]**
- Django Girls demonstrates a beginner-oriented instructional ecosystem: open reusable material, coach guidance, pre-installation, translation, a one-day scope, deployment, and extensions. Its reported reach—1,192 past events and 26,341 attendees on the resources page—is evidence of use, not learning effectiveness. **[Direct evidence; High confidence on use.]**
- Long-term-support releases can reduce how often a course must absorb breaking changes. **[Direct factual evidence plus inference; High confidence.]**

## Anxieties

- **Practical concern:** “Can I teach all the prerequisites and Django in the time?” MDN recommends general programming/Python and prior server-side concepts; Django's own tutorial immediately introduces generated files, packages, settings, URLs, ASGI, and WSGI. **[Direct evidence; High confidence that the concept surface is broad.]**
- **Practical concern:** “Will every student's environment behave the same?” OS, Python, Django, editor, database, browser, and deployment differences are legitimate classroom risks. **[Inference supported by installation/version practices; High confidence.]**
- **Legitimate limitation:** Django can accelerate a working CRUD application while increasing cognitive load through conventions and abstractions. Programming already requires multiple competencies; a 2022 systematic review found cognitive-load research commonly uses worked examples and load measurement. Django-specific cognitive-load studies were not found. **[Direct general evidence plus inference; Medium-High confidence.]**
- **Perceived risk:** built-ins may let learners succeed without understanding HTTP, SQL, authorization, or deployment. This is plausible and should be tested through explanation, modification, and debugging, not assumed from finished output. **[Inference; High confidence.]**
- **Perceived risk:** material may teach a version or hosting workflow that expires mid-course. **[Direct versioning facts plus inference; High confidence.]**
- **Emotional resistance:** instructors with teaching expertise but limited web experience may fear losing authority; developer-instructors may fear lacking pedagogical skill. Secondary CS teachers in one 1,032-person study rated content and technology knowledge higher than pedagogical-content and technological-content knowledge. **[Direct evidence; Medium confidence outside that national context.]**
- **AI anxiety:** learners may submit plausible code they cannot explain, debug, or verify. This is directly reported by computing instructors. **[Direct evidence; High confidence.]**

## Habits and inertia

- Reuse last year's slides, starter repository, dependency pins, grading rubric, and hosting path because changing any one creates preparation and support work. **[Inference; High confidence.]**
- Teach the framework in the order its reference/tutorial presents it, even when the cohort's prerequisite model differs. **[Inference; Medium confidence.]**
- Prefer the language/framework the educator already knows, or one embedded in a mandated curriculum. **[Inference supported by instructor-background research; Medium-High confidence.]**
- Continue step-by-step imitation because it produces a visible result on schedule, even when transfer is uncertain. **[Qualitative signal plus inference; Medium confidence.]**
- Grade the final repository because process, oral defense, and repeated low-stakes assessment cost more time. GenAI is pushing many instructors to change this habit. **[Direct current evidence plus inference; High confidence.]**
- Rely on personal troubleshooting rather than shared instructor notes or community help, especially when the educator is the only CS teacher. Teacher isolation is documented in K–12 research. **[Direct evidence; Medium-High confidence.]**

## Decision criteria

There is no evidence-based ranking for educators choosing a web framework. These importance bands synthesize instructor constraints, pedagogy research, and current curriculum practice.

| Criterion | Importance | Confidence | What the educator needs to judge |
|---|---|---|---|
| Fit to intended learning outcomes and prerequisites | Very high | High | Whether the framework reveals or obscures the concepts students must transfer; assumed Python, web, SQL, and command-line knowledge |
| Teachable sequence and cognitive load | Very high | High generally; Medium for Django | Time to a motivating result; number of simultaneous concepts; quality of worked examples and fading scaffolds |
| Classroom reliability and reproducibility | Very high | High | Supported Python/OS versions, installation steps, starter state, offline/fallback options, deterministic checks |
| Authentic project capability | High | High | Whether students can build, test, secure, and deploy a meaningful application in the course window |
| Formative assessment and debuggability | High | High | Observable checkpoints, common-error explanations, tests, code-reading/debugging tasks, progress visibility |
| Educator-ready support | High | Medium-High | Instructor notes, solutions, misconception guidance, rubrics, extension tasks, update notices, peer help |
| Accessibility, inclusion, and differentiation | High | High generally; Low-Medium for Django evidence | Low-floor/high-ceiling tasks, screen/keyboard accessibility, relevant project choice, structured collaboration |
| Maintenance and version stability | High | High | LTS window, deprecations, compatibility, migration effort, example ownership |
| Assessment integrity in an AI-assisted environment | High and rising | High | Ability to assess comprehension, process, debugging, and explanation under a clear AI policy |
| Industry/career relevance | High in bootcamps; medium elsewhere | Medium | Transferable web concepts, authentic workflows, local opportunity evidence; popularity alone is insufficient |
| Cost and infrastructure | Context-dependent, often high | Medium-High | Student devices, network restrictions, hosting, database, classroom accounts, privacy, and staff time |

## Main concerns

The dominant concern is **instructional tractability**: can one educator help a varied cohort reach independent understanding before setup, abstraction, and support load consume the available time? **[Inference grounded in multiple evidence types; High confidence.]**

Closely related concerns are transferable understanding rather than tutorial completion; early visibility into misconceptions; fair assessment with peer/AI assistance; inclusive participation; reliable deployment; and the ongoing labor of keeping examples, dependencies, and explanations current. **[Direct evidence plus inference; High confidence generally, Medium for Django-specific magnitude.]**

## Objections and perceived risks

- **“Django is too much for beginners.”** A legitimate contextual objection, not a universal truth. A framework that exposes models, migrations, URLs, templates, forms, settings, admin, and deployment can overload learners without prerequisites and staged scaffolding. Django Girls demonstrates that complete beginners can be coached through a bounded blog, but that does not prove independent mastery or suitability for every class. **[High confidence on tradeoff; Low on comparative outcome.]**
- **“The built-ins do too much, so students will not learn the web.”** Plausible but unproven. Educators can surface request flow, generated SQL, authentication boundaries, and deployment explicitly; finished CRUD output alone cannot establish understanding. **[Inference; Medium-High confidence.]**
- **“A real-world framework is automatically motivating and employable.”** Overstated. Relevant, personally meaningful context supports engagement, but employment value depends on market and broader skills. The evidence does not show Django instruction causes employment. **[Direct general evidence; High confidence.]**
- **“The official tutorial is a complete curriculum.”** Unsupported. It is a versioned learning-by-example path, but a curriculum also needs outcomes, prerequisite handling, formative assessment, differentiation, instructor notes, grading, accessibility, pacing, and transfer tasks. **[Direct factual comparison plus inference; High confidence.]**
- **“LTS means course maintenance disappears.”** Incorrect. LTS reduces framework churn but does not freeze Python, packages, browsers, operating systems, editors, or hosting. **[High confidence.]**
- **“Pairing or AI solves limited instructor bandwidth.”** Unsupported as a blanket claim. Pair programming improves several academic outcomes on average but not affective outcomes in the 2017 meta-analysis; AI can provide help while introducing dependency, misinformation, and assessment problems. **[Direct evidence; High confidence.]**
- **“Django is old, therefore not current enough to teach.”** “Current” and the intended outcome need definition. Django 5.2 was released as an LTS in April 2025 and is used in active curricula; this refutes abandonment, not every relevance concern. **[Direct evidence; High confidence.]**

## Information needed to make progress

- A prerequisite map separating Python, command line, Git, HTML/CSS, HTTP, databases/SQL, and deployment from Django-specific concepts.
- A concept sequence tied to observable student actions: predict, trace, explain, modify, test, debug, secure, and deploy.
- Tested setup matrices and precise version/support dates, with recovery paths for common OS and environment failures.
- Instructor notes explaining why each generated file or convention exists, common misconceptions, likely errors, formative questions, and extension paths.
- Evidence of what students can build within a stated number of contact and practice hours, clearly labeled as case evidence rather than causal proof.
- Assessment designs that distinguish product from process and support code explanation, debugging, tests, incremental commits, and disclosed AI use.
- Differentiation options for zero-experience and advanced learners without creating two unrelated courses.
- Accessibility and privacy implications of editors, hosting, third-party accounts, deployment, and example applications.
- A maintenance owner and update path for starter code, dependencies, screenshots, hosting steps, solutions, and rubrics.

These are **[inferred with High confidence]** from the documented readiness, cognitive-load, setup, assessment, and maintenance jobs. The best packaging and sequence require direct instructor research.

## Trusted content formats

- **Runnable, version-pinned exemplar plus checkpoints:** lets the educator rehearse the exact learner path and detect drift. **[Direct practice plus inference; High confidence.]**
- **Instructor guide paired with learner material:** objectives, timing, explanations, misconceptions, solutions, formative questions, accessibility notes, and fallback plans. Django Girls and Software Carpentry demonstrate this separation. **[Direct practice evidence; High confidence.]**
- **Worked example followed by completion, modification, and independent creation:** aligns with programming cognitive-load and PRIMM evidence. **[Direct general evidence; Medium-High confidence.]**
- **Short live-coding or video demonstration paired with written reference:** supports demonstration and later recovery; comparative evidence for the pairing was not found. **[Inference; Medium confidence.]**
- **Project brief, rubric, tests, and sample submissions at different quality levels:** supports authentic practice and grading calibration. **[Inference; High confidence.]**
- **Troubleshooting trees and common-error corpus:** targeted-feedback research supports misconception-aware intervention. **[Direct general evidence plus inference; High confidence.]**
- **Facilitated educator workshop or peer rehearsal:** first-time teacher research favors classroom-ready confidence and material over content knowledge alone. **[Direct but small-sample evidence; Medium confidence.]**

## Discovery, evaluation, validation, and engagement channels

- **Discovery:** educator colleagues, teaching communities such as CSTA, course repositories, conferences/PD, search, and practitioner recommendations expose possible stacks and curricula. Instructor discussions show peers being asked for curriculum maps and classroom routines. This supports the behavioral role, not channel prevalence. **[Direct qualitative evidence; Medium-Low confidence.]**
- **Evaluation:** official versioned documentation, a learner-facing tutorial, instructor notes, sample syllabus, dependency/support policy, and a rehearsal of the complete assignment help estimate concept load and classroom failure points. CS50, MDN, Django Girls, and the Django tutorial are direct evaluation artifacts. **[Direct evidence of availability, inferred behavior; Medium-High confidence.]**
- **Validation:** teaching a small pilot, observing whether students can explain and modify the project, checking with experienced instructors, and reviewing current course implementations provide stronger validation than popularity. A deployed demo validates technical feasibility; student work validates teachability. **[Inference; High confidence conceptually, no prevalence data.]**
- **Ongoing engagement:** release notes and official docs support version maintenance; GitHub repositories support issue reporting and curriculum adaptation; teaching communities support pedagogy; Django Forum/Stack Overflow can help with technical failure cases. **[Direct channel affordances plus inference; Medium confidence.]**

No solid evidence was found that Django Discord, mailing lists, podcasts, or short-form social materially drive educator evaluation or teaching practice. Conferences and professional networks are plausible discovery/engagement channels, but direct educator-specific behavioral data is limited.

## Decision-makers and influencers

In an independent course or workshop, the educator may be initiator, evaluator, approver, operator, support desk, and bearer of student-outcome consequences. Learners influence continuation through observed progress, questions, attendance, submissions, and feedback. Mentors/TAs shape whether the selected approach is supportable. **[Inference; High confidence.]**

In schools and universities, a department, exam specification, curriculum committee, IT/security team, accessibility office, or LMS policy may preselect content or block tools. The individual educator still decides pacing, explanation, examples, scaffolding, formative checks, and much day-to-day adaptation. In bootcamps, program owners and employer promises may constrain the stack and pace, while instructors and mentors bear immediate delivery consequences. **[Inference supported by institutional and bootcamp evidence; Medium-High confidence.]**

Students, former students, teaching assistants, other instructors, developer practitioners, education researchers, and framework communities influence judgment. Framework maintainers provide authoritative version and security information; they are not authoritative on local learning outcomes without educational evidence. **[Inference; High confidence.]**

## Appropriate next actions for Django to encourage

These actions advance an educator's teaching job; they are not asset or campaign recommendations.

1. **State the cohort's intended outcomes and prerequisites before selecting a framework path** → serves the learnable-progression job.
2. **Run the entire learner setup and first feature on the actual classroom environments** → serves the reliability job.
3. **Teach one thin request-to-response slice, then ask learners to predict and modify it** → serves understanding and transfer.
4. **Add low-stakes checks for misconceptions at each abstraction boundary** → serves early intervention.
5. **Move from worked example to completion, modification, and an original feature** → serves authentic independent practice.
6. **Use structured pair/peer work with explicit roles and individual explanation** → serves collaboration without surrendering assessment.
7. **Require tests, debugging, process evidence, and a brief code defense under a declared AI policy** → serves credible assessment.
8. **Deploy a bounded project with security and operations responsibilities made explicit** → serves authentic web-system understanding.
9. **Record version pins, support dates, known failure modes, and the next maintenance review** → serves course currency.
10. **Share one observed misconception or teaching adaptation with educator peers or the relevant curriculum repository** → serves teaching-specific expertise and reduces isolation.

**[Inference; High confidence in job alignment, Low confidence on comparative completion effects until tested.]**

## Overlaps with other audiences

- **First-time programmers and Python developers new to web:** they are the learners whose readiness and motivations shape this educator's choices; they do not share the educator's cohort-level job.
- **Bootcamp/career-changing learners:** overlap through employment-oriented projects and compressed pacing, but career investment is the learner job and teaching effectiveness is the educator job.
- **Existing Django professionals:** an educator may also be a professional developer who needs current best practice; pedagogical-content knowledge remains distinct from framework expertise.
- **Institutional education decision-makers:** they set standards, budgets, staffing, procurement, and approved platforms; this audience adapts and teaches within those constraints.
- **Community organizers and mentors:** workshop organizers overlap operationally; coaches belong here when explaining and supporting learning.
- **Contributors:** educators may contribute tutorial corrections, translations, examples, or misconception reports, but contribution is a supporting behavior, not the primary job.

## Possible segmentation problems

- “Educator” hides enormous differences in age, prerequisites, cohort size, duration, assessment stakes, and instructor autonomy.
- Bootcamp teachers should not be treated as a proxy for all career educators; satisfaction and employment pressure change the job.
- A course creator with no live learners has maintenance and explanation jobs but less direct intervention work.
- A developer who presents a one-hour workshop is not equivalent to a trained teacher, though both may need instructor-ready material.
- Framework selector and framework teacher may be different people; assuming the teacher controls adoption confuses institutional and individual jobs.
- Django may be the object of instruction, a vehicle for teaching web concepts, or incidental infrastructure for a domain project. These contexts require different criteria.
- Beginner workshop completion, semester learning, portfolio quality, and employment are different outcomes and must not be merged.
- Most cited studies concern introductory programming rather than web frameworks, and much teacher-survey evidence is U.S. K–12. Transfer to global higher education and independent training is uncertain.

## Existing-analysis claim audit

No supplied hypothesis directly names individual educators; that omission itself requires research. Relevant adjacent claims are audited below.

| Existing-analysis claim | Audit | Evidence and limits |
|---|---|---|
| Early-career/self-taught/bootcamp/CS/career-changing developers evaluate a framework as a career investment, portfolio tool, modern-app tool, and route to community; homepage/social/video/community discovery is claimed. | **Partially supported** | Educators do design for authentic projects, confidence, belonging, and—in bootcamps—career outcomes. CS50 and bootcamp evidence support project/career context. This does not establish that all learners evaluate frameworks themselves; educators often preselect them. No evidence here validates homepage or short-form social as important educator channels. |
| Existing professional Django developers seek current best practice, releases/upgrades, scaling help, greater expertise, and possible progression from user to contributor. | **Partially supported for educator-developers** | Version currency, testing, security, deployment, and release compatibility matter to keeping a course credible and runnable. Educator progression to contribution is plausible through open curriculum repositories but was not evidenced as a central job. |
| Claimed touchpoints include docs/release notes, forums/Discord, GitHub/issue tracker, mailing lists, conferences/sprints, podcasts, professional peer networks, and short-form social. | **Partially supported** | Official docs and release notes serve evaluation/maintenance; GitHub supports curriculum adaptation/issues; educator peers and PD serve discovery/engagement; technical forums serve troubleshooting. Evidence is insufficient for Discord, mailing lists, podcasts, sprints, or short-form social as material educator channels. |
| Ecosystem/core contributors seek recognition, governance understanding and influence, co-maintainers, less burnout, and a clear participation pathway. | **Requires further research for overlap** | Individual educators may maintain teaching materials or contribute fixes, but this research found no evidence that recognition/governance is part of their core teaching job. Do not project contributor motivations onto them. |

## Evidence table

| Finding | Source (title, publisher/author, date, URL) | Evidence type | Direct evidence or inference | Confidence | Research notes |
|---|---|---|---|---|---|
| U.S. PK–12 CS teachers report limited preparation, workload/time constraints, and inconsistent support; only 17% can access PD as needed. | [2025 Computer Science Teacher Landscape Report, CSTA/Kapor Center, 2025](https://landscape.csteachers.org/) | Nationwide survey summary, n=2,882 | Direct | High for surveyed U.S. PK–12 teachers | Not higher education, bootcamps, or global evidence. |
| First-time CS teachers wanted confidence teaching actual learners and classroom-ready material, not only more content knowledge. | [K-12 Teachers' Perceptions and Experiences in Starting to Teach Computer Science, Northrup et al., *Education Sciences*, 2022](https://doi.org/10.3390/educsci12110742) | Pre/post quantitative study | Direct | Low-Medium | Only seven teachers taught after the endorsement; useful depth, very limited generality. |
| Programming requires multiple competencies; worked examples are prominent in cognitive-load evidence. | [Cognitive Load Theory in the Context of Teaching and Learning Computer Programming, Berssanette & de Francisco, *IEEE Transactions on Education*, Aug. 2022](https://eric.ed.gov/?id=EJ1345090) | Systematic literature review, 2010–2020 | Direct generally; inferred for Django | High generally, Medium for Django | No Django-specific effect estimate. |
| Misconception-aware, targeted feedback can reduce unproductive attempts and support conceptual change. | [Using Targeted Feedback to Address Common Student Misconceptions in Introductory Programming, Qian & Lehman, 2019](https://doi.org/10.1177/2158244019885136) | Design-based empirical study | Direct | Medium | High-school Java context; transfer to Django/web instruction is inference. |
| PRIMM uses prediction, running, investigation, modification, and making to support dialogue and attainment. | [Teaching computer programming with PRIMM: a sociocultural perspective, Sentance, Waite & Kallia, 2019](https://eprints.gla.ac.uk/229013/) | Empirical pedagogy study | Direct generally; inferred application | Medium-High | Secondary-school programming, not web-framework selection. |
| Pair programming showed positive effects for assignments, exams, and pass rates, but not affective measures. | [A Meta-Analysis of Pair-Programming in Computer Programming Courses, Umapathy & Ritzhaupt, ACM TOCE, Sept. 2017](https://eric.ed.gov/?id=EJ1252509) | Meta-analysis, 18 manuscripts, 3,308 students | Direct | High within studied higher education | Does not justify unstructured pairing or effects in every cohort. |
| Bootcamp experience is shaped jointly by instructor quality, mentors/TAs, curriculum rigor, pedagogy, technology, peer environment, and career support. | [Coding Bootcamp Satisfaction: A Research Model and Survey Instrument, Lang & Sharp, ISEDJ, Apr. 2022](https://isedj.org/2022-20/n2/ISEDJv20n2.pdf) | Qualitative content analysis of learner reviews | Direct | Medium | One review platform; model proposed, not quantitatively validated. |
| GenAI is already changing teaching and assessment; dependency, cheating, and misinformation lead concerns. | [ACM Task Force on Generative AI and Programming Assessment report, Gordon et al., Feb. 16, 2026](https://acm-education-genai-task-force.github.io/ACM_Taskforce_GenAI_Report_16Feb26.pdf) | Instructor survey and qualitative responses | Direct | High for respondents; Medium for prevalence | 64% of 469 changed teaching; 68% of 459 changed assessment; sampling limits should be checked before population claims. |
| Most surveyed K–12 CS teachers think AI belongs in fundamental CS and want more resources/PD. | [Guidance on the Future of Computer Science Education in an Age of AI, TeachAI & CSTA, updated July 7, 2025](https://www.teachai.org/cs) | Survey-backed professional guidance, n=364 in 2024 | Direct | Medium-High | 85% inclusion; 88% want resources/PD; K–12 focus. |
| Relevance, inclusive community, confidence, and professional identity support engagement and persistence. | [NCWIT Engagement Practices Framework, NCWIT, Nov. 11, 2025](https://ncwit.org/resource/ncwit-engagement-practices-framework/) | Research-backed practice synthesis | Direct synthesis | Medium-High | Underlying studies vary; not Django-specific. |
| A live Django curriculum can sequence HTML/CSS, Git, Python, Django, data, JavaScript, testing, scalability, and security around projects. | [CS50's Web Programming with Python and JavaScript: Projects, Harvard/CS50, current page accessed July 18, 2026](https://cs50.harvard.edu/web/projects/) and [Spring 2025 syllabus](https://cs50.harvard.edu/extension/web/2025/spring/syllabus/) | Deployed curriculum and syllabus | Direct practice evidence | High for existence, Low for causal outcomes | Demonstrates one prerequisite/sequence choice, not superiority. |
| MDN offers a multi-part Django project from setup through testing/deployment plus an independent assessment. | [Django Web Framework (Python), MDN Web Docs, last modified Apr. 11, 2025](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Server-side/Django) | Open learning module | Direct practice evidence | High for existence | Lists programming/Python and server-side concepts as readiness guidance. |
| Beginner workshop design separates pre-installation, learner tutorial, coaching practice, one-day scope, deployment, and extensions. | [Django Girls Resources, current page accessed July 18, 2026](https://djangogirls.org/en/resources/) and [Coaching Manual](https://coach.djangogirls.org/intro/) | Large-scale community curriculum/practice | Direct | High for practice; Low-Medium for learning efficacy | Reach counts are usage, not controlled outcomes. |
| Django's official first-app tutorial is version-specific and immediately exposes a broad generated project structure. | [Writing your first Django app, part 1, Django 5.2 documentation, accessed July 18, 2026](https://docs.djangoproject.com/en/5.2/intro/tutorial01/) | Official technical documentation | Direct | High | Authoritative on Django, not on pedagogy. |
| Django 5.2 is an LTS with compatibility/deprecation information and at least three years of security updates. | [Django 5.2 release notes, Django project, Apr. 2, 2025](https://docs.djangoproject.com/en/dev/releases/5.2/) | Official release documentation | Direct | High | Supports maintenance judgments, not student outcomes. |
| Teachers ask peers how to handle wide prior-experience ranges and revise project sequencing after unsuccessful delivery. | [Teaching CS in High School: How Do You Approach Curriculum?, r/CSEducation, Oct. 17, 2024](https://www.reddit.com/r/CSEducation/comments/1g5hu3t/) | Instructor discussion | Direct qualitative signal | Low | Useful for language and edge cases; not representative. |
| Educators report rehearing canned curriculum, grading friction, stale content, and a need for teaching practice rather than simply doing projects. | [Preparing for class when using canned CS curriculum, r/CSEducation, June 5, 2020](https://www.reddit.com/r/CSEducation/comments/gx6xk3/) | Instructor discussion | Direct qualitative signal | Low | Older isolated thread; triangulated with current workload and PD evidence. |
| Teacher knowledge can be stronger in content/technology than in their combinations with pedagogy. | [Measuring the TPACK of in-service computer science teachers, Doukakis et al., 2021](https://arxiv.org/abs/2105.09252) | National survey, n=1,032 secondary teachers | Direct | Medium | One national context; self-ratings; supports segmenting developer expertise from teaching expertise. |

## Unanswered research questions

1. What learning outcome is Django most effective at supporting: introductory web mental models, database-backed CRUD, secure full-stack practice, APIs, deployment, or software engineering integration?
2. For which prerequisite profiles and course lengths does Django's integrated surface reduce total cognitive load, and when does it add too much?
3. How do completion, transfer, misconception, retention, and belonging compare across Django-based sequences and other instructional approaches after controlling for instructor and cohort?
4. Which Django abstractions most commonly produce novice misconceptions—project/app structure, URL dispatch, ORM/querysets, migrations, templates, forms, authentication, class-based views, settings, or deployment?
5. What do individual university, bootcamp, independent, and global-south educators actually use to discover, evaluate, and maintain Django curricula?
6. How much unpaid preparation and repetitive support time does a Django unit require by cohort size and environment, and which supports reduce it?
7. What evidence would persuade an educator to adopt, continue, revise, or stop teaching with Django after a pilot?
8. How do student device limitations, unreliable internet, disability access, third-party account requirements, and hosting/privacy rules affect feasibility?
9. Which assessment patterns validly distinguish understanding from copied, peer-produced, or AI-generated Django code without making grading unmanageable?
10. Do LTS-based course environments materially reduce maintenance incidents over an academic year, including third-party packages and hosting?
11. What instructor notes, error corpora, formative questions, rubrics, and project variants are most reusable across settings?
12. How often is the individual educator actually the framework decision-maker, versus an implementer of institutional or commercial curriculum?
