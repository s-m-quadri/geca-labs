-- Task 4: Scalar subquery -- products priced above the average product price
\c view_lab

-- TODO: SELECT name, price FROM products
--       WHERE price > ( ... scalar subquery for AVG(price) ... );
select
    prod_name,
    unit_price
from
    products
where
    unit_price > (select avg(unit_price) from products);    
    