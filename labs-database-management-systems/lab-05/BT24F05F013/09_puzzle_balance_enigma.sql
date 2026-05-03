USE proc_lab;

SELECT
  (SELECT MIN(balance) FROM accounts) *
  (SELECT MAX(balance) FROM accounts) AS secret_code;