import pandas as pd

def find_customer_referee(customer: pd.DataFrame) -> pd.DataFrame:
    result = customer.loc[(customer['referee_id'] != 2) | (customer['referee_id'].isnull()),['name']]
    return result