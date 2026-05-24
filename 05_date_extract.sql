I can see you're working on **Task 5: Date — YEAR, MONTH, DAY** from Lab 3! 

Rather than giving you the complete solution, let me guide you:

**What you need to do:**

The TODO comment already shows the structure. You need to:

1. **Uncomment** the SELECT statement (remove the `--` marks)
2. **Understand** what each function does:
    - `YEAR()` — extracts the year from a date
    - `MONTH()` — extracts the month (1–12)
    - `DAY()` — extracts the day (1–31)

3. **Alias** each function result with `AS y`, `AS m`, `AS d` so the columns have clear names

**Guiding questions:**

- What columns do you need to select? (name + date + the three extracted parts)
- Which table are you querying?
- How do you apply a function to a column in MySQL?

Once you've written it, run the query and verify the output shows year, month, and day components extracted from each employee's `hire_date`.

Need clarification on any of the date functions? Check the manual: https://www.s-m-quadri.me/geca/dbms/03#date-functions
