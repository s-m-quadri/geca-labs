-- ddl.sql: Student Attendance System Schema
-- --------------------------------------

-- Drop tables if they exist (for repeatability)
DROP TABLE IF EXISTS Attendance;
DROP TABLE IF EXISTS Classes;
DROP TABLE IF EXISTS Students;
DROP TABLE IF EXISTS Teachers;
DROP TABLE IF EXISTS Courses;

-- 1. Courses
CREATE TABLE Courses (
    course_id INT AUTO_INCREMENT PRIMARY KEY,
    course_name VARCHAR(100) NOT NULL UNIQUE
);

-- 2. Teachers
CREATE TABLE Teachers (
    teacher_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE
);

-- 3. Classes
CREATE TABLE Classes (
    class_id INT AUTO_INCREMENT PRIMARY KEY,
    class_name VARCHAR(100) NOT NULL,
    teacher_id INT,
    FOREIGN KEY (teacher_id) REFERENCES Teachers(teacher_id)
        ON DELETE SET NULL
);

-- 4. Students
CREATE TABLE Students (
    student_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    course_id INT,
    FOREIGN KEY (course_id) REFERENCES Courses(course_id)
        ON DELETE SET NULL
);

-- 5. Attendance
CREATE TABLE Attendance (
    attendance_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT NOT NULL,
    class_id INT NOT NULL,
    date DATE NOT NULL,
    status ENUM('Present', 'Absent') NOT NULL,
    CONSTRAINT fk_student FOREIGN KEY (student_id) REFERENCES Students(student_id)
        ON DELETE CASCADE,
    CONSTRAINT fk_class FOREIGN KEY (class_id) REFERENCES Classes(class_id)
        ON DELETE CASCADE,
    CONSTRAINT uc_attendance UNIQUE (student_id, class_id, date)
);

-- Indexes for performance
CREATE INDEX idx_attendance_student ON Attendance(student_id);
CREATE INDEX idx_attendance_class ON Attendance(class_id);
CREATE INDEX idx_attendance_date ON Attendance(date);
