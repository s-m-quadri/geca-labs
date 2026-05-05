DROP DATABASE IF EXISTS hostel_db;
CREATE DATABASE hostel_db;
USE hostel_db;

-- Table: Hostels
CREATE TABLE hostels (
  hostel_id INT AUTO_INCREMENT PRIMARY KEY,
  hostel_name VARCHAR(50) NOT NULL UNIQUE,
  address VARCHAR(100),
  total_rooms INT NOT NULL
);

-- Table: Rooms
CREATE TABLE rooms (
  room_id INT AUTO_INCREMENT PRIMARY KEY,
  hostel_id INT NOT NULL,
  room_number VARCHAR(10) NOT NULL,
  capacity INT NOT NULL,
  status VARCHAR(20) DEFAULT 'Available',
  FOREIGN KEY (hostel_id) REFERENCES hostels(hostel_id)
);

-- Table: Students (Residents)
CREATE TABLE students (
  student_id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(50) NOT NULL,
  email VARCHAR(50) NOT NULL UNIQUE,
  phone VARCHAR(15),
  enrollment_date DATE NOT NULL
);

-- Table: Allocations (Room Assignments)
CREATE TABLE allocations (
  allocation_id INT AUTO_INCREMENT PRIMARY KEY,
  room_id INT NOT NULL,
  student_id INT NOT NULL,
  check_in_date DATE NOT NULL,
  check_out_date DATE,
  status VARCHAR(20) DEFAULT 'Active',
  FOREIGN KEY (room_id) REFERENCES rooms(room_id),
  FOREIGN KEY (student_id) REFERENCES students(student_id)
);

-- Table: Bills
CREATE TABLE bills (
  bill_id INT AUTO_INCREMENT PRIMARY KEY,
  student_id INT NOT NULL,
  allocation_id INT,
  amount DECIMAL(10,2) NOT NULL,
  bill_date DATE NOT NULL,
  status VARCHAR(20) DEFAULT 'Pending',
  FOREIGN KEY (student_id) REFERENCES students(student_id),
  FOREIGN KEY (allocation_id) REFERENCES allocations(allocation_id)
);
