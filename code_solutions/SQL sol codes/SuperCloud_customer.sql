SELECT c.customer_id
FROM customer_contracts c
join products p on c.product_id = p.product_id
group by c.customer_id
having count(DISTINCT p.product_category) = (
  select count(distinct product_category) 
  from products
  )
