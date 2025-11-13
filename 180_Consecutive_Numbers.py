import pandas as pd

def consecutive_numbers(logs: pd.DataFrame) -> pd.DataFrame:
    n = 3  # 至少連續 3 次
    # Step 1: 建立「連續群組」，並新增欄位到 logs
    logs = logs.sort_values('id').reset_index(drop=True)
    logs['grp'] = (logs['num'] != logs['num'].shift()).fillna(True).cumsum().astype(int)
    
    #print(logs)
    # Step 2: 計算每個群組中相同數字的長度
    group_counts = logs.groupby(['grp', 'num']).size().reset_index(name='count')
    
    # Step 3: 篩出連續 >= n 次的數字
    result = group_counts.loc[group_counts['count'] >= n, ['num']].drop_duplicates()
    #print(group_counts)

    # Step 4: 回傳結果，欄位改成題目要求
    return result.rename(columns={'num': 'ConsecutiveNums'})