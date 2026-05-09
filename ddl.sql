CREATE TABLE Students (
    student_id INTEGER PRIMARY KEY,
    student_name TEXT,
    course TEXT,
    phone TEXT
);

CREATE TABLE Books (
    book_id INTEGER PRIMARY KEY,
    book_name TEXT,
    author TEXT,
    quantity INTEGER
);

CREATE TABLE IssueBooks (
    issue_id INTEGER PRIMARY KEY,
    student_id INTEGER,
    book_id INTEGER,
    issue_date TEXT,
    return_date TEXT
);