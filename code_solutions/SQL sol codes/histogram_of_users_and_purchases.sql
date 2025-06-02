
select transaction_date, user_id, count(user_id) as count
from user_transactions
group by user_id, transaction_date
having transaction_date in (select max(transaction_date) from user_transactions group by user_id)
order by count , transaction_date 