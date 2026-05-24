-- Q1: Show tokens with user + service (JOIN)
SELECT u.name, s.service_name, t.token_number, t.status
FROM token t
JOIN user_table u ON t.user_id = u.user_id
JOIN service s ON t.service_id = s.service_id;

-- Q2: Count tokens per service
SELECT s.service_name, COUNT(t.token_id) AS total_tokens
FROM service s
LEFT JOIN token t ON s.service_id = t.service_id
GROUP BY s.service_name;

-- Q3: Services with more than 2 tokens
SELECT s.service_name, COUNT(*)
FROM service s
JOIN token t ON s.service_id = t.service_id
GROUP BY s.service_name
HAVING COUNT(*) > 2;

-- Q4: Users currently waiting
SELECT u.name, t.token_number
FROM token t
JOIN user_table u ON t.user_id = u.user_id
WHERE t.status = 'waiting';

-- Q5: Subquery → users who completed service
SELECT name
FROM user_table
WHERE user_id IN (
    SELECT user_id FROM token WHERE status = 'completed'
);

-- Q6: Latest token issued
SELECT * FROM token
ORDER BY created_at DESC
LIMIT 1;

-- Q7: Create VIEW
CREATE VIEW active_queue AS
SELECT u.name, s.service_name, t.token_number
FROM token t
JOIN user_table u ON t.user_id = u.user_id
JOIN service s ON t.service_id = s.service_id
WHERE t.status = 'waiting';

-- Q8: Use VIEW
SELECT * FROM active_queue;

-- Q9: Business Question
-- Which service has highest demand?
SELECT s.service_name, COUNT(*) AS total
FROM token t
JOIN service s ON t.service_id = s.service_id
GROUP BY s.service_name
ORDER BY total DESC
LIMIT 1;