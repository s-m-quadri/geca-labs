-- Task 2: User variables and arithmetic (+ − * /)
-- No procedures yet.

USE proc_lab;

-- TODO: SET @a := 17; SET @b := 5;
-- TODO: SELECT @a + @b AS sum_, @a - @b AS diff, @a * @b AS prod, @a / @b AS quot;

set @a:=17,@b:=15;
select @a+@b as sum_,@a-@b as diff,@a*@b as prod,@a/@b as quot;