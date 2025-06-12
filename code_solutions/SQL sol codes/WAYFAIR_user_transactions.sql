with cte as(
  SELECT EXTRACT(year from transaction_date) as year,
  product_id,
  sum(spend) as total_spend
  FROM user_transactions
  group by year, product_id
  )
select year,
  product_id,
  total_spend as curr_year_spend,
  lag(total_spend) over(PARTITION by product_id order by product_id, year) as prev_year_spend,
  round(((total_spend- lag(total_spend) over(PARTITION by product_id order by product_id, year))/lag(total_spend) over(PARTITION by product_id order by product_id, year))*100, 2) as yoy
from cte
order by product_id, year asc