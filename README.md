# Lab 1: DDL Commands

This lab focuses on Data Definition Language (DDL) commands in SQL.

## Objectives

- Master CREATE, ALTER, DROP, and TRUNCATE commands
- Understand constraints (PRIMARY KEY, FOREIGN KEY, UNIQUE, NOT NULL, CHECK)
- Practice schema design and modification
- Learn database object management

## Files to Complete

1. **create_database.sql** - Create the college_db database
2. **create_tables.sql** - Create tables with constraints
3. **alter_table.sql** - Modify table structures
4. **drop_operations.sql** - Practice DROP operations
5. **truncate_table.sql** - Understand TRUNCATE vs DELETE
6. **advanced_ddl.sql** - Complex DDL operations

## How to Work

1. Each SQL file contains TODO comments indicating what you need to implement
2. Read the lab manual at [geca-labs documentation](https://github.com/s-m-quadri/geca-labs)
3. Complete each TODO section with the appropriate SQL commands
4. Test your work by executing each file

## Testing Your Work

Execute files in this order:

```bash
# 1. Create database
sudo mysql < create_database.sql

# 2. Create tables
sudo mysql college_db < create_tables.sql

# 3. Modify tables
sudo mysql college_db < alter_table.sql

# 4. Practice drop operations
sudo mysql college_db < drop_operations.sql

# 5. Practice truncate
sudo mysql college_db < truncate_table.sql

# 6. Advanced DDL
sudo mysql college_db < advanced_ddl.sql
```

## Verification

After completing all files, verify your work:

```bash
# Check database exists
sudo mysql -e "SHOW DATABASES LIKE 'college_db';"

# Check tables exist
sudo mysql -e "USE college_db; SHOW TABLES;"

# Check table structures
sudo mysql -e "USE college_db; DESCRIBE students;"
sudo mysql -e "USE college_db; DESCRIBE departments;"
sudo mysql -e "USE college_db; DESCRIBE courses;"
sudo mysql -e "USE college_db; DESCRIBE enrollments;"
```

## Getting Help

- Review the lab manual for detailed explanations
- Use GitHub Copilot to assist with syntax (but understand what you're writing!)
- Check MySQL documentation: https://dev.mysql.com/doc/
- Ask your instructor if you're stuck

## Submission

1. Complete all TODO sections in each file
2. Test that all files execute without errors
3. Commit your changes: `git add . && git commit -m "[YOUR_PRN] Lab 1: DDL Commands"`
4. Push to your fork: `git push origin lab-dbms-01`
5. Create a Pull Request with title: `Submission of Lab 1 by [YOUR_PRN]`

## Important Notes

- DDL commands are auto-committed and cannot be rolled back
- Always backup important data before DDL operations
- Read each TODO carefully before implementing
- Test each file individually before moving to the next
- Understand what each command does, don't just copy solutions

Good luck! 🚀
