# Database Design: Hospital Management System (HMS)

## 1. Relational Schema Structure
The system is designed with a normalized relational structure to ensure data integrity and minimize redundancy.

| Table | Primary Key (PK) | Description |
| :--- | :--- | :--- |
| **`department`** | `dept_id` | Stores hospital divisions like Cardiology or Neurology[cite: 1]. |
| **`doctor`** | `doctor_id` | Contains practitioner details assigned to a specific department[cite: 1]. |
| **`patient`** | `patient_id` | Central registry for all admitted or visiting patients[cite: 1]. |
| **`appointment`** | `appt_id` | The transaction hub linking a patient to a doctor at a specific time[cite: 1]. |
| **`diagnosis`** | `diag_id` | Records clinical findings/ICD codes for each appointment[cite: 1]. |
| **`prescription`** | `rx_id` | Details medication and dosage prescribed during a visit[cite: 1]. |
| **`bill`** | `bill_id` | Manages the financial ledger for a specific appointment[cite: 1]. |

---

## 2. Referential Integrity & Foreign Key Chains
To satisfy complex reporting requirements, the schema implements a multi-level Foreign Key (FK) chain[cite: 1]:
*   **Chain Logic:** `diagnosis` → `appointment` → `doctor` → `department`[cite: 1].
*   This structure allows administrators to track clinical outcomes (diagnoses) back to specific hospital departments[cite: 1].

### Entity Relationships & Cardinality
*   **Department to Doctor (1:N):** A department employs many doctors, but a doctor belongs to one department[cite: 1].
*   **Patient to Appointment (1:N):** A single patient can have multiple historical visits[cite: 1].
*   **Appointment to Bill (1:1):** Every individual appointment results in exactly one unique invoice[cite: 1].
*   **Appointment to Diagnosis/Prescription (1:N):** One visit may result in multiple diagnoses or medicine lines[cite: 1].

---

## 3. Data Maintenance Policies (ON DELETE)
Operational rules are enforced via SQL constraints to prevent accidental data loss or orphaned records[cite: 1].

| Constraint | Behavior | Rationale |
| :--- | :--- | :--- |
| **`doctor.dept_id`** | `RESTRICT` | Prevents deleting a department while it still has active staff[cite: 1]. |
| **`appt.patient_id`** | `CASCADE` | If a patient record is purged, all associated history is removed[cite: 1]. |
| **`bill.appt_id`** | `CASCADE` | Financial and clinical notes are deleted if the appointment record is removed[cite: 1]. |

---

## 4. Normalization Compliance
The schema adheres to **Third Normal Form (3NF)** standards[cite: 1]:
*   **1NF:** Atomic values only; no comma-separated lists for medicines or phone numbers[cite: 1].
*   **2NF:** Every non-key column is fully dependent on the primary key[cite: 1].
*   **3NF:** Eliminated transitive dependencies; e.g., department names are stored only in the `department` table and referenced via ID[cite: 1].

---

## 5. Visual Entity Relationship (ER) Concept
```text
[department] --< [doctor] --< [appointment] >-- [patient]
                                |
                +---------------+---------------+
                |               |               |
           [diagnosis]    [prescription]      [bill]