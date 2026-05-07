-- Hospital Database Schema
-- Simple project with Department, Doctor, Patient, Appointment

CREATE TABLE Department (
    dept_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE,
    location VARCHAR(100)
);

CREATE TABLE Doctor (
    doc_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    dept_id INT,
    specialization VARCHAR(100),
    FOREIGN KEY (dept_id) REFERENCES Department(dept_id) ON DELETE SET NULL
);

CREATE TABLE Patient (
    pat_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    dob DATE,
    address TEXT
);

CREATE TABLE Appointment (
    appt_id INT AUTO_INCREMENT PRIMARY KEY,
    pat_id INT,
    doc_id INT,
    appt_date DATE NOT NULL,
    appt_time TIME,
    reason TEXT,
    FOREIGN KEY (pat_id) REFERENCES Patient(pat_id) ON DELETE CASCADE,
    FOREIGN KEY (doc_id) REFERENCES Doctor(doc_id) ON DELETE CASCADE
);