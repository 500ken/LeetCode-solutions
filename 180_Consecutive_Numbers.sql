SELECT DISTINCT Num AS ConsecutiveNums
FROM (
    SELECT 
        Num,
        LAG(Num, 1) OVER (ORDER BY Id) AS prev1,
        LAG(Num, 2) OVER (ORDER BY Id) AS prev2
    FROM Logs
) t
WHERE Num = prev1 AND Num = prev2;