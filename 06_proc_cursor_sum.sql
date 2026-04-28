-- Task 6: Cursor + loop — sum every row in accounts.balance into OUT total
-- Run: ./run_source.sh proc_lab 06_proc_cursor_sum.sql
-- Test: CALL sum_balances(@t); SELECT @t;

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