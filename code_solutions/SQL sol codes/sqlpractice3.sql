select city , count(patient_id) num_patients
from patients
group by city
order by num_patients desc, city asc;