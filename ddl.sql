/* Database Setup for Hospital System */
DROP DATABASE IF EXISTS hospital_db;
CREATE DATABASE hospital_db;
USE hospital_db;

/* Table: Department */
CREATE TABLE Department (
    dept_id       INT PRIMARY KEY AUTO_INCREMENT,
    dept_name     VARCHAR(100) NOT NULL,
    location      VARCHAR(100)
);

/* Table: Doctor */
CREATE TABLE Doctor (
    doctor_id       INT PRIMARY KEY AUTO_INCREMENT,
    name            VARCHAR(100) NOT NULL,
    specialization  VARCHAR(100),
    phone           VARCHAR(15),
    dept_id         INT,
    FOREIGN KEY (dept_id) REFERENCES Department(dept_id)
);

/* Table: Patient */
CREATE TABLE Patient (
    patient_id    INT PRIMARY KEY AUTO_INCREMENT,
    name          VARCHAR(100) NOT NULL,
    age           INT,
    gender        VARCHAR(10),
    phone         VARCHAR(15),
    address       VARCHAR(200)
);

/* Table: Appointment */
CREATE TABLE Appointment (
    appt_id       INT PRIMARY KEY AUTO_INCREMENT,
    patient_id    INT,
    doctor_id     INT,
    appt_date     DATE,
    reason        VARCHAR(200),
    status        VARCHAR(20) DEFAULT 'Scheduled',
    FOREIGN KEY (patient_id) REFERENCES Patient(patient_id),
    FOREIGN KEY (doctor_id)  REFERENCES Doctor(doctor_id)
);

/* Table: Bill */
CREATE TABLE Bill (
    bill_id       INT PRIMARY KEY AUTO_INCREMENT,
    patient_id    INT,
    appt_id       INT,
    amount        DECIMAL(10, 2),
    paid          VARCHAR(5) DEFAULT 'No',
    bill_date     DATE,
    FOREIGN KEY (patient_id) REFERENCES Patient(patient_id),
    FOREIGN KEY (appt_id)    REFERENCES Appointment(appt_id)
);