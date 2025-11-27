import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    counts = employee['managerId'].value_counts()
    managers = counts[counts >= 5].index

    return employee.loc[
        employee['id'].isin(managers), 
        ['name']
    ].rename(columns={'name': 'name'})