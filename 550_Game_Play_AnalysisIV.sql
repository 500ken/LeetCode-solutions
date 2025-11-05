# Write your MySQL query statement below
SELECT 
    ROUND(
        COUNT(DISTINCT b.player_id) / COUNT(DISTINCT a.player_id), 2 ) AS fraction
FROM 
    Activity a
LEFT JOIN 
    Activity b
ON 
    a.player_id = b.player_id 
    AND DATEDIFF(b.event_date, a.event_date) = 1
WHERE 
    a.event_date = (
        SELECT MIN(event_date)
        FROM Activity
        WHERE player_id = a.player_id
    );