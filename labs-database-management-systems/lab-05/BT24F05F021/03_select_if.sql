-- Task 3: Conditional expression in a query (PostgreSQL uses CASE WHEN, not IF())
-- Label each account as 'high' if balance >= 1000 else 'low'
\c proc_lab

-- TODO: SELECT holder, balance,
--              CASE WHEN balance >= 1000 THEN 'high' ELSE 'low' END AS tier
--       FROM accounts;
-- Connect to the database
\c proc_lab

-- Categorize accounts based on their current balance
SELECT 
    holder, 
    balance,
    CASE 
        WHEN balance >= 1000 THEN 'high' 
        ELSE 'low' 
    END AS tier
FROM accounts;