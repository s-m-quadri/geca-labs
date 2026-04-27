USE proc_lab;

-- TODO: CALL apply_rate(200, 10, @out);
-- TODO: SELECT @out AS with_tax;
CALL apply_rate(200, 10, @out);
SELECT @out AS with_tax;
