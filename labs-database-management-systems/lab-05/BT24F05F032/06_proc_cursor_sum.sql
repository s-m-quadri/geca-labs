-- Task 6: Function with cursor loop -- sum every row in accounts.balance
-- Returns total as DECIMAL(14,2)
-- Test: SELECT sum_balances();

                
USE proc_lab;
DROP FUNCTION IF EXISTS sum_balances;
CREATE FUNCTION sum_balances() RETURNS DECIMAL(14,2) LANGUAGE plpgsql AS $
DECLARE
  total DECIMAL(14,2) := 0;
  bal DECIMAL(10,2);
  cur CURSOR FOR SELECT balance FROM accounts;
BEGIN
  OPEN cur;
  LOOP
    FETCH cur INTO bal;
    EXIT WHEN NOT FOUND;
    total := total + bal;
  END LOOP;
  CLOSE cur;
  RETURN total;
END;
$;  
