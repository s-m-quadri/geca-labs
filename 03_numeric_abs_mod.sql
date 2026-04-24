I can see you're working on **Task 3** of Lab 3—using `ABS()` and `MOD()` functions! Let me guide you rather than give the complete solution.

## Key Concepts

**ABS(x)** — returns the absolute value (distance from zero)
- Example: `ABS(salary - 50000)` gives how far each salary is from 50k

**MOD(x, y)** — returns the remainder after division
- Example: `MOD(emp_id, 3)` gives the remainder when emp_id is divided by 3

## Your Task

Looking at the TODO comment, you need to:

1. **SELECT** the columns listed in the comment
2. **Calculate** the distance of each salary from 50000 using `ABS()`
3. **Calculate** each employee's ID modulo 3 using `MOD()`
4. **Use aliases** like `dist_from_50k` and `id_mod_3`

## Guided Questions

- What MySQL syntax takes a column/expression and gives a result with a label? (Hint: think `AS`)
- Do you need a WHERE clause, or should you see all employees?

## Next Steps

Once you write your query:
1. Run it to check the output
2. Then run `15_check_status.sql` to verify (if available)

Need a hint on the exact syntax, or are you ready to try?

📖 **Reference**: https://www.s-m-quadri.me/geca/dbms/03
