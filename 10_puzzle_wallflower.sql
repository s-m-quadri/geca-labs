-- Puzzle B (riddle)
-- "Who never pressed checkout? List customer names with zero orders."
\c view_lab

-- TODO: anti-join or NOT EXISTS
select name from customers c
where not exists (
  select 1 from orders o where o.cust_id = c.cust_id
);
and name not in (
  select c.name from customers c
  join orders o on c.cust_id = o.cust_id
);
customers with zero orders:
select name from customers c
where c.cust_id not in (
  select cust_id from orders
);      