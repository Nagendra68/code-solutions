SELECT title, release_year
FROM movies
WHERE title LIKE "%Thor%"
ORDER BY release_year desc