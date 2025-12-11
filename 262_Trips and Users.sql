WITH valid_clients AS (
  SELECT DISTINCT users_id
  FROM Users
  WHERE banned = 'No' AND role = 'client'
),
valid_drivers AS (
  SELECT DISTINCT users_id
  FROM Users
  WHERE banned = 'No' AND role = 'driver'
)
SELECT
    t.request_at AS Day,
    --：將 COUNT(*) 轉換為 DECIMAL/FLOAT，避免整數除法錯誤
    ROUND(
        SUM(CASE WHEN LOWER(TRIM(t.status)) LIKE 'cancelled%' THEN 1 ELSE 0 END) 
        / CAST(COUNT(*) AS DECIMAL(10, 2)),
        2
    ) AS "Cancellation Rate"
 
FROM Trips t
JOIN valid_clients c ON t.client_id = c.users_id
JOIN valid_drivers d ON t.driver_id = d.users_id
WHERE
    -- LeetCode 262 題目的要求：限定日期範圍
    t.request_at BETWEEN '2013-10-01' AND '2013-10-03' 
GROUP BY
    t.request_at
ORDER BY
    t.request_at;