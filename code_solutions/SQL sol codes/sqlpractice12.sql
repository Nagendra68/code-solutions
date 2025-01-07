select d.first_name, d.last_name,count(a.patient_id) as admission_total
from admissions a
join doctors d
on a.attending_doctor_id = d.doctor_id
group by d.doctor_id;