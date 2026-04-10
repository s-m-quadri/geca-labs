-- Task 5: Modify Column
-- Change 'age' column to be TINYINT with NOT NULL constraint


-- TODO: Write your ALTER TABLE MODIFY COLUMN command here
INSERT INTO students (id,name,age,email)
VALUES(1,'TOM',15,'tomschool.com');

INSERT INTO students (id,name,age,email)
VALUES(2,'JULLY',16,'jullyschool.com');

SELECT * FROM students;