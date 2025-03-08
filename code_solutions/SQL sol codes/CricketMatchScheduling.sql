WITH RankedTeams as (
    select
        team_name,
        row_number() over(order by team_name) as rn
    from 
        teams
),
MatchSchedule as(
    SELECT
        ROW_NUMBER() OVER (ORDER BY t1.rn, t2.rn) AS match_id,
        t1.team_name AS home_team,
        t2.team_name AS away_team
    FROM RankedTeams t1 
    JOIN RankedTeams t2 ON t1.rn < t2.rn

    union all

        SELECT
        ROW_NUMBER() OVER (ORDER BY t1.rn, t2.rn) + 28 AS match_id,
        t2.team_name AS home_team,
        t1.team_name AS away_team
    FROM RankedTeams t1 
    JOIN RankedTeams t2 ON t1.rn < t2.rn
)   
select * from MatchSchedule