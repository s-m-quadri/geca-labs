-- Hotel Management System


CREATE DATABASE IF NOT EXISTS hotel_db;
USE hotel_db;

-- Departments in the hotel
CREATE TABLE Departments (
    dept_id    INT PRIMARY KEY AUTO_INCREMENT,
    dept_name  VARCHAR(50) NOT NULL,
    manager    VARCHAR(50)
);

-- Hotel staff
CREATE TABLE Staff (
    staff_id  INT PRIMARY KEY AUTO_INCREMENT,
    dept_id   INT,
    name      VARCHAR(50) NOT NULL,
    role      VARCHAR(30),
    phone     VARCHAR(15),
    salary    DECIMAL(8,2),
    FOREIGN KEY (dept_id) REFERENCES Departments(dept_id)
);

-- Guest details
CREATE TABLE Guests (
    guest_id  INT PRIMARY KEY AUTO_INCREMENT,
    name      VARCHAR(50) NOT NULL,
    email     VARCHAR(50) UNIQUE,
    phone     VARCHAR(15),
    address   TEXT,
    id_proof  VARCHAR(50)  
);

-- Room categories (Standard, Deluxe, Suite)
CREATE TABLE RoomTypes (
    type_id         INT PRIMARY KEY AUTO_INCREMENT,
    type_name       VARCHAR(30) NOT NULL,
    price_per_night DECIMAL(8,2) NOT NULL,
    max_persons     INT DEFAULT 2
);

-- Individual rooms
CREATE TABLE Rooms (
    room_id   INT PRIMARY KEY AUTO_INCREMENT,
    room_no   VARCHAR(10) UNIQUE NOT NULL,
    type_id   INT,
    floor     INT,
    status    VARCHAR(20) DEFAULT 'Available',  -- Available / Occupied / Maintenance
    FOREIGN KEY (type_id) REFERENCES RoomTypes(type_id)
);

-- Room booking
CREATE TABLE Reservations (
    res_id    INT PRIMARY KEY AUTO_INCREMENT,
    guest_id  INT,
    room_id   INT,
    staff_id  INT,
    check_in  DATE NOT NULL,
    check_out DATE NOT NULL,
    status    VARCHAR(20) DEFAULT 'Confirmed',  -- Confirmed / Checked-In / Checked-Out / Cancelled
    FOREIGN KEY (guest_id) REFERENCES Guests(guest_id),
    FOREIGN KEY (room_id)  REFERENCES Rooms(room_id),
    FOREIGN KEY (staff_id) REFERENCES Staff(staff_id)
);

-- Bill for each stay
CREATE TABLE Billing (
    bill_id      INT PRIMARY KEY AUTO_INCREMENT,
    res_id       INT UNIQUE,
    room_charge  DECIMAL(10,2),
    extra_charge DECIMAL(10,2) DEFAULT 0,
    tax_percent  DECIMAL(5,2)  DEFAULT 18.00,
    total        DECIMAL(10,2),
    pay_method   VARCHAR(20),   -- Cash / UPI / Card / Net Banking
    pay_status   VARCHAR(15) DEFAULT 'Pending',
    FOREIGN KEY (res_id) REFERENCES Reservations(res_id)
);

-- Housekeeping tasks
CREATE TABLE Housekeeping (
    task_id   INT PRIMARY KEY AUTO_INCREMENT,
    room_id   INT,
    staff_id  INT,
    task_type VARCHAR(40),  -- Cleaning / Linen Change / Repair
    task_date DATE,
    status    VARCHAR(20) DEFAULT 'Pending',
    FOREIGN KEY (room_id)  REFERENCES Rooms(room_id),
    FOREIGN KEY (staff_id) REFERENCES Staff(staff_id)
);