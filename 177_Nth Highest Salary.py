import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    s = employee['salary'].drop_duplicates().sort_values(ascending=False).reset_index(drop=True)
    # 2) 取第 N 高
    if N <= 0 or N > len(s):
        val = None
    else:
        val = s.iloc[N-1]
    
    return pd.DataFrame({'getNthHighestSalary('+str(N)+')': [val]})