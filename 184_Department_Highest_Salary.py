import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    #combine
    full_table=pd.merge(employee,department,how='left',left_on='departmentId',right_on='id',suffixes=('_e', '_d')
      )  # _e = employee, _d = department)
    # 選擇欄位並重新命名
    full_table = full_table[['name_d', 'name_e', 'salary']]
    full_table.columns = ['Department', 'Employee', 'Salary']

    #找出rank 1
    full_table['Rank'] = full_table.groupby('Department')['Salary'].rank(method='dense', ascending=False)

    result = full_table[full_table['Rank'] == 1].drop(columns='Rank').reset_index(drop=True)
    return result
    
