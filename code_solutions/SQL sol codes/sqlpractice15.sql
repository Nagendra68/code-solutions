SELECT
  CONCAT(patients.first_name,' ',patients.last_name) as patient_name,
  diagnosis,
  CONCAT(doctors.first_name,' ',doctors.last_name) as doctor_name
FROM patients
  JOIN admissions ON admissions.patient_id = patients.patient_id
  JOIN doctors ON doctors.doctor_id = admissions.attending_doctor_id;




-- select
--   concat(p.first_name, ' ', p.last_name) patient_name,
--   a.diagnosis,
--   concat(d.first_name, ' ', d.last_name) doctor_name
-- from patients p
--   join admissions a on p.patient_id = a.patient_id
--   join doctors d on a.attending_doctor_id = d.doctor_id
-- group by
--   a.patient_id,
--   a.admission_date,
--   a.discharge_date,
--   a.diagnosis,
--   a.attending_doctor_id;