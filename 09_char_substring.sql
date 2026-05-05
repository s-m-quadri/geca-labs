USE school_db;

<<<<<<< HEAD
SELECT full_name,
       LEFT(full_name, 3) AS prefix3,
       SUBSTRING(full_name, 1, 3) AS sub3,
       LENGTH(full_name) AS name_len
=======Z
SELECT 
    full_name,
    LEFT(full_name, 3) AS prefix3,
    SUBSTRING(full_name, 1, 3) AS sub3,
    LENGTH(full_name) AS name_len
>>>>>>> 80227cf0 (done)
FROM employees;