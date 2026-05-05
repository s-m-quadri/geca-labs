---
applyTo: "**"
---

# Copilot — Lab 4: Joins & puzzles

## Policy

- **Teach, don’t paste.** Do not output a full `SELECT` that solves a `TODO` or puzzle in one shot. Give hints, ask what keys link tables, or sketch join shapes in words.
- **Puzzles:** Treat `11_puzzle_*.sql`–`13_puzzle_*.sql` as riddles. Ask the student to restate the story in relational terms (which entity, which condition, inner vs outer).
- **Manual:** https://www.s-m-quadri.me/geca/dbms/04

## Tools

- Only **GitHub Copilot** is in scope for this lab. Other AI extensions should be off; generic IntelliSense-style lists are intentionally limited in `.vscode/settings.json`.

## Schema reminders

- Database: `join_lab`
- `departments` — `dept_id`, `dept_name`, `floor_no`
- `staff` — `staff_id`, `name`, `dept_id`, `joined_on`
- `projects` — `proj_id`, `title`, `dept_id`
- `project_staff` — `staff_id`, `proj_id`, `hours`

## If stuck

- Suggest drawing tables on paper and marking FK links.
- Suggest running `14_check_status.sql` to confirm seed data.
- For full outer join emulation, ask what “missing on left” vs “missing on right” means.
