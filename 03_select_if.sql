\c proc_lab

SELECT 
  holder, 
  balance,
  CASE 
    WHEN balance >= 1000 THEN 'high' 
    ELSE 'low' 
  END AS tier
FROM accounts;