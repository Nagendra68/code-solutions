WITH c1 AS (
  SELECT
    artist_name
    , concert_revenue
    , genre
    , number_of_members
    , concert_revenue / number_of_members AS revenue_per_member
    FROM
      concerts
)

SELECT
  *
FROM
  c1
WHERE revenue_per_member = (
  SELECT MAX(revenue_per_member)
  FROM c1 AS c2
  WHERE c1.genre = c2.genre
  )
ORDER BY
  revenue_per_member DESC, genre ASC