SELECT province_name
FROM (
    SELECT 
        pn.province_name, 
        COUNT(CASE WHEN p.gender = 'M' THEN 1 END) AS male_cnt,
        COUNT(CASE WHEN p.gender = 'F' THEN 1 END) AS female_cnt
    FROM patients p
    JOIN province_names pn
    ON p.province_id = pn.province_id
    GROUP BY pn.province_name
) AS gender_counts
WHERE male_cnt > female_cnt;