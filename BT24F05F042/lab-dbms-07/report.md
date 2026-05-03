# College Management System

## 1. Introduction
This project implements a simple College Management System using SQL.  
It manages data related to students, faculty, courses, and enrollments.  
The goal is to demonstrate core DBMS concepts such as table design, relationships, joins, aggregation, and subqueries.

---

## 2. Problem Statement
Managing academic data manually is inefficient and error-prone.  
This system provides a structured way to store and query:
- Student details
- Faculty information
- Course offerings
- Student enrollments and grades

---

## 3. Database Design
The system consists of the following tables:

### Students
Stores student information such as ID, name, and department.

### Faculty
Stores faculty details including department.

### Courses
Each course is linked to a faculty member.

### Enrollments
Represents a many-to-many relationship between students and courses.  
Includes grade and semester information.

Relationships are enforced using **foreign keys** to maintain data integrity.

---

## 4. Queries Implemented
The following SQL concepts were demonstrated:

- **JOINs**  
  Used to combine data from students, courses, and enrollments.

- **GROUP BY & Aggregation**  
  Used to count students per course and analyze enrollments.

- **Subqueries**  
  Used to filter students based on course enrollment.

- **Views**  
  Created to simplify frequently used queries.

---

## 5. Sample Output
The queries generate useful outputs such as:
- List of students with their enrolled courses
- Number of students per course
- Students with specific grades
- Course-wise statistics

---

## 6. Limitations
- Does not include attendance tracking  
- Does not handle exam scheduling or results in detail  
- No user interface (SQL-only system)

---

## 7. Conclusion
This project demonstrates how relational databases can efficiently manage structured data.  
It highlights the importance of proper schema design, normalization, and query optimization in real-world applications.