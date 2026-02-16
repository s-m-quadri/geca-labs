# Lab 2: DML Commands

This lab focuses on Data Manipulation Language (DML) commands in SQL.

## Objectives

- Master INSERT, SELECT, UPDATE, and DELETE commands
- Learn data filtering with WHERE clause
- Understand sorting and limiting results
- Practice transaction management
- Query data with JOINs and subqueries

## Files to Complete

1. **setup.sql** - Database and table setup
2. **insert_data.sql** - INSERT operations
3. **select_queries.sql** - SELECT queries with various clauses
4. **update_data.sql** - UPDATE operations
5. **delete_data.sql** - DELETE operations
6. **transactions.sql** - Transaction management
7. **advanced_dml.sql** - Complex DML operations

## How to Work

1. Each SQL file contains TODO comments indicating what you need to implement
2. Read the lab manual at [geca-labs documentation](https://github.com/s-m-quadri/geca-labs)
3. Complete each TODO section with the appropriate SQL commands
4. Test your work by executing each file

## Testing Your Work

Execute files in this order:

```bash
# 1. Setup database and tables
sudo mysql < setup.sql

# 2. Insert data
sudo mysql college_db < insert_data.sql

# 3. Practice SELECT queries
sudo mysql college_db < select_queries.sql

# 4. Practice UPDATE
sudo mysql college_db < update_data.sql

# 5. Practice DELETE
sudo mysql college_db < delete_data.sql

# 6. Learn transactions
sudo mysql college_db < transactions.sql

# 7. Advanced DML
sudo mysql college_db < advanced_dml.sql
```

## Verification

After completing, verify your work:

```bash
# Check data exists
sudo mysql -e "USE college_db; SELECT COUNT(*) FROM students;"
sudo mysql -e "USE college_db; SELECT * FROM students LIMIT 3;"

# Check relationships
sudo mysql -e "USE college_db; 
SELECT s.first_name, d.department_name 
FROM students s 
JOIN departments d ON s.department_id = d.department_id 
LIMIT 3;"
```

## Getting Help

- Review the lab manual for detailed explanations
- Use GitHub Copilot to assist with syntax (but understand what you're writing!)
- Check MySQL documentation: https://dev.mysql.com/doc/
- Ask your instructor if you're stuck

## Submission

1. Complete all TODO sections in each file
2. Test that all files execute without errors
3. Commit your changes: `git add . && git commit -m "[YOUR_PRN] Lab 2: DML Commands"`
4. Push to your fork: `git push origin lab-dbms-02`
5. Create a Pull Request with title: `Submission of Lab 2 by [YOUR_PRN]`

## Important Notes

- DML commands can be rolled back using transactions
- Always test your WHERE conditions with SELECT before UPDATE/DELETE
- Use transactions for multi-step operations
- Understand JOIN types and when to use each
- Practice reading and understanding query results

Good luck! 🚀
