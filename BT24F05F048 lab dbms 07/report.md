# Hospital Database Mini Project

## Problem Statement
This project is designed to manage hospital operations such as patient details, doctor information, appointments, treatments, and billing. It organizes data efficiently and allows easy retrieval of information.

## Objective
- To design a relational database for a hospital system  
- To maintain structured and normalized data  
- To perform useful queries for decision-making  

## Database Design

### Tables Used
- Patients: Stores patient details (name, age, gender, phone)  
- Doctors: Stores doctor details (name, specialization, experience)  
- Appointments: Connects patients and doctors with appointment dates  
- Treatments: Stores treatment details and cost  
- Bills: Stores billing information and payment status  

### Relationships
- One patient can have many appointments (1:N)  
- One doctor can handle many appointments (1:N)  
- One appointment can have multiple treatments (1:N)  
- Each treatment has one bill (1:1)  

### Normalization
The database is normalized to reduce redundancy. Separate tables are used for different entities, foreign keys maintain relationships, and duplicate data is avoided.

## Sample Queries
- Display patient and doctor details using JOIN  
- Calculate total bill per patient using GROUP BY  
- Find doctors with more than one appointment using HAVING  
- Show expensive treatments  
- Display paid bills  

## Sample Output
Example of patient-doctor query:

patient_name | doctor_name  
-------------+-------------  
Rahul        | Dr. Sharma  
Priya        | Dr. Mehta  

## Tools Used
- PostgreSQL  
- SQL (DDL, DML, Queries)  
- GitHub  
- Codespaces  

## Limitations
- No user interface  
- Basic billing system  
- No patient history tracking  

## Future Improvements
- Add advanced billing system  
- Implement triggers and procedures  
- Add frontend interface  
- Improve data validation  

## Conclusion
This project demonstrates the use of relational databases in managing hospital data. It shows how structured tables and SQL queries can efficiently handle real-world scenarios.