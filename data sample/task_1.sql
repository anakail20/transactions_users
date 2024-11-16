-- Create a CTE to gather transactions made in the last 7 days - excluding current transactions
with trx_last_7days as (
    select
        t1.transaction_id,
        t1.user_id,
        t1.date,
        t2.transaction_id as transactions_last_7days
    from transactions as  t1
    left join transactions as t2
        on t1.user_id = t2.user_id
        and t2.date >= date_add( t1.date, interval -7 day)
        and t2.date < t1.date
)
-- Aggregate results to count transactions in the last 7 days for each transaction
select 
    transaction_id,
    user_id,
    date,
    count(transactions_last_7days) as no_txn_last_7days
from 
    trx_last_7days
group by 1,2,3
order by 3
