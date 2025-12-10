import pandas as pd

def find_investments(insurance: pd.DataFrame) -> pd.DataFrame:
     # 計算每個 tiv_2015 與每個位置 (lat, lon) 的出現次數
    insurance = insurance.copy()
    insurance['cnt_2015'] = insurance.groupby('tiv_2015')['tiv_2015'].transform('size')
    insurance['cnt_loc'] = insurance.groupby(['lat', 'lon'])['lat'].transform('size')
    
    # 過濾並加總 2016 保額，同時四捨五入
    total = round(insurance.loc[
        (insurance['cnt_2015'] > 1) & (insurance['cnt_loc'] == 1),'tiv_2016'].sum(), 2)
    
    # 回傳 DataFrame
    return pd.DataFrame({'tiv_2016': [total]})