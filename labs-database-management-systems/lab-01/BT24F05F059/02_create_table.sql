
USE school_db;


    CREATE TABLE students (
        id INT PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        age INT,
        email VARCHAR(100) UNIQUE
    );
    USE school_db;
    DESCRIBE students;