-- Puzzle B (riddle)
-- "Who never pressed checkout? List customer names with **zero** orders."

USE view_lab;

-- TODO: anti-join or NOT EXISTS
SELECT name
FROM view_lab.customers c
WHERE NOT EXISTS (
    SELECT 1
    FROM view_lab.orders o
    WHERE o.cust_id = c.cust_id
);