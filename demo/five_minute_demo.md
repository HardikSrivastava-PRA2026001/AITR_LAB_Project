# Five-minute demonstration

**0:00–0:40 — Research question:** connect the experiment to the prior review and distinguish token likelihood from semantic uncertainty.

**0:40–1:20 — Dataset/protocol:** show official HaluEval QA source, schema, sampling seed, 1,000-pair classifier sample, pair-aware 80/20 split and 100-pair likelihood sample.

**1:20–2:20 — Code:** show TF-IDF, Logistic Regression, Linear SVM and GPT-2 conditional scoring. Explain that answers are supplied candidates, not GPT-2 generations.

**2:20–3:20 — Results:** show baseline CSV and the weak likelihood results: AUROC 0.4437 expected direction, 0.5563 reversed.

**3:20–4:20 — Deeper analysis:** show actual confusion matrices/error examples from final notebook; discuss score-direction sensitivity, benchmark construction and limitations.

**4:20–5:00 — Reproducibility:** show README, config, environment, CSVs, LaTeX and provenance logs. Rerun one metric if asked.

Only show actual notebook outputs; never present placeholders as evidence.
