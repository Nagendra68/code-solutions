with cte1 as (
    select m.movie_id, m.title , (f.revenue - f.budget) as profit
    from movies m
    join financials f
    on m.movie_id = f.movie_id
    where m.industry = "Hollywood" and m.release_year > 2000
)

select movie_id, title, profit
from cte1
where profit>500;