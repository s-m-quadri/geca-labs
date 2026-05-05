# Lab Report 7: Relational Schema for an Integrated Hospital Management System

## 1. Project Overview & Scope

**Primary Stakeholders**: Medical administrators and front-desk coordinators.

**Objective**: To engineer a relational database capable of centralizing patient interactions, streamlining clinician scheduling, and maintaining financial transparency across various medical departments.

**Key Analytical Requirements:**
* **Traceability:** Linking specific clinical encounters to the responsible physician and department.
* **Clinical Record Keeping:** Archiving diagnoses and pharmacological treatments per visit.
* **Financial Oversight:** Aggregating revenue streams by department and identifying liquidity risks (unpaid accounts).

---

## 2. Architectural Framework

### Relational Schema Rationale

| Entity | Strategic Purpose |
| :--- | :--- |
| `Department` | Acts as the top-level container for resource allocation and financial reporting. |
| `Doctor` | Stores practitioner credentials; linked via Foreign Key to `Department` to maintain a strict 1:N hierarchy. |
| `Patient` | Maintains demographic integrity. Fields like `DOB` are prioritized over `Age` to prevent data staleness. |
| `Appointment` | The "Transaction Hub." It serves as the associative entity linking patients, doctors, and temporal data. |
| `Diagnosis` | Supports multiple entries per visit to accommodate patients with complex comorbidities. |
| `Prescription` | Details therapeutic interventions; decoupled from `Diagnosis` to allow for symptomatic treatment records. |
| `Invoice` | Tracks the fiscal lifecycle of an appointment (Billed vs. Collected). |

### Normalization & Optimization Strategy
* **Elimination of Redundancy:** Doctor specialties are stored once in the `Doctor` table, rather than repeated in every appointment record (3NF compliance).
* **Derived Data Policy:** To ensure data integrity, "Total Outstanding" is not a static column but a calculated difference between `total_billed` and `amount_paid`.
* **Relationship Enforcement:** We utilize **ON DELETE RESTRICT** constraints on departments to ensure a department cannot be removed if it still contains active medical staff.

---

## 3. Data Insights (Sample Output)

### Table A: Clinical Encounter Log (Subset)
*Demonstrates the successful JOIN of Patient, Doctor, and Department entities.*

| Patient Name | Practitioner | Specialty | Date | Status |
| :--- | :--- | :--- | :--- | :--- |
| Arjun More | Dr. Rohan Desai | Cardiology | 2025-01-10 | Finalized |
| Sarita Chopra | Dr. Suresh Kumar | General Medicine | 2025-01-12 | Finalized |
| Rajeev Iyer | Dr. Amit Joshi | Neurology | 2025-01-15 | Finalized |

### Table B: Departmental Financial Performance
*Aggregated metrics for administrative review.*

| Department | Revenue Billed | Revenue Realized | Arrears |
| :--- | :--- | :--- | :--- |
| Cardiology | 12,300.00 | 4,300.00 | 8,000.00 |
| General Medicine | 1,500.00 | 1,500.00 | 0.00 |
| Neurology | 1,100.00 | 1,100.00 | 0.00 |

---

## 4. System Constraints & Boundary Conditions

While robust for outpatient tracking, the current schema has identified limitations:
1.  **Inpatient Logistics:** The model lacks `Ward` or `Bed_ID` tracking for long-term stays.
2.  **Diagnostic Services:** Radiology and Pathology results are currently noted as text in `Diagnosis` rather than distinct relational entities.
3.  **Static Pricing:** The system assumes a flat consultation fee; it does not yet support an itemized "Chargemaster" for specific procedures or medications.
4.  **Temporal Consistency:** There is no "Slowly Changing Dimension" (SCD) logic for doctors who might switch departments.

---

## 5. Future Engineering Roadmap

Given additional development cycles, the following features are prioritized:
* **Automated Billing Trigger:** A database trigger to instantiate an `Invoice` record the moment an `Appointment` status is updated to 'Completed'.
* **Pharmacy Integration:** A `Pharmacy_Stock` table that decrements medicine counts when a `Prescription` is filled.
* **Concurrency Control:** Implementation of check constraints to prevent double-booking a doctor for the same time slot.
* **Security Layer:** Introduction of a `User_Roles` table to restrict billing access to accounting staff only.

---

## 6. Scholarly References

* *Database Systems: The Complete Book* (Garcia-Molina, Ullman, & Widom).
* PostgreSQL 16.0 Documentation (Schema Design & Constraints).
* Standardized Medical Data Formats (ICD-10-CM guidelines).
* GECA Computer Science Lab Manual – Experiment 7.

---

**Technical Note:** *Refinements to SQL constraints (specifically the `CHECK` parameters for patient gender and appointment status) were assisted by LLM tools to ensure syntax accuracy. All architectural design decisions and relational mapping are original.*