# Lab 7 Report — Hospital Management System

## 1. Problem

**User**: Hospital administration staff who need to manage patient records,
schedule appointments, record diagnoses and prescriptions, and track billing.

**Core questions the database must answer:**
- Which doctor saw which patient, when, and for what?
- What was diagnosed and prescribed?
- How much has each department billed/collected?
- Which patients have unpaid dues?

---

## 2. Design Decisions

### Why these tables?

| Table         | Why it exists                                               |
|---------------|-------------------------------------------------------------|
| `department`  | Organises doctors by specialty; enables department-level reports |
| `doctor`      | Separate from department for 1:N; stores speciality independently |
| `patient`     | Core entity; DOB/gender enable age-based analytics          |
| `appointment` | Central junction — links patient to doctor on a specific date |
| `diagnosis`   | ICD-coded; N diagnoses per appointment (e.g., comorbidities)|
| `prescription`| N medicines per appointment; `duration_days` enables compliance reporting |
| `bill`        | 1:1 with appointment; decoupled so billing can be updated separately |

### What was normalised away?

- Doctor's department name is **not** stored in `doctor` — fetched via JOIN.
- Patient's doctor name is **not** stored in `appointment` — fetched via JOIN.
- Department of a diagnosis is derived via `diagnosis → appointment → doctor → department` (no shortcut FK stored).
- Billing amount per prescription line is intentionally absent — the bill is a flat consultation fee, not itemised (YAGNI for this scope).

---

## 3. Sample Query Results

### Q1 — Appointment detail (first 3 rows)
| patient        | doctor         | department       | appt_date  | status    |
|----------------|----------------|------------------|------------|-----------|
| Arjun More     | Rohan Desai    | Cardiology       | 2025-01-10 | Completed |
| Sarita Chopra  | Suresh Kumar   | General Medicine | 2025-01-12 | Completed |
| Rajeev Iyer    | Amit Joshi     | Neurology        | 2025-01-15 | Completed |

### Q2 — Revenue by department
| dept_name        | total_billed | total_collected | outstanding |
|------------------|--------------|-----------------|-------------|
| Cardiology       | 12300.00     | 4300.00         | 8000.00     |
| General Medicine | 1500.00      | 1500.00         | 0.00        |
| Neurology        | 1100.00      | 1100.00         | 0.00        |

### Q7 — Outstanding dues
| patient      | amount_due |
|--------------|------------|
| Rajeev Iyer  | 1800.00    |
| Arjun More   | 4200.00    |
| Nikhil Deshmukh | 750.00  |

---

## 4. Limitations

1. **No room/bed management** — inpatient admissions are not modelled.
2. **No lab tests** — diagnostic tests (X-ray, blood work) are not tracked.
3. **Bill is flat** — real-world billing is itemised (consultation + procedures + medicines).
4. **No audit trail** — updated records overwrite previous values (no history table / temporal table).
5. **Single doctor per appointment** — team consultations are not supported.
6. **No authentication** — in a real system, staff roles and access control are required.

---

## 5. What I Would Add With More Time

- `lab_test` table linked to appointment (FK chain extension)
- `admission` table for inpatient stays with room assignment
- Stored procedure: `book_appointment(patient_id, doctor_id, date, time)` with availability check
- Trigger: automatically create a `bill` row when appointment status changes to `Completed`
- Views for patient history and monthly financial dashboard

---

## 6. References

- PostgreSQL Documentation — https://www.postgresql.org/docs/
- ICD-10 Code Reference — https://www.icd10data.com/
- Ramakrishnan & Gehrke. *Database Management Systems*, 3rd ed., McGraw-Hill.
- GECA Lab 7 Manual — lab specification document

---

*AI assistance: GitHub Copilot was used to suggest two column constraint patterns
(CHECK on `gender` and `status`). All table design, query logic, and analysis
are the author's own work.*