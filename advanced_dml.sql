-- Lab 2: DML Commands - advanced_dml.sql
-- Task: Practice advanced DML operations

USE college_db;

-- TODO: Use window function ROW_NUMBER() to rank students by GPA


-- TODO: Use RANK() and DENSE_RANK() to rank students


-- TODO: Use window function with PARTITION BY to rank students within each department


-- TODO: Calculate running total of department budgets


-- TODO: Create CTE (Common Table Expression) for high performers (gpa > 3.70)
-- Then select from it with JOIN to departments


-- TODO: Create recursive CTE for organizational hierarchy
-- First create employees table with emp_id, emp_name, manager_id
-- Insert hierarchical data (CEO, VPs, Managers, etc.)
-- Write recursive query to show hierarchy with levels


-- TODO: Create a pivot-like query using CASE statements
-- Show count of enrollments by status for each department


-- TODO: Create department_summary table


-- TODO: INSERT INTO department_summary using SELECT with aggregation
-- Calculate total_students, avg_gpa, max_gpa per department


-- TODO: Use INSERT ON DUPLICATE KEY UPDATE (upsert) to update or insert


-- TODO: Use REPLACE to delete and insert


-- TODO: Demonstrate multi-table DELETE
-- Delete students and their enrollments where gpa < 2.00


-- TODO: Demonstrate multi-table UPDATE
-- Update students' GPA based on calculated grades from enrollments


-- TODO: Create student_metadata table with JSON column


-- TODO: Insert JSON data for students (hobbies, languages, etc.)


-- TODO: Query JSON data using JSON_EXTRACT


-- TODO: Update JSON data using JSON_SET


-- TODO: Cleanup: Drop temporary tables

