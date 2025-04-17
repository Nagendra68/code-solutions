SELECT order_id,
  CASE
    when mod(order_id, 2) = 1 and LEAD(order_id) over(order by order_id) is not NULL
      THEN LEAD(item) over(order by order_id)
    WHEN mod(order_id, 2) = 0 
      THEN LAG(item) over(order by order_id)
    ELSE
      item
    end as corrected_item
FROM orders;