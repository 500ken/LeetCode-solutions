import pandas as pd

def human_traffic(stadium: pd.DataFrame) -> pd.DataFrame:

    # 1. 先篩選符合人流量條件的資料
    df=stadium[stadium['people']>=100].copy()
        
    # 2. 核心邏輯：偵測斷點
    # df['id'].diff() 會計算與上一筆的差值
    # 如果差值 != 1，代表中間有斷開，回傳 True (1)，否則 False (0)
    is_break = df['id'].diff() !=1
        
    # 3. 建立群組編號
    # 用 cumsum() 將布林值累加。每遇到一個 True (斷點)，編號就會 +1
    df['grp'] = is_break.cumsum()
    # 4. 計算組內數量並篩選
    df['cnt'] = df.groupby('grp')['id'].transform('count')
    
    return df[df['cnt'] >= 3][['id', 'visit_date', 'people']].sort_values('visit_date')