SELECT m.title , l.name
FROM movies m 
join languages l 
on m.language_id = l.language_id