import pandas as pd

def sales_analysis(product: pd.DataFrame, sales: pd.DataFrame) -> pd.DataFrame:
     # 1) Q1 銷售紀錄
    q1_sales = sales[sales['sale_date'].between('2019-01-01', '2019-03-31')]

    # 2) 找出 Q1 之外有銷售的商品
    outside_q1_products = sales[~sales['sale_date'].between('2019-01-01', '2019-03-31')]['product_id'].unique()

    # 3) Q1 銷售且沒有 Q1 之外銷售的商品
    valid_product_ids = q1_sales[~q1_sales['product_id'].isin(outside_q1_products)]['product_id'].unique()

    # 4) 從 Product 表取出商品名稱
    result = product[product['product_id'].isin(valid_product_ids)][['product_id', 'product_name']]

    return result