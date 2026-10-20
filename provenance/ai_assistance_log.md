# AI assistance and research integrity log

This log records the kinds of assistance used during project development. The author must edit it to match the actual course disclosure policy and the actual work completed.

| Activity | AI assistance | Author verification still required |
|---|---|---|
| Scope narrowing | Helped narrow the prior review to a small comparison of lexical classifiers and conditional likelihood | Confirm that the research question accurately reflects the work |
| Data preparation | Suggested HaluEval loading, paired labels, sampling and group split | Re-run notebook, inspect schema and group separation |
| Baselines | Suggested TF-IDF with Logistic Regression and Linear SVM | Understand features, labels, split and metrics |
| Likelihood scoring | Suggested GPT-2 candidate-answer scoring and a character-offset answer-token variant | Independently inspect token indexing, truncation, offsets and saved metrics; corrected metrics matching prior values is not proof of correctness |
| Interpretation | Helped interpret metrics and articulate limitations | Ensure all claims match actual results and avoid unsupported claims |
| Paper and repository | Helped organize manuscript and documentation | Verify primary-source citations, course format, authorship and disclosure rules |

## Result provenance
- Initial uploaded run is retained under `results/uploaded_run/`.
- Corrected GPT-2 outputs are separately saved under `results/` with `_corrected` in the filename.
- The paper uses classifier metrics from `results/baseline_metrics.csv` and GPT-2 metrics from `results/token_likelihood_metrics_corrected.csv`.
- No confidence intervals, significance tests or unrun experiments are claimed.

The author should add exact dates, prompt excerpts or other disclosures if required by the course. Do not claim verification steps that were not performed.
