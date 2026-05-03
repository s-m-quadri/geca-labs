-- Task 3: Conditional expression in a query (PostgreSQL uses CASE WHEN, not IF())
-- Label each account as 'high' if balance >= 1000 else 'low'
\c proc_lab

-- TODO: SELECT holder, balance,
--              CASE WHEN balance >= 1000 THEN 'high' ELSE 'low' END AS tier
--       FROM accounts;

-- Label each employee as 'bonus' if bonus_eligible is true else 'no bonus'
    SELECT name, bonus_eligible,
           CASE WHEN bonus_eligible = true THEN 'bonus' ELSE 'no bonus' END AS eligibility
    FROM employees;





                        
