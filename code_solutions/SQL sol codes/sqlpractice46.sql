select movie_id, title, imdb_rating
from movies
having imdb_rating > (select sum(imdb_rating)/count(imdb_rating) from movies)