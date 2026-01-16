import pandas as pd

def user_activity(activity: pd.DataFrame) -> pd.DataFrame:
    # 1. 確保日期欄位是 datetime 格式 (如果本來就是就不用這行)
    activity['activity_date'] = pd.to_datetime(activity['activity_date'])

    # 2. 設定日期範圍過濾
    # 2019-07-27 往前 30 天 (含當天) 的起始日是 2019-06-28
    mask = (activity['activity_date'] > '2019-06-27') & \
           (activity['activity_date'] <= '2019-07-27')
    df = activity[mask]
    
    # 3. 分組並計算唯一用戶數 (nunique)
    result = df.groupby('activity_date')['user_id'].nunique().reset_index()
    
    # 4. 重新命名欄位
    result.columns = ['day', 'active_users']
    
    return result