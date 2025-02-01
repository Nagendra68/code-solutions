select * from movies
where 
    release_year = (select  max(release_year) from movies) or 
    release_year = (select min(release_year) from movies)