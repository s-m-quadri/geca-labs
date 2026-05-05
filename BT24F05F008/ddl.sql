DROP DATABASE IF EXISTS placement_db;
CREATE DATABASE placement_db;
\c placement_db;

-- Students
CREATE TABLE student (
    student_id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    cgpa DECIMAL(3,2),
    branch VARCHAR(50)
);

-- Companies
CREATE TABLE company (
    company_id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    min_cgpa DECIMAL(3,2),
    role VARCHAR(100)
);

-- Applications (junction table: M:N)
CREATE TABLE application (
    app_id SERIAL PRIMARY KEY,
    student_id INT REFERENCES student(student_id) ON DELETE CASCADE,
    company_id INT REFERENCES company(company_id) ON DELETE CASCADE,
    status VARCHAR(20) CHECK (status IN ('Applied','Shortlisted','Rejected'))
);

-- Interview rounds (chain)
CREATE TABLE interview (
    interview_id SERIAL PRIMARY KEY,
    app_id INT REFERENCES application(app_id) ON DELETE CASCADE,
    round_name VARCHAR(50),
    result VARCHAR(20)
);