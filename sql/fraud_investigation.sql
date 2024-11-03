-- quick lookup for accounts sharing the same ip with previous chargebacks/disputes
select 
    ip_address,
    count(distinct user_id) as linked_user_count,
    count(*) as total_orders,
    sum(case when status in ('chargeback', 'refund_fraud') then 1 else 0 end) as flagged_count
from orders
where created_at >= now() - interval '60 days'
group by ip_address
having count(distinct user_id) > 1
order by flagged_count desc, linked_user_count desc;

-- velocity check: more than 4 successful orders in 30 mins
select 
    user_id,
    count(*) as tx_count,
    sum(amount) as total_eur,
    max(created_at) as latest_tx
from orders
where created_at >= now() - interval '30 minutes'
group by user_id
having count(*) >= 4;
