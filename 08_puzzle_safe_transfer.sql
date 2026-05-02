\c proc_lab

CREATE OR REPLACE PROCEDURE safe_transfer(
  from_id INT,
  to_id   INT,
  amount  DECIMAL(12,2)
) LANGUAGE plpgsql AS $$
DECLARE
  donor_bal DECIMAL(12,2);
BEGIN
  -- Get donor balance
  SELECT balance INTO donor_bal 
  FROM accounts 
  WHERE id = from_id;

  -- If insufficient funds, do nothing
  IF donor_bal < amount THEN
    RETURN;
  END IF;

  -- Deduct from donor
  UPDATE accounts
  SET balance = balance - amount
  WHERE id = from_id;

  -- Add to receiver
  UPDATE accounts
  SET balance = balance + amount
  WHERE id = to_id;

END;
$$;