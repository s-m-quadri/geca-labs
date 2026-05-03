-- Task 3: Conditional expression in a query (PostgreSQL uses CASE WHEN, not IF())
-- Label each account as 'high' if balance >= 1000 else 'low'
\c proc_lab

USE proc_lab;

SELECT holder, balance, IF(balance >= 1000, 'high', 'low') AS tier FROM accounts;
