-- Task 10: Check Status
-- View current database status

-- Show all databases
SHOW DATABASES;

-- Use your database
USE school_db;

-- Show all tables
SHOW TABLES;

-- Show students table structure when it exists
SELECT
		COLUMN_NAME,
		COLUMN_TYPE,
		IS_NULLABLE,
		COLUMN_KEY,
		EXTRA
FROM information_schema.columns
WHERE table_schema = 'school_db'
	AND table_name = 'students';

-- Show row count when the table exists
SET @students_count_sql := IF(
		@students_table_exists > 0,
		'SELECT COUNT(*) AS total_students FROM students;',
		'SELECT 0 AS total_students;'
);

PREPARE students_count_stmt FROM @students_count_sql;
EXECUTE students_count_stmt;
DEALLOCATE PREPARE students_count_stmt;

-- View all data when the table exists; otherwise show a friendly message
SET @students_table_exists := (
		SELECT COUNT(*)
		FROM information_schema.tables
		WHERE table_schema = 'school_db'
			AND table_name = 'students'
);

SET @students_sql := IF(
		@students_table_exists > 0,
		'SELECT * FROM students;',
		'SELECT ''students table not found'' AS status_message;'
);

PREPARE students_stmt FROM @students_sql;
EXECUTE students_stmt;
DEALLOCATE PREPARE students_stmt;
