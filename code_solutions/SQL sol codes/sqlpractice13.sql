SELECT doctor_id, concat(d.first_name,' ',d.last_name) as full_name,
		min(a.admission_date) AS first_admission_date,
        max(admission_date) AS last_admission_date
from doctors d
join admissions a
on a.attending_doctor_id = d.doctor_id
group by d.doctor_id