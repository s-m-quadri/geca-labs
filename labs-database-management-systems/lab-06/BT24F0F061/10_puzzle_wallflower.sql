-- Puzzle B (riddle)
-- "Who never pressed checkout? List customer names with zero orders."


-- TODO: anti-join or NOT EXISTS
select name from customers c
where not exists (
  select 1 from orders o where o.cust_id = c.cust_id
);

