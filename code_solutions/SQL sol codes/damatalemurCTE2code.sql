WITH cte1 AS (
  SELECT 
    c.customer_id, 
    COUNT(DISTINCT p.product_category) AS cnt
  FROM customer_contracts c
  JOIN products p
    ON c.product_id = p.product_id
  GROUP BY c.customer_id
)

SELECT customer_id
FROM cte1
WHERE cnt = (
  SELECT COUNT(DISTINCT product_category)
  FROM products
)
