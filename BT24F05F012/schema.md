# Defence Staff Management System - Schema Documentation

## Executive Summary

This database manages defence staff personnel, their qualifications, training records, and operational assignments. The system is designed to track military/defence personnel across departments with their ranks, certifications, and current job assignments.

---

## Entity-Relationship Diagram (ER) Diagram)

```
┌─────────────────────────────────────────────────────────────┐
│ RANKS                                                       │
├─────────────────────────────────────────────────────────────┤
│ PK: rank_id (INT)                                          │
│ rank_name (VARCHAR) - UNIQUE                               │
│ seniority_level (INT)                                      │
│ description (TEXT)                                          │
│ created_at (TIMESTAMP)                                     │
└─────────────────────────────────────────────────────────────┘
           │
           │ 1:N
           ▼
┌─────────────────────────────────────────────────────────────┐
│ STAFF (Main Entity)                                         │
├─────────────────────────────────────────────────────────────┤
│ PK: staff_id (INT)                                         │
│ title, first_name, last_name (VARCHAR)                     │
│ date_of_birth (DATE)                                       │
│ FK: rank_id → RANKS(rank_id)                              │
│ FK: dept_id → DEPARTMENTS(dept_id)                        │
│ service_start_date (DATE)                                 │
│ status (ENUM: active, inactive, on_leave, retired)       │
│ created_at, updated_at (TIMESTAMP)                        │
└─────────────────────────────────────────────────────────────┘
    │                    │                    │
    │ 1:N               │ 1:N                │ 1:N
    ▼                    ▼                    ▼
┌───────────────────────┐  ┌────────────────┐  ┌─────────────┐
│ STAFF_QUALIFICATIONS  │  │ ASSIGNMENTS    │  │ TRAINING    │
├───────────────────────┤  ├────────────────┤  │ _RECORDS    │
│ PK: staff_qual_id     │  │ PK: assign_id  │  ├─────────────┤
│ FK: staff_id (STAFF)  │  │ FK: staff_id   │  │ PK: train_id│
│ FK: qual_id           │  │ title (VARCHAR)│  │ FK: staff_id│
│ acquired_date (DATE)  │  │ start_date     │  │ FK: qual_id │
│ expiry_date (DATE)    │  │ end_date       │  │ train_type  │
│ certification_level   │  │ is_current     │  │ completion_%
│ (ENUM: basic,...)     │  │ priority (ENUM)│  │ trainer_name│
└───────────────────────┘  └────────────────┘  │ notes       │
           │                                     └─────────────┘
           │ N:M
           ▼
┌─────────────────────────────────────────────────────────────┐
│ QUALIFICATIONS                                              │
├─────────────────────────────────────────────────────────────┤
│ PK: qual_id (INT)                                          │
│ qual_name (VARCHAR) - UNIQUE                               │
│ description (TEXT)                                          │
│ renewal_months (INT)                                        │
│ created_at (TIMESTAMP)                                     │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│ DEPARTMENTS                                                 │
├─────────────────────────────────────────────────────────────┤
│ PK: dept_id (INT)                                          │
│ dept_name (VARCHAR) - UNIQUE                               │
│ description (TEXT)                                          │
│ location (VARCHAR)                                          │
│ head_count (INT)                                            │
│ created_at (TIMESTAMP)                                     │
└─────────────────────────────────────────────────────────────┘
           ▲
           │ 1:N
           │
        FK: dept_id (STAFF)
```

---

## Database Design Rationale

### **Foreign Key Chain** (As required)
The schema implements a **3-level FK chain**:

```
DEPARTMENTS (1) ──→ STAFF (N) ──→ STAFF_QUALIFICATIONS (N) ──→ QUALIFICATIONS
```

**Explanation:**
- Every **STAFF** member belongs to exactly one **DEPARTMENT**
- Every **STAFF_QUALIFICATIONS** record links a staff member to a qualification
- This creates a dependency chain: If a department changes, it cascades to its staff; if a staff member is deleted, their qualifications are removed

---

### **Table Relationships**

| Table | Type | Purpose | Related To |
|-------|------|---------|-----------|
| **RANKS** | Lookup | Military rank definitions | STAFF (1:N) |
| **DEPARTMENTS** | Lookup | Defence units/branches | STAFF (1:N) |
| **QUALIFICATIONS** | Lookup | Available certifications | STAFF_QUALIFICATIONS (N:M) |
| **STAFF** | Main | Personnel records | All others via FK |
| **STAFF_QUALIFICATIONS** | Junction | M:N bridge (Staff ↔ Qualifications) | STAFF, QUALIFICATIONS |
| **ASSIGNMENTS** | Transactional | Current/past job assignments | STAFF (1:N) |
| **TRAINING_RECORDS** | Transactional | Training completion history | STAFF, QUALIFICATIONS (1:N) |

---

### **Normalization Decisions**

#### **Why 7 Tables?**

1. **RANKS** (Separate lookup table)
   - ✅ Avoids data duplication (same rank across many staff)
   - ✅ Seniority level in one place for consistency
   - ❌ Alternative: Store rank_name as VARCHAR in STAFF → Causes redundancy

2. **DEPARTMENTS** (Separate lookup table)
   - ✅ Enables department-wide analysis
   - ✅ Tracks head_count and location centrally
   - ❌ Alternative: Denormalize into STAFF → Can't track empty departments

3. **STAFF_QUALIFICATIONS** (Junction table for M:N)
   - ✅ Allows multiple qualifications per staff member
   - ✅ Allows multiple staff to share the same qualification
   - ✅ Stores acquisition date and certification level
   - ❌ Alternative: Array field → Not standard SQL, reduces flexibility

4. **ASSIGNMENTS** (Separate from STAFF)
   - ✅ Tracks current AND historical assignments
   - ✅ Can query assignment timeline per staff member
   - ✅ Supports concurrent multiple assignments (future extension)
   - ❌ Alternative: Single assignment_title column in STAFF → Can't track history

5. **TRAINING_RECORDS** (Separate from STAFF_QUALIFICATIONS)
   - ✅ TRAINING_RECORDS = process (multiple trainings for same qual)
   - ✅ STAFF_QUALIFICATIONS = outcome (acquired qualification status)
   - ✅ Can audit all training history
   - ❌ Alternative: Single table → Confuses training history with qualification possession

---

### **Data Integrity Constraints**

```sql
-- Unique constraint: No duplicate (first_name, last_name, DOB)
UNIQUE KEY unique_staff (first_name, last_name, date_of_birth)

-- Cascade deletes: Removing staff automatically removes their qualifications/assignments
FOREIGN KEY (staff_id) REFERENCES staff(staff_id) ON DELETE CASCADE

-- Check constraint: Completion percentage must be 0-100
CHECK (completion_percentage >= 0 AND completion_percentage <= 100)

-- Unique qualification per staff (no duplicate rows)
UNIQUE KEY unique_qualification (staff_id, qual_id)
```

---

### **Why NOT Include...**

- **Performance Review Scores**: Not in scope for management system
- **Salary Information**: Typically in HR/Finance system (separation of concerns)
- **Medical Records**: Sensitive PII; separate system recommended
- **Equipment Assignments**: Could be added in extension; not core to MVP

---

## Data Seeding Strategy

### **Sample Data Breakdown**

| Table | Row Count | Rationale |
|-------|-----------|-----------|
| RANKS | 10 | Full military rank hierarchy (Sepoy to Lt. General) |
| DEPARTMENTS | 6 | Representative defence branches |
| QUALIFICATIONS | 8 | Mix of pilot, combat, medical, signals, cyber training |
| STAFF | 12 | Sufficient for meaningful analytics (>8 rows rule) |
| STAFF_QUALIFICATIONS | 15 | ~1.25 qualifications per staff on average |
| ASSIGNMENTS | 13 | Mix of current (is_current=TRUE) and past assignments |
| TRAINING_RECORDS | 19 | Tracks all training history (some staff trained multiple times) |

**Why 12 staff members?**
- Exceeds minimum 8-row requirement
- Distributed across 6 departments (allows GROUP BY analysis)
- Mix of seniority levels and expertise
- Realistic for operational analysis queries

---

## Query Coverage

### **Queries Included (12 total)**

| # | Type | Purpose |
|---|------|---------|
| 1 | Multi-table JOIN | Staff + Rank + Dept + Current Assignment |
| 2 | GROUP BY + HAVING | Departments with >2 staff members |
| 3 | Subquery | Expiring certifications (next 6 months) |
| 4 | CREATE VIEW + SELECT | Expert-level staff by department |
| 5 | Complex JOIN + Aggregate | Training statistics per staff |
| 6 | Nested Subquery | Above-average qualifications by dept |
| 7 | Multiple JOIN + Business Logic | High-priority assignments tracking |
| 8 | Window Function | Rank staff by seniority & experience |
| 9 | Cross Join + Aggregate | Qualification coverage analysis |
| 10 | LEFT JOIN + CASE | Assignment history & transitions |
| 11 | Conditional SELECT | Staff on leave status |
| 12 | Time-based Query | New hire orientation checklist |

---

## Performance Optimization

### **Indexes Created**

```sql
CREATE INDEX idx_staff_rank ON staff(rank_id);
CREATE INDEX idx_staff_dept ON staff(dept_id);
CREATE INDEX idx_staff_status ON staff(status);
CREATE INDEX idx_assignments_start ON assignments(start_date);
CREATE INDEX idx_training_completion ON training_records(completion_date);
```

**Why these?**
- STAFF queries filter by rank/dept/status frequently
- ASSIGNMENTS queries often sort by start_date
- TRAINING_RECORDS queries search by completion_date

---

## Extension Points (Future Work)

1. **Audit Trail**: Add created_by, modified_by columns
2. **Equipment Management**: New table linking STAFF ↔ EQUIPMENT
3. **Performance Reviews**: New table for annual reviews
4. **Deployment Tracking**: New table for field deployment dates/locations
5. **Promotion History**: Track rank changes over time (audit table)
6. **Leave Balance**: Track annual/sick leave in separate table

---

## System Limitations & Design Trade-offs

| Limitation | Reason | Mitigation |
|-----------|--------|-----------|
| Single rank per staff | Real systems need rank history | Add RANK_HISTORY table if needed |
| Single department tracking | Can't handle temporary postings | Add DEPARTMENT_HISTORY table |
| Soft delete not implemented | Simplicity; relies on status enum | Add is_deleted flag if archival needed |
| No audit logging | Not in MVP scope | Add trigger-based audit trail |

---

## How to Use This Schema

### **Setup**
```bash
mysql -u root -p < ddl.sql      # Create schema and tables
mysql -u root -p < seed.sql     # Load sample data
```

### **Run Analytics**
```bash
mysql -u root -p defence_staff_mgmt < queries.sql  # Execute all queries
```

### **Key Operational Queries**

- **Find high-priority assignments**: Query #7
- **Identify expiring certifications**: Query #3
- **Analyze dept staffing**: Query #2
- **Track assignment history**: Query #10
- **New hire onboarding**: Query #12
