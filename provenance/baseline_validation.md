# Baseline validation report

## Verified from the uploaded run artifacts
- Both text baselines completed and wrote `baseline_metrics.csv`.
- The classifier metrics report 800 total test prediction rows across the two classifiers (400 per classifier).
- Both confusion-matrix figures are preserved in `paper/figures/`.
- The test split is group-based with `random_state=42` according to the executed notebook code.
- The uploaded runtime was CPU-based; CUDA was unavailable.

## Results
| Model | Accuracy | Precision | Recall | F1 | AUROC | AUPRC | Fit time (s) |
|---|---:|---:|---:|---:|---:|---:|---:|
| TF-IDF + Logistic Regression | 0.6300 | 0.6429 | 0.5850 | 0.6126 | 0.6862 | 0.6876 | 0.79 |
| TF-IDF + Linear SVM | 0.6375 | 0.6708 | 0.5400 | 0.5983 | 0.7009 | 0.7059 | 0.71 |

## Limitations
This is a single split. There are no confidence intervals or significance tests. The results are a small benchmark experiment and do not demonstrate generalization.
