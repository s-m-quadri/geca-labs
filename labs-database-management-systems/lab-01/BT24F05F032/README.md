# Lab 1: DDL Commands

Learn SQL Data Definition Language commands through simple, progressive tasks.

## Objectives

- Create and manage databases and tables
- Practice ALTER TABLE commands
- Understand DROP operations
- Learn basic data manipulation

## Tasks

Complete these 10 simple tasks in order:

1. **01_create_database.sql** - Create school_db database
2. **02_create_table.sql** - Create students table
3. **03_insert_data.sql** - Add sample student records
4. **04_alter_add_column.sql** - Add grade column
5. **05_alter_modify.sql** - Modify age column
6. **06_alter_rename.sql** - Rename name column
7. **07_update_data.sql** - Update student grade
8. **08_delete_data.sql** - Delete a student
9. **09_drop_table.sql** - Drop students table
10. **10_check_status.sql** - View database status

## How to Work

1. Open each file in order (01, 02, 03, ...)
2. Read the TODO comment
3. Write the SQL command
4. Test by running the file
5. Move to next task

## Running Your Code

Execute one file at a time:

```bash
# Task 1: Create database
sudo mysql < 01_create_database.sql

# Task 2: Create table
sudo mysql < 02_create_table.sql

# Task 3: Insert data
sudo mysql < 03_insert_data.sql

# Continue with remaining tasks...
# Task 4-9
sudo mysql < 04_alter_add_column.sql
sudo mysql < 05_alter_modify.sql
sudo mysql < 06_alter_rename.sql
sudo mysql < 07_update_data.sql
sudo mysql < 08_delete_data.sql
sudo mysql < 09_drop_table.sql

# Task 10: Check status anytime
sudo mysql < 10_check_status.sql
```

## Check Your Work

Use `10_check_status.sql` to see current database status:

```bash
sudo mysql < 10_check_status.sql
```

This shows:
- All databases
- All tables in school_db
- Students table structure
- Number of rows
- All student data

## Getting Help

- Check the lab manual for examples
- Use GitHub Copilot for syntax help
- Run `10_check_status.sql` if confused
- Ask instructor if stuck

## Submission

1. Complete all 10 tasks
2. Test each file works
3. Commit: `git add . && git commit -m "[YOUR_PRN] Lab 1 DDL"`
4. Push: `git push origin lab-dbms-01`
5. Create Pull Request: `Submission of Lab 1 by [YOUR_PRN]`

Good luck!
