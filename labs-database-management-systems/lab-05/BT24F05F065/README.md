# Lab 5-v2: Procedural SQL (PostgreSQL) — arithmetic, functions, cursors, puzzles

PostgreSQL variant of Lab 5. Uses `$$ ... $$` dollar quoting — no `DELIMITER` or `run_source.sh` needed.

## Environment

- **Copilot only** among AI assistants: see `.vscode/settings.json` and `.devcontainer/devcontainer.json`.
- PostgreSQL is installed automatically via `.devcontainer/setup-postgres.sh`.
- Start it manually if needed: `sudo service postgresql start`

## Running files

```bash
sudo -u postgres psql -f 01_setup.sql
sudo -u postgres psql -d proc_lab -f 02_user_vars_arithmetic.sql
```

## Problem set

| File | Notes |
| --- | --- |
| `01_setup.sql` | Run first — creates the database and seed data |
| `02_user_vars_arithmetic.sql` | Arithmetic in SELECT |
| `03_select_if.sql` | CASE WHEN conditional expression |
| `04_proc_apply_rate.sql` | Function with RETURNS |
| `05_call_procedures.sql` | Call apply_rate after task 4 |
| `06_proc_cursor_sum.sql` | Cursor loop that accumulates a sum |
| `07_proc_cursor_bonus.sql` | Cursor-driven UPDATE |
| `08_puzzle_safe_transfer.sql` | Puzzle A: safe bank transfer procedure |
| `09_puzzle_balance_enigma.sql` | Puzzle B: scalar subquery riddle |
| `10_check_status.sql` | Verify final state |

## Manual

https://www.s-m-quadri.me/geca/dbms/05

## Submit

`[YOUR_PRN] Lab 5-v2: Procedural SQL (PostgreSQL) & puzzles`
