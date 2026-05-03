DELIMITER $$

CREATE PROCEDURE pay_bill(
  IN b_id INT
)
BEGIN
  UPDATE bills
  SET status = 'Paid'
  WHERE bill_id = b_id;
END $$

DELIMITER ;