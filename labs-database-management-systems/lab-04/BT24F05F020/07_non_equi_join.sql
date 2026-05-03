-- Task 7: Non-equi join — pairs of staff where person A joined **strictly before** person B (same department)

USE join_lab;

SELECT a.name AS joined_earlier,
       b.name AS joined_later,
       a.joined_on AS earlier_date,
       b.joined_on AS later_date
FROM staff a
JOIN staff b
  ON a.dept_id = b.dept_id
 AND a.joined_on < b.joined_on
ORDER BY a.dept_id, a.joined_on, b.joined_on;
