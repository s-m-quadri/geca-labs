-- Task 1: Setup database and employees table
-- You need sample data for later tasks (at least 5 rows, 2+ departments).

-- TODO: DROP DATABASE IF EXISTS school_db; then CREATE DATABASE school_db;

-- TODO: USE school_db;

-- TODO: CREATE TABLE employees with:
--   emp_id INT PRIMARY KEY AUTO_INCREMENT
--   full_name VARCHAR(60) NOT NULL
--   dept VARCHAR(40)
--   salary DECIMAL(10,2)
--   hire_date DATE
--   phone VARCHAR(25)

-- TODO: INSERT at least 5 rows. Vary dept, salary, hire_date.
-- Optional: put leading/trailing spaces in some phone values for TRIM task later.

-- TODO: SELECT * FROM employees;

I'd like to guide you through this rather than just provide the solution. Let's break down Task 1:

**What you need to do:**

1. **Drop and create the database** — Start fresh. Which MySQL statement drops a database only if it exists?

2. **Use the database** — How do you select `school_db` as your working database?

3. **Create the table** — You have the column definitions in the comments. Think about:
    - What's the correct syntax for `CREATE TABLE`?
    - Which column should auto-increment?
    - Which column has a NOT NULL constraint?

4. **Insert sample data** — Remember:
    - **At least 5 rows** with **2+ departments** (e.g., "HR", "IT", "Finance")
    - **Vary the salaries and hire dates** so later aggregate functions are interesting
    - **Tip for TRIM task**: Add leading/trailing spaces in a few phone numbers (e.g., `'  555-1234  '`)

5. **Verify with SELECT** — Query the table to confirm data is there.

**Questions to guide you:**
- What MySQL keywords do you need for DROP, CREATE, USE, INSERT?
- How many VALUES rows will you insert? (aim for 5+)
- Which departments will you use?

Once you've written the code, you can run it and verify with the manual here: https://www.s-m-quadri.me/geca/dbms/03

Give it a try, and let me know if you get stuck on any specific step!