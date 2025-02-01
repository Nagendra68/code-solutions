select l.name, count(m.movie_id)  movie_count
from movies m
join languages l
on m.language_id = l.language_id
group by l.name