WITH flagged AS (
    SELECT
        tiv_2016,
        COUNT(*) OVER (PARTITION BY tiv_2015) AS cnt_2015,
        COUNT(*) OVER (PARTITION BY lat, lon) AS cnt_loc
    FROM insurance
)
SELECT ROUND(SUM(tiv_2016), 2) AS tiv_2016
FROM flagged
WHERE cnt_2015 > 1    -- tiv_2015 出現 >= 2 次（條件 1）
  AND cnt_loc = 1;    -- (lat, lon) 位置唯一（條件 2）