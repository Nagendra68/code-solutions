SELECT
	employee_id, 
    order_id, 
    customer_id, 
    required_date, 
    shipped_date 
from
	orders
where shipped_date > required_date;