select province_id, sum(height) as sum_height
from patients
group by province_id
having sum_height >= 7000;