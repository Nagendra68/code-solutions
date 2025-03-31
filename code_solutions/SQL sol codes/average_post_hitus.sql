SELECT
  user_id,
 EXTRACT(day from (max(post_date) - min(post_date))) as days_between
FROM posts
WHERE post_date BETWEEN '2021-01-01' AND '2021-12-31'
group by user_id
having count(post_id) > 1;