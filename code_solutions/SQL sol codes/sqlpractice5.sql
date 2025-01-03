select allergies, count(patient_id) as total_diagnosis
from patients
where allergies is not null
group by allergies
order by total_diagnosis desc;