DROP DATABASE IF EXISTS online_course_db;
CREATE DATABASE online_course_db;
\c online_course_db;

CREATE TABLE instructor (
    instructor_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL
);

CREATE TABLE student (
    student_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL
);

CREATE TABLE course (
    course_id SERIAL PRIMARY KEY,
    title VARCHAR(150) NOT NULL,
    instructor_id INT NOT NULL,
    FOREIGN KEY (instructor_id)
        REFERENCES instructor(instructor_id)
        ON DELETE CASCADE
);

CREATE TABLE enrollment (
    enrollment_id SERIAL PRIMARY KEY,
    student_id INT NOT NULL,
    course_id INT NOT NULL,
    enrollment_date DATE DEFAULT CURRENT_DATE,
    status VARCHAR(20) CHECK (status IN ('active', 'completed')),

    FOREIGN KEY (student_id)
        REFERENCES student(student_id)
        ON DELETE CASCADE,

    FOREIGN KEY (course_id)
        REFERENCES course(course_id)
        ON DELETE CASCADE,

    UNIQUE (student_id, course_id)
);

