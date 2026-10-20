# Research decisions and evidence ledger

| Decision | Reason | Status | Follow-up |
|---|---|---|---|
| Keep topic tied to prior review | Course requires continuity | Verified from course brief/review | Cite original sources |
| Use HaluEval QA | Paired answers and supporting knowledge | Verified from official repository and notebook summary | Recheck URL and terms |
| Compare Logistic Regression and Linear SVM | Lightweight lexical baselines | Reported as run | Rerun and preserve output |
| Group split by question+knowledge | Avoid paired-answer leakage | Reported protocol | Add explicit assertion |
| Score GPT-2 conditional likelihood | Feasible probability-based signal | Reported as run on 200 candidates | Describe as supplied-candidate scoring |
| Report weak likelihood result | Expected direction AUROC 0.4437 | Reported metric | Rerun score-direction code |
| Do not claim semantic entropy | No semantic clustering/multiple samples | Verified scope | Future work only |
| Treat results as exploratory | One split, small likelihood sample | Verified protocol | Avoid significance claims |
