from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
metrics = pd.read_csv(ROOT / "results" / "baseline_metrics.csv")
required = {"model", "accuracy", "precision", "recall", "f1", "auroc", "auprc"}
assert required.issubset(metrics.columns)
assert len(metrics) >= 2
assert metrics[list(required - {"model"})].notna().all().all()
assert metrics["model"].is_unique
print(metrics.to_string(index=False))
print("\nCSV schema and baseline count checks passed.")
print("Reconcile these transcribed metrics with the final executed notebook.")
