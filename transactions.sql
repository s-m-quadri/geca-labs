-- Lab 2: DML Commands - transactions.sql
-- Task: Learn transaction management (ACID properties)

USE college_db;

-- TODO: Create bank_accounts table with:
--   - account_id (INT PRIMARY KEY)
--   - account_holder (VARCHAR(100))
--   - balance (DECIMAL(10, 2))


-- TODO: Insert two accounts (Alice with 1000.00, Bob with 500.00)


-- TODO: View accounts before transaction


-- TODO: Start a transaction


-- TODO: Debit 200 from Alice (account_id 1)


-- TODO: Credit 200 to Bob (account_id 2)


-- TODO: View changes (not yet committed)


-- TODO: Commit the transaction


-- TODO: Verify final state


-- TODO: Demonstrate ROLLBACK:
-- Start transaction, update balances, check state, then rollback


-- TODO: Verify data is back to previous state


-- TODO: Student enrollment transaction:
-- Start transaction
-- Check current enrollments for a course
-- Insert new enrollment
-- Check again
-- Commit if successful


-- TODO: Transaction with SAVEPOINT:
-- Start transaction
-- Insert a student
-- Create savepoint after_student_insert
-- Insert enrollment for that student
-- Commit everything


-- TODO: Show current isolation level


-- TODO: Set isolation level to READ COMMITTED


-- TODO: Demonstrate locking: Use SELECT ... FOR UPDATE


-- TODO: Show autocommit status


-- TODO: Disable autocommit, do some work, then commit manually


-- TODO: Re-enable autocommit


-- TODO: Drop bank_accounts table (cleanup)


-- Key Transaction Concepts:
-- - ACID: Atomicity, Consistency, Isolation, Durability
-- - START TRANSACTION begins a transaction
-- - COMMIT saves changes permanently
-- - ROLLBACK undoes changes
-- - SAVEPOINT creates a checkpoint within transaction
-- - Transactions ensure data integrity
