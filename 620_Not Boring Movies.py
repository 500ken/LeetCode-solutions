import pandas as pd

def not_boring_movies(cinema: pd.DataFrame) -> pd.DataFrame:
    # 1. 篩選條件：id 是奇數 (id % 2 != 0) 且 description 不是 'boring'
    condition = (cinema['id'] % 2 != 0) & (cinema['description'] != 'boring')
    
    # 2. 應用條件並排序
    result = cinema[condition].sort_values(by='rating', ascending=False)
    
    return result