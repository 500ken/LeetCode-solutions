import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    # 合併 customers 和 orders，保留所有顧客
    merged = customers.merge(orders, left_on='id', right_on='customerId',  how='left',suffixes=('_cus', '_ord'))

    # 統計每個顧客的訂單數
    order_count = merged.groupby(['id_cus', 'name'])['customerId'].count().reset_index()

    # 篩出沒有訂單的顧客（count == 0）
    result = (
        order_count
        .loc[order_count['customerId'] <1, ['name']]
        .rename(columns={'name': 'Customers'})
    )
    return result