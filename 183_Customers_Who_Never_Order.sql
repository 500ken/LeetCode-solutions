SELECT c.name AS Customers 
FROM Customers c 
left join Orders o on c.id=o.customerId 
GROUP BY c.id, c.name
HAVING COUNT(o.id)<1;