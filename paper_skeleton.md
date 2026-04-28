# The Plural of Anecdote Is Data

## Subtitle

How Patients Describe Using Large Language Models for Health

## Working Abstract

Large language models (LLMs) are increasingly used by patients and caregivers for health-related sensemaking outside formal clinical settings. While prior work has evaluated LLM accuracy on medical benchmarks and clinician-authored prompts, less is known about how people describe using these tools in everyday illness, uncertainty, and care navigation. We compiled a seed corpus of public online anecdotes in which patients, caregivers, or peers described using LLMs for health-related purposes, including both perceived benefits and failures. We coded accounts by source type, health domain, use case, outcome claim, and risk mechanism.

Early analysis suggests that patients use LLMs less as stand-alone doctors than as always-available sensemaking tools: translating medical language, preparing questions, synthesizing fragmented records, supporting behavior change, and providing emotional containment between encounters. However, the same properties that make LLMs useful also create risk, especially when models provide confident triage, reinforce rumination or delusional beliefs, suggest unsafe self-treatment, or encourage users to upload sensitive records. Public anecdotes cannot establish clinical efficacy, but they can identify real-world use patterns and failure modes that deserve systematic study.

## Central Claim

Public anecdotes are not clinical proof, but they are data about patient behavior. They reveal where people already insert LLMs into the care process, what they believe the tools do for them, and which system gaps make AI feel useful or necessary.

## Research Questions

1. What health-related tasks do patients and caregivers describe delegating to LLMs?
2. What benefits do users report, and what kinds of evidence do they provide for those benefits?
3. What harms, failures, or near misses appear in public accounts?
4. What do these anecdotes reveal about gaps in healthcare communication, access, coordination, and emotional support?

## Suggested Article Type

Best fit:

- qualitative evidence map
- scoping review of public online narratives
- thematic analysis of public first-person accounts

Avoid framing as:

- clinical efficacy study
- diagnostic accuracy study
- "AI beats doctors" paper

## Introduction Outline

1. LLMs have moved into consumer health behavior faster than clinical governance can evaluate them.
2. Population surveys now show substantial use of AI chatbots for physical health, mental health, lab interpretation, treatment comparison, and care-seeking decisions.
3. Existing research largely evaluates model accuracy, benchmark performance, or clinician workflows.
4. But patient behavior is already happening in the wild, and public anecdotes offer early qualitative evidence of how these tools are actually used.
5. Anecdotes are limited, biased, and non-representative, yet they are valuable for identifying use cases, meanings, risks, and unmet needs.
6. This study maps public online accounts of LLM use for health, including both perceived benefits and failures.

## Methods Outline

### Data Sources

Initial sources:

- Reddit posts and comments
- Mayo Clinic Connect patient forums
- personal blogs and essays
- Medium
- journalism-mediated patient accounts
- peer-reviewed case reports when they describe patient-initiated LLM use

### Search Strategy

Use structured searches combining:

- tool terms: `ChatGPT`, `GPT-4`, `GPT-4o`, `Gemini`, `Claude`, `AI chatbot`, `LLM`
- health-use terms: `diagnosed`, `symptoms`, `doctor`, `lab results`, `blood work`, `pathology report`, `mental health`, `therapy`, `weight loss`, `quit`, `cancer`, `chronic illness`, `saved my life`, `made worse`
- source filters: `site:reddit.com`, `site:connect.mayoclinic.org`, `site:medium.com`, plus general web search

### Inclusion Criteria

Include accounts where:

- a patient, caregiver, family member, or peer describes a concrete LLM use for health
- the account contains enough context to classify the task
- the use concerns health, illness, symptoms, treatment, mental health, behavior change, or care navigation
- the account reports a perceived outcome, action, concern, or failure

### Exclusion Criteria

Exclude:

- generic speculation about AI in medicine without a user story
- clinician-only workflow examples unless a patient-use anecdote is included
- non-LLM AI tools unless the interaction is chatbot-like and comparable
- purely promotional vendor content
- posts where the health claim is too vague to code

### Coding

Use the codebook in `codebook.md`.

Primary code families:

- account type
- source quality
- health-use category
- outcome claim
- risk mechanism
- evidence quality
- system gap

### Ethics

Public posts are not the same as consented interviews. We will:

- paraphrase sensitive accounts by default
- avoid usernames and unnecessary identifying details
- use direct quotes sparingly
- avoid quoting crisis, mental health, pediatric, or rare-disease posts in ways that make them searchable
- distinguish poster claims from clinically verified facts

## Results Structure

### Theme 1: The LLM as Medical Translator

Users paste or describe lab results, imaging reports, pathology reports, biopsy reports, surgical notes, and diagnoses. The benefit is often not a new diagnosis but a lower-friction explanation before a clinical appointment.

Representative records:

- LHA-009: diagnosis explanation after short doctor's appointment
- LHA-031 and LHA-032: oncology bloodwork and pathology report interpretation
- LHA-033: colon cancer pathology and staging explanation
- LHA-034: breast biopsy/pathology report explanation
- LHA-037: CT and echo report interpretation

### Theme 2: The LLM as Pattern Finder

Patients with long or fragmented histories use LLMs to connect symptoms, labs, food triggers, wearable data, specialist notes, or multi-year records.

Representative records:

- LHA-007: food-trigger pattern after ileum/cecal valve removal
- LHA-008: ten years of labs and health records
- LHA-024: chronic fatigue/pain and vitamin D hypothesis
- LHA-025: twenty-year diagnostic odyssey
- LHA-036: multi-specialist complex diagnosis

### Theme 3: The LLM as Appointment Amplifier

LLMs help people decide what to ask, how to summarize their story, and when to seek care. This can make scarce clinician time more productive but can also create unnecessary workload or false reassurance.

Representative records:

- LHA-002: urgent care after bleeding-risk triage
- LHA-028: shingles question-led triage
- LHA-031: oncologist follow-up questions
- LHA-033: cancer appointment preparation
- LHA-040: peer advice to generate doctor questions

### Theme 4: The LLM as Always-On Companion

Users describe emotional support, journaling, addiction recovery, anxiety reduction, self-reflection, and daily accountability.

Representative records:

- LHA-011: early mental health support thread
- LHA-012: mental health, pain, exercise, and meal planning
- LHA-013: attachment-theory self-understanding
- LHA-022 and LHA-023: cannabis cessation support
- LHA-033: cancer-related emotional processing

### Theme 5: The LLM as Behavior-Change Scaffold

Some accounts emphasize planning, tracking, and accountability for weight loss, blood pressure, diet, exercise, rehabilitation, and substance use.

Representative records:

- LHA-020: weight loss, blood pressure, LDL
- LHA-021: meal logging
- LHA-022: quitting cannabis
- LHA-023: quitting weed
- LHA-033: post-surgical rehab strategy

### Theme 6: The LLM as Risky Validator

Negative cases show that fluent, personalized responses can mislead users or intensify psychological vulnerability.

Representative records:

- LHA-014: worsening spiraling and interpersonal distress
- LHA-015: OCD reassurance seeking
- LHA-016: mania/delusion validation media case
- LHA-017: rash misclassified as ringworm rather than shingles
- LHA-018: unsafe or contradictory pediatric/medication advice
- LHA-019: bromide toxicity after diet-related AI use
- LHA-038: pediatric diagnostic dead-end despite AI use

## Discussion Argument

The corpus suggests that LLMs are already embedded in patient work: the unpaid, often invisible labor of understanding records, preparing appointments, monitoring symptoms, coordinating specialists, changing habits, and coping emotionally. Many success stories are less about replacing clinical expertise than about compensating for missing time, continuity, explanation, and accessibility.

The risk is that patients may not know when the task has shifted from explanation to diagnosis, from support to treatment, or from reflection to crisis. LLMs are unusually good at making these transitions feel smooth. This smoothness is useful when the task is comprehension, but dangerous when the task requires examination, urgency judgment, safeguarding, or accountability.

## Possible Contribution

This paper contributes:

- a taxonomy of patient-described LLM health use
- an evidence-quality framework for anecdotal AI-health narratives
- a risk taxonomy grounded in public accounts rather than hypothetical benchmarks
- a reframing of anecdotes as early signals of unmet care needs

## Limitations

- Public anecdotes are self-selected and likely biased toward unusually positive or negative experiences.
- Claims are often unverifiable.
- Reddit and patient-forum demographics are not representative.
- Posts may be deleted, edited, exaggerated, or strategically narrated.
- Media accounts may compress or dramatize patient stories.
- The corpus is English-heavy unless later expanded.
- Platform search algorithms affect discoverability.

## Candidate Closing

The plural of anecdote is not proof. But in a fast-moving domain where private behavior outpaces formal study, anecdotes are data about what people need, what they try, and where systems fail them. Listening carefully to these stories can help researchers, clinicians, and designers distinguish the uses of LLMs that amplify care from those that quietly place patients at risk.
