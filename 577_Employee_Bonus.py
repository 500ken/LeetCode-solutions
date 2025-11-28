import pandas as pd

def employee_bonus(employee: pd.DataFrame, bonus: pd.DataFrame) -> pd.DataFrame:
    
    df = employee.merge(bonus, on='empId', how='left')
    result = df[df['bonus'].isna() | (df['bonus'] < 1000)][['name', 'bonus']]

    #import numpy as np
    #df = employee.merge(bonus, on='empId', how='left')

    #mask = (df['bonus'].to_numpy() < 1000) | np.isnan(df['bonus'].to_numpy())
    #result = df.loc[mask, ['name', 'bonus']]
    return result