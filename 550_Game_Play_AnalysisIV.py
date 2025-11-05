import pandas as pd

def gameplay_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    # Step 1️⃣ 找出每位玩家的首次登入日期
    first_login = activity.groupby('player_id', as_index=False)['event_date'].min().rename(columns={'event_date': 'first_login_date'})

    # Step 2️⃣ 合併原始資料
    merged = activity.merge(first_login, on='player_id', how='left')

    # Step 3️⃣ 找出隔天登入的玩家
    next_day = merged[merged['event_date'] == merged['first_login_date'] + pd.Timedelta(days=1)]

    # Step 4️⃣ 計算留存率
    retained_players = next_day['player_id'].nunique()
    total_players = first_login['player_id'].nunique()
    fraction = retained_players / total_players

    return pd.DataFrame({'fraction': [round(fraction, 2)]})