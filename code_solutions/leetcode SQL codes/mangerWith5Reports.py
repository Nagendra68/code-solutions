select name from Employee
where id in(
    select managerId
    from Employee
    where managerId is not null
    group by managerId
    having count(id)>=5
)