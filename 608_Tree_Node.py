import pandas as pd

def tree_node(tree: pd.DataFrame) -> pd.DataFrame:
    tree['type']=''
    parent_ids = set(tree['p_id'].dropna())
    # 1. Root：沒有 p_id
    tree.loc[tree['p_id'].isna(), 'type'] = 'Root'

    # 2. Inner：有 p_id，且自己是 parent（在 parent_ids 裡）
    tree.loc[
        (tree['p_id'].notna()) & (tree['id'].isin(parent_ids)),     'type'] = 'Inner'

    # 3. Leaf：有 p_id，且不是 parent（不在 parent_ids）
    tree.loc[
        (tree['p_id'].notna()) & (tree['id'].isin(parent_ids) == False),'type'] = 'Leaf'

    return tree[['id', 'type']]
