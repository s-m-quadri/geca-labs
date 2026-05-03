-- view_lab sanity check
USE view_lab

SELECT tablename FROM pg_tables WHERE schemaname = 'public';
SELECT COUNT(*) AS customers FROM customers;
SELECT COUNT(*) AS orders    FROM orders;
SELECT * FROM products;
