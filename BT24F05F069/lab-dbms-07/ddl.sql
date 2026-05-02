-- Create the database
DROP DATABASE IF EXISTS clinic_db;
CREATE DATABASE clinic_db;
USE clinic_db;

-- Parent table: Medical Specializations
CREATE TABLE specializations (
    spec_id INT AUTO_INCREMENT PRIMARY KEY,
    spec_name VARCHAR(80) NOT NULL
);

-- Child table: Doctors linked to a specialization
CREATE TABLE doctors (
    doc_id INT AUTO_INCREMENT PRIMARY KEY,
    doc_name VARCHAR(80) NOT NULL,
    spec_id INT NOT NULL,
    FOREIGN KEY (spec_id) REFERENCES specializations(spec_id)
);

CREATE OR REPLACE VIEW v_doctor_directory AS
SELECT d.doc_name, s.spec_name 
FROM doctors d
JOIN specializations s ON d.spec_id = s.spec_id;