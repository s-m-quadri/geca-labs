-- Defence Staff Management System - Database Schema (DDL)
-- This schema manages defence staff, their qualifications, training, and assignments

-- Create database
CREATE DATABASE IF NOT EXISTS defence_staff_mgmt;
USE defence_staff_mgmt;

-- ============================================================================
-- Table 1: Ranks
-- Lookup table for military/defence ranks (e.g., Officer, Soldier, Captain)
-- ============================================================================
CREATE TABLE IF NOT EXISTS ranks (
    rank_id INT PRIMARY KEY AUTO_INCREMENT,
    rank_name VARCHAR(50) NOT NULL UNIQUE,
    seniority_level INT NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- ============================================================================
-- Table 2: Departments
-- Lookup table for defence departments (Infantry, Aviation, Intelligence, etc.)
-- ============================================================================
CREATE TABLE IF NOT EXISTS departments (
    dept_id INT PRIMARY KEY AUTO_INCREMENT,
    dept_name VARCHAR(100) NOT NULL UNIQUE,
    description TEXT,
    location VARCHAR(100),
    head_count INT DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- ============================================================================
-- Table 3: Qualifications
-- Lookup table for staff qualifications (Pilot's License, Weapons Training, etc.)
-- ============================================================================
CREATE TABLE IF NOT EXISTS qualifications (
    qual_id INT PRIMARY KEY AUTO_INCREMENT,
    qual_name VARCHAR(100) NOT NULL UNIQUE,
    description TEXT,
    renewal_months INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- ============================================================================
-- Table 4: Staff (Main entity)
-- FK Chain: DEPARTMENTS -> STAFF
-- ============================================================================
CREATE TABLE IF NOT EXISTS staff (
    staff_id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(10),
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    date_of_birth DATE NOT NULL,
    rank_id INT NOT NULL,
    dept_id INT NOT NULL,
    service_start_date DATE NOT NULL,
    status ENUM('active', 'inactive', 'on_leave', 'retired') DEFAULT 'active',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (rank_id) REFERENCES ranks(rank_id),
    FOREIGN KEY (dept_id) REFERENCES departments(dept_id),
    UNIQUE KEY unique_staff (first_name, last_name, date_of_birth)
);

-- ============================================================================
-- Table 5: Staff_Qualifications (Junction table for M:N relationship)
-- FK Chain: STAFF -> STAFF_QUALIFICATIONS -> QUALIFICATIONS
-- ============================================================================
CREATE TABLE IF NOT EXISTS staff_qualifications (
    staff_qual_id INT PRIMARY KEY AUTO_INCREMENT,
    staff_id INT NOT NULL,
    qual_id INT NOT NULL,
    acquired_date DATE NOT NULL,
    expiry_date DATE,
    certification_level ENUM('basic', 'intermediate', 'advanced', 'expert') DEFAULT 'basic',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (staff_id) REFERENCES staff(staff_id) ON DELETE CASCADE,
    FOREIGN KEY (qual_id) REFERENCES qualifications(qual_id),
    UNIQUE KEY unique_qualification (staff_id, qual_id)
);

-- ============================================================================
-- Table 6: Assignments
-- FK Chain: STAFF -> ASSIGNMENTS (Assignments depend on Staff)
-- Tracks current and historical assignments/roles
-- ============================================================================
CREATE TABLE IF NOT EXISTS assignments (
    assignment_id INT PRIMARY KEY AUTO_INCREMENT,
    staff_id INT NOT NULL,
    assignment_title VARCHAR(100) NOT NULL,
    description TEXT,
    start_date DATE NOT NULL,
    end_date DATE,
    is_current BOOLEAN DEFAULT TRUE,
    priority ENUM('low', 'medium', 'high', 'critical') DEFAULT 'medium',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (staff_id) REFERENCES staff(staff_id) ON DELETE CASCADE,
    INDEX idx_staff_current (staff_id, is_current)
);

-- ============================================================================
-- Table 7: Training_Records
-- Tracks all training completed by staff members
-- ============================================================================
CREATE TABLE IF NOT EXISTS training_records (
    training_id INT PRIMARY KEY AUTO_INCREMENT,
    staff_id INT NOT NULL,
    qual_id INT NOT NULL,
    training_type ENUM('formal', 'on_the_job', 'workshop', 'certification') NOT NULL,
    completion_date DATE NOT NULL,
    completion_percentage INT CHECK (completion_percentage >= 0 AND completion_percentage <= 100),
    trainer_name VARCHAR(100),
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (staff_id) REFERENCES staff(staff_id) ON DELETE CASCADE,
    FOREIGN KEY (qual_id) REFERENCES qualifications(qual_id)
);

-- Create indexes for performance
CREATE INDEX idx_staff_rank ON staff(rank_id);
CREATE INDEX idx_staff_dept ON staff(dept_id);
CREATE INDEX idx_staff_status ON staff(status);
CREATE INDEX idx_assignments_start ON assignments(start_date);
CREATE INDEX idx_training_completion ON training_records(completion_date);
