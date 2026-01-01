# Write your MySQL query statement below
With filterpeople As (
    select *,
           id-row_number() over(order by id) as grp
    from Stadium
    where people >=100
),
continuedate As (
    select *,
        count(*) over(partition by grp) as cnt
    from 
        filterpeople
)
select id,visit_date,people
from continuedate
where cnt>=3
order by visit_date