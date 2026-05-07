-- Task 6: Function with cursor loop -- sum every row in accounts.balance
-- Returns total as DECIMAL(14,2)
-- Test: SELECT sum_balances();
\c proc_lab
DROP FUNCTION IF EXISTS sum_balances();
CREATE FUNCTION sum_balances()    