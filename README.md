# Lab 2: DML Commands

Learn SQL Data Manipulation Language through 15 simple progressive tasks.

## Objectives

- INSERT data into tables
- SELECT data with filters and sorting
- UPDATE existing records
- DELETE unwanted data
- Use aggregate functions (COUNT, AVG, MAX, MIN)
- GROUP data and filter groups

## Tasks

Complete these 15 tasks in order:

1. **01_setup.sql** - Create database and students table
2. **02_insert_one.sql** - Insert one student
3. **03_insert_multiple.sql** - Insert multiple students at once
4. **04_select_all.sql** - Select all students
5. **05_select_where.sql** - Select with WHERE filter
6. **06_select_order.sql** - Select with ORDER BY
7. **07_update_one.sql** - Update one student
8. **08_update_multiple.sql** - Update multiple students
9. **09_delete_where.sql** - Delete with WHERE
10. **10_count.sql** - Count total students
11. **11_avg.sql** - Calculate average age
12. **12_max_min.sql** - Find MAX and MIN age
13. **13_group_by.sql** - Group students by grade
14. **14_having.sql** - Filter groups with HAVING
15. **15_check_status.sql** - View database status

## How to Work

1. Open files in order (01, 02, 03, ...)
2. Read TODO comments
3. Write SQL commands
4. Test by running file
5. Move to next task

## Running Your Code

Execute one file at a time:

```bash
# Task 1: Setup
sudo mysql < 01_setup.sql

# Task 2-3: Insert data
sudo mysql < 02_insert_one.sql
sudo mysql < 03_insert_multiple.sql

# Task 4-6: Select queries
sudo mysql < 04_select_all.sql
sudo mysql < 05_select_where.sql
sudo mysql < 06_select_order.sql

# Task 7-9: Update and Delete
sudo mysql < 07_update_one.sql
sudo mysql < 08_update_multiple.sql
sudo mysql < 09_delete_where.sql

# Task 10-14: Aggregate functions
sudo mysql < 10_count.sql
sudo mysql < 11_avg.sql
sudo mysql < 12_max_min.sql
sudo mysql < 13_group_by.sql
sudo mysql < 14_having.sql

# Task 15: Check status anytime
sudo mysql < 15_check_status.sql
```

## Check Your Work

Use `15_check_status.sql` anytime to see:
- All databases
- All tables
- Table structure
- Row count
- All student data
- Summary by grade

```bash
sudo mysql < 15_check_status.sql
```

## Getting Help

- Check lab manual for examples
- Use GitHub Copilot for syntax
- Run `15_check_status.sql` if confused
- Ask instructor if stuck

## Submission

1. Complete all 15 tasks
2. Test each file works
3. Commit: `git add . && git commit -m "[YOUR_PRN] Lab 2 DML"`
4. Push: `git push origin lab-dbms-02`
5. Create Pull Request: `Submission of Lab 2 by [YOUR_PRN]`

Good luck!
