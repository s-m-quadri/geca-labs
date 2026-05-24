-- Puzzle A (riddle)
-- "Two sibling projects share a name prefix and the same home department.
--  Only one person booked hours on **both**. Who is it?"
-- Hint: inspect projects.title and project_staff; avoid hard-coding IDs in your
-- final query if you can use titles or dept instead.

USE join_lab;

-- TODO: Write one SELECT that returns exactly one name (the solver).
To solve this puzzle, restate the story in relational terms: Which entities (tables) represent the "sibling projects," the "home department," and the "person who booked hours on both"? What conditions define "share a name prefix" and "same home department"? Which joins (inner or outer) might help find the unique person across project_staff? Sketch the table relationships on paper first.