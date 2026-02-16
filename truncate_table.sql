-- Lab 1: DDL Commands - truncate_table.sql
-- Task: Understand TRUNCATE vs DELETE

USE college_db;

-- TODO: Create a table 'activity_logs' with columns:
--   - log_id (INT PRIMARY KEY AUTO_INCREMENT)
--   - user_id (INT)
--   - activity (VARCHAR(255))
--   - log_time (TIMESTAMP DEFAULT CURRENT_TIMESTAMP)


-- TODO: Insert 4 sample rows with different user_ids and activities


-- TODO: View all data in activity_logs


-- TODO: Count total logs


-- TODO: TRUNCATE the activity_logs table


-- TODO: Verify data is gone but structure remains


-- TODO: Show table structure to confirm it still exists


-- TODO: Insert a new row and observe that AUTO_INCREMENT resets to 1


-- TODO: View the new row to confirm ID started from 1


-- TODO: Drop the activity_logs table (cleanup)


-- Key Differences to Remember:
-- - TRUNCATE removes all rows quickly
-- - TRUNCATE resets AUTO_INCREMENT counter
-- - TRUNCATE cannot use WHERE clause
-- - TRUNCATE cannot be rolled back
-- - DELETE can use WHERE to remove specific rows
-- - DELETE does not reset AUTO_INCREMENT
-- - DELETE can be rolled back in a transaction
