-- Task 3: Conditional expression in a query (MySQL IF(expr, a, b))
-- Label each account as 'high' if balance >= 1000 else 'low'

-- TODO: SELECT holder, balance,
--              CASE WHEN balance >= 1000 THEN 'high' ELSE 'low' END AS tier
--       FROM accounts;
select holder, balance,
       case when balance >= 1000 then 'high' else 'low' end as tier
from accounts;  
        
