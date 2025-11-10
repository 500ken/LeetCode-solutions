import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    # RANK 模擬 SQL RANK
    scores['rank'] = scores['score'].rank(method='dense', ascending=False).astype(int)
    result = scores.sort_values(by='rank', ascending=True)[['score','rank']].reset_index(drop=True)

    return result

#| SQL 函數         | Pandas 對應               | 特點            |
#| -------------- | ----------------------- | ------------- |
#`RANK()`       | `.rank(method='min')`   | 有 tie 跳號      |
#| `DENSE_RANK()` | `.rank(method='dense')` | 有 tie 不跳號     |
#| `ROW_NUMBER()` | `.rank(method='first')` | 每筆唯一排名，不論 tie |
