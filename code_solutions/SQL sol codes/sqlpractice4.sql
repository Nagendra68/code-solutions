select
      first_name,
      last_name,
      'Doctor' as role
    from doctors
union all
select
      first_name,
      last_name,
      'Patient' AS role
    from patients;