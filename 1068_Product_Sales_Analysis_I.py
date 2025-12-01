import pandas as pd

def sales_analysis(sales: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    result=pd.merge(sales,product)[['product_name','year','price']].sort_values(['product_name','year']).reset_index(drop=True)
    return result