CREATE DATABASE IF NOT EXISTS hostel_db;
USE hostel_db;

-- STUDENTS
CREATE TABLE students (
    student_id INT PRIMARY KEY AUTO_INCREMENT,
    roll_no VARCHAR(20) UNIQUE,
    name VARCHAR(100),
    branch VARCHAR(50),
    year INT,
    contact_no VARCHAR(15),
    address VARCHAR(255)
);

-- ROOMS
CREATE TABLE rooms (
    room_id INT PRIMARY KEY AUTO_INCREMENT,
    room_no VARCHAR(10),
    floor INT,
    capacity INT
);

-- ROOM ALLOTMENT
CREATE TABLE room_allotment (
    allotment_id INT PRIMARY KEY AUTO_INCREMENT,
    student_id INT,
    room_id INT,
    allot_date DATE,
    vacate_date DATE,

    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (room_id) REFERENCES rooms(room_id)
);

-- OFFICIALS
CREATE TABLE officials (
    official_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    role VARCHAR(20), -- warden / rector
    contact VARCHAR(15)
);

-- COMPLAINTS
CREATE TABLE complaints (
    complaint_id INT PRIMARY KEY AUTO_INCREMENT,
    student_id INT,
    complaint_text VARCHAR(255),
    complaint_date DATE,
    status VARCHAR(20),

    FOREIGN KEY (student_id) REFERENCES students(student_id)
);