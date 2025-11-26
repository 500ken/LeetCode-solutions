import pandas as pd

def top_three_salaries(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    # merge department name
    df = employee.merge(department, left_on='departmentId', right_on='id', suffixes=('','_dept'))

    # 計算部門內薪水的 dense rank（由高到低）
    df['rnk'] = df.groupby('departmentId')['salary'].rank(method='dense', ascending=False)

    # 取前 3 名（包含並列）
    df = df[df['rnk'] <= 3]

    # 輸出格式符合題目
    return df[['name_dept', 'name', 'salary']].rename(
        columns={'name_dept':'Department', 'name':'Employee'}
    ).sort_values(['Department', 'salary'], ascending=[True, False])
