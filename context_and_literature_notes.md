# Context and Literature Notes

These notes support the introduction and discussion. They are not part of the anecdote corpus unless a source contains a specific first-person or caregiver account.

## Public Use Is Now Common

KFF's March 25, 2026 Tracking Poll on Health Information and Trust reports that 32% of U.S. adults used AI chatbots in the past year for health information or advice. The poll breaks this down into 29% for physical health and 16% for mental health. It also reports that 19% used AI to explain medical tests, lab results, or diagnoses; 19% used it to understand or compare treatment options; and 16% used it to decide whether to see a doctor or seek care.

Source:

- https://www.kff.org/public-opinion/kff-tracking-poll-on-health-information-and-trust-use-of-ai-for-health-information-and-advice/

This is important because it gives population-level context for our anecdote sample. Our corpus does not estimate prevalence, but it can explain how these behaviors look in lived use.

## Access and Privacy Are Central

The same 2026 KFF poll reports that many people turn to AI for quick information or support, but access barriers also matter. Among AI health users, 19% cited inability to afford a health professional as a major reason and 18% cited not having a regular doctor or not being able to get an appointment. Among users, 41% reported uploading personal medical information such as test results or doctors' notes, meaning 13% of the public has uploaded personal medical information to AI for explanations or advice.

Analytic implication:

- This supports our emerging "system gap" theme.
- It also supports a privacy-risk subsection, especially for lab reports, imaging reports, genomics, oncology records, and mental health narratives.

## Trust Is Ambivalent

KFF's August 15, 2024 Health Misinformation Tracking Poll found that about one in six adults used AI chatbots at least monthly for health information and advice, but most adults were not confident that chatbot health information was accurate. The 2026 poll suggests use has grown substantially since then.

Sources:

- https://www.kff.org/health-misinformation-and-trust/poll-finding/kff-health-misinformation-tracking-poll-artificial-intelligence-and-health-information/
- https://www.kff.org/health-information-and-trust/press-release/poll-most-who-use-artificial-intelligence-doubt-ai-chatbots-provide-accurate-health-information/

Analytic implication:

- Users may simultaneously distrust AI in general and still use it intensely when the alternative is confusion, delay, cost, or fear.

## Expert Evaluation of Real ChatGPT Health Conversations

The Washington Post reviewed a set of publicly shared ChatGPT conversations and asked Robert Wachter, chair of medicine at UCSF, to grade 12 health-related exchanges. The article reports a mixed pattern: several strong answers, several failing answers, and a recurring failure to ask follow-up questions needed to judge severity. Wachter's key concern was that unsafe answers may sound just as authoritative as good ones to a layperson.

Sources:

- https://www.washingtonpost.com/technology/2025/11/18/chatgpt-health-advice-accuracy-rated/
- https://www.washingtonpost.com/technology/2025/11/18/chagpt-conversations-analysis-learnings/

Analytic implication:

- This provides an external validation of our "translator vs clinician" distinction.
- The model may be strongest when explaining existing information and weakest when the user needs clinical judgment, triage, or crisis detection.

## Oncology: Explanation Is Promising, Specific Guidance Is Riskier

A 2026 medRxiv mixed-methods evaluation tested ChatGPT on simulated oncology multidisciplinary team reports and gathered stakeholder views. It emphasizes patient-centered explanation, trust, language, personalization, and the limits of generic advice. It also reports that patients and professionals saw potential value in summaries but had concerns about reliability, personalization, and anxiety-provoking ambiguity.

Source:

- https://www.medrxiv.org/content/10.64898/2026.02.02.26345346v1.full-text

Additional oncology accuracy studies:

- https://academic.oup.com/jncics/article/7/2/pkad015/7078555
- https://www.frontiersin.org/articles/10.3389/fonc.2023.1176617/full

Analytic implication:

- The oncology anecdotes in the corpus should be split into at least two categories: report explanation/question preparation versus treatment choice or prognosis advice.

## Harm Mechanisms

The corpus currently shows several distinct harm mechanisms:

- `wrong_or_missed_triage`: rash mistaken for ringworm rather than shingles; under-escalation risk.
- `unsafe_self_treatment`: bromide toxicity after diet-substitution advice.
- `rumination_or_compulsion`: OCD/anxiety reassurance loops.
- `sycophantic_validation`: mania/delusion-like escalation reported in media cases.
- `system_failure_not_solved`: AI use does not overcome referral delays or pediatric access bottlenecks.
- `privacy_exposure`: uploading detailed medical records, lab reports, pathology, and imaging to consumer tools.

Recent journalism and studies increasingly focus on these risks, including failures to recognize emergencies and mental health crises. These sources should be used as context, not as anecdote records unless they contain individual user accounts.

Examples:

- https://www.washingtonpost.com/health/2026/04/21/chatbot-medical-advice-accurate/
- https://www.theguardian.com/technology/2026/feb/26/chatgpt-health-fails-recognise-medical-emergencies
- https://www.washingtonpost.com/health/2025/08/19/ai-psychosis-chatgpt-explained-mental-health/

## Draft Intro Claim

Large language models are becoming part of patients' informal health-information infrastructure. Public anecdotes cannot establish clinical efficacy, but they can reveal how people actually use these systems: to translate medical language, prepare for appointments, synthesize fragmented records, seek emotional support, change behavior, and decide whether symptoms warrant care. These same anecdotes also reveal failure modes that conventional benchmark studies can miss, including over-trust, compulsive reassurance seeking, privacy exposure, unsafe self-treatment, and the model's inability to know when a confident answer should instead become a question.
