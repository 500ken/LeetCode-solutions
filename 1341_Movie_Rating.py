import pandas as pd

def movie_rating(movies: pd.DataFrame, users: pd.DataFrame, movie_rating: pd.DataFrame) -> pd.DataFrame:
    # 1. 篩選 2020-02 的資料
    feb = movie_rating[
        movie_rating['created_at'].between('2020-02-01', '2020-02-29')
    ]
    # 2. 最活躍使用者（評分最多 + 字典序最小）
    user_cnt = (
        movie_rating.groupby('user_id')
        .size()
        .reset_index(name='cnt')
        .merge(users, on='user_id')
        .sort_values(['cnt', 'name'], ascending=[False, True])
    )
    top_user = user_cnt['name'].iloc[0]

    # 3. 找平均評分最高的電影（平均 DESC + 標題 ASC）
    movie_avg = (
        feb.groupby('movie_id')['rating']
        .mean()
        .reset_index(name='avg_rating')
        .merge(movies, on='movie_id')
        .sort_values(['avg_rating', 'title'], ascending=[False, True])
    )
    top_movie = movie_avg['title'].iloc[0]

    # 4. 回傳兩筆結果
    return pd.DataFrame({
        'results': [top_user, top_movie]
    })