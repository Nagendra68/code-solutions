select
  concat(first_name, ' ', last_name) as patient_name,
  round((height / 30.48), 1) height,
  round((weight * 2.205), 0) weight,
  birth_date,
  case
    when gender = 'M' then 'MALE'
    else 'FEMALE'
  end as gender_type
from patients