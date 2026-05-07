USE BookingSystemDB;

INSERT INTO Departments (DeptName, LeadManager) VALUES
('Concierge', 'Laura Palmer'), ('Operations', 'Dale Cooper');

INSERT INTO Employees (DeptID, Name, Role, Phone, Salary) VALUES
(1, 'Audrey Horne', 'Desk Clerk', '444-1234', 31000),
(2, 'Shelly Johnson', 'Cleaner', '444-5678', 21000);

INSERT INTO Customers (Name, Email, Phone, DocProof) VALUES
('Leland Palmer', 'leland@twin.com', '444-9999', 'SSN-123'),
('Pete Martell', 'pete@twin.com', '444-8888', 'SSN-456');

INSERT INTO RoomClasses (ClassName, Price, Beds) VALUES
('Single', 900, 1), ('Double', 1800, 2);

INSERT INTO HotelRooms (RoomTag, ClassID, Status) VALUES
('R1', 1, 'Empty'), ('R2', 2, 'Taken');

INSERT INTO Stays (CustomerID, RoomID, EmpID, InDate, OutDate, Status) VALUES
(1, 2, 1, '2025-10-01', '2025-10-03', 'Checked-In');

INSERT INTO Payments (StayID, RoomTotal, Taxes, FinalBill, IsPaid) VALUES
(1, 3600, 18, 4248, TRUE);