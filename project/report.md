🚆 Railway / Bus Reservation System
📌 1. Problem Statement (Who is the user?)

The system is designed for:

Passengers who want to book seats for travel
Transport administrators who manage vehicles, routes, and schedules

The main problem addressed is:

Managing seat reservations efficiently while avoiding conflicts such as double booking and ensuring proper tracking of trips, passengers, and routes.

In real-world scenarios, manual booking systems are error-prone and inefficient. This system digitizes the process, ensuring accuracy, speed, and data consistency.

📌 2. Design (Why these tables? Normalization)
🧩 Tables Used:
Passenger
Vehicle
Route
Trip
Seat
Booking
🧠 Design Justification
1. Passenger Table

Stores user details separately to avoid duplication across bookings.

2. Vehicle Table

Stores train/bus info once instead of repeating it in every trip.

3. Route Table

Separates source and destination logic to:

Avoid redundancy
Enable route-based queries (like most popular route)
4. Trip Table

Represents a specific journey instance

Same vehicle can run multiple trips
Same route can be used multiple times
5. Seat Table

Handles seat structure per vehicle:

Avoids storing seat numbers in booking repeatedly
Enables seat availability logic
6. Booking Table

Central table connecting:

Passenger
Trip
Seat

This ensures:
✔ Strong relational integrity
✔ Easy query execution

🔄 Normalization

The database is normalized up to 3NF (Third Normal Form):

No repeating groups
No partial dependencies
No transitive dependencies
Example:

❌ Without normalization:

Booking table storing vehicle name, route, passenger details repeatedly

✔ With normalization:

Each entity stored once and referenced via foreign keys
📌 3. Sample Query Results
🔍 Query 1: Passenger Booking Details
SELECT p.name, r.source, r.destination, b.status
FROM Passenger p
JOIN Booking b ON p.passenger_id = b.passenger_id
JOIN Trip t ON b.trip_id = t.trip_id
JOIN Route r ON t.route_id = r.route_id;
✅ Output:
name	source	destination	status
Amit	Mumbai	Pune	Booked
Riya	Mumbai	Pune	Booked
Rahul	Aurangabad	Pune	Booked
🔍 Query 2: Most Popular Route
SELECT r.source, r.destination, COUNT(*) AS bookings
FROM Route r
JOIN Trip t ON r.route_id = t.route_id
JOIN Booking b ON t.trip_id = b.trip_id
GROUP BY r.source, r.destination
ORDER BY bookings DESC;
✅ Output:
source	destination	bookings
Mumbai	Pune	4
🔍 Query 3: Trips Without Bookings
SELECT trip_id
FROM Trip
WHERE trip_id NOT IN (SELECT trip_id FROM Booking);
✅ Output:
trip_id
8
🔍 Query 4: Bookings per Trip
SELECT trip_id, COUNT(*) 
FROM Booking
GROUP BY trip_id;
✅ Output:
trip_id	count
1	2
2	1
📌 4. Limitations

Despite being functional, the system has some limitations:

❌ No payment integration
❌ No real-time seat locking system
❌ No cancellation refund handling
❌ No user authentication/login system
❌ Limited UI (database-focused only)
📌 5. Future Improvements

With more time, the following features can be added:

💳 Online payment system
📱 User login & authentication
🎟️ Ticket generation (PDF/QR code)
🔄 Real-time seat availability tracking
📊 Admin dashboard for analytics
🧠 Smart seat allocation algorithm
📌 6. References

The following resources were used for syntax and understanding:

PostgreSQL Documentation (SQL syntax and constraints)
W3Schools SQL Tutorial
GeeksforGeeks DBMS Concepts
Lecture notes from DBMS course
🎯 Conclusion

The Railway / Bus Reservation System demonstrates how relational databases can be used to efficiently manage real-world booking systems. By applying normalization and relational integrity, the system ensures accuracy, scalability, and ease of data retrieval.