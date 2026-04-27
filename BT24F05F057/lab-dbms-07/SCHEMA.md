# Schema — Hospital Management System

## Domain

A small private hospital needs to track departments, doctors, patients,
appointments, diagnoses, prescriptions, and bills.

---

## Tables & Primary Keys

| Table          | PK            | Description                                    |
|----------------|---------------|------------------------------------------------|
| `department`   | `dept_id`     | Hospital departments (Cardiology, Neurology…)  |
| `doctor`       | `doctor_id`   | Doctors, each assigned to one department       |
| `patient`      | `patient_id`  | Registered patients                            |
| `appointment`  | `appt_id`     | Scheduled/completed visits (patient ↔ doctor) |
| `diagnosis`    | `diag_id`     | ICD-coded diagnoses per appointment            |
| `prescription` | `rx_id`       | Medicines prescribed per appointment           |
| `bill`         | `bill_id`     | One bill per appointment                       |

---

## Foreign Key Chain (A → B → C)

```
department
    ↑ (dept_id)
doctor
    ↑ (doctor_id)
appointment ← patient (patient_id)
    ↑ (appt_id)         ↑ (appt_id)         ↑ (appt_id)
diagnosis           prescription            bill
```

The chain `diagnosis → appointment → doctor → department` satisfies the
≥ 1 FK chain requirement (3 levels deep).

---

## Relationships & Cardinality

| Relationship                       | Cardinality | Notes                              |
|------------------------------------|-------------|------------------------------------|
| Department → Doctor                | 1 : N       | A dept. has many doctors           |
| Doctor → Appointment               | 1 : N       | A doctor has many appointments     |
| Patient → Appointment              | 1 : N       | A patient can revisit              |
| Appointment → Diagnosis            | 1 : N       | Multiple diagnoses per visit       |
| Appointment → Prescription         | 1 : N       | Multiple medicines per visit       |
| Appointment → Bill                 | 1 : 1       | Exactly one bill per appointment   |

---

## ON DELETE Behaviour

| FK                              | Behaviour   | Reasoning                                      |
|---------------------------------|-------------|------------------------------------------------|
| `doctor.dept_id`                | RESTRICT    | Cannot delete a dept with active doctors       |
| `appointment.patient_id`        | CASCADE     | Deleting a patient removes all their data      |
| `appointment.doctor_id`         | RESTRICT    | Protect appointment history                    |
| `diagnosis.appt_id`             | CASCADE     | Diagnoses belong to the appointment            |
| `prescription.appt_id`          | CASCADE     | Prescriptions belong to the appointment        |
| `bill.appt_id`                  | CASCADE     | Bills belong to the appointment                |

---

## Normalisation Notes

- **1NF** – Every column stores a single atomic value. Phone numbers, addresses
  are single fields; multiple medicines use separate rows in `prescription`.
- **2NF** – No partial dependencies (all non-key columns depend on the full PK).
- **3NF** – Doctor's department is stored via FK (`dept_id`), not by duplicating
  `dept_name` in the `doctor` table; bill amount is not derived from prescription
  duration (billing is independent).

---

## ER Diagram (Text)

```
[department] --< [doctor] --< [appointment] >-- [patient]
                                   |
                    +--------------+---------------+
                    |              |               |
               [diagnosis]  [prescription]      [bill]
```

Crow's foot notation: `--<` = one-to-many, `>--` = many-to-one.