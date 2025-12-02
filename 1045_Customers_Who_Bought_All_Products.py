import pandas as pd

def find_customers(customer: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    # 1) 計算每個顧客購買過的不同產品數
    cust_product_count = customer.groupby('customer_id')['product_key'].nunique().reset_index()
    cust_product_count.rename(columns={'product_key': 'unique_products'}, inplace=True)

    # 2) 總產品數
    total_products = product['product_key'].nunique()
    
    # 3) 篩選顧客
    result=cust_product_count[cust_product_count['unique_products']==total_products][['customer_id']]
    
    return result
    