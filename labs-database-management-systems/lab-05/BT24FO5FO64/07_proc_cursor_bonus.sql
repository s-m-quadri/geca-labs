-- Task 7: Procedure that UPDATEs rows (bonus on payroll)
-- For each row with bonus_eligible = TRUE, add 100 to salary using a cursor loop.
-- Reset with 01_setup.sql if you need fresh numbers.
\c proc_lab

DROP FUNCTION IF EXISTS apply_bonus();
CREATE FUNCTION apply_bonus()
RETURNS VOID AS $$
DECLARE
    rec RECORD;
BEGIN
    FOR rec IN SELECT id, salary FROM payroll WHERE bonus_eligible = TRUE
    LOOP
        UPDATE payroll SET salary = salary + 100 WHERE id = rec.id;
    END LOOP;
END;
$$ LANGUAGE plpgsql;  