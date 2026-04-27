-- proc_lab sanity check
SELECT 'accounts' AS t, COUNT(*) AS n FROM accounts
UNION ALL
SELECT 'payroll', COUNT(*) FROM payroll;
SELECT * FROM accounts;
SELECT * FROM payroll;