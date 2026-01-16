# Write your MySQL query statement below

SELECT 
    CASE 
        -- 如果是奇數且是最後一個，id 不變
        WHEN id % 2 = 1 AND id = (SELECT MAX(id) FROM Seat) THEN id
        -- 如果是奇數（非最後一個），id + 1
        WHEN id % 2 = 1 THEN id + 1
        -- 如果是偶數，id - 1
        ELSE id - 1
    END AS id,
    student
FROM Seat
ORDER BY id; -- 最後一定要按新 id 排序