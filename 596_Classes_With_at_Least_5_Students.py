import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    # 1️⃣ 分組計算每班人數
    class_count = courses.groupby('class').size().reset_index(name='num_students')
    #class_count = (courses.groupby('class')['student'].count().reset_index(name='num_students'))

    # 2️⃣ 篩選人數 >= 5
    result = class_count[class_count['num_students'] >= 5][['class']]
    return result
