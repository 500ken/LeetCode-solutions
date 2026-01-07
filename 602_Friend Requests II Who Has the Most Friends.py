import pandas as pd
import numpy as np
def most_friends(request_accepted: pd.DataFrame) -> pd.DataFrame:

    # 1. 將每一行的兩個 ID 進行排序，確保 (1, 2) 和 (2, 1) 內容一致
    # np.sort(axis=1) 會橫向排序每一行
    pairs = np.sort(request_accepted[['requester_id', 'accepter_id']].values, axis=1)
    
    # 2. 去除重複的對 (Deduplicate Pairs)
    unique_df = pd.DataFrame(pairs, columns=['p1', 'p2']).drop_duplicates()
    
    # 3. 展開並計數 (與之前邏輯相同)
    all_ids = pd.concat([unique_df['p1'], unique_df['p2']])
    result = all_ids.value_counts().reset_index()
    result.columns = ['id', 'num']
    
    return result.head(1)