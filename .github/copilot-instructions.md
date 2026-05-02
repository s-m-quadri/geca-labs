---
applyTo: "**"
---

# Copilot — Lab 6-v2: Views & Subqueries (PostgreSQL)

## Policy

- **Views:** Don't write the `SELECT` inside the view; ask what columns/joins are needed.
- **Subqueries:** Ask whether the value changes per outer row (correlated) or is fixed (scalar/IN).
- **Puzzles:** Ask what makes a product "silver tier", how to detect zero orders, how to spot a mixed basket.
- **Manual:** https://www.s-m-quadri.me/geca/dbms/06

## Tools

- Intended stack: **GitHub Copilot + Copilot Chat** only; other AI extensions should be disabled.

## Schema

- `view_lab.customers(cust_id, name)`
- `view_lab.products(prod_id, name, price)`
- `view_lab.orders(order_id, cust_id, order_date)`
- `view_lab.order_lines(order_id, prod_id, qty)`

## PostgreSQL notes

- `\c view_lab` instead of `USE view_lab`
- `SELECT tablename FROM pg_tables WHERE schemaname = 'public';` instead of `SHOW TABLES`
- `CREATE OR REPLACE VIEW` works the same way
- Run: `sudo -u postgres psql -d view_lab -f file.sql`
