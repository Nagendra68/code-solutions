with cte1 as (
    select movie_id,budget,revenue, unit, currency,revenue - budget as profit
    from financials
)

select * , round((profit/budget)*100, 1) as profit_pct from cte1