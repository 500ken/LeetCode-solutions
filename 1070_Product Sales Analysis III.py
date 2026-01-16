import pandas as pd

def sales_analysis(sales: pd.DataFrame) -> pd.DataFrame:
    # 1. 計算每個產品的最小年份，並將結果廣播 (broadcast) 回每一行
    sales['min_year']=sales.groupby('product_id')['year'].transform('min')
    # 2. 篩選出年份等於最小年份的資料
    result=sales[sales['year']==sales['min_year']]
    # 3. 重新命名與挑選欄位
    result=result.rename(columns={'year':'first_year'})
    return result[['product_id','first_year','quantity','price']]