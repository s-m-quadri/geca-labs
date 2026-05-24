# Task 6: Date — DATEDIFF and DATE_ADD

Great! You're working on date arithmetic. Let me guide you through this.

## Key Concepts

**DATEDIFF in MySQL:**
- Syntax: `DATEDIFF(end_date, start_date)`
- Returns the **number of days** between two dates
- Order matters: end date first, start date second

**DATE_ADD:**
- Syntax: `DATE_ADD(date, INTERVAL value UNIT)`
- UNIT can be: `DAY`, `MONTH`, `YEAR`, etc.

## Questions to Guide You

1. **For the first query**: You want to find how many days each employee has been employed.
    - What should be the "end date"? (Hint: today's date)
    - What should be the "start date"? (Hint: when they were hired)

2. **For the second query**: You're calculating their one-year anniversary.
    - Which function adds time to a date?
    - What interval should you use?

## Next Steps

✅ Uncomment the first TODO and fill in the `DATEDIFF()` call with the correct argument order.

✅ Uncomment the second TODO and complete the `DATE_ADD()` call.

**Need help?** Review the date functions section here: https://www.s-m-quadri.me/geca/dbms/03

Once you're done, run `15_check_status.sql` to verify your work!
