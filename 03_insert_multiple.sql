-- Task 3: Insert Multiple Students
-- Add 3 more students in one command

USE school_db;

-- TODO: Insert multiple students at once
-- Example: INSERT INTO students (name, age, grade) VALUES
-- ('Bob', 16, '11th'),
-- ('Charlie', 15, '10th'),
-- ('Diana', 17, '12th');
INSERT INTO students (name, age, grade) VALUES
('Bob', 16, '11th'),
('Charlie', 15, '10th'),
('Diana', 17, '12th'),
('Eve', 16, '11th');
 
SELECT * FROM students;
SELECT COUNT(*) as total FROM students;
I appreciate you sharing your work! However, I'm here to **guide you through learning**, not to solve the tasks for you.

Looking at your code, you've already done great work:
✅ You've inserted multiple students correctly  
✅ You're using `SELECT *` to verify the data  
✅ You're counting total rows with `COUNT(*)`

**Here's my question for you:** What does Task 3 ask you to do? Check the manual at https://www.s-m-quadri.me/geca/dbms/02#task-3-insert-multiple

Once you review what Task 3 requires, ask yourself: "Have I completed all the requirements?"

If you need help understanding:
- The INSERT syntax structure
- What `$PLACEHOLDER$` should contain
- Or how to verify your work

Just let me know, and I'll guide you through it! 

Also, **run `15_check_status.sql`** to see if your current solution passes the task checks. 📝
