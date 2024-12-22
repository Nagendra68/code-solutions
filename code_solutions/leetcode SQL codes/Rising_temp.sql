-- SELECT id
-- FROM (
--     SELECT id, recordDate, temperature, 
--            LAG(recordDate) OVER (ORDER BY recordDate) AS prev_date,
--            LAG(temperature) OVER (ORDER BY recordDate) AS prev_temp
--     FROM Weather
-- ) AS temp_diff
-- WHERE DATEDIFF(recordDate, prev_date) = 1
--   AND temperature > prev_temp;

select w1.id 
from weather w1, weather w2
where datediff(w1.recordDate, w2.recordDate) = 1 
and w1.temperature > w2.temperature;