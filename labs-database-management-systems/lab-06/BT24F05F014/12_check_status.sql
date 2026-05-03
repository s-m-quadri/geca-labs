-- view_lab sanity check
USE view_lab;

SHOW TABLES;
SELECT table_name 
FROM information_schema.tables
WHERE table_schema = 'view_lab';
SELECT COUNT(*) AS customers FROM customers;
SELECT COUNT(*) AS orders    FROM orders;
SELECT * FROM products;