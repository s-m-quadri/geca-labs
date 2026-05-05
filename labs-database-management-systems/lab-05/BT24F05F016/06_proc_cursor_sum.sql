-- Task 6: Function with cursor loop -- sum every row in accounts.balance
-- Returns total as DECIMAL(14,2)
-- Test: SELECT sum_balances();
\c proc_lab

CREATE OR REPLACE FUNCTION sum_balances()
RETURNS DECIMAL(14,2) LANGUAGE plpgsql AS $$
DECLARE
  total DECIMAL(14,2) := 0;
  b     DECIMAL(12,2);
  cur   CURSOR FOR SELECT balance FROM accounts;
BEGIN
  OPEN cur;
  LOOP
    FETCH cur INTO b;
    EXIT WHEN NOT FOUND;
      -- Hint: accumulate each fetched balance into `total` (e.g. total := total + b)
  END LOOP;
  CLOSE cur;
  RETURN total;
END;
$$;

  SELECT sum_balances();
