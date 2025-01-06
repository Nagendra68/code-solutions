SELECT
  patient_id,
  attending_doctor_id,
  diagnosis
FROM admissions
WHERE
  (
    patient_id % 2 != 0
    AND attending_doctor_id IN (1, 5, 19)
  )
  OR (
    cast(attending_doctor_id AS TEXT) like '%2%'
    AND LENGTH(CAST(patient_id AS TEXT)) = 3
  );

-- SELECT
--   patient_id,
--   attending_doctor_id,
--   diagnosis
-- FROM admissions
-- WHERE
--   (
--     attending_doctor_id IN (1, 5, 19)
--     AND patient_id % 2 != 0
--   )
--   OR (
--     attending_doctor_id LIKE '%2%'
--     AND len(patient_id) = 3
--   )