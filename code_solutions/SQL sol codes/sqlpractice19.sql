with cte1 as(
	select count(patient_id) as cnt
  from admissions
  group by admission_date
)

select max(cnt) max_visits, MIN(cnt) min_visits,
	round(avg(cnt), 2)  average_visits
from cte1