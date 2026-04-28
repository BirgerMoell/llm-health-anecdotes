# Initial Codebook

This codebook is for qualitative coding of public anecdotes about LLM use for health. The unit of analysis is one discrete account of LLM use by a patient, caregiver, family member, or peer supporter.

## Inclusion Fields

### Account Type

- `first_person_patient`: The person used the LLM for their own health.
- `caregiver_or_family`: The person used the LLM for a child, spouse, parent, partner, or other family member.
- `peer_support`: The person recommends or applies AI for another forum member.
- `reported_by_media`: A journalist or institution reports a person's story.
- `clinical_case_report`: A medical publication reports a case linked to LLM use.

### Source Quality

- `raw_public_account`: Public post, comment, patient forum, blog, or personal essay.
- `media_mediated`: News or magazine coverage.
- `clinical_publication`: Peer-reviewed case report or study.
- `secondary_summary`: Blog/news summary of another source.
- `candidate_needs_permalink`: Thread-level URL exists but exact comment URL is still missing.

## Health-Use Codes

### Diagnostic and Triage Use

- `urgent_triage`: LLM prompts urgent care or emergency evaluation.
- `differential_generation`: LLM suggests possible diagnoses or ranked possibilities.
- `rare_disease_navigation`: LLM helps generate hypotheses after a long diagnostic odyssey.
- `second_opinion_after_clinician`: LLM used after an initial clinician explanation or diagnosis.
- `image_or_photo_assessment`: User submits a photo, usually dermatology or visible symptom.

### Health Literacy and Communication

- `medical_translation`: LLM explains jargon, reports, staging, pathology, imaging, or labs.
- `question_preparation`: LLM generates questions for doctor visits.
- `record_synthesis`: LLM integrates longitudinal records, labs, notes, wearable data, or multi-specialist input.
- `visit_rehearsal`: User practices how to talk to clinicians or communicate symptoms.
- `care_coordination`: LLM helps navigate fragmented specialties, referrals, or treatment decisions.

### Self-Management

- `behavior_change`: Diet, weight loss, exercise, sleep, smoking/cannabis reduction, or adherence support.
- `symptom_tracking`: User logs symptoms and asks LLM to identify patterns.
- `rehabilitation_planning`: Return-to-activity, physical therapy, or recovery planning.
- `medication_or_supplement_decision`: LLM informs medication, supplement, or dose-related choices.
- `addiction_support`: LLM used for cravings, withdrawal, accountability, or recovery reflection.

### Mental Health and Emotional Support

- `emotional_support`: User experiences comfort, containment, or nonjudgmental listening.
- `psychoeducation`: LLM explains attachment, trauma, diagnoses, coping strategies, or therapy concepts.
- `journaling_or_reflection`: LLM structures self-reflection or meaning-making.
- `rumination_or_compulsion`: LLM reinforces reassurance seeking, spiraling, or compulsive checking.
- `sycophantic_validation`: LLM intensifies grandiose, paranoid, or distorted beliefs.

## Outcome Codes

- `clinician_or_test_confirmed`: The account reports later confirmation by a clinician, lab, imaging, genetic test, or pathology.
- `clinician_disconfirmed`: The account reports that a clinician later contradicted the LLM.
- `self_reported_improvement`: The user reports improvement without external confirmation.
- `understanding_improved`: User reports better comprehension, confidence, or preparedness.
- `care_escalated`: LLM output led to urgent care, specialist appointment, test request, or clinician contact.
- `care_delayed_or_risked`: LLM output may have delayed care or created a safety risk.
- `no_resolution`: AI was used but did not solve the user's problem.
- `distress_reduced`: User reports less fear, anxiety, shame, or confusion.
- `distress_increased`: User reports worse anxiety, rumination, mania, delusion, or interpersonal conflict.

## Risk Codes

- `privacy_exposure`: User uploads sensitive medical records, identifiable data, or genomics.
- `overconfidence`: User or model frames output as certain.
- `clinical_complexity`: Case involves cancer, pediatrics, pregnancy, psychiatry, emergency symptoms, or polypharmacy.
- `unsafe_self_treatment`: LLM use leads to medication, supplement, diet, or treatment change without clinical oversight.
- `model_instability`: User notes outputs changed across models or over time.
- `system_gap`: AI is used because care is inaccessible, rushed, siloed, expensive, or dismissive.

## Analytic Memos

For each included anecdote, write 2-4 sentences answering:

1. What gap in care or understanding did the LLM fill?
2. What did the user do differently because of the LLM?
3. What evidence supports the claimed outcome?
4. What is the main safety or interpretation risk?

## Working Higher-Order Themes

1. **The LLM as translator**
   Makes medical records, reports, and clinical jargon legible.

2. **The LLM as pattern finder**
   Synthesizes longitudinal symptoms and fragmented records.

3. **The LLM as appointment amplifier**
   Helps patients ask better questions and use scarce clinician time more effectively.

4. **The LLM as always-on companion**
   Provides emotional processing, journaling, and behavioral support between encounters.

5. **The LLM as risky validator**
   May reinforce false certainty, rumination, compulsions, or unsafe decisions.

6. **The LLM as workaround for system gaps**
   Users turn to AI when healthcare feels inaccessible, rushed, siloed, or non-explanatory.
