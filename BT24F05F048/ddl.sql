DROP DATABASE IF EXISTS hospital_db;
CREATE DATABASE hospital_db;
\c hospital_db;

CREATE TABLE patients (
  patient_id SERIAL PRIMARY KEY,
  name VARCHAR(100),
  age INT,
  gender VARCHAR(10),
  phone VARCHAR(15)
);

CREATE TABLE doctors (
  doctor_id SERIAL PRIMARY KEY,
  name VARCHAR(100),
  specialization VARCHAR(100),
  experience INT
);

CREATE TABLE appointments (
  appointment_id SERIAL PRIMARY KEY,
  patient_id INT REFERENCES patients(patient_id),
  doctor_id INT REFERENCES doctors(doctor_id),
  appointment_date DATE
);

CREATE TABLE treatments (
  treatment_id SERIAL PRIMARY KEY,
  appointment_id INT REFERENCES appointments(appointment_id),
  description TEXT,
  cost INT
);

CREATE TABLE bills (
  bill_id SERIAL PRIMARY KEY,
  treatment_id INT REFERENCES treatments(treatment_id),
  total_amount INT,
  payment_status VARCHAR(20)
);