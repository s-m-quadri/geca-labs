-- Task 4: Date — current date and time
-- Compare hire_date to today using CURDATE() and show NOW() once.

USE school_db;

-- TODO: SELECT NOW() AS server_time;

-- TODO: SELECT full_name, hire_date, CURDATE() AS today,
--   (CURDATE() >= hire_date) AS hired_on_or_before_today
-- FROM employees;
I'll guide you through Task 4 rather than write the complete solution.

**What you need to do:**

1. **First TODO** – Uncomment and run `SELECT NOW() AS server_time;` to see the server's current date and time.

2. **Second TODO** – Uncomment and run the SELECT statement that compares `hire_date` to today using `CURDATE()`.

**Key concept to remember:**
- `NOW()` returns date **and** time (e.g., `2024-01-15 14:23:45`)
- `CURDATE()` returns only the date part (e.g., `2024-01-15`)
- Both are useful for comparing against your `hire_date` column

**Your task:**
Simply uncomment both TODO blocks (remove the `--` at the start of each line) and run the file. The logic is already there—no new code needed!

**Hint:** After you uncomment, what do you expect to see in the `hired_on_or_before_today` column? Why?

See the manual for more details: https://www.s-m-quadri.me/geca/dbms/03

Need clarification on CURDATE vs NOW?