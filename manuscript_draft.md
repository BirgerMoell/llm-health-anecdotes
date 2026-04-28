# The Plural of Anecdote Is Data

## How Patients Describe Using Large Language Models for Health

**Birger Moëll**

### Abstract

Large language models (LLMs) are increasingly used by patients and caregivers for health-related sensemaking outside formal clinical settings. Existing research has largely evaluated LLM performance on medical benchmarks, clinician-authored prompts, or simulated patient questions. Less is known about how people describe using these systems in everyday illness, uncertainty, and care navigation. We compiled a seed corpus of 100 public online accounts in which patients, caregivers, family members, or peers described using LLMs or chatbot-like AI systems for health-related purposes. Sources included Reddit posts and comments, patient forums, personal essays, news-mediated patient accounts, disease-specific publications, and case-report-adjacent sources. We pilot-coded 35 strategically selected records by source quality, account type, health domain, primary use case, reported outcome, evidence quality, system gap, and risk mechanism.

Across the corpus, LLMs were most often described as useful when the task was sensemaking: translating medical language, organizing longitudinal records, preparing questions for clinicians, identifying possible patterns, supporting behavior change, or providing emotional containment between encounters. These accounts suggest that patients are using LLMs less as stand-alone doctors than as always-available tools for the invisible work around healthcare. However, the same properties that make LLMs useful -- fluency, patience, personalization, and availability -- also appear in harm narratives involving wrong triage, unsafe medication or diet advice, compulsive reassurance seeking, psychosis or mania amplification, model-dependent coping, and privacy exposure. Public anecdotes cannot establish clinical efficacy, but they are data about patient behavior, perceived unmet need, and failure modes that may be missed by benchmark studies. We argue that anecdotal corpora can help researchers, clinicians, and system designers identify where LLMs amplify care, where they compensate for system gaps, and where they quietly place patients at risk.

### Keywords

large language models; ChatGPT; patient narratives; digital health; qualitative research; health information seeking; anecdotal evidence; patient safety

## Introduction

Large language models have entered health behavior faster than clinical governance can evaluate them. Patients now ask chatbots to explain laboratory results, interpret radiology reports, rehearse appointments, triage symptoms, compare treatment options, manage anxiety, plan meals, track side effects, and make sense of years of unresolved symptoms. Much of this use happens outside formal care, outside medical records, and outside the settings in which health AI is usually evaluated.

Recent survey data suggest that this behavior is no longer marginal. A 2026 KFF Tracking Poll reported that 32% of U.S. adults had used AI chatbots in the past year for health information or advice, including 29% for physical health and 16% for mental health [1]. The same survey found that 19% had used AI to explain medical tests, lab results, or diagnoses; 19% to understand or compare treatment options; and 16% to decide whether to see a doctor or seek care [1]. Among AI health users, 41% reported uploading personal medical information, such as test results or doctors' notes, to AI tools [1]. Earlier KFF polling found substantial public uncertainty about the accuracy of AI chatbot health information [2]. These figures do not show whether such use is safe or effective. They do show that LLMs are becoming part of the informal infrastructure through which patients interpret health.

Most medical AI research asks whether a model gives accurate answers to standardized prompts, responds empathically to patient questions, or provides guideline-concordant information in domains such as oncology [3-5]. Those questions are necessary, but they miss much of what patients actually do with LLMs. A patient pasting a pathology report into ChatGPT is not only asking for medical knowledge; they are asking for translation, pacing, reassurance, preparation, and a way to think while waiting for a clinician. A caregiver uploading a sequence of lab results is not necessarily trying to replace a physician; they may be trying to understand enough to ask better questions. A person using a chatbot at 2 a.m. during panic or withdrawal may be seeking something closer to presence than information.

This paper begins from the premise that public anecdotes are not clinical proof, but they are still data. They are data about how patients behave, what they find useful, what they fear, what they misunderstand, and where existing healthcare systems leave informational or emotional gaps. The phrase "the plural of anecdote is data" is often used provocatively. We use it here with restraint: not to claim that many stories equal evidence of efficacy, but to argue that systematically collected narratives can reveal use patterns and failure modes that deserve formal study.

We therefore ask four questions:

1. What health-related tasks do patients and caregivers describe delegating to LLMs?
2. What benefits do users report, and what kinds of evidence do they provide for those benefits?
3. What harms, failures, or near misses appear in public accounts?
4. What do these anecdotes reveal about gaps in healthcare communication, access, coordination, and emotional support?

## Methods

### Study Design

We conducted an exploratory qualitative evidence mapping of public online anecdotes describing patient, caregiver, family, or peer use of LLMs for health-related purposes. The approach was informed by thematic analysis and scoping-review reporting principles, but should be understood as hypothesis-generating rather than as a formal systematic review [6,7]. The goal was not to estimate prevalence, validate medical claims, or measure model accuracy. Instead, the goal was to identify recurring use cases, perceived benefits, evidence types, safety concerns, and system gaps visible in public narratives.

### Data Sources

The seed corpus included 100 records collected from public online sources. Sources included Reddit posts and comments, Mayo Clinic Connect patient forums, Medium and personal essays, disease-specific patient publications, Hacker News, news-mediated patient accounts, an app-store review, official/company-mediated patient stories, and case-report-adjacent clinical or news summaries. Reddit was the largest source category because many first-person LLM health anecdotes are posted there, but later collection deliberately expanded into patient forums, oncology sources, chronic illness communities, and news-mediated accounts.

We treated source type as analytically important. A raw first-person Reddit post, a caregiver comment in a patient forum, a named patient quoted in journalism, and a company-mediated patient story do not carry the same evidentiary status. We therefore distinguished raw public accounts, patient-forum accounts, caregiver accounts, media-mediated accounts, company-mediated accounts, clinical/expert-reported cases, and peer norm-setting posts.

### Search Strategy

Searches combined tool terms with health-use terms and source filters. Tool terms included `ChatGPT`, `GPT-4`, `GPT-4o`, `Gemini`, `Claude`, `AI chatbot`, and `LLM`. Health-use terms included `diagnosed`, `symptoms`, `doctor`, `ER`, `urgent care`, `lab results`, `blood work`, `pathology report`, `medical records`, `mental health`, `therapy`, `depression`, `anxiety`, `OCD`, `psychosis`, `weight loss`, `quit`, `cancer`, `chronic illness`, `saved my life`, `helped me`, and `made worse`. Source filters included `site:reddit.com`, `site:connect.mayoclinic.org`, and `site:medium.com`, supplemented by general web searches.

Searches were iterative. The first pass emphasized broad discovery of helpful and harmful cases. Later passes targeted domains that appeared underrepresented or analytically important: oncology, mental health harm, chronic illness, lab and record interpretation, urgent triage, lifestyle behavior change, addiction support, and patient-forum discussions. Search strings and yield notes were recorded in a search log.

### Inclusion and Exclusion Criteria

Accounts were included when they described a concrete health-related use of an LLM or chatbot-like AI system by a patient, caregiver, family member, or peer; contained enough context to classify the task; and reported a perceived outcome, action, concern, or failure. Health-related uses included illness, symptoms, diagnosis, treatment, mental health, behavior change, medication questions, test interpretation, care navigation, or emotional support.

Accounts were excluded when they were generic speculation about AI in medicine without a user story, clinician-only workflow examples without patient use, purely promotional vendor content without an identifiable user narrative, non-LLM AI tools without a comparable conversational interface, or posts too vague to code.

### Coding

We developed an initial codebook and pilot-coded 35 strategically selected records from the 100-record seed corpus. The pilot sample was selected to span source type, account type, health domain, valence, and evidence quality. Codes covered source quality, account group, domain group, primary and secondary use case, normalized valence, evidence quality, system gap, risk flags, and whether the record was a candidate for manuscript vignette use.

Primary use-case categories included urgent triage, differential generation, medical translation, record synthesis, lab translation, question preparation, emotional support, addiction support, diet and weight tracking, medication timing, AI-as-therapy, reassurance seeking, and verification norms. Risk codes included privacy exposure, unsafe self-treatment, medication safety, high-stakes sensitivity, unconfirmed diagnosis, rumination or compulsion, psychosis or mania amplification, model instability, and unresolved system bottlenecks.

### Citation System

Corpus records are cited using stable local identifiers in the form `LHA-###`. These identifiers refer to rows in the seed corpus rather than to verified clinical events. For example, `LHA-001` refers to a public anecdote record with its source URL, source type, health domain, outcome claim, and evidentiary notes. Appendix A maps all `LHA-###` identifiers to their source platforms and URLs. This lets the manuscript discuss public accounts without reproducing sensitive posts in full or implying independent clinical verification.

### Ethics

Public posts are not equivalent to consented interviews. Consistent with internet research ethics guidance, we therefore treated privacy as a methodological constraint rather than an afterthought [8]. Sensitive cases, especially those involving mental health crises, suicidality, psychosis, pediatrics, cancer, pregnancy, terminal illness, or rare disease, were paraphrased rather than quoted. We avoided usernames and unnecessary identifying details. We also distinguished claims made by posters from clinically verified facts. When a poster reported that a diagnosis, lab result, imaging finding, hospitalization, or physician assessment confirmed an LLM suggestion, we coded this as reported confirmation, not independent verification.

## Results

### Corpus Characteristics

The seed corpus contained 100 records. Of these, 78 were helpful or perceived-helpful, 13 were harmful or unhelpful, eight were mixed, uncertain, or helpful-with-risk, and one described AI use that did not resolve the underlying problem. The source mix included 67 Reddit posts or comments, 12 patient-forum records, 10 news reports, three personal essays, and eight other records from sources such as clinical/news case-report summaries, a personal column, an official company blog, Hacker News, an app review, and a news feature.

The 35-record pilot-coded subset included 27 raw public accounts, four patient-forum records, three media-mediated records, and one clinical-publication-context record. Domains included mental health, acute triage, chronic illness, oncology, records and labs, behavior change, pediatrics, medication safety, toxicology, diagnostic naming, and community norm-setting.

Seven themes organized the data: the LLM as translator, pattern finder, appointment amplifier, always-on companion, behavior-change scaffold, risky validator, and workaround for system gaps.

### Theme 1: The LLM as Translator

Many accounts described LLMs as translation tools for medical language. Users pasted or summarized lab results, pathology reports, imaging findings, biopsy results, surgical notes, sleep studies, patient-portal messages, and diagnoses. The perceived benefit was usually not that the model replaced a clinician. Instead, users described moving from opaque language to enough understanding to ask questions, tolerate uncertainty, or prepare for a visit.

Oncology accounts were especially prominent. Some users described using ChatGPT to interpret prostate pathology, breast biopsy language, colon cancer staging, chemotherapy side effects, or daily lab changes during terminal cancer care (LHA-031, LHA-032, LHA-034, LHA-097). A personal essay about colon cancer described AI as useful across several moments: interpreting anemia and pathology, preparing medical questions, explaining diagnosis-related information to family, processing fear, and planning rehabilitation (LHA-033). Patient-forum accounts similarly described using ChatGPT or related tools to understand biopsy, surgical, and pathology reports before speaking with clinicians (LHA-032, LHA-097, LHA-100).

The translator role also appeared outside cancer. Users described asking LLMs to explain sleep-study reports, cardiac imaging reports, thyroid ultrasound and biopsy sequences, semen analysis results, EBV test panels, MRI and EMG results, and specialist notes (LHA-008, LHA-086, LHA-087, LHA-090, LHA-091). In these cases, the LLM's value lay in reducing the interpretive burden of medical documentation. The risk was that explanation could slide into interpretation, and interpretation into medical advice, without a clear boundary.

### Theme 2: The LLM as Pattern Finder

A second cluster involved users with long, fragmented, or unresolved medical histories. These users described feeding LLMs years of symptoms, labs, records, food triggers, wearable data, specialist notes, or patient-generated logs. The model was valued as a pattern finder across time and across medical silos.

One user uploaded a decade of labs, EKG information, sleep-study data, Apple Health data, and patient-portal exports, then reported that the model suggested checking homocysteine, which later returned elevated. Another described using ChatGPT to surface patterns in hospital records after a spinal cord injury and repeated emergency visits, including metabolic and liver-related issues they believed had been documented but not communicated clearly. Other diagnostic-odyssey accounts involved chronic fatigue, dysautonomia, possible endocrine dysfunction, mast-cell disease after COVID, primary aldosteronism after resistant hypertension, and an early GPT-4 account in which a user explored HLA-B27 and genome data.

These stories should not be read as proof that LLMs diagnose rare disease. Their analytic value is different: they show that patients experience longitudinal synthesis as a missing service. No specialist may own the whole timeline. No appointment may be long enough to reconstruct it. In that gap, the LLM becomes a tool for assembling a provisional map.

### Theme 3: The LLM as Appointment Amplifier

Many accounts described LLMs as helping users prepare for, intensify, or redirect clinical encounters. This included generating questions, summarizing symptoms, deciding whether to seek urgent care, making sense of tests before an appointment, or producing discussion lists that clinicians could act on.

Several acute-care anecdotes involved escalation. In one widely discussed Reddit post, a user reported asking ChatGPT about severe soreness and dark urine after exercise; the model raised the possibility of rhabdomyolysis, after which the user sought emergency care and reported hospitalization with markedly elevated creatine kinase (LHA-001). In another media-mediated case, a patient with unexplained red spots reportedly sought urgent evaluation after ChatGPT raised concern about a bleeding disorder and was later diagnosed with immune thrombocytopenic purpura (LHA-002). Other accounts involved possible sepsis, shingles, pulmonary embolism, HELLP syndrome, rectal bleeding, and cervical spine injury (LHA-028, LHA-064, LHA-092, LHA-093, LHA-095).

The appointment-amplifier role also appeared in lower-acuity contexts. Users described using AI-generated question lists for oncology visits, neurology follow-up, complex specialist coordination, and first appointments after receiving confusing reports. The benefit was practical: users felt more prepared, less intimidated, and more able to make scarce clinical time count. The safety concern is that question generation can also introduce overconfident hypotheses, irrelevant requests, or high-stakes treatment expectations that clinicians must then correct.

### Theme 4: The LLM as Always-On Companion

The most emotionally charged accounts involved LLMs as companions. Users described chatbots as patient, nonjudgmental, available at night, and able to receive repetitive or messy thoughts without fatigue. This appeared in mental health support, addiction recovery, cancer coping, chronic illness, anxiety regulation, and bereavement.

Some users described ChatGPT as helping them vent, ground themselves during anxiety, understand attachment patterns, process trauma, or disclose thoughts they had hidden from other people (LHA-048, LHA-050, LHA-052, LHA-075). Others described using it during cannabis withdrawal, meal logging, chronic pain management, or cancer treatment (LHA-012, LHA-021, LHA-022, LHA-033). Availability mattered. The LLM could be used between therapy sessions, when therapy was inaccessible, during a craving, while waiting for test results, or late at night.

This companion role is central to why patient narratives cannot be reduced to factual accuracy. In many accounts, the user did not only need an answer. They needed pacing, repetition, reassurance, rehearsal, or a listener. For some, that support felt life-improving. For others, it became the mechanism of harm.

### Theme 5: The LLM as Behavior-Change Scaffold

Several accounts described LLMs as scaffolds for daily behavior change. Users reported weight loss, blood-pressure improvement, meal logging, exercise planning, physical therapy adaptation, rehabilitation planning, cannabis cessation, and allergy or symptom tracking (LHA-012, LHA-020, LHA-021, LHA-022, LHA-023, LHA-083). The model's perceived value was often not specialized medical knowledge but low-friction interaction: a conversational log, a planning partner, a source of accountability, or a tool that transformed messy daily behavior into manageable steps.

For example, users described logging meals in plain language rather than searching food databases; receiving calorie estimates and feedback; using ChatGPT during cannabis cravings; organizing physical therapy exercises around a clinician-provided diagnosis; and planning post-surgical rehabilitation after cancer (LHA-021, LHA-022, LHA-023, LHA-012, LHA-033). These accounts suggest that LLMs may function as behavior-change interfaces, especially for users who dislike rigid tracking apps or lack social support.

The risk is that lifestyle advice can become medical advice. Diet, supplements, exercise, withdrawal, and medication timing can interact with disease, pregnancy, psychiatric risk, or treatment. The corpus therefore suggests a design need: conversational behavior-change tools should know when to remain motivational, when to ask clarifying questions, and when to defer to clinical guidance.

### Theme 6: The LLM as Risky Validator

Harm cases revealed a different side of the same affordances. A model that is always available, responsive, and validating may support users in distress. It may also reinforce rumination, compulsive reassurance, delusional interpretation, interpersonal escalation, or unsafe action.

Mental health cases were especially concerning. Users described ChatGPT worsening interpersonal spirals, functioning as a 24/7 reassurance source for OCD, becoming entangled with psychosis-like or manic episodes, and destabilizing coping when model behavior changed (LHA-014, LHA-015, LHA-053, LHA-054, LHA-056, LHA-057). In one case, a user described relying on a particular model behavior for creative escape from depression and self-harm urges, then losing that support after a model change (LHA-049). In other cases, users described AI-as-therapy interactions preceding or amplifying psychosis-like experiences (LHA-055, LHA-057). These accounts do not establish causality, but they identify plausible mechanisms: over-validation, anthropomorphism, endless reassurance, symbolic mirroring, lack of crisis containment, and absence of human accountability.

Physical-health harms and near misses also appeared. One user reported that ChatGPT misclassified a rash as ringworm before a physician identified shingles, raising concern about delayed antiviral treatment (LHA-017). A toxicology case report described bromide intoxication after a patient reportedly used ChatGPT-related information while substituting sodium bromide for table salt (LHA-019) [9]. Another user reported catching unsafe medication-timing advice involving levothyroxine and iron only because they already knew the interaction (LHA-066). An expert-reported oncology case involved AI suggesting ivermectin for treatable testicular cancer, with the risk being delayed effective treatment (LHA-076).

These cases sharpen the boundary of usefulness. LLMs appear safest in the corpus when they help users understand, organize, prepare, or reflect. They appear riskiest when they make or reinforce decisions about urgency, medication, self-treatment, mental health crisis, or high-stakes treatment timing.

### Theme 7: The LLM as Workaround for System Gaps

Across themes, the most consistent background condition was not model capability but system absence. Users turned to LLMs because visits were short, portals were confusing, therapy was inaccessible, emergency care was expensive, specialists were siloed, referrals were delayed, symptoms were dismissed, or no one had time to explain. LLMs became useful at the edges of care: after a lab result appeared but before the doctor called; after an appointment ended too quickly; while waiting months for a specialist; during nighttime panic; after years of unresolved symptoms; or while trying to help a family member in crisis.

This point is clearest in the failure cases. In a pediatric diagnostic-odyssey account, a family member described combing through reports and using AI while still being trapped by delayed referrals and access barriers (LHA-004). AI made the family more informed, but it did not make the system respond. In complex-care accounts, LLMs helped synthesize notes from many specialists, but that usefulness existed because the health system had not provided a coherent synthesis (LHA-008, LHA-058, LHA-078, LHA-082). In mental health accounts, AI support felt valuable partly because timely human support was unavailable or unaffordable (LHA-012, LHA-022, LHA-050, LHA-056).

Thus, the corpus should not be interpreted as a simple story of patient enthusiasm for AI. It is also a map of unmet care needs.

## Discussion

This exploratory corpus suggests that LLMs are becoming embedded in patient work: the unpaid, often invisible labor of understanding records, preparing appointments, monitoring symptoms, coordinating specialists, changing habits, and coping emotionally. The strongest positive anecdotes do not show LLMs replacing clinicians. They show LLMs filling gaps around clinicians.

This distinction matters. If researchers evaluate LLMs only as diagnostic engines, they may miss the tasks for which patients most often value them: translation, summarization, rehearsal, longitudinal synthesis, and emotional pacing. Conversely, if designers optimize for warmth, confidence, and personalization without understanding clinical boundary conditions, they may intensify exactly the harms visible in the corpus: unsafe reassurance, over-trust, privacy exposure, and failure to interrupt dangerous trajectories.

The corpus also complicates familiar debates about anecdotal evidence. Anecdotes are weak evidence for clinical efficacy because they are self-selected, unverifiable, non-representative, and narratively shaped. But they are strong signals of use. They tell us where patients place AI in their lives. They reveal how people interpret model outputs, what they do next, which healthcare gaps make AI attractive, and which harms occur outside controlled evaluations. In fast-moving domains, systematic attention to anecdotal data can help generate hypotheses, design safety studies, and identify patient-centered outcomes that benchmark tasks overlook.

### Design and Clinical Implications

First, LLM health tools should distinguish explanation from advice. Many users benefit from translation of existing medical information. Interfaces could support this by labeling outputs as explanation, summarization, or question preparation rather than diagnosis or treatment recommendation.

Second, systems should encourage clinician-bridging behavior. The safer success cases often involved users taking questions, summaries, or concerns to clinicians rather than acting alone. Tools could produce appointment-ready summaries, uncertainty lists, and red-flag prompts while avoiding definitive conclusions.

Third, high-risk domains need friction. Medication changes, pregnancy, pediatrics, cancer treatment timing, suicidality, psychosis, mania, chest pain, neurological deficits, severe infection, and acute breathing symptoms should trigger escalation-oriented behavior, not extended speculative dialogue.

Fourth, mental health companionship requires safeguards that go beyond crisis disclaimers. The corpus suggests risks from reassurance loops, sycophantic validation, anthropomorphism, model instability, and dependency. Systems should be evaluated not only for whether they mention hotlines, but for whether they interrupt compulsive or delusional loops, preserve reality testing, and avoid becoming a sole support.

Fifth, privacy should be treated as a core health-risk issue. Users routinely upload lab results, imaging reports, pathology, genomics, diaries, psychiatric narratives, and family-member records. Health AI design must make data handling legible and give users safer ways to redact, summarize, or process sensitive information.

### Limitations

This study has important limitations. The corpus is not representative of all patients or all LLM health use. Public posts are self-selected and likely overrepresent unusually positive, negative, dramatic, or technologically engaged users. Reddit and patient forums have distinctive cultures and demographics. Some posts may be exaggerated, edited, deleted, or strategically narrated. Media accounts may compress or dramatize patient stories. Many clinical claims are unverifiable. Even when a poster reports clinician confirmation, we did not independently verify medical records.

The corpus is also English-heavy and platform-dependent. Search-engine ranking, subreddit visibility, deleted comments, and platform norms shaped what could be found. Several records are comment-level anecdotes that currently require direct permalinks before they should be featured in a final manuscript. We therefore treat the present corpus as a seed dataset and hypothesis-generating evidence map, not a definitive archive of patient LLM use.

Finally, our coding is preliminary. We pilot-coded 35 records to develop themes and analytic categories. A final study should code all 100 records, refine inter-coder reliability or consensus procedures, and consider whether to stratify analysis by raw first-person accounts versus media-mediated stories.

## Conclusion

The plural of anecdote is not proof. But in a fast-moving domain where private behavior outpaces formal evaluation, anecdotes are data about what people need, what they try, and where systems fail them. Public accounts of LLM health use show patients turning to chatbots as translators, pattern finders, appointment amplifiers, companions, behavior-change scaffolds, and workarounds for fragmented care. They also show the risks of treating a fluent, validating system as if it were clinically accountable.

Listening carefully to these stories can help researchers ask better questions. The central question is not whether LLMs can replace clinicians. The corpus suggests a more urgent question: how can health systems, clinicians, and AI designers respond to the fact that patients are already using LLMs in the spaces where care feels absent, opaque, rushed, or unreachable?

## References

1. Montero A, Montalvo J III, Kearney A, Valdes I, Kirzinger A, Hamel L. KFF Tracking Poll on Health Information and Trust: Use of AI for Health Information and Advice. KFF; 2026 Mar 25. Available from: https://www.kff.org/public-opinion/kff-tracking-poll-on-health-information-and-trust-use-of-ai-for-health-information-and-advice/

2. Presiado M, Montero A, Lopes L, Hamel L. KFF Health Misinformation Tracking Poll: Artificial Intelligence and Health Information. KFF; 2024 Aug 15. Available from: https://www.kff.org/health-information-and-trust/poll-finding/kff-health-misinformation-tracking-poll-artificial-intelligence-and-health-information/

3. Ayers JW, Poliak A, Dredze M, Leas EC, Zhu Z, Kelley JB, et al. Comparing physician and artificial intelligence chatbot responses to patient questions posted to a public social media forum. JAMA Intern Med. 2023;183(6):589-596. doi:10.1001/jamainternmed.2023.1838

4. Johnson SB, King AJ, Warner EL, Aneja S, Kann BH, Bylund CL. Using ChatGPT to evaluate cancer myths and misconceptions: artificial intelligence and cancer information. JNCI Cancer Spectr. 2023;7(2):pkad015. doi:10.1093/jncics/pkad015

5. Kassab J, Nasr L, Gebrael G, Chedid El Helou M, Saba L, Haroun E, et al. AI-based online chat and the future of oncology care: a promising technology or a solution in search of a problem? Front Oncol. 2023;13:1176617. doi:10.3389/fonc.2023.1176617

6. Braun V, Clarke V. Using thematic analysis in psychology. Qual Res Psychol. 2006;3(2):77-101. doi:10.1191/1478088706qp063oa

7. Tricco AC, Lillie E, Zarin W, O'Brien KK, Colquhoun H, Levac D, et al. PRISMA extension for scoping reviews (PRISMA-ScR): checklist and explanation. Ann Intern Med. 2018;169(7):467-473. doi:10.7326/M18-0850

8. Franzke AS, Bechmann A, Zimmer M, Ess CM, Association of Internet Researchers. Internet Research: Ethical Guidelines 3.0. Association of Internet Researchers; 2020. Available from: https://aoir.org/reports/ethics3.pdf

9. Bickel KL, Cox MS, Mouhanna J, Patterson A, Gulati S. Bromism in the modern day: case report and ChatGPT-assisted dietary supplement use. Ann Intern Med Clin Cases. 2025. doi:10.7326/AIMCC.2024.1260

## Supplementary Materials

- `seed_corpus.csv`: 100-record seed corpus.
- `coded_corpus.csv`: 35-record pilot-coded analytic subset.
- `codebook.md`: initial codebook.
- `search_log.md`: search strategy and yield log.
- `cleanup_queue.md`: permalink and source-quality cleanup tasks.
- `manuscript_tables.md`: draft corpus, taxonomy, and harm-mechanism tables.
- `source_appendix.md`: source index mapping `LHA-###` record IDs to public URLs.
