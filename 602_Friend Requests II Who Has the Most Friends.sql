# Write your MySQL query statement below
WITH UniquePairs AS (
    -- 無論 1-2 還是 2-1，都統一轉成 (1, 2) 並去重
    SELECT DISTINCT
        CASE WHEN requester_id < accepter_id THEN requester_id ELSE accepter_id END AS p1,
        CASE WHEN requester_id < accepter_id THEN accepter_id ELSE requester_id END AS p2
    FROM RequestAccepted
),
AllIDs AS (
    -- 從去重後的關係中抓出 ID
    SELECT p1 AS id FROM UniquePairs
    UNION ALL --union會去除重複所以用union all
    SELECT p2 AS id FROM UniquePairs
)
SELECT id, COUNT(*) AS num
FROM AllIDs
GROUP BY id
ORDER BY num DESC
LIMIT 1;