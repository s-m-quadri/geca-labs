# Defence Staff Management System - Readme

Complete DBMS mini project for Lab 7 — Defence Staff Management System.

## 📁 Project Structure

```
defence-staff-mgmt/
├── ddl.sql          # Database schema (7 tables, normalized, FK chains)
├── seed.sql         # Sample data (70+ records across all tables)
├── queries.sql      # 12 production queries with varied complexity
├── schema.md        # ER diagram, design rationale, normalization analysis
├── report.md        # Complete project report with test results
└── README.md        # This file
```

## 🎯 Quick Start

### 1. Create Database & Schema
```bash
mysql -u root -p < ddl.sql
```

### 2. Load Sample Data
```bash
mysql -u root -p < seed.sql
```

### 3. Run All Queries
```bash
mysql -u root -p defence_staff_mgmt < queries.sql
```

## 📋 What's Included

### ✅ Schema (ddl.sql)
- **7 normalized tables** with clear primary & foreign keys
- **Foreign key chain**: DEPARTMENTS → STAFF → STAFF_QUALIFICATIONS → QUALIFICATIONS
- **Data integrity**: Unique constraints, check constraints, cascading deletes
- **Performance**: 5 strategic indexes on frequently queried columns

### ✅ Sample Data (seed.sql)
- **12 staff members** across 6 defence departments
- **10 military ranks** (Sepoy to Lieutenant General)
- **8 qualifications** with varying certification levels
- **15 staff qualifications** (M:N relationships)
- **13 assignments** (current and historical)
- **19 training records** (audit trail of all training)

### ✅ Queries (queries.sql)
**12 production-ready queries** covering:
1. Multi-table JOINs (4+ tables)
2. GROUP BY with HAVING
3. Subqueries and CTEs
4. CREATE VIEW + SELECT
5. Window functions (ROW_NUMBER)
6. Complex business logic
7. Time-based filtering
8. Aggregates and analytics

### ✅ Documentation
- **schema.md** — ER diagram (ASCII art), normalization decisions, extension points
- **report.md** — Complete project report: problem statement, design rationale, test results, limitations

## 🔍 Sample Queries

### Find High-Priority Assignments
```sql
SELECT * FROM defence_staff_mgmt.assignments 
WHERE priority IN ('high', 'critical') AND is_current = TRUE;
```

### Departments with >2 Active Staff
```sql
SELECT d.dept_name, COUNT(s.staff_id) 
FROM departments d 
JOIN staff s ON d.dept_id = s.dept_id 
WHERE s.status = 'active'
GROUP BY d.dept_id 
HAVING COUNT(s.staff_id) > 2;
```

### Expert-Level Staff
```sql
SELECT * FROM expert_staff_view;
```

See **queries.sql** for all 12 queries with comments.

## 📊 Data Model Highlights

| Entity | Purpose | Rows |
|--------|---------|------|
| STAFF | Core personnel record | 12 |
| RANKS | Military rank hierarchy | 10 |
| DEPARTMENTS | Organizational units | 6 |
| QUALIFICATIONS | Certifications | 8 |
| STAFF_QUALIFICATIONS | Skills per person (M:N) | 15 |
| ASSIGNMENTS | Job roles (current & historical) | 13 |
| TRAINING_RECORDS | Training completion audit | 19 |

## 🔗 Foreign Key Chain
```
DEPARTMENTS (1) ──→ STAFF (N) ──→ STAFF_QUALIFICATIONS (N) ──→ QUALIFICATIONS
```

## 🚀 Future Enhancements

- **Audit Trail** — Track who modified what and when
- **Rank History** — Store promotion timeline
- **Leave Management** — Annual/sick leave tracking
- **Performance Reviews** — Staff evaluation scores
- **Equipment Assignments** — Link gear to personnel
- **Stored Procedures** — Automated qualification renewal checks
- **Triggers** — Enforce business rules (e.g., prevent delete with active assignments)

## 📝 Project Rubric Alignment

✅ **Schema**: 7 tables with clear PK/FK, 3+ FK chain, normalized  
✅ **Data**: 12+ rows per table, no empty query results  
✅ **Queries**: 12 queries covering all required types  
✅ **Documentation**: ER diagram, design rationale, test results  
✅ **Report**: Problem statement, limitations, references  

## 🛠️ Technical Stack

- **Database**: MySQL 8.0+
- **Engine**: InnoDB (ACID + Relational Integrity)
- **Normalization**: 3NF+
- **Scripting**: Pure SQL (DDL, DML, views, indexes)

## 📞 Support

For issues or questions:
1. Check **schema.md** for design decisions
2. Review **report.md** for test scenarios
3. Examine **queries.sql** for example usage
4. Refer to normalization decisions in **schema.md**

---

**Status**: ✅ Complete  
**Date**: May 2, 2026  
**Lab**: 7 — DBMS Mini Project (Defence Staff Management)
