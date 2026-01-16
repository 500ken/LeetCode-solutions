import pandas as pd

def largest_orders_fastest(orders: pd.DataFrame) -> pd.DataFrame:
    if orders.empty:
        return pd.DataFrame(columns=['customer_number'])
    
    # value_counts() 是專門優化的計數函數，比 groupby 快速得多
    # idxmax() 直接回傳最大值的索引，不需排序
    top_customer = orders['customer_number'].value_counts().idxmax()
    
    return pd.DataFrame({'customer_number': [top_customer]})