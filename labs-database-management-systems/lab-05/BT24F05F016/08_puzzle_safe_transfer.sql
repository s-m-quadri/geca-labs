-- Puzzle A (riddle)
-- "Two vaults move coins only if the donor can afford it; otherwise the bank stays silent."
-- Implement safe_transfer(from_id, to_id, amount) on table accounts.
-- Rules: if balance < amount, do not change any row; else subtract from donor, add to receiver.
-- Test: SELECT * FROM accounts; CALL safe_transfer(1,2,100); SELECT * FROM accounts;
\c proc_lab

CREATE OR REPLACE PROCEDURE safe_transfer(
  from_id INT,
  to_id   INT,
  amount  DECIMAL(12,2)
) LANGUAGE plpgsql AS $$
DECLARE
  donor_bal DECIMAL(12,2);
BEGIN
  -- Hint: fetch the donor's balance into `donor_bal` (SELECT ... INTO donor_bal).
  -- Hint: if `donor_bal` is less than `amount`, exit the procedure without changing rows.
  -- Hint: otherwise perform two updates inside a transaction: subtract from donor, add to receiver.
END;
$$;
