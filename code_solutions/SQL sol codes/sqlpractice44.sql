select
	e.first_name, e.last_name,
    count(o.order_id) num_orders,
    CASE 
    WHEN o.shipped_date <= o.required_date THEN 'On Time'
    WHEN o.shipped_date > o.required_date THEN 'Late'
    when o.shipped_date is null then 'Not Shipped'
    END AS Shipped

from employees e
join orders o
on e.employee_id = o.employee_id
group by e.first_name, e.last_name,shipped
order by e.last_name, e.first_name,num_orders desc;