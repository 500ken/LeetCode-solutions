import pandas as pd
import numpy as np

def triangle_judgement(triangle: pd.DataFrame) -> pd.DataFrame:
    # 同時檢查三個條件
    condition = (triangle['x'] + triangle['y'] > triangle['z']) & \
                (triangle['x'] + triangle['z'] > triangle['y']) & \
                (triangle['y'] + triangle['z'] > triangle['x'])
    
    # 根據條件填入 'Yes' 或 'No'
    triangle['triangle'] = np.where(condition, 'Yes', 'No')
    
    return triangle