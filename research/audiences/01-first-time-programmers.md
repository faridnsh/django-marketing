# First-time programmers seeking a first web-building success

## Audience definition and boundaries

This audience consists of people with no programming experience or only enough experience to be learning variables, control flow, functions, errors, files, and basic command-line use. They may be school or university students, adult hobbyists, people automating part of another job, or career-curious adults. Age, employment status, and formal education do not define the audience; practical programming independence does.

The more useful boundary is **readiness, not identity**. A learner exits this audience when they can independently write and debug small Python programs and explain basic web request/response concepts. They may then become an early-career, self-taught, bootcamp, CS, or career-changing framework evaluator. The two groups overlap, but should not be merged: the first-time programmer is choosing a learning path and trying to establish capability, while the framework evaluator can compare architecture, ecosystem, employability, and production fit.

Django is usually one layer above this audience's immediate starting point. Django 6.0's own getting-started page says learners get more from Django with “minimal comfort” in Python and sends people entirely new to programming to Python resources. MDN places general server-side and client/server understanding before its Django module. At the same time, Django Girls demonstrates that a coached, end-to-end sequence can take people with no previous programming knowledge through command line, Python, Django, HTML/CSS, and deployment to a first web application. Therefore Django is plausible as a **scaffolded first project context**, not well evidenced as a standalone first programming abstraction. (Direct evidence; confidence: High.)

## Important subsegments

- **Teacher-led beginners:** students whose sequence, tools, pace, and often language are selected by an instructor or curriculum. Their “decision” is frequently whether to persist, not whether to adopt Django.
- **Independent hobby or personal-project beginners:** adults or young people starting from curiosity or a website idea. They control the path but face resource-selection and help-seeking burdens.
- **Career-curious beginners and career changers at day zero:** motivated partly by future work, but not yet equipped to evaluate a framework as a career investment. They become a separate early-career audience as competence grows.
- **Work-adjacent beginners:** people learning to automate or create a small internal/personal tool while their primary identity remains analyst, researcher, educator, administrator, or small-business owner.
- **Workshop-supported beginners:** learners in a short, mentor-rich event such as Django Girls. This context can compress prerequisites because coaches absorb setup and debugging burden.
- **Access-constrained beginners:** learners sharing devices, using low-spec hardware, working in a second language, or relying on intermittent connectivity. Device, installation, time, cost, and language can dominate any framework-level consideration.

These are contexts rather than mutually exclusive personas. Evidence is strongest for higher-education learners and Django Girls attendees, and much weaker for minors, older adults, disabled learners, low-connectivity learners, and beginners outside English-language communities. (Direct evidence about studied samples; confidence: High. Segmentation synthesis: inference; confidence: Medium.)

## Primary job to be done

> **When I decide to try programming because I want to create something or test whether coding is for me, I want to turn understandable steps into a small working program I can explain and change, so I can experience real progress and decide confidently whether to continue.**

This job is not “learn Django.” The desired progress is a credible mastery experience: the learner can connect an action to an outcome, recover from at least simple errors, and make a personally meaningful change. The 2024 JetBrains learner survey found creative and problem-solving motives alongside practical ones, and hands-on projects were the most strongly valued course-design feature. Django Girls' explicit outcome is a small working web application put online. (Direct evidence for motives and project preference; inferred JTBD synthesis; confidence: Medium-High.)

**Job hierarchy:** functional core (produce, understand, and change a working artifact); emotional support (gain confidence through a mastery experience); social support, when relevant (show the artifact or learn alongside others); supporting jobs (setup, foundational Python/web concepts, debugging, and next-step selection).

## Additional jobs to be done

1. **Build a usable mental model:** When code or generated project files behave unexpectedly, I want an explanation of what ran and why, so I can predict the next result instead of copying blindly. **Dimensions:** functional core; emotional support through reduced helplessness.
2. **Get unstuck without surrendering the learning:** When an error blocks me, I want timely, level-appropriate guidance that reveals the next diagnostic step, so I can continue and learn how to recover. **Dimensions:** functional support; emotional core; social support where help comes from a person or community.
3. **Find a bounded path through a vast field:** When many languages, tools, tutorials, and opinions compete for attention, I want a progressive sequence with explicit prerequisites and outcomes, so I can spend scarce time practicing rather than continually re-choosing. **Dimensions:** functional support; emotional support through reduced overload.
4. **Create something that matters to me or that others can see:** When abstract exercises feel detached from my reason for starting, I want to customize and, where appropriate, share a small artifact, so I can make progress feel relevant and concrete. **Dimensions:** functional core; emotional core; optional social support through sharing.
5. **Test belonging and capability:** When difficulty makes me question whether I am “a programming person,” I want normalised struggle, respectful support, and evidence of my own progress, so I can decide based on interest rather than avoidable intimidation. **Dimensions:** emotional and social core; functional mastery experiences as support. This is a hypothesis supported by introductory-CS belonging/self-efficacy research but not measured specifically for independent Django beginners.
6. **Assess the next investment:** When I complete a first project, I want to know what I understood, what the framework handled, and what to learn next, so I can choose whether to continue toward web development, another computing path, or a non-career use. **Dimensions:** functional support; emotional support through an informed, non-shaming decision.

Jobs 1–4 have direct support from learner surveys, curricula, and programming-education research; confidence: Medium-High. Jobs 5–6 are cross-source inferences; confidence: Medium.

## Functional, emotional, and social dimensions

- **Functional:** run code; understand basic cause and effect; make a small change; diagnose a simple failure; finish and optionally deploy an artifact; know the next prerequisite. Direct evidence; confidence: High.
- **Emotional:** reduce intimidation, frustration, and imposter feelings; feel capable enough to persist; preserve curiosity. **Hypothesis for Django-specific learners**, supported directly in broader CS learners and introductory courses; confidence: Medium.
- **Social:** be able to show a result to friends, classmates, mentors, or family; ask questions without status loss; see people with relevant backgrounds participating. **Hypothesis**, with belonging and Django Girls evidence but little first-time-Django causal research; confidence: Medium.
- **Supporting jobs:** install or access a working environment, interpret terminology, manage limited study time, judge source quality, and receive feedback. Direct evidence in curricula and learner surveys; confidence: High.

## Triggering situations

**Recurring triggers** include curiosity about how software works; a recurring manual task; desire for a personal site or small tool; exposure through school; and seeing a peer create something. Creative interest, problem-solving, automation, hobbies, and creating a website/game all appear in the JetBrains survey, although its sample includes many experienced learners. (Direct evidence; confidence: Medium.)

**Event-triggered situations** include enrolling in an introductory course or workshop; a teacher assigning a web project; a role change or redundancy prompting career exploration; a friend or relative's invitation; or acquiring reliable device/time access. A Django Girls event is a particularly strong event trigger because the schedule, mentor, peer group, and “first web application” outcome arrive together. (Direct evidence for course/workshop contexts; inference for relative trigger strength; confidence: Medium.)

## Desired outcomes

- Reach a first visible output quickly enough to connect code with effect, then progress to a small app rather than remaining in setup.
- Complete a bounded sequence and make at least one un-scripted change that still works.
- Explain, in beginner language, the roles of Python, Django, browser, server, URL, view, template, model, and database at the level encountered.
- Recover from a simple syntax, configuration, or routing error with an explicit diagnostic process.
- Put a small artifact where another person can see it when sharing is safe and desired.
- Finish knowing the next step and whether continued learning still serves the learner's underlying goal.

These are directionally measurable outcomes, not evidence-backed numeric targets. Django Girls directly establishes completion of a small deployed blog as feasible in a coached path; independent completion, comprehension, time-to-success, and continuation rates by pathway remain unmeasured. (Direct evidence plus operational inference; confidence: Medium.)

## Current behaviour or status quo

Beginners commonly combine structured courses, coding platforms, videos, documentation, search, forums, AI assistants, books, teachers, friends, and classmates. In the 2025 Stack Overflow survey, respondents aged 18–24 used documentation, general online resources, Stack Overflow, videos, and school; this is not a pure first-timer sample. JetBrains' 2024 learner survey similarly found coding platforms, YouTube, and documentation to be leading learning resources, with Google, AI assistants, Stack Overflow, YouTube, friends/classmates, and educators used for questions.

They often start with language fundamentals before web frameworks. The same JetBrains survey recorded C, Python, Java, and C++ as the most common first languages, and CS50—explicitly designed for people with or without prior experience—places programming fundamentals, Python, SQL, and browser technologies before a server framework. Some learners nevertheless follow an end-to-end Django tutorial immediately, particularly in workshops. (Direct evidence; confidence: Medium because samples blend experience levels and educational traditions.)

Qualitative Django and learn-programming threads repeatedly show beginners asking how much Python and web knowledge is required, reporting confusion about many files/imports, or being advised to learn Python basics first. These are useful signals of vocabulary and anxiety, not prevalence estimates. (Direct qualitative evidence; confidence: Low for representativeness, Medium for identifying recurring concerns.)

## Pushes

- Abstract exercises do not produce the website, automation, or visible artifact that motivated the learner.
- Unengaging or irrelevant content, too little practice, and time pressure make the current path feel ineffective. JetBrains reports these among stated reasons for quitting courses.
- Repeated setup failures, opaque errors, and fragmented tutorials stall momentum.
- An upcoming class, workshop, or personal deadline creates urgency for a complete path.
- A prior welcoming encounter or small success weakens the belief that programming is inaccessible.

Direct evidence for general learning pushes; confidence: Medium-High. Django-specific magnitude is unknown.

## Pulls

- A concrete, visible outcome: a working data-backed site rather than isolated snippets.
- Python's broad learning relevance and Django's included project structure, database mapping, forms, admin, and development server can make sophisticated behavior visible quickly.
- A progressive, copyable path with explanations, checkpoints, and an explicit end state.
- Free/open access, cross-platform instructions, translations, mentors, and a respectful community.
- The prospect of customizing and sharing the result, then continuing into deeper web skills.

The “batteries included” pull is double-edged: it accelerates output but can conceal causal understanding. Evidence for quick end-to-end output is direct from Django/Django Girls curricula; evidence that these pulls determine selection is inferential; confidence: Medium.

## Anxieties

- “I am not technical/a real programmer” or everyone else has prior experience.
- The number of concepts—Python, terminal, packages, virtual environments, HTTP, HTML/CSS, database, framework, Git, and deployment—will be overwhelming.
- An error means lack of aptitude rather than a normal debugging event.
- Following instructions will create a site without creating transferable understanding.
- Version or operating-system differences will make the tutorial fail.
- Asking a “basic” question will invite judgment; AI may answer instantly but incorrectly or do the learning on the user's behalf.
- The time or money spent may not lead to a useful capability or enjoyable practice.

Complex concepts, getting stuck, field vastness, imposter syndrome, root-cause identification, lack of guidance, and stack overload all appear in the JetBrains survey. A 2024 systematic review finds debugging difficult and consequential for beginners, affecting frustration, self-assessment, and persistence. (Direct evidence for broader novice populations; confidence: High. Django-specific ordering: unknown.)

## Habits and inertia

Learners remain with familiar media and low-commitment activities: sequential video watching, copying examples, restarting courses, searching each error, asking an AI for finished code, or postponing projects until they “know enough.” Self-paced tutorials and free MOOCs are also the most commonly reported type of recently abandoned course in the JetBrains sample, suggesting accessibility alone does not create persistence.

Changing paths has a cost: a new instructor, editor, vocabulary, and sequence can reset the sense of progress. Conversely, a school or mentor-selected stack has strong inertia because the human support is attached to it. These behavioral interpretations are inference from survey and qualitative evidence; confidence: Medium-Low.

## Decision criteria

The following tiers reflect evidence strength, not a universal rank.

**High importance / Medium-High confidence:**

- Hands-on exercises and a meaningful finished project.
- Progressive structure, clear objectives, and explicit prerequisites.
- Explanations that simplify concepts without hiding what the learner needs to understand.
- Fast, comprehensible feedback and a route to help when stuck.
- Affordable access, usable materials, and compatibility with the learner's device/operating system.

**Likely important / Medium confidence:**

- Time flexibility, manageable session size, and ability to resume after interruption.
- Current, internally consistent instructions and dependency versions.
- Supportive community, empathetic mentor/instructor, inclusive environment, and language accessibility.
- Relevance to personal goals and a visible/shareable result.

**Context-dependent / Low-Medium confidence:**

- Certification, career guidance, industry reputation, portfolio value, or peer collaboration. These matter more to some career-curious or formally enrolled learners than to the audience as a whole.

JetBrains respondents rated hands-on projects, structured curricula, clear objectives, access to materials, and feedback strongly; however, the study is not restricted to first-time programmers and was recruited partly through JetBrains/Hyperskill and tech channels. No evidence supports a universal framework-selection ranking for this audience.

## Main concerns

**Practical concerns:** setup, device/OS differences, terminology, tutorial currency, time, cost, accessibility, language, and getting timely help.

**Legitimate limitations:** Django introduces multiple layers at once and assumes at least minimal Python comfort; framework conventions and generated structure can exceed a first-timer's mental model; deployment adds external-service complexity. These limitations can be mitigated by scaffolding but not wished away.

**Perceived risks:** “Django is too big for a beginner,” “framework code is not real programming,” or “I must master all Python/web development before starting.” Each contains a partial truth but becomes misleading when stated absolutely: a coached path can work from zero, while an unsupported framework-first path can indeed overload the learner.

**Misconceptions:** Python and Django are alternatives; successful tutorial completion equals independent proficiency; every generated file must be understood immediately; errors demonstrate unsuitability.

**Emotional resistance:** intimidation, shame in asking, fear of wasting time, and discouragement from slow progress. Broader learner data supports the categories, but their Django-specific prevalence is unknown. (Mixed direct evidence and inference; confidence: Medium.)

## Objections and perceived risks

- **“I should learn Python first.”** Substantially legitimate. Django itself recommends minimal Python comfort. A zero-experience Django path must deliberately teach or provide the needed Python rather than imply no prerequisite burden.
- **“There are too many files and concepts.”** Legitimate cognitive-load concern. Generated conventions reduce typing while increasing the number of relationships to explain.
- **“I copied a blog but cannot build my idea.”** Legitimate transfer risk. Worked examples help novices, but open-ended use introduces decision, search, and integration barriers.
- **“A simpler or browser-only environment would let me start faster.”** Contextually legitimate, especially where setup is the dominant blocker. The appropriate choice depends on whether the immediate job is programming fundamentals or an end-to-end web artifact.
- **“AI can build it for me.”** AI can explain and unblock, but generated correctness is not evidence of learner understanding. Stack Overflow's 2025 survey shows high AI adoption alongside lower favorable sentiment among learners than professionals; novice-specific learning effects remain unsettled.
- **“This will get me a job.”** Unsupported as a first-project promise. Django Girls' older follow-up suggests continued learning and later tech employment for some attendees, but it explicitly warns of positive response bias and cannot establish causality.

## Information needed to make progress

- A readiness description in tasks, not labels: what Python, terminal, HTML, and web ideas are needed now, and where each will be taught.
- A map from the learner's goal to an appropriate sequence and a clear definition of the first finished outcome.
- A plain-language system map showing browser request → URL routing → view → model/template → response.
- Installation paths by operating system, plus a browser/cloud option where appropriate and recovery steps for common failures.
- Explanations of what generated commands/files do, which details can wait, and where the learner should experiment.
- Error-reading and debugging routines, with examples that teach diagnosis rather than only provide a fix.
- Expected time/effort ranges stated honestly as context-dependent, along with pause/resume checkpoints.
- How to ask for help safely: include goal, command, full error, expected/actual result, versions, and attempted steps.
- What tutorial completion does and does not demonstrate, and a next project that requires meaningful modification.

This synthesis follows direct evidence on novice difficulties, course choice, help seeking, and Django prerequisites; confidence: Medium-High.

## Trusted content formats

Beginners use multiple formats for different jobs. **Guided interactive exercises** create practice and feedback; **short demonstrations** make unfamiliar actions visible; **written step-by-step tutorials** provide searchable, resumable instructions; **annotated worked examples and diagrams** build mental models; **error clinics/checklists** support recovery; **live workshops, office hours, or mentor sessions** add adaptive help and emotional safety; **small capstone projects** test transfer.

Documentation is widely used, but novice web-search research shows that locating and applying useful pages is itself difficult. Trust therefore depends on visible version/date, prerequisite clarity, reproducibility, explanation of expected output, and a maintained correction route—not merely institutional authority. Videos are strong for discovery and demonstration but weak as the sole debugging reference; written text is easier to scan and compare against local output. AI chat is useful for explanation and question reformulation, but should be treated as guided assistance requiring verification. (Direct evidence for use patterns and novice search difficulty; format-to-job mapping is inference; confidence: Medium.)

## Discovery, evaluation, validation, and engagement channels

- **Discovery:** teachers, school curricula, friends/family, workshops, search, coding platforms, YouTube, social/tech content, and AI assistants introduce the possibility of learning or a project path. No evidence shows the Django homepage is a major discovery channel for true first-timers.
- **Evaluation:** course outlines, prerequisite lists, sample lessons, setup checks, small first exercises, instructor/mentor advice, and learner discussions help judge whether the path is understandable and achievable. Framework production testimonials are remote from this job.
- **Validation:** a locally running result, automated exercise feedback, successful customization, mentor review, a deployed small app, and stories from genuinely comparable beginners validate progress. Search and forums validate specific fixes only when the learner can reproduce and understand them.
- **Ongoing engagement:** a progressive curriculum, recurring class/workshop cohort, beginner-safe forum or Discord space, peer group, mentor, and next project sustain practice. Documentation becomes more useful as vocabulary and self-directed search skill grow.

The 2024 JetBrains and 2025 Stack Overflow surveys directly support search, documentation, video, courses, AI, peers, and educators as learning/help channels, but neither isolates first-time Django learners. Django documentation offers Discord and forum help, while behavioral usage by this audience is not measured. Release notes, mailing lists, issue trackers, conferences/sprints, podcasts, professional networks, and short-form social may serve later audiences; there is insufficient evidence that they are meaningful first-time-programmer evaluation channels. (Direct evidence plus role inference; confidence: Medium.)

## Decision-makers and influencers

- **Independent adult:** usually initiator, evaluator, approver, user, and bearer of time/cost consequences; friends, creators, teachers, and online communities influence.
- **School/university learner:** instructor or department selects the sequence and tools; institution may approve platforms; learner bears workload, assessment, and belonging consequences; classmates and teaching assistants strongly influence persistence.
- **Minor:** teacher/program organizer selects; parent or guardian may approve time, device, travel, privacy, and cost; learner bears learning and social consequences.
- **Workshop learner:** organizer and curriculum select Django; coaches act as evaluators and blockers/unblockers; sponsors/venues enable access; participant decides whether to attend and continue.
- **Work-adjacent beginner:** manager may authorize time or tooling and colleagues validate usefulness; the learner bears maintenance and learning costs.

Role mapping is contextual inference supported by observed course/workshop structures; confidence: Medium.

## Appropriate next actions for Django to encourage

These are learner actions, each tied to a job, not asset or campaign recommendations.

1. **Take a short readiness check and, if needed, complete Python fundamentals** — serves the bounded-path and mental-model jobs.
2. **Run one tiny Django request end to end and predict the output before refreshing** — serves visible progress and causal understanding.
3. **Change one field, route, view, and template element with an explanation of the effect** — tests transfer beyond copying.
4. **Use a beginner debugging routine on a deliberately introduced error** — serves getting unstuck without surrendering learning.
5. **Ask one well-formed question in a coached or beginner-safe setting** — builds help-seeking skill and tests social safety.
6. **Customize and, if desired, deploy a bounded personal project** — creates a meaningful, showable result.
7. **Reflect on what Python did, what Django provided, what remains unclear, and choose the next learning step** — serves informed continuation rather than premature framework loyalty.

Appropriateness is inferred from the job hierarchy and educational evidence; confidence: Medium.

## Overlaps with other audiences

- **Early-career/self-taught/bootcamp/CS/career-changing developers:** overlap in motivation and learning channels; differ in ability to evaluate Django as career or architecture investment.
- **Educators and workshop organizers:** often control the first-timer's path and absorb support burden; their job is instructional effectiveness and inclusion, not the learner's mastery job.
- **Existing Django developers:** may mentor beginners, but seek current practices, upgrades, scaling, or contribution rather than first capability.
- **People in non-developer roles:** may remain work-adjacent beginners even when the goal is automation rather than a developer career.
- **Underrepresented or access-constrained learners:** cross-cutting contexts that change support, belonging, language, hardware, and cost needs; they are not a single motivational segment.

## Possible segmentation problems

“First-time programmers” can be too broad because a 12-year-old in class, an adult hobbyist, and a displaced worker share low experience but not decision authority, time, risk, or outcome. It also becomes misleading when used as shorthand for “junior developer”: professional aspirations do not establish programming readiness.

A better operational segmentation combines **readiness** (no code, basic syntax, small-program independence), **learning context** (independent, formal, workshop, workplace), **goal** (curiosity, artifact, task, career exploration), and **constraint** (time, device, language, accessibility, cost). Further splitting is warranted only after Django-specific behavioral research identifies materially different paths; current evidence does not support precise segment sizes or conversion priorities. (Inference; confidence: High on the conceptual problem, Low on market sizing.)

## Existing-analysis claim audit

| Existing-analysis hypothesis | Audit | Audience-specific assessment |
|---|---|---|
| Early-career/self-taught/bootcamp/CS/career-changing developers evaluate a framework as a career investment, portfolio tool, modern-app tool, and route to a welcoming community; homepage/social/video/community discovery is claimed. | **Partially supported** | Surveys support creative projects, career motives, video, communities, and supportive learning contexts across broad learner populations. Django Girls supports first web-app creation and continued learning for some attendees. But this claim merges first-time programmers with framework-ready early-career evaluators. There is no direct evidence here that true first-timers evaluate Django as a framework investment, that a portfolio is primary, or that the Django homepage is a material discovery route. |
| Claimed touchpoints include docs/release notes, forums/Discord, GitHub/issue tracker, mailing lists, conferences/sprints, podcasts, professional peer networks, and short-form social. | **Partially supported** | Documentation, general forums/communities, search, videos, AI, friends/classmates, and educators are evidenced learning/help channels. Django explicitly offers its forum and Discord, but audience usage is unmeasured. Release notes, issue trackers, mailing lists, conferences/sprints, podcasts, and professional networks are weakly evidenced or mismatched for this audience's immediate job. |

Other supplied hypotheses concern donors, enterprise approvers, professional Django developers, contributors, and Django-dependent companies and are outside this audience/JTBD scope.

## Evidence table

| Finding | Source (title, publisher/author, date, URL) | Evidence type | Direct evidence or inference | Confidence | Research notes |
|---|---|---|---|---|---|
| Learners value making things, solving problems, and practical projects; complex concepts, getting stuck, field vastness, imposter syndrome, and root-cause identification are common reported challenges. | [Computer Science Learning Curve Survey 2024 Report](https://lp.jetbrains.com/cs-learning-curve-report-2024/), JetBrains Academy, data collected Feb–Jun 2024; report 2024 | Global survey, final n=23,991 | Direct for respondents; inference to first-time Django learners | Medium | Broad CS learner sample includes professionals and experienced learners; recruited partly through vendor/tech channels. Raw data and methodology are provided. |
| Hands-on projects (76% “very important”), structured curriculum (66%), clear objectives (65%), access to resources (74%), and regular feedback (49%) matter in course choice. | [Computer Science Learning Curve Survey 2024 Report](https://lp.jetbrains.com/cs-learning-curve-report-2024/), JetBrains Academy, 2024 | Global learner survey | Direct | Medium-High | Multi-select/ratings across mixed-experience learners; supports criteria tiers, not a Django/framework ranking. |
| Unengaging content, time/workload, insufficient practice, relevance, burnout, and difficulty contribute to course quitting; self-paced tutorials and free MOOCs are frequently the most recently quit formats. | [Computer Science Learning Curve Survey 2024 Report](https://lp.jetbrains.com/cs-learning-curve-report-2024/), JetBrains Academy, 2024 | Global learner survey | Direct | Medium | 64% reported quitting a course; cannot infer completion rates for any specific course or causal effects. |
| Documentation, general online resources, Stack Overflow, video, AI, school, and interpersonal help coexist in learning behavior; “learning to code” respondents are a small, younger subset of the Stack Overflow sample. | [2025 Developer Survey: Developers](https://survey.stackoverflow.co/2025/developers), Stack Overflow, 2025 | Global developer survey | Direct | Medium | 76% of total respondents were professional developers; not representative of all first-time programmers. Useful for channel behavior, not audience size. |
| AI use is widespread, but learners report less favorable sentiment toward AI tools than professionals (53% versus 61% in the survey tabs); use should not be treated as unqualified trust or evidence of learning. | [2025 Developer Survey: AI](https://survey.stackoverflow.co/2025/ai), Stack Overflow, 2025 | Global developer survey | Direct for sentiment; inference for learning implication | Medium-Low | Survey respondents are developer-oriented and “learning to code” is broader than first-time programming; the survey does not measure conceptual transfer. |
| Django's official starting guidance treats minimal Python comfort as advantageous and redirects complete programming beginners to Python resources. | [Getting started, Django 6.0 documentation](https://docs.djangoproject.com/en/6.0/intro/), Django Software Foundation/contributors, 2025–2026 documentation; accessed 2026-07-18 | Authoritative project documentation | Direct | High | Establishes intended prerequisite boundary, not learner outcomes. |
| A mainstream independent Django curriculum assumes general server-side/client-server understanding and command-line/package installation knowledge. | [Django introduction](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Server-side/Django/Introduction) and [Setting up a Django development environment](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Server-side/Django/development_environment), MDN contributors, updated 2025–2026; accessed 2026-07-18 | Maintained curriculum/prerequisite guidance | Direct | High | Independent of Django governance; prerequisites vary by curriculum. |
| A coached zero-prior-knowledge pathway can use Django to produce a first web app by teaching command line, Python, Django, HTML/CSS, Git/deployment in sequence. | [Django Girls Tutorial](https://tutorial.djangogirls.org/en/), Django Girls contributors, continuously maintained; accessed 2026-07-18; [Organize a workshop](https://djangogirls.org/en/organize/), Django Girls, accessed 2026-07-18 | Curriculum and program guidance | Direct | High for feasibility; Low for independent causal outcomes | Django-controlled but concrete. Mentor-rich, one-day workshop context is not equivalent to unsupported self-study. |
| In an older follow-up, 79% of 519 responding Django Girls alumni reported continuing to learn and 21% reported developer employment; the report warns results may be positively skewed. | [Django Girls Impact Report 2016–2017](https://djangogirls.org/en/2016-2017/), Django Girls Foundation, 2017 | Alumni survey / program impact report | Direct self-report; causal impact inference not supported | Low-Medium | Old, organization-controlled, self-selected respondents, no comparison group. Useful as feasibility/continuation signal only. |
| Beginner-oriented CS curricula teach fundamentals and web concepts before a server framework. | [CS50x 2025](https://cs50.harvard.edu/x/2025/) and [Summer 2025 syllabus](https://cs50.harvard.edu/summer/2025/syllabus/), Harvard University/CS50, 2025 | Authoritative curriculum sequence | Direct | Medium-High | One influential curriculum, not proof of a universally optimal sequence; uses Flask rather than Django. |
| Debugging is difficult and consequential for beginners; structured practice, scaffolding, hints, tracing/comprehension, and feedback are recurring intervention approaches. | [Decoding Debugging Instruction: A Systematic Literature Review of Debugging Interventions](https://doi.org/10.1145/3690652), Yang, Baird, O'Rourke, Brennan & Schneider, ACM TOCE, Nov 2024 | Systematic literature review, 43 papers (2010–2022) | Direct | High for novice programming generally; Medium for Django transfer | Study settings skew university/high school and span languages/tools. |
| Web search is itself a learned skill for novices; strategies vary and do not reliably lead to successful understanding or reuse. | [Analysis of Novices' Web-Based Help-Seeking Behavior While Programming](https://isnap.csc.ncsu.edu/home/public/publication/skripchuk-2023-sigcse/), Skripchuk et al., ACM SIGCSE, Jan 2023 | Think-aloud, screen recording, and log study | Direct | Medium | Small qualitative/observational study; supports guided help-seeking, not channel prevalence. |
| Worked examples can reduce cognitive load, but open-ended projects add decision, search, and integration barriers. | [Effects of Worked Examples with Explanation Types and Learner Motivation on Cognitive Load and Programming Problem-solving Performance](https://doi.org/10.1145/3732791), Schaper, ACM TOCE, May 2025; [Novices' Learning Barriers When Using Code Examples in Open-Ended Programming](https://arxiv.org/abs/2104.11806), Wang et al., Apr 2021 | Controlled study (75 first-course non-CS majors); classroom deployment (44 novices) | Direct | Medium | Neither study is Django-specific; supports progression from guided example to constrained customization. |
| Belonging/self-efficacy are associated with persistence, and a brief introductory-CS belonging intervention increased self-efficacy and one belonging factor, with limited other significant effects. | [Adapting an Ecological Belonging Intervention to an Introductory Computer Science Course](https://doi.org/10.1145/3819078), Jiang et al., ACM TOCE, 30 May 2026 | Between-subjects introductory-course study | Direct | Medium | Recent single-course context; does not establish effects for independent or Django learners. Avoid overgeneralizing. |
| Beginner community questions repeatedly frame Python and web fundamentals as prerequisites and describe overload from Django's files/imports. | [Django vs Python for starters](https://www.reddit.com/r/learnprogramming/comments/129tq9y/), r/learnprogramming, Apr 2023; [What are the prerequisites?](https://www.reddit.com/r/django/comments/1boax3y/), r/django, Mar 2024; [How you guys learned Django after Python?](https://www.reddit.com/r/django/comments/15gbcna/), r/django, Aug 2023 | Community discussion threads | Direct qualitative signal | Low | Isolated/self-selected posts; useful for language and recurring concerns, never prevalence or representative proof. |

## Unanswered research questions

1. What proportion of people arriving at Django-controlled entry points have never programmed, and what goals and constraints brought them there?
2. Where do zero-experience learners first encounter Django, and which channels move them from curiosity to a completed first session rather than merely generate awareness?
3. How do completion, comprehension, independent modification, and four- or twelve-week continuation differ among Python-first, integrated Django-first, coached workshop, and self-paced paths?
4. Which setup failures and conceptual transitions cause first-time learners to abandon a Django path, by OS, device, language, accessibility need, and connectivity?
5. What amount of Python and web knowledge predicts productive use of the official Django tutorial without creating an unnecessarily high gate?
6. Do Django's forum or Discord feel safe and useful to true beginners, and what happens after a first question?
7. How do learners use AI while following Django material: explanation, debugging, code substitution, or verification—and what patterns improve versus weaken transfer?
8. Which emotional and belonging needs are specific to independent learners, minors, career changers, and historically excluded groups rather than to “beginners” generally?
9. What do first-time learners believe tutorial completion demonstrates, and how does that belief compare with their ability to build or debug a second small app?
10. How many workshop attendees continue because of Django specifically versus mentoring, peer belonging, a visible artifact, or broader interest in programming?
