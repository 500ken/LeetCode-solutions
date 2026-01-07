import pandas as pd

def biggest_single_number(my_numbers: pd.DataFrame) -> pd.DataFrame:
    # 1. 找出只出現過一次的數字 (keep=False 代表只要重複就全部丟掉)
    single_list=my_numbers.drop_duplicates(subset='num',keep=False)
    # 2. 取得最大值
    # 如果 unique_nums 是空的，max() 會回傳 NaN
    max_num=single_list['num'].max()

    # 3. 依照題目要求回傳 DataFrame 格式
    return pd.DataFrame({'num': [max_num]})