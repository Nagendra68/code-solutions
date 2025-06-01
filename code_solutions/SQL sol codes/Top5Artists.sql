WITH cte1 AS (
  SELECT a.artist_id, a.artist_name
  FROM artists a
  JOIN songs s ON a.artist_id = s.artist_id
  JOIN global_song_rank g ON s.song_id = g.song_id
  WHERE g.rank <= 10
),

cte2 AS (
  SELECT artist_id, artist_name, COUNT(*) AS cnt
  FROM cte1
  GROUP BY artist_id, artist_name
)

SELECT artist_name, artist_rank
FROM (
  SELECT artist_name,
         DENSE_RANK() OVER (ORDER BY cnt DESC) AS artist_rank
  FROM cte2
) ranked
WHERE artist_rank <= 5;
