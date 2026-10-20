# Dataset access

Primary source: RUCAIBox/HaluEval official GitHub repository:
https://github.com/RUCAIBox/HaluEval

The official QA file is `data/qa_data.json` in the upstream repository. Fields used:
- `knowledge`
- `question`
- `right_answer`
- `hallucinated_answer`

The upstream README describes 10,000 QA examples. The current notebook loaded 10,000 records, sampled 1,000 pairs with `random_state=42` for text classifiers, and scored the first 100 sampled pairs (200 candidate answers) with GPT-2.

## Download in Colab
```python
import pandas as pd
url = "https://raw.githubusercontent.com/RUCAIBox/HaluEval/main/data/qa_data.json"
df = pd.read_json(url)
print(df.shape)
print(df.columns.tolist())
df.head()
```
If the URL/repository layout changes, use the official repository and record the exact source path. Do not commit raw data unless upstream terms and course policy allow it.
