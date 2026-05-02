-- ============================================================
-- Lab 7: Hospital Management System
-- ddl.sql - Schema Definition
-- ============================================================

DROP DATABASE IF EXISTS hospital_db;
CREATE DATABASE hospital_db;
-- \c hospital_db;

-- -----------------------------------------------
-- 1. DEPARTMENT
-- -----------------------------------------------
CREATE TABLE department (
    dept_id   SERIAL PRIMARY KEY,
    dept_name VARCHAR(80)  NOT NULL UNIQUE,
    location  VARCHAR(100) NOT NULL,
    phone     VARCHAR(20)
);

-- -----------------------------------------------
-- 2. DOCTOR  (belongs to a department)
-- -----------------------------------------------
CREATE TABLE doctor (
    doctor_id    SERIAL PRIMARY KEY,
    first_name   VARCHAR(50) NOT NULL,
    last_name    VARCHAR(50) NOT NULL,
    speciality   VARCHAR(80) NOT NULL,
    email        VARCHAR(100) UNIQUE,
    dept_id      INT NOT NULL REFERENCES department(dept_id) ON DELETE RESTRICT
);

-- -----------------------------------------------
-- 3. PATIENT
-- -----------------------------------------------
CREATE TABLE patient (
    patient_id   SERIAL PRIMARY KEY,
    first_name   VARCHAR(50) NOT NULL,
    last_name    VARCHAR(50) NOT NULL,
    dob          DATE        NOT NULL,
    gender       CHAR(1)     CHECK (gender IN ('M','F','O')),
    phone        VARCHAR(20),
    address      TEXT
);

-- -----------------------------------------------
-- 4. APPOINTMENT  (patient ↔ doctor — chain: appointment → doctor → department)
-- -----------------------------------------------
CREATE TABLE appointment (
    appt_id      SERIAL PRIMARY KEY,
    patient_id   INT  NOT NULL REFERENCES patient(patient_id)  ON DELETE CASCADE,
    doctor_id    INT  NOT NULL REFERENCES doctor(doctor_id)     ON DELETE RESTRICT,
    appt_date    DATE NOT NULL,
    appt_time    TIME NOT NULL,
    status       VARCHAR(20) DEFAULT 'Scheduled'
                 CHECK (status IN ('Scheduled','Completed','Cancelled','No-Show')),
    notes        TEXT
);

-- -----------------------------------------------
-- 5. DIAGNOSIS  (linked to appointment; M:N via junction would be complex—
--    here each appointment can have many diagnosis rows)
-- -----------------------------------------------
CREATE TABLE diagnosis (
    diag_id      SERIAL PRIMARY KEY,
    appt_id      INT          NOT NULL REFERENCES appointment(appt_id) ON DELETE CASCADE,
    icd_code     VARCHAR(10)  NOT NULL,
    description  TEXT         NOT NULL,
    severity     VARCHAR(20)  DEFAULT 'Moderate'
                 CHECK (severity IN ('Mild','Moderate','Severe','Critical'))
);

-- -----------------------------------------------
-- 6. PRESCRIPTION  (linked to appointment)
-- -----------------------------------------------
CREATE TABLE prescription (
    rx_id        SERIAL PRIMARY KEY,
    appt_id      INT         NOT NULL REFERENCES appointment(appt_id) ON DELETE CASCADE,
    medicine     VARCHAR(100) NOT NULL,
    dosage       VARCHAR(50)  NOT NULL,
    duration_days INT         NOT NULL CHECK (duration_days > 0)
);

-- -----------------------------------------------
-- 7. BILL  (one bill per appointment)
-- -----------------------------------------------
CREATE TABLE bill (
    bill_id      SERIAL PRIMARY KEY,
    appt_id      INT          NOT NULL UNIQUE REFERENCES appointment(appt_id) ON DELETE CASCADE,
    amount       NUMERIC(10,2) NOT NULL CHECK (amount >= 0),
    paid         BOOLEAN       DEFAULT FALSE,
    payment_date DATE
);