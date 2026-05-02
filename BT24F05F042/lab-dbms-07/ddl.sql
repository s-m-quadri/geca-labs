CREATE TABLE students (
  student_id INT PRIMARY KEY,
  name VARCHAR(50),
  department VARCHAR(50)
);

CREATE TABLE faculty (
  faculty_id INT PRIMARY KEY,
  name VARCHAR(50),
  department VARCHAR(50)
);

CREATE TABLE courses (
  course_id INT PRIMARY KEY,
  course_name VARCHAR(50),
  faculty_id INT,
  FOREIGN KEY (faculty_id) REFERENCES faculty(faculty_id)
);

CREATE TABLE enrollments (
  student_id INT,
  course_id INT,
  grade VARCHAR(2),
  PRIMARY KEY (student_id, course_id),
  FOREIGN KEY (student_id) REFERENCES students(student_id),
  FOREIGN KEY (course_id) REFERENCES courses(course_id)
);