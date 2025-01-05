select day(admission_date) day_number, count(admission_date) number_of_admissions
from admissions
group by day_number
order by number_of_admissions desc;