-- Lab 2: DML Commands - select_queries.sql
-- Task: Practice SELECT queries with various clauses

USE college_db;

-- TODO: Select all columns from students table


-- TODO: Select only first_name, last_name, and email from students


-- TODO: Select with column aliases (first_name AS 'First Name', etc.)


-- TODO: Select students with gpa > 3.70 (use WHERE)


-- TODO: Select students from department_id 1 AND gpa > 3.60


-- TODO: Select students from department_id 1 OR department_id 2


-- TODO: Select students where department_id IN (1, 2, 5)


-- TODO: Select students with gpa BETWEEN 3.50 AND 3.80


-- TODO: Select students whose first_name starts with 'A' (use LIKE)


-- TODO: Select students whose email ends with '@college.edu'


-- TODO: Select enrollments where grade IS NULL


-- TODO: Select enrollments where grade IS NOT NULL


-- TODO: Select students ordered by gpa in descending order


-- TODO: Select students ordered by last_name ASC, then first_name ASC


-- TODO: Select top 3 students by gpa (use LIMIT)


-- TODO: Select students with pagination (first 5: LIMIT 5 OFFSET 0)


-- TODO: Select DISTINCT department_ids from students


-- TODO: Count total number of students


-- TODO: Calculate average GPA of all students


-- TODO: Find highest GPA


-- TODO: Find lowest GPA


-- TODO: Calculate total budget of all departments


-- TODO: Count students in each department (use GROUP BY)


-- TODO: Calculate average GPA per department (use GROUP BY)


-- TODO: Show departments with more than 1 student (use HAVING)


-- TODO: INNER JOIN students and departments to show student names with department names


-- TODO: LEFT JOIN students and departments


-- TODO: Join students, enrollments, and courses to show student names with their courses and grades


-- TODO: Use subquery: Select students with gpa above average


-- TODO: Use subquery in FROM clause to show department stats


-- TODO: Use EXISTS to find departments that have students


-- TODO: Use UNION to combine students from department 1 and department 2


-- TODO: Use CASE statement to categorize students by GPA:
--   - >= 3.80: 'Excellent'
--   - >= 3.50: 'Good'
--   - >= 3.00: 'Average'
--   - else: 'Below Average'


-- TODO: Create computed columns:
--   - Full name (CONCAT first and last name)
--   - Age from dob
--   - Days enrolled


-- TODO: Use string functions: UPPER, LOWER, LENGTH, SUBSTRING

