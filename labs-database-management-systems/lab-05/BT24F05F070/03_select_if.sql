-- Task 3: Conditional expression in a query (PostgreSQL uses CASE WHEN, not IF())
-- Label each account as 'high' if balance >= 1000 else 'low'
--\c proc_lab

-- TODO: SELECT holder, balance,
--              CASE WHEN balance >= 1000 THEN 'high' ELSE 'low' END AS tier
--       FROM accounts;

SELECT holder, balance,
             CASE WHEN balance >= 1000 THEN 'high' ELSE 'low' END AS tier
      FROM accounts;
