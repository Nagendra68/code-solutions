SELECT first_name, last_name, COUNT(*) as num_of_duplicates
FROM patients
GROUP BY first_name, last_name
HAVING COUNT(*) > 1;