# Hallucination Detection on HaluEval QA: Small-Scale Study

This repository compares three approaches on HaluEval QA: (1) TF-IDF + Logistic Regression, (2) TF-IDF + Linear SVM, and (3) GPT-2 conditional candidate-answer likelihood. This is an exploratory course project; it does not implement semantic entropy.

## Main results

| Model | Accuracy | F1 | AUROC | AUPRC |
|---|---:|---:|---:|---:|
| TF-IDF + Logistic Regression | 0.6300 | 0.6126 | 0.6862 | 0.6876 |
| TF-IDF + Linear SVM | 0.6375 | 0.5983 | 0.7009 | 0.7059 |
| GPT-2 likelihood (original score direction) | -- | -- | 0.4437 | 0.4380 |
| GPT-2 likelihood (reversed score direction) | -- | -- | 0.5563 | 0.5023 |

Classifier metrics are from the uploaded experiment CSV. GPT-2 metrics are from the separately preserved corrected export. The small likelihood sample provides weak discrimination; likelihood is not a direct measure of truth.

## Repository layout

- `notebooks/`: starter and uploaded executed notebooks.
- `results/`: initial uploaded run, actual CSVs, corrected likelihood exports and figures.
- `paper/main.tex`: LaTeX source.
- `paper/main.pdf`: compiled paper PDF.
- `paper/references.bib`: bibliography file.
- `provenance/`: research brief, decisions, baseline validation, AI assistance and evidence ledger.
- `demo/five_minute_demo.md`: presentation outline.

## Reproduce

1. Create a Python environment compatible with the pinned versions in `requirements.txt` (the recorded run used Python 3.13.16).
2. Install dependencies: `pip install -r requirements.txt`.
3. Open `notebooks/AITR_Hallucination_Uncertainty_executed.ipynb` in Google Colab or Jupyter.
4. Follow `data/README.md` to retrieve HaluEval from the official repository. Do not assume reruns will be bit-for-bit identical across dependency versions or hardware.
5. Run all cells in order. Outputs are saved by the notebook to its configured results directory.

## Paper build

From `paper/`, compile with `pdflatex main.tex` twice if needed. The manuscript includes the actual recorded classifier metrics and corrected likelihood metrics; check the citations and formatting against the course instructions before submission.

## Data and limitations

The raw dataset is not redistributed. The classifier experiment uses 1,000 sampled pairs (2,000 answer instances) and one group-based 80/20 split. GPT-2 scores 100 pairs (200 answer instances). There are no multi-seed estimates, confidence intervals or significance tests. See `provenance/` and the paper for the full limitations.
