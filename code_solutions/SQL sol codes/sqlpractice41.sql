select c.category_name , round(avg(p.unit_price), 2)
from categories c
join products p
on c.category_id = p.category_id
group by c.category_id