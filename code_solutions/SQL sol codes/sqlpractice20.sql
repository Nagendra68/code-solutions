-- with cte1 as (
--   SELECT
--   	patient_id,
--     weight,
--     FLOOR(weight / 10)*10  AS weight_group
-- FROM 
--     patients
-- ORDER BY 
--     weight)
    
-- select count(patient_id) patients_in_group, weight_group
-- from cte1
-- group by weight_group
-- order by weight_group desc

'''more efficient approach with cte is behind , it is more efficient because 
The query processes the data in one step, grouping and counting in the same operation.'''

SELECT 
    FLOOR(weight / 10) * 10 AS weight_group,
    COUNT(patient_id) AS patients_in_group
FROM 
    patients
GROUP BY 
    FLOOR(weight / 10) * 10
ORDER BY 
    weight_group DESC;

