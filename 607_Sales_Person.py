import pandas as pd

def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    order_comp=orders.merge(company,on='com_id' ,how='left',suffixes=('_o','_c'))
    red_sale=order_comp[order_comp['name'] == 'RED']['sales_id'].unique()
    #red_sale = orders.merge(company, on='com_id').query("name == 'RED'")['sales_id'].unique()

    target=sales_person[~sales_person['sales_id'].isin(red_sale)][['name']]
    return target