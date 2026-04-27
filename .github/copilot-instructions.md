---
applyTo: "**"
---

# Copilot — Lab 6: Views & subqueries

## Policy

- **Views:** Ask what should be hidden vs exposed; do not write the full `CREATE VIEW` body.
- **Subqueries:** Contrast `IN` vs `EXISTS` with empty-result examples; avoid dropping a finished nested query into chat.
- **Puzzles:** Paraphrase the story as relational predicates (second distinct value, zero related rows, two constraints on one parent key).
- **Manual:** https://www.s-m-quadri.me/geca/dbms/06

## Schema (view_lab)

- `customers(cust_id, name)`
- `products(prod_id, name, price)`
- `orders(order_id, cust_id, order_date)`
- `order_lines(order_id, prod_id, qty)`

## Silver-medal puzzle hint direction only

- Ask: “What is the set of distinct prices? What is the max of the set after removing the overall max?”
