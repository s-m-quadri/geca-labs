# Lab 5: Procedural SQL (MySQL) — arithmetic, cursors, updates, puzzles

Bundles **arithmetic in SQL**, **stored procedures**, **cursors**, **cursor-driven updates**, and **riddle-style** tasks (former syllabus spread across procedural topics).

## Environment

- **Copilot only** among AI assistants: see `.vscode/settings.json` and `.devcontainer/devcontainer.json`.
- Turn off Tabnine, Cody, Codeium, and similar if your Codespace profile adds them.
- Generic autocomplete lists are intentionally reduced so **Copilot + this repo’s `.github/copilot-instructions.md`** stay primary.

## DELIMITER / procedures

MySQL batch mode and `mysql < file` **do not** handle `DELIMITER` reliably. Use the helper:

```bash
chmod +x run_source.sh
./run_source.sh proc_lab 04_proc_apply_rate.sql
```

Plain `.sql` files without procedures can still use:

```bash
sudo mysql proc_lab < 02_user_vars_arithmetic.sql
```

## Problem set

| File | Notes |
| --- | --- |
| `01_setup.sql` | Run first |
| `02`–`03` | Variables + `IF()` |
| `04`, `06`–`08` | Use `./run_source.sh` after editing |
| `05` | `CALL` after `04` loads |
| `09` | Puzzle (plain SQL) |
| `10_check_status.sql` | Verify |

## Manual

https://www.s-m-quadri.me/geca/dbms/05

## Submit

`[YOUR_PRN] Lab 5: Procedural SQL & puzzles`
