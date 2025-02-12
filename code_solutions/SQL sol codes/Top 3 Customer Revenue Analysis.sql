select customer_id, sum(amount) as total_revenue
from bookings
group by customer_id
order by total_revenue desc limit 3