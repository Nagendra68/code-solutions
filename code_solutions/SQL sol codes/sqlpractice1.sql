SELECT first_name, last_name, allergies
from patients
where allergies in ('Penicillin','Morphine')
ORDER BY allergies, first_name, last_name;