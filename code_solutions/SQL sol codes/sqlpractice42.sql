select c.city, c.company_name, c.contact_name, 'customers' as relationship
from customers c
union all
select s.city, s.company_name, s.contact_name, 'suppliers' as relationship
from suppliers s
order by city