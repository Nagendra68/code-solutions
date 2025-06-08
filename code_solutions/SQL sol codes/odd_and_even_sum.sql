with cte1 as (
  SELECT 
    measurement_id,
    measurement_value,
    measurement_time::date AS Date,
    measurement_time::time AS Time
  FROM measurements
),
cte2 as(
  select
    measurement_id,
    measurement_value,
    date as measurement_day,
    row_number() over(partition by Date order by time)
  from cte1
)

SELECT 
  measurement_day,
  SUM(CASE WHEN row_number % 2 != 0 THEN measurement_value ELSE 0 END) AS odd_sum,
  SUM(CASE WHEN row_number % 2 = 0 THEN measurement_value ELSE 0 END) AS even_sum
FROM cte2
GROUP BY measurement_day;