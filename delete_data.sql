-- Lab 2: DML Commands - delete_data.sql
-- Task: Practice DELETE operations safely

USE college_db;

-- TODO: View archived_students before deletion


-- TODO: Delete a single record from archived_students (choose any student_id)


-- TODO: Verify the deletion


-- TODO: Delete enrollments with status = 'Dropped'


-- TODO: Delete enrollments for courses with less than 3 credits (use subquery)


-- TODO: Delete enrollments using JOIN - remove enrollments for students with GPA < 3.00


-- TODO: Delete specific number of records (use ORDER BY and LIMIT)
-- Delete 2 students with lowest GPA from archived_students


-- TODO: View remaining data in archived_students


-- TODO: View remaining enrollments


-- TODO: Demonstrate transaction with DELETE
-- Start transaction, delete some data, view it, then commit


-- Remember: 
-- - TRUNCATE removes all rows but is faster
-- - TRUNCATE resets AUTO_INCREMENT
-- - DELETE with WHERE removes specific rows
-- - DELETE without WHERE removes all rows (dangerous!)
-- - Always use transactions for important deletions
