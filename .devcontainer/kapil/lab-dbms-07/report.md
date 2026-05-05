# DBMS Mini Project Report

## 1. Problem Statement
This project models an online course platform where students enroll in courses taught by instructors.

## 2. Design Decisions
- Separate tables for students, instructors, and courses to maintain normalization.
- A junction table (enrollments) is used to handle the many-to-many relationship between students and courses.

## 3. Queries Explanation
- JOIN queries are used to combine data from multiple tables.
- Aggregate function (COUNT) is used to calculate number of students per course.
- Subquery is used to find students enrolled in a specific course.
- A view is created for simplified access to student-course data.

## 4. Limitations
- No grading system included.
- No authentication or user roles.
- No course completion tracking.

## 5. Future Improvements
- Add grades and performance tracking.
- Add login system.
- Add course reviews and ratings.