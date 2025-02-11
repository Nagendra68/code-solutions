with tp as (
    select
    c.customer_id,
    c.customer_name,
    sum(oi.quantity* oi.price_per_unit) as total_spent
from customers c
join orders o on c.customer_id = o.customer_id
join order_items oi on o.order_id = oi.order_id
where month(o.order_date) = 6 and year(o.order_date) = 2024
group by c.customer_id, c.customer_name
),

cnt as(
    select
        c.customer_id,
        c.customer_name,
        count(o.order_id) as countt
    from customers c
    join orders o on c.customer_id = o.customer_id
    join order_items oi on o.order_id = oi.order_id
    where month(o.order_date) = 6 and year(o.order_date) = 2024
    group by c.customer_id, c.customer_name
)

select
    tp.customer_id,
    tp.customer_name,
    tp.total_spent ,
    tp.total_spent/cnt.countt as avg_order_value
from
    tp join cnt on tp.customer_id = cnt.customer_id
order by tp.total_spent desc limit 5