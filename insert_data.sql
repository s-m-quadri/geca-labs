-- Lab 2: DML Commands - insert_data.sql
-- Task: Practice INSERT operations

USE college_db;

-- TODO: Insert one department (Computer Science, Engineering Block A, 500000.00)


-- TODO: Insert multiple departments at once:
--   - Electronics, Engineering Block B, 450000.00
--   - Mechanical, Workshop Building, 600000.00
--   - Civil, Civil Block, 400000.00
--   - Information Technology, IT Block, 480000.00


-- TODO: View all inserted departments


-- TODO: Insert at least 8 students with various details
-- Include first_name, last_name, email, phone, dob, department_id, gpa
-- Use department_ids 1-5 (reference the departments you created)


-- TODO: View all inserted students


-- TODO: Insert at least 8 courses with course_code, course_name, credits, department_id


-- TODO: View all inserted courses


-- TODO: Insert enrollments (at least 12) linking students to courses
-- Include student_id, course_id, grade (some NULL for active), status


-- TODO: View all inserted enrollments


-- TODO: Create a table called archived_students with same structure as students (use LIKE)


-- TODO: Insert data into archived_students using SELECT (copy students with gpa < 3.50)


-- TODO: View archived_students


-- TODO: Insert a new department with only department_name (test DEFAULT values)


-- TODO: Insert a new student and get the last inserted ID using LAST_INSERT_ID()


-- TODO: Show row counts for all tables using UNION


