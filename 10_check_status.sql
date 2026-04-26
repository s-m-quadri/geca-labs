-- proc_lab sanity check
\c proc_lab

SELECT 'accounts' AS t, COUNT(*) AS n FROM accounts
UNION ALL
SELECT 'payroll', COUNT(*) FROM payroll;
SELECT * FROM accounts;
SELECT * FROM payroll;
CREATE OR REPLACE PROCEDURE process_payroll()
LANGUAGE plpgsql
AS $$
DECLARE
    cur CURSOR FOR SELECT emp_id, name, salary, bonus_eligible FROM payroll;
    rec RECORD;
    pct NUMERIC;
BEGIN
    OPEN cur;
    LOOP
        FETCH cur INTO rec;
        EXIT WHEN NOT FOUND;
        -- Trace one iteration on paper: which row is fetched first, what values are in rec variables?
        -- For arithmetic, remember order of operations; pct relates to percent increase.
    END LOOP;
    CLOSE cur;
END;
$$;