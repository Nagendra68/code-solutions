select year(o.order_date) as order_year, round(sum(p.unit_price*od.quantity*od.discount),2) as discount_amount
from orders o
join order_details od
on o.order_id = od.order_id
join products p
on p.product_id = od.product_id
group by order_year
order by order_year desc