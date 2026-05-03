CREATE DATABASE hospital_db;
USE hospital_db;

CREATE TABLE patients (
  patient_id INT PRIMARY KEY,
  name VARCHAR(50) NOT NULL,
  age INT,
  gender VARCHAR(10)
);

CREATE TABLE doctors (
  doctor_id INT PRIMARY KEY,
  name VARCHAR(50) NOT NULL,
  specialization VARCHAR(50)
);

CREATE TABLE appointments (
  appointment_id INT PRIMARY KEY,
  patient_id INT,
  doctor_id INT,
  appointment_date DATE,
  FOREIGN KEY (patient_id) REFERENCES patients(patient_id),
  FOREIGN KEY (doctor_id) REFERENCES doctors(doctor_id)
);

CREATE TABLE bills (
  bill_id INT PRIMARY KEY,
  patient_id INT,
  amount DECIMAL(10,2),
  status VARCHAR(20),
  FOREIGN KEY (patient_id) REFERENCES patients(patient_id)
);