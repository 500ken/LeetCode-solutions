import pandas as pd
import numpy as np

def trips_and_users(trips: pd.DataFrame, users: pd.DataFrame) -> pd.DataFrame:
    
    # 1. 找出所有未被停權的使用者 ID 列表
    unbanned_ids = users[users['banned'] == 'No']['users_id'].tolist()
    
    # 2. 執行向量化篩選 (單次操作，最高效)
    #    檢查 client_id 和 driver_id 都在 unbanned_ids 列表中的行
    valid_mask = (trips['client_id'].isin(unbanned_ids)) & \
                 (trips['driver_id'].isin(unbanned_ids))
    valid_trips = trips[valid_mask].copy()

    # 3. 篩選日期範圍
    start_date = '2013-10-01'
    end_date = '2013-10-03'
    valid_trips = valid_trips[
        (valid_trips['request_at'] >= start_date) & 
        (valid_trips['request_at'] <= end_date)
    ]
    
    # 4. 建立輔助欄位：'is_cancelled'
    valid_trips['is_cancelled'] = np.where(
        valid_trips['status'] != 'completed', 
        1, 
        0
    )
    
    # 5. 分組計算
    daily_stats = valid_trips.groupby('request_at').agg(
        total_trips=('id', 'count'),
        cancelled_trips=('is_cancelled', 'sum')
    ).reset_index()
    
    # 6. 計算並格式化取消率
    daily_stats['Cancellation Rate'] = (
        daily_stats['cancelled_trips'] / daily_stats['total_trips']
    ).round(2)
    
    return daily_stats.rename(columns={'request_at': 'Day'})[['Day', 'Cancellation Rate']]