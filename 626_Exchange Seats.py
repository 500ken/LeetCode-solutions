import pandas as pd
import numpy as np

def exchange_seats(seat: pd.DataFrame) -> pd.DataFrame:
    n = len(seat)
    
    # 建立一個 id 的副本來進行修改
    new_id = seat['id'].copy()
    
    # 邏輯 1：偶數 id -> 變成 id - 1
    new_id[seat['id'] % 2 == 0] -= 1
    
    # 邏輯 2：奇數 id -> 變成 id + 1
    # 但要注意不能超過總人數（處理奇數總數的最後一位）
    mask_odd = (seat['id'] % 2 == 1) & (seat['id'] < n)
    new_id[mask_odd] += 1
    
    # 將修改後的 id 填回去並重新排序
    seat['id'] = new_id
    return seat.sort_values('id')