-- Task 2: Arithmetic in a SELECT (+ - * /)
-- PostgreSQL has no session variables (@a := ...); just SELECT the expressions.

USE proc_lab;

SET @a := 17; SET @b := 5;
SELECT @a + @b AS sum_, @a - @b AS diff, @a * @b AS prod, @a / @b AS quot;
