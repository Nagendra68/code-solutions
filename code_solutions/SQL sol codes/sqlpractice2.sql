select patient_id, diagnosis
FROM admissions
group by patient_id, diagnosis
having count(patient_id)>1;