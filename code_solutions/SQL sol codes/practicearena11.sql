select  m.title, f.revenue, f.currency, f.unit
from movies m
join financials f on m.movie_id = f.movie_id
join languages l on m.language_id = l.language_id
where l.name = "Hindi"
order by f.revenue desc