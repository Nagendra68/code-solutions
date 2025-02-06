with next_purchases as (
    select
    customer_id,
    purchase_id,
    purchase_date, 
    lead(purchase_date) over(partition by customer_id order by purchase_date) as next_purchase_date
from purchases )


select
    *,
    DATEDIFF(next_purchase_date, purchase_date) as days_until_next_purchase
from 
next_purchases
where next_purchase_date is not null;