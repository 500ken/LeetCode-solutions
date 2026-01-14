import pandas as pd

def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    # 1. 根據演員和導演分組，並計算每組出現的次數 (size)
    # reset_index() 是為了把分組的索引變回普通的欄位，方便後續篩選
    stats=actor_director.groupby(['actor_id', 'director_id']).size().reset_index(name='counts')
    
    # 2. 篩選出次數 >= 3 的組合
    result = stats[stats['counts'] >= 3]
    
    # 3. 回傳題目要求的欄位
    return result[['actor_id', 'director_id']]