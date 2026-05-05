CREATE TABLE Passenger (
    passenger_id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    phone VARCHAR(15)
);

CREATE TABLE Vehicle (
    vehicle_id SERIAL PRIMARY KEY,
    type VARCHAR(10),
    name VARCHAR(100),
    total_seats INT
);

CREATE TABLE Route (
    route_id SERIAL PRIMARY KEY,
    source VARCHAR(100),
    destination VARCHAR(100),
    distance_km INT
);

CREATE TABLE Trip (
    trip_id SERIAL PRIMARY KEY,
    vehicle_id INT REFERENCES Vehicle(vehicle_id),
    route_id INT REFERENCES Route(route_id),
    travel_date DATE,
    departure_time TIME
);

CREATE TABLE Seat (
    seat_id SERIAL PRIMARY KEY,
    vehicle_id INT REFERENCES Vehicle(vehicle_id),
    seat_number VARCHAR(10)
);

CREATE TABLE Booking (
    booking_id SERIAL PRIMARY KEY,
    passenger_id INT REFERENCES Passenger(passenger_id),
    trip_id INT REFERENCES Trip(trip_id),
    seat_id INT REFERENCES Seat(seat_id),
    booking_date DATE,
    status VARCHAR(20)
);