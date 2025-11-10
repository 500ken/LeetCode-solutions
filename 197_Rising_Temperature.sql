select b.id 
    from Weather a 
        left join weather b on DATEDIFF(b.recordDate, a.recordDate) = 1
where b.temperature > a.temperature;