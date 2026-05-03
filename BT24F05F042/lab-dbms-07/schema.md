# Schema Design

## Overview
This project implements a College Management System database.  
It is designed to store and manage information about students, faculty, courses, and enrollments.

---

## Tables

### 1. Students
- **student_id (PK)**: Unique identifier for each student  
- name: Name of the student  
- department: Department of the student  

---

### 2. Faculty
- **faculty_id (PK)**: Unique identifier for each faculty member  
- name: Name of the faculty  
- department: Department of the faculty  

---

### 3. Courses
- **course_id (PK)**: Unique identifier for each course  
- course_name: Name of the course  
- credits: Number of credits assigned  
- **faculty_id (FK)**: References faculty table  

---

### 4. Enrollments
- **student_id (FK)**: References students table  
- **course_id (FK)**: References courses table  
- grade: Grade obtained by the student  
- semester: Semester of enrollment  
- **Composite Primary Key**: (student_id, course_id)  

---

## Relationships

- **Faculty → Courses**  
  One faculty member can teach multiple courses (1:N relationship)

- **Students ↔ Courses**  
  Many students can enroll in many courses (M:N relationship)  
  This is implemented using the **enrollments table**

---

## Design Justification
- The schema follows relational design principles  
- Redundancy is minimized using normalization  
- Relationships are maintained using foreign keys  
- Composite key ensures unique enrollment records  

---

## Summary
This schema ensures data integrity, supports efficient querying, and reflects a real-world academic system structure.