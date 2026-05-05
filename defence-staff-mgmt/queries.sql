-- Defence Staff Management System - Queries
-- Non-trivial queries for defence staff management operations

USE defence_staff_mgmt;

-- ============================================================================
-- QUERY 1: Multi-table JOIN - Staff with their rank, department, and current assignments
-- Shows: Staff member details, their rank, department, and active assignments
-- ============================================================================
SELECT 
    s.staff_id,
    CONCAT(s.title, ' ', s.first_name, ' ', s.last_name) AS staff_name,
    r.rank_name,
    d.dept_name,
    a.assignment_title,
    a.priority,
    a.start_date
FROM staff s
JOIN ranks r ON s.rank_id = r.rank_id
JOIN departments d ON s.dept_id = d.dept_id
LEFT JOIN assignments a ON s.staff_id = a.staff_id AND a.is_current = TRUE
WHERE s.status = 'active'
ORDER BY s.staff_id;

-- ============================================================================
-- QUERY 2: GROUP BY with HAVING - Count staff per department with more than 2 members
-- Business Question: Which departments have more than 2 active staff members?
-- ============================================================================
SELECT 
    d.dept_name,
    d.location,
    COUNT(s.staff_id) AS active_staff_count,
    AVG(r.seniority_level) AS avg_seniority_level
FROM departments d
JOIN staff s ON d.dept_id = s.dept_id
JOIN ranks r ON s.rank_id = r.rank_id
WHERE s.status = 'active'
GROUP BY d.dept_id, d.dept_name, d.location
HAVING COUNT(s.staff_id) > 2
ORDER BY active_staff_count DESC;

-- ============================================================================
-- QUERY 3: Subquery - Staff members with expiring certifications in next 6 months
-- Business Question: Which staff members have qualifications expiring soon?
-- ============================================================================
SELECT 
    s.staff_id,
    CONCAT(s.first_name, ' ', s.last_name) AS staff_name,
    r.rank_name,
    q.qual_name,
    sq.expiry_date,
    DATEDIFF(sq.expiry_date, CURDATE()) AS days_until_expiry
FROM staff s
JOIN ranks r ON s.rank_id = r.rank_id
JOIN staff_qualifications sq ON s.staff_id = sq.staff_id
JOIN qualifications q ON sq.qual_id = q.qual_id
WHERE sq.expiry_date BETWEEN CURDATE() AND DATE_ADD(CURDATE(), INTERVAL 6 MONTH)
    AND s.status IN ('active', 'on_leave')
ORDER BY sq.expiry_date ASC;

-- ============================================================================
-- QUERY 4: CREATE VIEW and SELECT - Expert-level staff by department
-- Shows all staff with expert-level certifications and their expertise areas
-- ============================================================================
CREATE OR REPLACE VIEW expert_staff_view AS
SELECT 
    s.staff_id,
    CONCAT(s.first_name, ' ', s.last_name) AS staff_name,
    r.rank_name,
    d.dept_name,
    q.qual_name,
    sq.certification_level,
    sq.acquired_date
FROM staff s
JOIN ranks r ON s.rank_id = r.rank_id
JOIN departments d ON s.dept_id = d.dept_id
JOIN staff_qualifications sq ON s.staff_id = sq.staff_id
JOIN qualifications q ON sq.qual_id = q.qual_id
WHERE sq.certification_level = 'expert' AND s.status = 'active';

-- Display results from the view
SELECT * FROM expert_staff_view
ORDER BY rank_name DESC, staff_name;

-- ============================================================================
-- QUERY 5: Complex JOIN with aggregates - Training completion statistics by staff
-- Shows staff members with their training count and average completion percentage
-- ============================================================================
SELECT 
    s.staff_id,
    CONCAT(s.title, ' ', s.first_name, ' ', s.last_name) AS staff_name,
    r.rank_name,
    d.dept_name,
    COUNT(tr.training_id) AS total_trainings_completed,
    ROUND(AVG(tr.completion_percentage), 2) AS avg_completion_percentage,
    MIN(tr.completion_date) AS first_training_date,
    MAX(tr.completion_date) AS latest_training_date
FROM staff s
JOIN ranks r ON s.rank_id = r.rank_id
JOIN departments d ON s.dept_id = d.dept_id
LEFT JOIN training_records tr ON s.staff_id = tr.staff_id
GROUP BY s.staff_id, s.title, s.first_name, s.last_name, r.rank_name, d.dept_name
ORDER BY COUNT(tr.training_id) DESC;

-- ============================================================================
-- QUERY 6: Nested subquery - Staff with more qualifications than department average
-- Business Question: Who has above-average qualifications for their department?
-- ============================================================================
SELECT 
    s.staff_id,
    CONCAT(s.first_name, ' ', s.last_name) AS staff_name,
    COUNT(sq.staff_qual_id) AS qualification_count,
    d.dept_name
FROM staff s
JOIN departments d ON s.dept_id = d.dept_id
LEFT JOIN staff_qualifications sq ON s.staff_id = sq.staff_id
GROUP BY s.staff_id, s.first_name, s.last_name, d.dept_id, d.dept_name
HAVING COUNT(sq.staff_qual_id) > (
    SELECT AVG(qual_count)
    FROM (
        SELECT COUNT(staff_qual_id) AS qual_count
        FROM staff_qualifications
        GROUP BY staff_id
    ) AS dept_avg
)
ORDER BY qualification_count DESC;

-- ============================================================================
-- QUERY 7: Multiple JOINs with business logic - Active high-priority assignments
-- Shows staff assigned to critical/high-priority missions with military rank
-- ============================================================================
SELECT 
    a.assignment_id,
    CONCAT(s.title, ' ', s.first_name, ' ', s.last_name) AS staff_name,
    r.rank_name,
    a.assignment_title,
    a.description,
    a.priority,
    DATEDIFF(CURDATE(), a.start_date) AS days_in_assignment,
    s.status AS staff_status
FROM assignments a
JOIN staff s ON a.staff_id = s.staff_id
JOIN ranks r ON s.rank_id = r.rank_id
WHERE a.is_current = TRUE 
    AND a.priority IN ('high', 'critical')
    AND s.status IN ('active', 'on_leave')
ORDER BY a.priority DESC, a.start_date ASC;

-- ============================================================================
-- QUERY 8: Window function / Advanced aggregate - Rank staff by seniority & experience
-- Shows staff ranked by their seniority level and years of service
-- ============================================================================
SELECT 
    s.staff_id,
    CONCAT(s.title, ' ', s.first_name, ' ', s.last_name) AS staff_name,
    r.rank_name,
    r.seniority_level,
    d.dept_name,
    YEAR(CURDATE()) - YEAR(s.service_start_date) AS years_of_service,
    ROW_NUMBER() OVER (PARTITION BY s.dept_id ORDER BY r.seniority_level DESC, s.service_start_date ASC) AS rank_in_dept
FROM staff s
JOIN ranks r ON s.rank_id = r.rank_id
JOIN departments d ON s.dept_id = d.dept_id
WHERE s.status = 'active'
ORDER BY d.dept_id, rank_in_dept ASC;

-- ============================================================================
-- QUERY 9: Qualification availability analysis - Departments needing specific skills
-- Business Question: Which departments are lacking in specific qualifications?
-- ============================================================================
SELECT 
    d.dept_name,
    q.qual_name,
    COUNT(DISTINCT sq.staff_id) AS staff_with_qualification,
    d.head_count AS total_staff,
    ROUND((COUNT(DISTINCT sq.staff_id) / d.head_count) * 100, 2) AS coverage_percentage
FROM departments d
CROSS JOIN qualifications q
LEFT JOIN staff s ON d.dept_id = s.dept_id AND s.status = 'active'
LEFT JOIN staff_qualifications sq ON s.staff_id = sq.staff_id AND q.qual_id = sq.qual_id
GROUP BY d.dept_id, d.dept_name, d.head_count, q.qual_id, q.qual_name
HAVING COUNT(DISTINCT sq.staff_id) > 0
ORDER BY d.dept_name, coverage_percentage DESC;

-- ============================================================================
-- QUERY 10: Assignment history and transition analysis
-- Shows staff assignment history including past and current assignments
-- ============================================================================
SELECT 
    s.staff_id,
    CONCAT(s.first_name, ' ', s.last_name) AS staff_name,
    a.assignment_title,
    a.description,
    a.start_date,
    a.end_date,
    CASE 
        WHEN a.is_current = TRUE THEN 'CURRENT'
        WHEN a.end_date IS NULL THEN 'ONGOING'
        ELSE CONCAT('ENDED (', DATEDIFF(a.end_date, a.start_date), ' days)')
    END AS assignment_status,
    a.priority,
    ROW_NUMBER() OVER (PARTITION BY s.staff_id ORDER BY a.start_date DESC) AS assignment_sequence
FROM staff s
JOIN assignments a ON s.staff_id = a.staff_id
WHERE s.status IN ('active', 'retired', 'on_leave')
ORDER BY s.staff_id, a.start_date DESC;

-- ============================================================================
-- Additional useful queries for operational management
-- ============================================================================

-- QUERY 11: Staff on leave status check
SELECT 
    s.staff_id,
    CONCAT(s.first_name, ' ', s.last_name) AS staff_name,
    r.rank_name,
    d.dept_name,
    s.status,
    COUNT(a.assignment_id) AS active_assignments_count
FROM staff s
JOIN ranks r ON s.rank_id = r.rank_id
JOIN departments d ON s.dept_id = d.dept_id
LEFT JOIN assignments a ON s.staff_id = a.staff_id AND a.is_current = TRUE
WHERE s.status = 'on_leave'
GROUP BY s.staff_id, s.first_name, s.last_name, r.rank_name, d.dept_name, s.status;

-- QUERY 12: New staff orientation checklist - Staff in first 6 months of service
SELECT 
    s.staff_id,
    CONCAT(s.title, ' ', s.first_name, ' ', s.last_name) AS staff_name,
    r.rank_name,
    d.dept_name,
    s.service_start_date,
    DATEDIFF(CURDATE(), s.service_start_date) AS days_of_service,
    COUNT(sq.staff_qual_id) AS qualifications_acquired,
    COUNT(tr.training_id) AS trainings_completed
FROM staff s
JOIN ranks r ON s.rank_id = r.rank_id
JOIN departments d ON s.dept_id = d.dept_id
LEFT JOIN staff_qualifications sq ON s.staff_id = sq.staff_id
LEFT JOIN training_records tr ON s.staff_id = tr.staff_id
WHERE DATEDIFF(CURDATE(), s.service_start_date) < 180 AND s.status = 'active'
GROUP BY s.staff_id, s.title, s.first_name, s.last_name, r.rank_name, d.dept_name, s.service_start_date
ORDER BY s.service_start_date DESC;
