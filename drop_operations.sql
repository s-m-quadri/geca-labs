-- Lab 1: DDL Commands - drop_operations.sql
-- Task: Practice DROP operations safely

USE college_db;

-- TODO: Create a temporary table 'temp_logs' with columns:
--   - log_id (INT, PRIMARY KEY)
--   - log_message (TEXT)
--   - log_date (TIMESTAMP, DEFAULT CURRENT_TIMESTAMP)


-- TODO: Insert a sample row into temp_logs


-- TODO: Drop the temp_logs table


-- TODO: Verify the table was dropped (use SHOW TABLES)


-- TODO: Drop a non-existent table safely (use DROP TABLE IF EXISTS)


-- TODO: Create a test_table with columns: id (INT PRIMARY KEY), name (VARCHAR(50))


-- TODO: Create an INDEX idx_test_name on test_table(name)


-- TODO: Show indexes on test_table


-- TODO: Drop the idx_test_name index


-- TODO: Verify index was dropped


-- TODO: Drop test_table


-- TODO: Create three temporary tables: temp1, temp2, temp3 (each with just id INT column)


-- TODO: Drop all three tables in a single statement


-- Note: To drop an entire database (very dangerous!):
-- DROP DATABASE database_name;
-- DO NOT execute this on college_db!
