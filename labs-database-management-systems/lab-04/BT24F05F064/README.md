# Lab 4: Joins and relational puzzles

Combines **join operations** (previous syllabus labs 4–8 slice: joins) with **riddle-style** queries. MySQL in Codespaces.

## Environment (important)

- **GitHub Copilot** (and Copilot Chat) are the intended assistants. Repo ships `.vscode/settings.json` and `.devcontainer/devcontainer.json` to **turn off generic editor completions** and reduce noise from other suggestion sources.
- **Disable other AI extensions** if your profile installs them (Tabnine, Cody, Codeium, etc.). Only Copilot should stay enabled for this lab.
- **Do not** paste full puzzle solutions into external chat tools; use the manual + Copilot with this repo’s instructions.

## Problem set

| File | Focus |
| --- | --- |
| `01_setup.sql` | Schema + seed (run first) |
| `02_cross_join.sql` … `10_natural_join_note.sql` | Core join patterns |
| `11_puzzle_*.sql` … `13_puzzle_*.sql` | Riddles (read comments carefully) |
| `14_check_status.sql` | Sanity check |

## Run

```bash
sudo mysql < 01_setup.sql
sudo mysql join_lab < 02_cross_join.sql
# …
sudo mysql < 14_check_status.sql
```

## Manual

https://www.s-m-quadri.me/geca/dbms/04

## Submit

`[YOUR_PRN] Lab 4: Joins & puzzles` → PR title `Submission of Lab 4 by [YOUR_PRN]`
