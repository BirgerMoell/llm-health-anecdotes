# The Plural of Anecdote Is Data

**How Patients Describe Using Large Language Models for Health**  
Birger Moëll

This repository contains an exploratory qualitative evidence map of public online accounts describing how patients, caregivers, family members, and peers use large language models for health-related sensemaking.

The project focuses on anecdotes as **behavioral and interpretive data**: not proof of clinical efficacy, but evidence of what people try, where care feels absent, what LLMs are asked to do, and where risks emerge.

## Paper

- [PDF paper](paper_pdf/the_plural_of_anecdote_is_data.pdf)
- [Manuscript draft](manuscript_draft.md)
- [GitHub Pages site](https://birgermoell.github.io/llm-health-anecdotes/)

## Repository Contents

- `seed_corpus.csv`: 100-record seed corpus of public anecdotes and source metadata.
- `coded_corpus.csv`: 35-record pilot-coded analytic subset.
- `source_appendix.md`: Appendix mapping `LHA-###` source IDs to public URLs.
- `codebook.md`: Initial qualitative codebook.
- `search_log.md`: Search strategy and yield notes.
- `manuscript_draft.md`: Current manuscript text.
- `build_journal_pdf.py`: Reproducible PDF, figure, table, and appendix builder.
- `paper_pdf/`: Generated PDF and publication-style figures.
- `docs/`: GitHub Pages site.

## Core Claim

The corpus suggests that patients are using LLMs less as stand-alone doctors than as tools for the unpaid work around care: translating records, preparing appointments, synthesizing fragmented information, supporting behavior change, and seeking emotional containment between clinical encounters.

The same affordances can also create risk: overconfident triage, unsafe medication or diet advice, compulsive reassurance, psychosis or mania amplification, privacy exposure, and failures to bridge back to accountable care.

## Figures

The PDF includes a visual atlas of the findings. Two centerpiece figures are:

- **Language of Patient Work**: a corpus-derived word/concept map showing how patients describe LLM use around care.
- **Narrative Grammar of LLM Health Use**: a flow model connecting system gaps, LLM functions, patient actions, and safety boundaries.

## Rebuild the PDF

From the repository root:

```bash
python3 build_journal_pdf.py
```

This regenerates:

- `paper_pdf/the_plural_of_anecdote_is_data.pdf`
- `paper_pdf/figures/*.png`
- `source_appendix.md`

## Limitations

The corpus is exploratory, self-selected, English-heavy, and platform-dependent. Public anecdotes do not verify diagnoses, outcomes, or causality. Counts describe the assembled corpus and pilot-coded subset; they are not prevalence estimates.

## Citation

Moëll B. *The Plural of Anecdote Is Data: How Patients Describe Using Large Language Models for Health*. Exploratory qualitative evidence map. 2026. Available from: https://github.com/birgermoell/llm-health-anecdotes

