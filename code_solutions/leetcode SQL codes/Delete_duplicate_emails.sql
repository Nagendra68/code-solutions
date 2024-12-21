DELETE from Person
where id not in (
    select id from (
    select min(id) AS id
    from Person
    Group by email
) AS temp_table
);