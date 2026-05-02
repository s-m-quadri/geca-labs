-- Q1: Students and companies they applied to
SELECT s.name, c.name AS company
FROM student s
JOIN application a ON s.student_id = a.student_id
JOIN company c ON a.company_id = c.company_id;

-- Q2: Count applications per student
SELECT s.name, COUNT(a.app_id) AS total_apps
FROM student s
LEFT JOIN application a ON s.student_id = a.student_id
GROUP BY s.name;

-- Q3: Students shortlisted in companies
SELECT s.name, c.name
FROM application a
JOIN student s ON a.student_id = s.student_id
JOIN company c ON a.company_id = c.company_id
WHERE a.status = 'Shortlisted';

-- Q4: Companies with CGPA > 7 requirement
SELECT name FROM company WHERE min_cgpa > 7;

-- Q5: Students eligible for Google (business logic)
-- "Which students meet Google's CGPA criteria?"
SELECT s.name
FROM student s
WHERE s.cgpa >= (
    SELECT min_cgpa FROM company WHERE name = 'Google'
);

-- Q6: Total shortlisted students per company
SELECT c.name, COUNT(*) 
FROM company c
JOIN application a ON c.company_id = a.company_id
WHERE a.status = 'Shortlisted'
GROUP BY c.name;

-- Q7: Create view for eligible applications
CREATE VIEW eligible_students AS
SELECT s.name, c.name AS company
FROM student s, company c
WHERE s.cgpa >= c.min_cgpa;

-- Q8: Query from view
SELECT * FROM eligible_students;

-- Q9: Students who cleared all interview rounds (advanced)
SELECT s.name
FROM student s
JOIN application a ON s.student_id = a.student_id
JOIN interview i ON a.app_id = i.app_id
GROUP BY s.name, a.app_id
HAVING COUNT(*) = SUM(CASE WHEN i.result = 'Pass' THEN 1 ELSE 0 END);