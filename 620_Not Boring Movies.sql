select *
from Cinema 
where description not like "%boring%"
    and MOD(id, 2) != 0
order by rating desc