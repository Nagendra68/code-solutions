with RankedTeams as (

    select team_name,
    row_number() over(order by team_name) as row_num
    from teams
),
MatchSchedule as (
    select 
        row_number() over (order by t1.row_num, t2.row_num) as match_id,
        t1.team_name as home_team,
        t2.team_name as away_team
    from
        RankedTeams t1
        join RankedTeams t2 on t1.row_num < t2.row_num
    
    union all

    select 
        row_number() over (order by t1.row_num, t2.row_num) + 28 as match_id,
        t2.team_name as home_team,
        t1.team_name as away_team
    from
        RankedTeams t1
        join RankedTeams t2 on t1.row_num < t2.row_num

)

select * from MatchSchedule;