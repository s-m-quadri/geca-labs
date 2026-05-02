DROP DATABASE IF EXISTS hospital_db;
CREATE DATABASE hospital_db;
\c hospital_db;

CREATE TABLE patients (
  patient_id SERIAL PRIMARY KEY,
  name VARCHAR(100)
);

CREATE TABLE doctors (
  doctor_id SERIAL PRIMARY KEY,
  name VARCHAR(100)
);

CREATE TABLE appointments (
  appointment_id SERIAL PRIMARY KEY,
  patient_id INT REFERENCES patients(patient_id),
  doctor_id INT REFERENCES doctors(doctor_id)
);