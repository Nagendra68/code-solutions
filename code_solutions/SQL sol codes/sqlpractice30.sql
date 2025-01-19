select 
	a.attending_doctor_id as doctor_id, concat(d.first_name, ' ', d.last_name) as doctor_name,
	d.specialty ,
    Year(admission_date) as selected_year, count(a.patient_id) as total_admissions
from admissions a 
join doctors d
on a.attending_doctor_id = d.doctor_id
group by doctor_id, selected_year