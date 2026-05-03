-- Task 7: Correlated subquery -- customers who spent more than 50 total
-- (sum of qty * price across all their order lines)
\c view_lab

-- TODO: correlated pattern on customers + orders + order_lines + products
select c.name from customers c
where (
  select sum(ol.qty * p.price) from orders o
  join order_lines ol on o.order_id = ol.order_id
  join products p on ol.prod_id = p.prod_id
  where o.cust_id = c.cust_id
) > 50;