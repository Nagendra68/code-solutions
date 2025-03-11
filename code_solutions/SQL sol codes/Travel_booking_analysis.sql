select booking_type, sum(amount) as total_revenue
from bookings
group by booking_type