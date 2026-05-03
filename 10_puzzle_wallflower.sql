-- Puzzle B (riddle)
-- "Who never pressed checkout? List customer names with zero orders."
\c view_lab

-- TODO: anti-join or NOT EXISTS
select c.name from customers c
where not exists(
    select 1 from orders o
    where o.cust_id=c.cust_id
);