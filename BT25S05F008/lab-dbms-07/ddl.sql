-- No CREATE DATABASE in SQLite

-- Table 1: Center
CREATE TABLE center (
    center_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    location TEXT
);

-- Table 2: Service
CREATE TABLE service (
    service_id INTEGER PRIMARY KEY AUTOINCREMENT,
    center_id INTEGER,
    service_name TEXT,
    FOREIGN KEY (center_id) REFERENCES center(center_id)
);

-- Table 3: User
CREATE TABLE user_table (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    phone TEXT
);

-- Table 4: Token
CREATE TABLE token (
    token_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    service_id INTEGER,
    token_number INTEGER,
    status TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES user_table(user_id),
    FOREIGN KEY (service_id) REFERENCES service(service_id)
);