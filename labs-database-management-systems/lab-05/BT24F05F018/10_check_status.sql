-- proc_lab sanity check
\c proc_lab



-- Check row counts in both tables
SELECT 'accounts' AS t, COUNT(*) AS n FROM accounts
UNION ALL
SELECT 'payroll', COUNT(*) FROM payroll;

-- View full tables
SELECT * FROM accounts;
SELECT * FROM payroll;