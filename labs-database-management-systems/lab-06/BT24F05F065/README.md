# Lab 6-v2: Views & Subqueries (PostgreSQL)

PostgreSQL variant of Lab 6. Standard SQL — identical logic to the MySQL version, just without `USE db` statements.

## Environment

- **Copilot only** among AI assistants: see `.vscode/settings.json` and `.devcontainer/devcontainer.json`.
- PostgreSQL is installed automatically via `.devcontainer/setup-postgres.sh`.

## Running files

```bash
sudo -u postgres psql -f 01_setup.sql
sudo -u postgres psql -d view_lab -f 02_create_view.sql
```

## Problem set

| File | Notes |
| --- | --- |
| `01_setup.sql` | Run first — creates database and seed data |
| `02_create_view.sql` | CREATE OR REPLACE VIEW |
| `03_select_view.sql` | Query the view |
| `04_subquery_scalar.sql` | Scalar subquery in WHERE |
| `05_subquery_in.sql` | IN subquery |
| `06_subquery_exists.sql` | EXISTS |
| `07_correlated_subquery.sql` | Correlated subquery |
| `08_derived_table.sql` | Derived table in FROM |
| `09_puzzle_silver_medal.sql` | Puzzle A: silver tier products |
| `10_puzzle_wallflower.sql` | Puzzle B: customers with zero orders |
| `11_puzzle_split_basket.sql` | Puzzle C: mixed-price basket |
| `12_check_status.sql` | Verify final state |

## Manual

https://www.s-m-quadri.me/geca/dbms/06

## Submit

`[YOUR_PRN] Lab 6-v2: Views & Subqueries (PostgreSQL)`
