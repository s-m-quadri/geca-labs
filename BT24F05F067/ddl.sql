-- Hospital Management System
-- DDL File - Table Definitions

-- Drop database if it already exists (clean setup ke liye)
DROP DATABASE IF EXISTS hospital_db;
CREATE DATABASE hospital_db;
USE hospital_db;


-- Table 1: Department
-- Stores different departments in the hospital

CREATE TABLE Department (
    dept_id     INT AUTO_INCREMENT PRIMARY KEY,
    dept_name   VARCHAR(100) NOT NULL,
    location    VARCHAR(100)
);


-- Table 2: Doctor
-- Stores doctor details and their department

CREATE TABLE Doctor (
    doctor_id       INT AUTO_INCREMENT PRIMARY KEY,
    name            VARCHAR(100) NOT NULL,
    specialization  VARCHAR(100),
    phone           VARCHAR(15),
    dept_id         INT,
    FOREIGN KEY (dept_id) REFERENCES Department(dept_id)
);


-- Table 3: Patient
-- Stores patient personal details

CREATE TABLE Patient (
    patient_id  INT AUTO_INCREMENT PRIMARY KEY,
    name        VARCHAR(100) NOT NULL,
    age         INT,
    gender      VARCHAR(10),
    phone       VARCHAR(15),
    address     VARCHAR(200)
);


-- Table 4: Appointment
-- Links patient with a doctor for a visit

CREATE TABLE Appointment (
    appt_id     INT AUTO_INCREMENT PRIMARY KEY,
    patient_id  INT,
    doctor_id   INT,
    appt_date   DATE,
    reason      VARCHAR(200),
    status      VARCHAR(20) DEFAULT 'Scheduled',
    FOREIGN KEY (patient_id) REFERENCES Patient(patient_id),
    FOREIGN KEY (doctor_id)  REFERENCES Doctor(doctor_id)
);


-- Table 5: Bill
-- Stores billing info for each appointment

CREATE TABLE Bill (
    bill_id     INT AUTO_INCREMENT PRIMARY KEY,
    patient_id  INT,
    appt_id     INT,
    amount      DECIMAL(10, 2),
    paid        VARCHAR(5) DEFAULT 'No',
    bill_date   DATE,
    FOREIGN KEY (patient_id) REFERENCES Patient(patient_id),
    FOREIGN KEY (appt_id)    REFERENCES Appointment(appt_id)
);