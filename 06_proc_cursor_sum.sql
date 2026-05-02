-- Task 6: Function with cursor loop -- sum every row in accounts.balance
-- Returns total as DECIMAL(14,2)
-- Test: SELECT sum_balances();
\c proc_lab



CREATE OR REPLACE FUNCTION sum_balances()
RETURNS DECIMAL(14,2) LANGUAGE plpgsql AS $$
DECLARE
  total DECIMAL(14,2);
BEGIN
  SELECT SUM(balance) INTO total FROM accounts;
  RETURN total;
END;
$$;
