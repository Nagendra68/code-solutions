select
	round(avg(unit_price), 2) Average_price,
    sum(units_in_stock) total_stock,
    sum(discontinued) total_discontinued
from
	products;