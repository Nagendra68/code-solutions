SELECT 
  admission_date,
  COUNT(patient_id) AS admission_count, 
  COUNT(patient_id) - LAG(COUNT(patient_id), 1, null) OVER (ORDER BY admission_date) AS admission_count_change
FROM admissions
GROUP BY admission_date;