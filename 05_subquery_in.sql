-- Task 5: IN subquery -- customers who ordered product id 20 (PenSet)
\c view_lab

-- TODO: SELECT name FROM customers
--       WHERE cust_id IN (
--         SELECT cust_id FROM orders o
--         JOIN order_lines ol ON o.order_id = ol.order_id
--         WHERE ol.prod_id = 20
--       );
select name from customers
where cust_id in (
  select cust_id from orders o
  join order_lines ol on o.order_id = ol.order_id
  where ol.prod_id = 20
);