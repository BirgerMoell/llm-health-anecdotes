# The Plural of Anecdote Is Data: Seed Corpus Memo

## Scope

This first-pass corpus collects public anecdotes where people describe using LLMs, mainly ChatGPT, for health-related purposes. I am treating these accounts as qualitative data about behavior, perceived benefit, unmet need, and risk. I am not treating them as evidence that an LLM clinically diagnosed or treated anyone.

Working inclusion rule:

- Include public first-person or caregiver accounts where an LLM was used for a health-related goal.
- Include negative and mixed cases, not only success stories.
- Prefer accounts with enough detail to code: symptoms, model/task, action taken, and claimed outcome.
- Separate raw first-person posts from journalism-mediated accounts and peer-reviewed case reports.
- Exclude generic opinion pieces unless they contain specific user stories.

## Search Strings Used

- `site:reddit.com ChatGPT helped me health diagnosis symptoms doctor`
- `site:reddit.com ChatGPT saved my life health diagnosis`
- `site:reddit.com "ChatGPT" "diagnosed" "doctor" "health"`
- `site:reddit.com "ChatGPT" "mental health" "helped me"`
- `"ChatGPT saved my life" health diagnosis`
- `"I used ChatGPT" "symptoms" "doctor" "diagnosed"`
- `"I asked ChatGPT" "symptoms" "doctor" "diagnosed"`
- `site:reddit.com ChatGPT gave me bad medical advice health`
- `site:reddit.com ChatGPT medical advice wrong symptoms`
- `site:reddit.com "ChatGPT" "misdiagnosed" "health"`
- `site:reddit.com ChatGPT helped me lose weight health meal plan`
- `site:reddit.com ChatGPT helped me quit smoking drinking THC health`
- `site:reddit.com ChatGPT helped me understand lab results doctor`

## Seed Findings

The first 30 candidate records are in `seed_corpus.csv`. They already suggest six major use patterns:

1. **Urgent triage and escalation**
   Users describe LLMs nudging them toward care for symptoms they might otherwise have minimized, including rhabdomyolysis, shingles, possible bleeding disorder, DVT/PE, and gallbladder-type symptoms.

2. **Diagnostic odyssey support**
   People with long-running unexplained symptoms use LLMs to synthesize history, labs, imaging reports, food triggers, and timelines. These stories often frame the model as a pattern finder after fragmented specialist care.

3. **Health literacy and translation**
   Users ask LLMs to explain diagnoses, lab reports, pathology, chemo side effects, medical records, or next questions for clinicians. This may become one of the paper's strongest non-sensational themes.

4. **Mental health support and self-reflection**
   Accounts describe venting, emotional regulation, attachment framing, trauma reflection, addiction recovery, and a sense of being heard. The same domain also contains some of the clearest harm patterns.

5. **Behavior change and self-management**
   People use LLMs for calorie logging, meal planning, exercise routines, sleep, addiction recovery, supplement tracking, and chronic symptom journals.

6. **Failure and harm**
   Negative cases include wrong rash interpretation, unsafe pediatric/medication advice, bromide toxicity after diet-related AI use, worsening rumination, reassurance-seeking in OCD, and delusion/mania reinforcement.

## Early Theoretical Angle

The most interesting story is not "AI beats doctors." That framing is too brittle and clinically risky. The stronger paper is:

> Public anecdotes show LLMs functioning as always-available sensemaking tools in the gaps between formal healthcare encounters.

That lets us analyze why users turn to LLMs:

- time scarcity in clinical visits
- fragmented records and specialists
- lack of explanation after tests
- dismissal of rare or complex symptoms
- need for emotionally safe rehearsal before appointments
- cost and access barriers
- desire for longitudinal memory and pattern tracking

It also lets us analyze why the same properties can be dangerous:

- fluent confidence without examination
- weak triage in atypical emergencies
- sycophantic validation
- over-personalization
- missing contextual constraints
- users acting before clinical confirmation

## Evidence Quality Labels

Suggested labels for later coding:

- `confirmed_by_clinician_or_test`: Account reports clinician/test confirmation.
- `self-reported_improvement`: User reports improvement without external confirmation.
- `media-mediated`: Story reported through journalism rather than raw public post.
- `clinical_case_report`: Published medical case rather than public online anecdote.
- `unconfirmed_diagnosis`: LLM suggestion not clinically verified in the account.
- `harm_or_near_miss`: Account reports physical, psychological, or care-delay risk.
- `communication_support`: LLM helped explain, summarize, prepare, or ask questions.

## Ethics Notes

- Do not reproduce sensitive posts in full.
- Use short excerpts only when analytically necessary; paraphrase by default.
- For Reddit comments, collect direct permalinks before final analysis.
- Avoid usernames in the manuscript unless the user is a named public interview subject in journalism.
- Treat all medical claims as claims made by the poster, not verified facts.
- Consider whether direct quotation could make a vulnerable person searchable.

## Next Collection Pass

1. Capture direct permalinks for Reddit comments currently represented only by thread URLs.
2. Deduplicate repeated media versions of the same underlying story, especially rhabdomyolysis and tethered cord syndrome.
3. Expand beyond Reddit with targeted searches across Medium, Substack, Hacker News, patient forums, TikTok/transcripted video coverage, and news interviews.
4. Add a source-quality field: raw first-person, caregiver, clinician, journalist-mediated, peer-reviewed case.
5. Build a codebook and double-code a 20-record pilot sample before scaling.

## Key Sources Already Identified

- Reddit rhabdomyolysis account: https://www.reddit.com/r/ChatGPT/comments/13pfkcv/chatgpt_saved_my_life/
- NPR/WFDD diagnosis article: https://www.wfdd.org/national/2026-01-30/chatgpt-saved-my-life-how-patients-and-doctors-are-using-ai-to-make-a-diagnosis
- Wired overview of patient diagnosis anecdotes: https://www.wired.com/story/dr-chatgpt-will-see-you-now-artificial-intelligence-llms-openai-health-diagnoses
- People / Phoebe Tesoriere rare genetic condition: https://people.com/woman-self-diagnosed-her-rare-condition-using-chatgpt-after-years-of-being-misdiagnosed-by-doctors-11949121
- Medium SIBO personal essay: https://medium.com/%40alissaandrade/chatgpt-knew-what-my-doctors-didnt-my-journey-with-sibo-ba69bf705f41
- Reddit mental health support thread: https://www.reddit.com/r/ChatGPT/comments/105qzsa
- Reddit mental health worsening thread: https://www.reddit.com/r/ChatGPT/comments/1pooz2c/chat_gpt_made_my_mental_health_issues_worse/
- Teen Vogue on OCD reassurance seeking: https://www.teenvogue.com/story/how-ai-chatbots-could-be-making-your-ocd-worse
- Live Science summary of bromism case report: https://www.livescience.com/health/food-diet/man-sought-diet-advice-from-chatgpt-and-ended-up-with-bromide-intoxication
- Reddit rash misclassification case: https://www.reddit.com/r/ChatGPT/comments/1lzy17b
- Reddit weight loss / blood pressure account: https://www.reddit.com/r/ChatGPT/comments/1s7cq27/chatgpt_helped_me_losing_weight_and_now_im_off_my/
- Reddit addiction recovery account: https://www.reddit.com/r/ChatGPT/comments/1nqboo1/how_chatgpt_helped_me_quit_weed_and_understand/

## Second-Pass Additions

After expanding into Mayo Clinic Connect and oncology-specific sources, the corpus included 40 records. This pass added less viral, more routine examples of AI use:

- oncology bloodwork and diet planning
- biopsy, surgical, and pathology report explanation
- multiple myeloma treatment-duration questions
- complex multi-specialist care coordination
- cardiology imaging report interpretation before follow-up
- pediatric diagnostic frustration where AI did not resolve the access problem
- peer-to-peer advice norms about confirming AI information with clinicians

This strengthens the argument that LLM health use is not only about spectacular "AI diagnosed me" stories. Much of the behavior is mundane but consequential: preparing, translating, organizing, and coping.

## Third-Pass Additions

The corpus now includes 70 records. The third pass mined high-yield Reddit threads where comments contained distinct first-person or caregiver anecdotes. This substantially broadened the corpus in two directions:

- More high-acuity physical-health triage and advocacy cases: sepsis, pulmonary embolism, shingles, telemetry during hospitalization, medication interactions, and nutrition support.
- More mental-health risk cases: OCD reassurance, psychosis-like feedback loops, model-dependent coping, self-harm-adjacent use, and AI-as-therapy narratives.

The mental-health material makes the paper more balanced. It shows that the same properties users praise -- availability, patience, validation, memory, and lack of judgment -- can also become the mechanism of harm when the user needs friction, reality testing, emergency escalation, or human containment.

## Fourth-Pass Additions

The corpus now has 100 records. The fourth pass intentionally diversified away from Reddit by adding news-mediated patient accounts, disease-specific patient essays, Mayo Clinic Connect forum discussions, Hacker News, Medium, an App Store review, and additional Reddit communities beyond r/ChatGPT.

The 100-record corpus is now large enough for:

- a pilot thematic analysis
- source-quality stratification
- a table of representative cases by use type
- a harm-mechanism table
- a methods section that distinguishes raw first-person posts, patient-forum posts, media-mediated cases, company-mediated cases, and clinical/expert-reported cases

Important caution: several records are thread comments with only thread-level URLs. Before publication, we should collect direct comment permalinks or demote those records to background examples.

## Initial Curation Layer

I added an initial analytic layer in `coded_corpus.csv`. This is not the final full coding pass; it is a pilot-coded subset of 35 strategically useful records. The subset was chosen to span:

- acute triage and emergency escalation
- lab/report translation
- chronic illness and diagnostic odyssey
- oncology management
- mental health support
- mental health harm
- medication safety
- behavior change and addiction support
- community norm-setting

This pilot confirms that the paper's strongest thematic structure is:

1. LLM as translator
2. LLM as pattern finder
3. LLM as appointment amplifier
4. LLM as always-on companion
5. LLM as behavior-change scaffold
6. LLM as risky validator
7. LLM as workaround for system gaps

The harm cases are not peripheral; they define the boundary conditions of usefulness.

## Current Files

- `seed_corpus.csv`: 40 candidate anecdote records.
- `codebook.md`: initial coding scheme.
- `search_log.md`: search strings and source-yield notes.
- `context_and_literature_notes.md`: polling, expert-review, and literature context for introduction/discussion.
