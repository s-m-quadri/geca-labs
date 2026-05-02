-- view_lab sanity check
\c view_lab

SELECT tablename FROM pg_tables WHERE schemaname = 'public';SELECT COUNT(*) AS customers FROM customers;