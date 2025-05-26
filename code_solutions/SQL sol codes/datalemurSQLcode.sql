SELECT order_id as corrected_order_id,
      case when order_id = (select count(order_id) from orders) 
      then item
      when order_id%2!=0
      then lead(item) over(order by order_id)
      else lag(item) over(order by order_id)
      end as item
from orders