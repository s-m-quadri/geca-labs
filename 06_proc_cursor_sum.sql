-- Task 6: Function with cursor loop -- sum every row in accounts.balance
-- Returns total as DECIMAL(14,2)
-- Test: SELECT sum_balances();
\c proc_lab

CREATE OR REPLACE FUNCTION sum_balances()
RETURNS DECIMAL(14,2) AS $$
DECLARE
  v_bal DECIMAL(12,2);
  v_total DECIMAL(14,2) := 0;
  cur CURSOR FOR SELECT balance FROM accounts;
BEGIN
  OPEN cur;
  LOOP
    FETCH cur INTO v_bal;
    EXIT WHEN NOT FOUND;
    -- Add current row balance to running total here.
    -- TODO: v_total := ...
  END LOOP;
  CLOSE cur;

  RETURN v_total;
END;
$$ LANGUAGE plpgsql;

-- TODO: Uncomment after completing the TODO in the loop.
-- SELECT sum_balances();