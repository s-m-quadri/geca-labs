-- ddl.sql
-- Student Management System schema

DROP TABLE IF EXISTS enrollment;
DROP TABLE IF EXISTS course;
DROP TABLE IF EXISTS semester;
DROP TABLE IF EXISTS student;
DROP TABLE IF EXISTS instructor;
DROP TABLE IF EXISTS department;

CREATE TABLE department (
  dept_id INT AUTO_INCREMENT PRIMARY KEY,
  dept_code VARCHAR(10) NOT NULL UNIQUE,
  name VARCHAR(100) NOT NULL,
  building VARCHAR(50)
) ENGINE=InnoDB;

CREATE TABLE instructor (
  instructor_id INT AUTO_INCREMENT PRIMARY KEY,
  first_name VARCHAR(50) NOT NULL,
  last_name VARCHAR(50) NOT NULL,
  email VARCHAR(100) NOT NULL UNIQUE,
  phone VARCHAR(20),
  dept_id INT NOT NULL,
  hire_date DATE,
  FOREIGN KEY (dept_id) REFERENCES department(dept_id)
    ON UPDATE CASCADE
    ON DELETE RESTRICT
) ENGINE=InnoDB;

CREATE TABLE student (
  student_id INT AUTO_INCREMENT PRIMARY KEY,
  first_name VARCHAR(50) NOT NULL,
  last_name VARCHAR(50) NOT NULL,
  email VARCHAR(100) NOT NULL UNIQUE,
  birth_date DATE,
  enrollment_date DATE NOT NULL,
  major_dept_id INT,
  status ENUM('active','inactive','graduated','suspended') NOT NULL DEFAULT 'active',
  FOREIGN KEY (major_dept_id) REFERENCES department(dept_id)
    ON UPDATE CASCADE
    ON DELETE SET NULL
) ENGINE=InnoDB;

CREATE TABLE semester (
  semester_id INT AUTO_INCREMENT PRIMARY KEY,
  term VARCHAR(20) NOT NULL,
  year YEAR NOT NULL,
  start_date DATE NOT NULL,
  end_date DATE NOT NULL,
  UNIQUE KEY uq_semester_term_year (term, year)
) ENGINE=InnoDB;

CREATE TABLE course (
  course_id INT AUTO_INCREMENT PRIMARY KEY,
  course_code VARCHAR(10) NOT NULL UNIQUE,
  title VARCHAR(150) NOT NULL,
  description TEXT,
  credits TINYINT NOT NULL DEFAULT 3,
  dept_id INT NOT NULL,
  instructor_id INT,
  FOREIGN KEY (dept_id) REFERENCES department(dept_id)
    ON UPDATE CASCADE
    ON DELETE RESTRICT,
  FOREIGN KEY (instructor_id) REFERENCES instructor(instructor_id)
    ON UPDATE CASCADE
    ON DELETE SET NULL
) ENGINE=InnoDB;

CREATE TABLE enrollment (
  enrollment_id INT AUTO_INCREMENT PRIMARY KEY,
  student_id INT NOT NULL,
  course_id INT NOT NULL,
  semester_id INT NOT NULL,
  enrollment_date DATE NOT NULL,
  grade ENUM('A','B','C','D','F','I','W') DEFAULT NULL,
  status ENUM('enrolled','completed','dropped') NOT NULL DEFAULT 'enrolled',
  UNIQUE KEY uq_student_course_semester (student_id, course_id, semester_id),
  FOREIGN KEY (student_id) REFERENCES student(student_id)
    ON UPDATE CASCADE
    ON DELETE CASCADE,
  FOREIGN KEY (course_id) REFERENCES course(course_id)
    ON UPDATE CASCADE
    ON DELETE RESTRICT,
  FOREIGN KEY (semester_id) REFERENCES semester(semester_id)
    ON UPDATE CASCADE
    ON DELETE RESTRICT
) ENGINE=InnoDB;
