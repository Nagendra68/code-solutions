SELECT u.city, count(t.order_id) total_orders
FROM trades t join users u on t.user_id = u.user_id
where t.status like '%Completed%'
group by u.city
order by total_orders DESC
limit 3;