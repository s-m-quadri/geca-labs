USE BookingSystemDB;

-- 1. List rooms and their pricing
SELECT h.RoomTag, c.ClassName, c.Price 
FROM HotelRooms h JOIN RoomClasses c ON h.ClassID = c.ClassID;

-- 2. Find empty rooms
SELECT h.RoomTag, c.ClassName 
FROM HotelRooms h JOIN RoomClasses c ON h.ClassID = c.ClassID 
WHERE h.Status = 'Empty';

-- 3. Get customer bill info
SELECT s.StayID, c.Name, p.FinalBill, p.IsPaid
FROM Stays s
JOIN Customers c ON s.CustomerID = c.CustomerID
JOIN Payments p ON s.StayID = p.StayID;