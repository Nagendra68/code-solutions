SELECT CONCAT(last_name, ',', first_name) AS new_name_format
FROM patients
ORDER BY first_name DESC;
