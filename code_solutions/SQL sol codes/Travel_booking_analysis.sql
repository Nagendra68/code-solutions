select booking_type, sum(amount) as total_revenue
from bookings
group by booking_type
order by total_revenue desc