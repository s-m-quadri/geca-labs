# Lab 3: Database Functions

Practice built-in SQL functions: numeric, date/time, string (character), aggregate/grouping, and counting.

## Objectives

- Apply numeric functions (ROUND, ABS, MOD)
- Use date functions (CURDATE, YEAR, MONTH, DATEDIFF, DATE_ADD)
- Manipulate text with character functions (CONCAT, UPPER, LOWER, SUBSTRING, LENGTH, TRIM)
- Combine rows with GROUP BY, filter groups with HAVING, and list members with GROUP_CONCAT
- Use COUNT and COUNT(DISTINCT)

## Tasks

Complete these 15 tasks in order:

1. **01_setup.sql** — Create `school_db` and `employees` table; insert sample rows
2. **02_numeric_round.sql** — ROUND on salary
3. **03_numeric_abs_mod.sql** — ABS and MOD
4. **04_date_current.sql** — CURDATE, NOW
5. **05_date_extract.sql** — YEAR, MONTH, DAY
6. **06_date_arithmetic.sql** — DATEDIFF, DATE_ADD
7. **07_char_case.sql** — UPPER, LOWER
8. **08_char_concat.sql** — CONCAT
9. **09_char_substring.sql** — SUBSTRING, LEFT, LENGTH
10. **10_char_trim.sql** — TRIM on phone
11. **11_count_basic.sql** — COUNT(*), conditional counts
12. **12_count_distinct.sql** — COUNT(DISTINCT dept)
13. **13_group_aggregate.sql** — GROUP BY with SUM and AVG
14. **14_group_having.sql** — HAVING and GROUP_CONCAT (two parts)
15. **15_check_status.sql** — Inspect database state

## Schema (reference)

Table `employees` (you create in task 1):

| Column     | Type           | Notes              |
| ---------- | -------------- | ------------------ |
| emp_id     | INT PK AI      | Primary key        |
| full_name  | VARCHAR(60)    | Employee name      |
| dept       | VARCHAR(40)    | Department         |
| salary     | DECIMAL(10,2)  | Monthly salary     |
| hire_date  | DATE           | Date joined        |
| phone      | VARCHAR(25)    | May include spaces |

## Running Your Code

```bash
sudo mysql < 01_setup.sql
sudo mysql school_db < 02_numeric_round.sql
# ... continue in order
sudo mysql < 15_check_status.sql
```

## Check Your Work

Run `15_check_status.sql` anytime:

```bash
sudo mysql < 15_check_status.sql
```

## Submission

1. Complete all 15 tasks
2. Test each file
3. Commit: `git add . && git commit -m "[YOUR_PRN] Lab 3 Database Functions"`
4. Push: `git push origin lab-dbms-03`
5. Open a Pull Request: `Submission of Lab 3 by [YOUR_PRN]`

## Manual

https://www.s-m-quadri.me/geca/dbms/03
