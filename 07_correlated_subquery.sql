-- Task 7: Correlated subquery -- customers who spent more than 50 total
-- (sum of qty * price across all their order lines)
\c view_lab

-- TODO: correlated pattern on customers + orders + order_lines + products
constraint: sum of line totals for each customer > 50
select
    cust_name
from
    customers c
where
    (select
        sum(ol.qty * p.unit_price)
    from
        orders o
    join    
        order_lines ol on o.order_id = ol.order_id
    join
        products p on ol.prod_id = p.prod_id
    where
        o.cust_id = c.cust_id
    ) > 50;     
        