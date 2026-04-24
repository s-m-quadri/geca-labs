To solve this puzzle, let's break it down step by step. Restate the riddle in relational terms: Which entities (tables) are involved, and what condition must hold for a staff member to be an "outsider" helping a project from another department?

- Think about the tables: `staff` (with `dept_id` for their official department), `projects` (with `dept_id` for the owning department), and `project_staff` (linking staff to projects).
- What keys link them? (Hint: `staff_id` and `proj_id`.)
- The condition: A staff member's `dept_id` should not match the project's `dept_id`.
- Join type: Since we want only staff who are actually assigned to such projects, an inner join makes sense. Sketch it in words: Start from `project_staff`, join to `staff` on `staff_id`, then join to `projects` on `proj_id`.

What SELECT would you write to get `name` and `title` for those rows? If stuck, draw the tables on paper and mark the FK links. You can run `14_check_status.sql` to see sample data.
