import pandas as pd

def delete_duplicate_emails(person: pd.DataFrame) -> None:
    # 先依照 id 排序（確保最小 id 在前）
    person.sort_values('id', inplace=True)
    # 刪除重複 email，只保留第一筆
    person.drop_duplicates(subset='email', keep='first',inplace=True)