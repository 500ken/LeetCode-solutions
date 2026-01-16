# Write your MySQL query statement below
with year_rank as(
    select  product_id, 
            year,
            quantity,
            price,
            rank() over(partition by product_id order by year ASC) as rnk
    from Sales 
    ) 
select product_id, year as first_year ,quantity,price
from year_rank
where rnk=1
