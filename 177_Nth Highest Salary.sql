CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
    SELECT salary
    FROM (
      SELECT salary, ROW_NUMBER() OVER (ORDER BY salary DESC) AS rn
      FROM (SELECT DISTINCT salary FROM Employee) AS t
    ) AS temp
    WHERE rn = N
  );
END