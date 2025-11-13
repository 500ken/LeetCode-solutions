/* Write your PL/SQL query statement below */
--Ans1
SELECT Department, Employee, Salary
FROM (
    SELECT 
        d.name AS Department,
        e.name AS Employee,
        e.salary AS Salary,
        RANK() OVER (PARTITION BY d.id ORDER BY e.salary DESC) AS rnk
    FROM Employee e
    JOIN Department d ON e.departmentID = d.id
) t
WHERE rnk = 1;

--Ans2
SELECT d.name AS Department, e.name AS Employee, e.salary AS Salary
FROM Employee e
JOIN Department d ON e.departmentID = d.id
WHERE e.salary = (
    SELECT MAX(salary) 
    FROM Employee 
    WHERE departmentID = e.departmentID
);