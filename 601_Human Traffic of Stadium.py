import pandas as pd

def human_traffic(stadium: pd.DataFrame) -> pd.DataFrame:
    # 1. 篩選符合條件的行 (people >= 100)
    df = stadium[stadium['people'] >= 100].copy()
    
    # 2. 必須先按 id 排序，確保「連續性」在物理位置上是相鄰的
    df = df.sort_values('id')
    
    # 3. 核心邏輯：差值分組法 (Gaps and Islands)
    # df['id']: 可能是 [2, 3, 5, 6, 7]
    # range(len(df)): 永遠是 [0, 1, 2, 3, 4]
    # 相減結果 (grp): [2-0, 3-1, 5-2, 6-3, 7-4] -> [2, 2, 3, 3, 3]
    # 相同的差值代表 id 是連續增長的，因此被歸為同一個群組 (grp)
    df['grp'] = df['id'] - range(len(df))
    
    # 4. 計算每個群組內的成員總數 (cnt)
    # transform('count') 會將計算結果填回每一行，方便後續過濾
    df['cnt'] = df.groupby('grp')['id'].transform('count')
    
    # 5. 篩選出成員數 >= 3 的群組，並整理欄位輸出
    result = df[df['cnt'] >= 3][['id', 'visit_date', 'people']]
    
    return result