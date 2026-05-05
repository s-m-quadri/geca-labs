# Hostel Management System

---

## 1. Problem Statement

The **Hostel Management System** is designed to efficiently manage student records, room allocations, complaints, and hostel officials in an organized manner.  
It replaces manual record-keeping with a structured database system, thereby improving efficiency, accuracy, and data consistency.

---

## 2. System Design

### Tables Used

- **students**  
  Stores student details such as roll number, name, branch, year, contact number, and address.

- **rooms**  
  Contains room information including room number, floor, and capacity.

- **room_allotment**  
  Maps students to rooms and stores allocation details such as allotment date and vacate date.

- **officials**  
  Stores hostel staff details, including wardens and the rector, using a role attribute.

- **complaints**  
  Records complaints raised by students along with the complaint date and status.

---

### Normalization

- Room details are stored separately in the **rooms** table to avoid redundancy.
- **student_id** is used as a foreign key instead of student name to ensure consistency.
- The **room_allotment** table resolves the relationship between students and rooms.
- Wardens and the rector are combined into a single **officials** table using a role field.

---

## 3. Relationships

- One **student** can have multiple room allotments over time (**1:N**).
- One **room** can accommodate multiple students (**1:N**).
- One **student** can raise multiple complaints (**1:N**).

The `room_allotment` table acts as a bridge between **students** and **rooms**.

---

## 4. Sample Data Description

The database includes:

- **6 students** from different branches (Civil, Mechanical, Electrical, CSE, ENTC, IT)
- **4 rooms** with varying capacities
- **Room allocations** where some rooms have multiple students
- **3 officials** (2 wardens and 1 rector)
- **6 complaints** with statuses such as _pending_ and _resolved_

---

## 5. Query Results & Observations

- Students are successfully mapped to their respective rooms using **JOIN** queries.
- Room occupancy is calculated using **GROUP BY** queries.
- Some rooms contain multiple students, reflecting real-world sharing scenarios.
- Complaints are effectively tracked along with their status.
- Subqueries help identify students who have raised complaints.
- Views simplify repeated access to complaint summaries.

---

## 6. Key Insights

- Room occupancy analysis helps in identifying overcrowded rooms.
- Complaint tracking highlights common issues such as water, electricity, and maintenance problems.
- The system supports efficient querying and reporting across multiple tables.

---

## 7. Limitations

- Room capacity is not strictly enforced (no constraint or trigger implemented).
- Complaints are not assigned to specific officials.
- No historical tracking is maintained when students change rooms.

---

## 8. Future Improvements

- Add triggers to enforce room capacity limits
- Assign complaints to wardens or the rector
- Maintain history of room changes
- Add a login system for students and administrators
- Implement automated complaint resolution tracking

---

## 9. Conclusion

The Hostel Management System demonstrates the effective use of relational database concepts such as normalization, foreign keys, joins, aggregation, and views.  
It provides a structured and scalable approach to managing hostel data and can be further extended with additional features.

---

## 10. References

- MySQL Documentation
- DBMS Lab Manual
