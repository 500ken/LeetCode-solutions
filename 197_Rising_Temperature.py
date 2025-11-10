import pandas as pd

def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    # 🪄 1️⃣ 自我 merge：讓每一筆都對應到「昨天」那筆資料
    df = weather.merge(
    weather,  # 自己 join 自己
    how='left',
    left_on='recordDate',
    right_on=weather['recordDate'] - pd.Timedelta(days=1),  # 左邊日期 -1 天,  # 對應右邊的日期
    suffixes=('_yesterday', '_today') )

    # 🪄 2️⃣ 篩選今天溫度 > 昨天溫度的紀錄
    result = df[df['temperature_today'] > df['temperature_yesterday']][['id_today']]

    # 🪄 3️⃣ 改欄名對齊題目
    result.columns = ['id']
    return result