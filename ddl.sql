CREATE DATABASE IF NOT EXISTS hotel_corp_db;
USE hotel_corp_db;

CREATE TABLE tbl_departments (
    id INT PRIMARY KEY AUTO_INCREMENT,
    department_name VARCHAR(50) NOT NULL,
    head_manager VARCHAR(50)
);

CREATE TABLE tbl_employees (
    emp_id INT PRIMARY KEY AUTO_INCREMENT,
    dept_id INT,
    full_name VARCHAR(50) NOT NULL,
    job_title VARCHAR(30),
    contact_no VARCHAR(15),
    base_salary DECIMAL(8,2),
    FOREIGN KEY (dept_id) REFERENCES tbl_departments(id)
);

CREATE TABLE tbl_guests (
    guest_id INT PRIMARY KEY AUTO_INCREMENT,
    full_name VARCHAR(50) NOT NULL,
    email_address VARCHAR(50) UNIQUE,
    contact_no VARCHAR(15),
    home_address TEXT,
    identity_document VARCHAR(50)  
);

CREATE TABLE tbl_room_categories (
    category_id INT PRIMARY KEY AUTO_INCREMENT,
    category_name VARCHAR(30) NOT NULL,
    rate_per_night DECIMAL(8,2) NOT NULL,
    capacity INT DEFAULT 2
);

CREATE TABLE tbl_rooms (
    room_id INT PRIMARY KEY AUTO_INCREMENT,
    room_number VARCHAR(10) UNIQUE NOT NULL,
    category_id INT,
    floor_level INT,
    current_status VARCHAR(20) DEFAULT 'Available',
    FOREIGN KEY (category_id) REFERENCES tbl_room_categories(category_id)
);

CREATE TABLE tbl_bookings (
    booking_id INT PRIMARY KEY AUTO_INCREMENT,
    guest_id INT,
    room_id INT,
    emp_id INT,
    check_in_date DATE NOT NULL,
    check_out_date DATE NOT NULL,
    booking_status VARCHAR(20) DEFAULT 'Confirmed',
    FOREIGN KEY (guest_id) REFERENCES tbl_guests(guest_id),
    FOREIGN KEY (room_id) REFERENCES tbl_rooms(room_id),
    FOREIGN KEY (emp_id) REFERENCES tbl_employees(emp_id)
);

CREATE TABLE tbl_invoices (
    invoice_id INT PRIMARY KEY AUTO_INCREMENT,
    booking_id INT UNIQUE,
    room_fees DECIMAL(10,2),
    additional_fees DECIMAL(10,2) DEFAULT 0,
    tax_rate DECIMAL(5,2) DEFAULT 18.00,
    grand_total DECIMAL(10,2),
    payment_mode VARCHAR(20),
    payment_status VARCHAR(15) DEFAULT 'Pending',
    FOREIGN KEY (booking_id) REFERENCES tbl_bookings(booking_id)
);