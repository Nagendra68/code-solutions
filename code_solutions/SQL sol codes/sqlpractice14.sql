select pr.province_name, count(p.patient_id) patient_count
from patients p
join province_names pr
on p.province_id = pr.province_id
group by pr.province_id
order by patient_count desc;