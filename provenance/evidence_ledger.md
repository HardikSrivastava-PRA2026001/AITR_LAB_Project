# Evidence ledger

## Source artifacts
- Executed notebook uploaded as `notebooks/AITR_Hallucination_Uncertainty.ipynb` (the submitted notebook copy is preserved).
- Initial run archive: `results/uploaded_run/`.
- Corrected GPT-2 exports: `results/token_likelihood_results_corrected.csv` and `results/token_likelihood_metrics_corrected.csv`.
- Classifier metrics: `results/baseline_metrics.csv`.
- Test predictions: `results/test_predictions.csv` and `results/svm_test_predictions.csv`.
- Error inspection: `results/error_analysis.csv`.

## Reported measurements
Classifier values are transcribed from `baseline_metrics.csv`. Corrected likelihood metrics are transcribed from `token_likelihood_metrics_corrected.csv`. No confidence intervals, significance tests or multi-seed estimates are present.

## Important caveat
The corrected metrics happen to match the earlier values reported in the user's corrected export history, but that equality does not independently prove implementation correctness. Keep both original and corrected exports and inspect the notebook code before claiming the corrected implementation has been independently validated.
