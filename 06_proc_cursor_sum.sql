-- Task 6: Function with cursor loop -- sum every row in accounts.balance
-- Returns total as DECIMAL(14,2)
-- Test: SELECT sum_balances();
\c proc_lab
CREATE OR REPLACE FUNCTION sum_balances()
RETURNS DECIMAL LANGUAGE plpgsql AS $$
DECLARE
  total DECIMAL := 0;
  b     DECIMAL;
  cur   CURSOR FOR SELECT balance FROM accounts;
BEGIN
  OPEN cur;
  LOOP
    FETCH cur INTO b;
    EXIT WHEN NOT FOUND;
    total := total + b;
  END LOOP;
  CLOSE cur;
  RETURN total;
END;
$$;
 
-- Test: should match SELECT SUM(balance) FROM accounts;
SELECT sum_balances() AS cursor_total;
SELECT SUM(balance) AS direct_total FROM accounts;