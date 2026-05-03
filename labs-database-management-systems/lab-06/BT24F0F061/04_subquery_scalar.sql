-- Task 4: Scalar subquery -- products priced above the average product price


-- TODO: SELECT name, price FROM products
--       WHERE price > ( ... scalar subquery for AVG(price) ... );
select name, price from products
where price > (select avg(price) from products);

