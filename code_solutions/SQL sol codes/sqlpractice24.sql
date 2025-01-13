-- with cte1 as (
--   select
--     patient_id,
--     case
--       when patient_id % 2 = 0 then 'Yes'
--       else 'No'
--     end as insurance
--   from admissions
-- ),
-- aggregated_cte as (
--   select
--     insurance,
--     count(patient_id) as patient_count
--   from cte1
--   group by insurance
-- )
-- select 
--   insurance as has_insurance,
--   case
--     when insurance = 'No' then patient_count * 50
--     when insurance = 'Yes' then patient_count * 10
--   end as cost_after_insurance
-- from aggregated_cte;

-- without using cte
select
  case
    when patient_id % 2 = 0 then 'Yes'
    else 'No'
  end as has_insurance,
  count(*) * 
    case
      when patient_id % 2 = 0 then 10
      else 50
    end as cost_after_insurance
from admissions
group by has_insurance;


-- my solution
-- with cte1 as (select
--   patient_id,
--   case
--     when patient_id % 2 = 0 then 'Yes'
--     else 'No'
--   End as insurance
-- from admissions)

-- select insurance as has_insurance, count(patient_id)*50 as cost_after_insurance
-- from cte1
-- where insurance = 'No'
-- union all
-- select insurance as has_insurance, count(patient_id)*10 as cost_after_insurance
-- from cte1
-- where insurance = 'Yes'