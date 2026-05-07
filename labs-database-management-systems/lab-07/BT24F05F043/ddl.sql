CREATE DATABASE hostel_db;
\c hostel_db;

CREATE TABLE hostel (
  hostel_id SERIAL PRIMARY KEY,
  hostel_name VARCHAR(100) NOT NULL,
  location VARCHAR(100)
);

CREATE TABLE room (
  room_id SERIAL PRIMARY KEY,
  hostel_id INT,
  room_number VARCHAR(10),
  capacity INT,
  FOREIGN KEY (hostel_id) REFERENCES hostel(hostel_id)
);

CREATE TABLE student (
  student_id SERIAL PRIMARY KEY,
  name VARCHAR(100),
  email VARCHAR(100),
  room_id INT,
  FOREIGN KEY (room_id) REFERENCES room(room_id)
);

CREATE TABLE fee (
  fee_id SERIAL PRIMARY KEY,
  student_id INT,
  amount DECIMAL(10,2),
  status VARCHAR(20),
  paid_date DATE,
  FOREIGN KEY (student_id) REFERENCES student(student_id)
);

CREATE TABLE complaint (
  complaint_id SERIAL PRIMARY KEY,
  student_id INT,
  description TEXT,
  status VARCHAR(20),
  created_at DATE,
  FOREIGN KEY (student_id) REFERENCES student(student_id)
);