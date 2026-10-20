# G1 Research brief

## Topic and continuity
The previous review, *Token-Level Uncertainty as a Predictor of Hallucination in Large Language Models*, discusses whether token/sequence probability signals can help predict hallucinations and the difference between wording uncertainty and semantic uncertainty.

## Gap
**Verified from the review and implementation scope:** token-level likelihood and semantic uncertainty are distinct; semantic entropy requires multiple generations and semantic-equivalence grouping, which this experiment did not implement.

**Inference to test:** a simple conditional-likelihood score may not reliably separate benchmark-provided correct and hallucinated candidate answers, while lexical supervised baselines may exploit answer-text patterns.

## Research question
On a reproducible sample of HaluEval QA pairs, how do TF-IDF + Logistic Regression, TF-IDF + Linear SVM, and GPT-2 conditional answer likelihood compare for distinguishing right answers from benchmark-provided hallucinated answers?

## Pathway
Pathway B: controlled comparative study.

## Dataset and feasibility
HaluEval QA: 10,000 examples according to the official repository; each includes knowledge, question, right answer, hallucinated answer. Classifier sample: 1,000 pairs/2,000 answer instances. GPT-2 sample: 100 pairs/200 answers. Recorded Colab hardware: Tesla T4.

## Metrics and decision rule
Accuracy, precision, recall, F1, AUROC, AUPRC and fit time where available. Treat results descriptively; no repeated splits or confidence intervals.

## Supporting papers to verify against primary sources
- Li et al. (2023), HaluEval, EMNLP 2023, DOI 10.18653/v1/2023.emnlp-main.397.
- Farquhar et al. (2024), semantic entropy, Nature, DOI 10.1038/s41586-024-07421-0.
- Vashurin et al. (2025), LM-Polygraph benchmark, TACL 13, DOI 10.1162/tacl_a_00737.
- Ravichander et al. (2025), HALoGEN, ACL 2025, DOI 10.18653/v1/2025.acl-long.71.

## Threats to validity
Constructed labels, small likelihood sample, one split, single model, likelihood not equivalent to factual correctness, prompt/truncation sensitivity, no confidence intervals, no semantic entropy.
