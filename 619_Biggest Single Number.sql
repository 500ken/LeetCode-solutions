With temp as(
    select num
        from MyNumbers
        group by num
        HAVING COUNT(num) = 1
        order by num desc
        limit 1)
select max(num) as num from temp