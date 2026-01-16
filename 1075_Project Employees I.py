import pandas as pd

def project_employees_i(project: pd.DataFrame, employee: pd.DataFrame) -> pd.DataFrame:
    # 1. Merge 兩個表格
    df =pd.merge(project,employee,on='employee_id')
    
    # 2. 依照 project_id 分組並計算平均值
    # .round(2) 處理四捨五入到小數點兩位
    result= df.groupby('project_id')['experience_years'].mean().round(2).reset_index()
        
    # 3. 重新命名欄位以符合 Output 要求
    result.columns = ['project_id', 'average_years']
    
    return result
  