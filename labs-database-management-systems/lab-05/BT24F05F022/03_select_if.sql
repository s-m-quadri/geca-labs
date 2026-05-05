-- Task 3: Conditional expression in a query (MySQL IF(expr, a, b))
-- Label each account as 'high' if balance >= 1000 else 'low'

USE proc_lab;

SELECT holder, balance, IF(balance >= 1000, 'high', 'low') AS tier FROM accounts;
