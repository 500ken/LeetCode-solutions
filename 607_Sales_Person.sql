# Write your MySQL query statement below
select sp.name
from SalesPerson sp
where sales_id not in 
(select sales_id 
    from Orders O
    join Company c on c.com_id =O.com_id
    where c.name = 'RED')