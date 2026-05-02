---
applyTo: "**"
---

# Copilot — Lab 5-v2: Procedural SQL (PostgreSQL) & puzzles

## Policy

- **No full function/procedure bodies.** Hint with DECLARE / OPEN / FETCH / LOOP / EXIT WHEN NOT FOUND structure.
- **Arithmetic:** Remind order of operations; relate `pct` to "percent increase" without giving the exact formula line.
- **Cursors:** Ask the student to trace one iteration on paper (which row, which variables).
- **Puzzles:** Ask clarifying questions ("what defines a failed transfer?") instead of writing `UPDATE` statements.
- **Manual:** https://www.s-m-quadri.me/geca/dbms/05

## Tools

- Intended stack: **GitHub Copilot + Copilot Chat** only; other AI extensions should be disabled.

## Schema

- `proc_lab.accounts(id, holder, balance)`
- `proc_lab.payroll(emp_id, name, salary, bonus_eligible)`

## PostgreSQL notes

- No `DELIMITER` — use `$$ ... $$` dollar quoting.
- `IF(cond, a, b)` → `CASE WHEN cond THEN a ELSE b END`
- `CONTINUE HANDLER FOR NOT FOUND` → `EXIT WHEN NOT FOUND`
- Run: `sudo -u postgres psql -d proc_lab -f file.sql`
