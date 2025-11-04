import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    result = (
    person['email']
    .value_counts()
    .loc[lambda x: x > 1]        # 篩選出現次數 > 1
    .index.to_frame(name='Email')  # 把 index 轉為 DataFrame
    )
    return result