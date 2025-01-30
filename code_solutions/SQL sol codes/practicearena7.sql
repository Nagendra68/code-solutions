select release_year, count(movie_id) as movie_count
from movies
group by release_year
order by release_year desc