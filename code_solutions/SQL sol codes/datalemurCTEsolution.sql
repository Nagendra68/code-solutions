with cte1 as 
  (
  select
    artist_id,
    artist_name,
    genre,
    concert_revenue,
    number_of_members,
    concert_revenue/number_of_members as revenue_per_member,
    rank() OVER( 
      PARTITION BY genre 
      order by concert_revenue/number_of_members desc
      ) as rank_over_genre
    FROM concerts
    )

select 
  artist_name,
  concert_revenue,
  genre,
  number_of_members,
  concert_revenue/number_of_members as revenue_per_member
from cte1
where rank_over_genre = 1
order by revenue_per_member desc

  