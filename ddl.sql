-- ==========================================
-- HOSPITAL MANAGEMENT SYSTEM SCHEMA
-- ==========================================

DROP DATABASE IF EXISTS hospital_db;
CREATE DATABASE hospital_db;
USE hospital_db;

-- 1. Department Table
CREATE TABLE Department (
    dept_id INT AUTO_INCREMENT PRIMARY KEY,
    dept_name VARCHAR(100) NOT NULL,
    location VARCHAR(100)
);

-- 2. Doctor Table
CREATE TABLE Doctor (
    doctor_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    specialization VARCHAR(100),
    phone VARCHAR(15),
    dept_id INT,
    FOREIGN KEY (dept_id) REFERENCES Department(dept_id)
);

-- 3. Patient Table
CREATE TABLE Patient (
    patient_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    age INT,
    gender VARCHAR(10),
    phone VARCHAR(15),
    address VARCHAR(200)
);

-- 4. Appointment Table
CREATE TABLE Appointment (
    appt_id INT AUTO_INCREMENT PRIMARY KEY,
    patient_id INT,
    doctor_id INT,
    appt_date DATE,
    reason VARCHAR(200),
    status VARCHAR(20) DEFAULT 'Scheduled',
    FOREIGN KEY (patient_id) REFERENCES Patient(patient_id),
    FOREIGN KEY (doctor_id) REFERENCES Doctor(doctor_id)
);

-- 5. Bill Table
CREATE TABLE Bill (
    bill_id INT AUTO_INCREMENT PRIMARY KEY,
    patient_id INT,
    appt_id INT,
    amount DECIMAL(10, 2),
    paid VARCHAR(5) DEFAULT 'No',
    bill_date DATE,
    FOREIGN KEY (patient_id) REFERENCES Patient(patient_id),
    FOREIGN KEY (appt_id) REFERENCES Appointment(appt_id)
);