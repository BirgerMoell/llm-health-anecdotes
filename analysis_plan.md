# Analysis Plan

## Goal

Move from a 100-record seed corpus to a defensible qualitative analysis of how patients and caregivers describe using LLMs for health.

## Immediate Priorities

1. **Freeze the seed corpus**
   Treat the current 100 records as version 0.1. Add new records only if they fill a clear gap or replace a weak source.

2. **Clean citation quality**
   The biggest weakness is direct traceability for thread comments. Many records currently point to the parent Reddit thread rather than a comment permalink.

3. **Normalize coding fields**
   Create a separate `coded_corpus.csv` rather than overloading the raw seed sheet.

4. **Pilot code 25 records**
   Choose a stratified sample across source type, health domain, valence, and evidence quality.

5. **Revise codebook**
   Update the codebook after pilot coding, especially around mental health, privacy exposure, and clinical confirmation.

6. **Code all 100**
   Then generate tables and counts for manuscript results.

## Recommended Corpus Versions

- `seed_corpus.csv`: raw-ish discovery spreadsheet; do not remove records casually.
- `coded_corpus.csv`: normalized analytic layer with stable categories.
- `representative_cases.md`: narrative case summaries for manuscript tables.
- `cleanup_queue.md`: permalink/source-quality tasks.

## Analytic Unit

One record equals one distinct account of LLM use for health. A thread can contribute multiple records when separate users describe separate experiences.

## Source Hierarchy

Use this hierarchy for manuscript evidence strength:

1. **Raw first-person public account**
   Example: Reddit post, patient forum post, personal essay.

2. **Raw caregiver/family account**
   Example: spouse, parent, sibling, partner describing use for another person.

3. **Disease-specific patient publication**
   Example: Lupus News Today column, personal health essay.

4. **Journalism-mediated patient account**
   Useful, but interpret as reported anecdote rather than raw narrative.

5. **Company-mediated account**
   Useful but potentially promotional; use with caution.

6. **Clinical/expert-reported case**
   Useful for harm/risk context but not the same as patient narrative.

7. **Peer advice/norm-setting**
   Use for diffusion and community norms, not outcome claims.

## Evidence Quality Labels

Recommended labels for `coded_corpus.csv`:

- `strong_self_report`: first-person or caregiver narrative with concrete symptoms/use/action/outcome.
- `reported_confirmation`: account reports clinician, lab, imaging, pathology, biopsy, genetic test, or hospitalization confirmation.
- `self_report_only`: perceived improvement without external confirmation.
- `media_mediated`: journalist/institution reports the story.
- `company_mediated`: source has direct commercial/company interest.
- `needs_permalink`: comment-level source currently lacks direct permalink.
- `high_stakes_sensitive`: pediatrics, cancer treatment decisions, pregnancy/obstetrics, suicidality, psychosis, acute emergencies, medication changes.
- `insufficient_detail`: useful signal but not enough detail for strong analysis.

## Recommended Sampling for Pilot

Pilot should include:

- 5 diagnostic/triage cases
- 5 report/lab translation cases
- 5 chronic illness/diagnostic odyssey cases
- 5 mental health/emotional support cases
- 5 harm/near-miss cases

Include at least:

- 10 raw first-person posts
- 3 caregiver accounts
- 3 patient-forum accounts
- 3 media-mediated accounts
- 5 negative or mixed-valence cases

## Outputs After Coding

1. **Table 1: Corpus characteristics**
   Source type, account type, health domain, valence, source quality.

2. **Table 2: Use-case taxonomy**
   Translator, pattern finder, appointment amplifier, always-on companion, behavior-change scaffold, risky validator, system workaround.

3. **Table 3: Harm mechanisms**
   Wrong triage, unsafe treatment suggestion, reassurance compulsion, psychosis/mania amplification, privacy exposure, model instability, unresolved system bottleneck.

4. **Figure 1: Patient work displaced onto LLMs**
   Records -> interpretation -> questions -> action -> clinician encounter.

5. **Manuscript case boxes**
   Short paraphrased vignettes, not long quotes.

## Decision Rule for Publication-Quality Cases

A case is publication-quality if it has:

- stable URL
- enough detail to identify the health task
- enough detail to identify the LLM role
- an action or outcome claim
- no need to quote sensitive identifying text
- a source quality label that matches its use in the paper

If a case lacks direct permalink or details, it can still inform exploratory coding but should not be a featured vignette.
