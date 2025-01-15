-- SELECT 
--   CONCAT(
--     ROUND(
--       (SELECT COUNT(*) FROM patients WHERE gender = 'M') * 100.0 / 
--       (SELECT COUNT(*) FROM patients), 
--     2), 
--     '%'
--   ) AS cnt_male_percentage;

WITH male_count AS (
  SELECT COUNT(*) AS cnt_m 
  FROM patients 
  WHERE gender = 'M'
), 
total_count AS (
  SELECT COUNT(*) AS cnt_t 
  FROM patients
)
SELECT CONCAT(ROUND(male_count.cnt_m * 100.0 / total_count.cnt_t, 2), '%') AS cnt_male_percentage
FROM male_count, total_count;
