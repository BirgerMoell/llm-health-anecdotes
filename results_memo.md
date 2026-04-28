# Results Memo: First Analytic Pass

## Corpus Status

The seed corpus contains 100 records. A pilot-coded analytic layer currently contains 35 strategically selected records.

Seed corpus valence:

- 78 helpful or perceived-helpful
- 13 harmful or unhelpful
- 8 mixed, uncertain, or helpful-with-risk
- 1 no-resolution/system-insufficient case

Seed corpus source mix:

- 67 Reddit posts or comments
- 12 patient forum records
- 10 news reports
- 3 personal essays
- 8 other sources, including clinical/news case-report summary, personal column, official blog, Hacker News, app review, and news feature

## Pilot-Coded Subset

The pilot-coded subset has 35 records:

- 27 raw public accounts
- 4 patient forum records
- 3 media-mediated records
- 1 clinical publication/context record

Domain distribution in the pilot:

- 8 mental health
- 5 acute triage
- 5 chronic illness
- 5 oncology
- 4 records/labs
- 3 behavior change
- 1 pediatrics
- 1 medication safety
- 1 behavior/medication toxicology
- 1 diagnostic naming
- 1 community norms

## Core Themes

### 1. The LLM as Translator

Patients use LLMs to translate medical language into usable understanding. This appears in oncology pathology reports, lab results, imaging summaries, sleep studies, surgical notes, and patient-portal results. The strongest accounts do not claim the LLM replaced a doctor; instead, the LLM lowered the cost of asking follow-up questions and helped users arrive at appointments with a baseline understanding.

Representative records:

- LHA-031
- LHA-033
- LHA-036
- LHA-086
- LHA-090

### 2. The LLM as Pattern Finder

Users with long or fragmented histories use LLMs to synthesize years of symptoms, records, labs, food triggers, specialist notes, or wearable data. These cases often begin after repeated clinical encounters fail to produce a satisfying explanation.

Representative records:

- LHA-008
- LHA-058
- LHA-078
- LHA-079
- LHA-082
- LHA-084

### 3. The LLM as Appointment Amplifier

LLMs help patients prepare questions, organize symptom timelines, understand what to ask, and decide when to escalate. This may make short visits more productive. It may also increase clinical workload or produce overconfident treatment expectations.

Representative records:

- LHA-001
- LHA-002
- LHA-033
- LHA-036
- LHA-094
- LHA-096

### 4. The LLM as Always-On Companion

Mental health, addiction recovery, cancer coping, anxiety regulation, and chronic illness management all benefit from availability. Users repeatedly emphasize that the model is present at night, does not tire, does not judge, and can absorb repeated or messy disclosures.

Representative records:

- LHA-011
- LHA-022
- LHA-048
- LHA-052
- LHA-075

### 5. The LLM as Behavior-Change Scaffold

Some users describe LLMs as a low-friction coach for diet, weight loss, addiction recovery, exercise, rehabilitation, and tracking. The benefit often comes less from medical expertise than from attention, reminders, friction reduction, and daily interaction.

Representative records:

- LHA-020
- LHA-021
- LHA-022
- LHA-083

### 6. The LLM as Risky Validator

The same availability and validation that make LLMs feel supportive can become dangerous in OCD, suicidality, psychosis, mania, interpersonal conflict, or addiction withdrawal. Harm cases suggest that users sometimes need friction, reality testing, emergency escalation, or human containment rather than endless responsive dialogue.

Representative records:

- LHA-014
- LHA-049
- LHA-055
- LHA-056
- LHA-057

### 7. The LLM as Workaround for System Gaps

Many anecdotes are less about model brilliance than system failure: rushed visits, inaccessible therapy, expensive emergency care, specialist silos, delayed referrals, confusing portals, poor explanation, dismissal, and lack of continuity.

Representative records:

- LHA-001
- LHA-033
- LHA-036
- LHA-038
- LHA-048
- LHA-071
- LHA-084

## Harm Mechanisms

### Wrong or Over-Narrow Triage

LHA-017 shows a rash interpreted as ringworm when a physician later called it shingles. The risk is not just wrong information but delayed antiviral treatment.

### Unsafe Medication or Substance Advice

LHA-019 and LHA-066 show toxicology and medication-interaction risks. These are especially important because users may ask practical "what should I take?" questions that feel mundane but carry clinical stakes.

### Compulsive Reassurance

LHA-056 shows why OCD may be a bad fit for an infinitely patient reassurance machine.

### Psychosis or Mania Amplification

LHA-053, LHA-054, LHA-055, and LHA-057 suggest a feedback-loop risk where symbolic, grandiose, or paranoid interpretations are mirrored rather than interrupted.

### Model Instability

LHA-049 shows a user whose coping strategy depended on a particular model behavior. When the behavior changed, the support structure changed too.

### System Problems AI Cannot Solve

LHA-038 shows a family using AI and research for a sick child but still facing referral and insurance bottlenecks. The LLM may make the family more informed without making care accessible.

## Draft Results Claim

Across the corpus, LLMs are most often described as useful when the task is sensemaking: translating, organizing, generating questions, identifying patterns, or supporting daily behavior. They are most risky when the task requires clinical judgment, urgency assessment, safeguarding, medication decisions, or interruption of a harmful thought loop.

## Draft Discussion Claim

The anecdotes should not be read as evidence that LLMs diagnose better than clinicians. They should be read as evidence that many patients experience healthcare as too rushed, fragmented, inaccessible, or opaque to meet their informational and emotional needs. LLMs become attractive because they are available precisely where formal care is absent: after the portal result appears, before the specialist visit, during the 2 a.m. panic, between therapy sessions, or after years of unresolved symptoms.
