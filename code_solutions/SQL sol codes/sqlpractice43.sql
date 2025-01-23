select
	year(order_date) as order_year,
    month(order_date) as order_month,
    count(order_id) as no_of_orders
from
	orders
group by order_year, order_month