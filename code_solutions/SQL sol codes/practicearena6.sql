select (
    select release_year
    from movies
    order by release_year
    limit 1) as min_year, 
    (select release_year
    from movies
    order by release_year desc
    limit 1) as max_year