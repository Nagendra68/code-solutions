select p.product_name, s.company_name, c.category_name
from categories c
join products p
on c.category_id = p.category_id
join suppliers s
on p.supplier_id = s.supplier_id