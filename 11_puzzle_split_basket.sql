-- Puzzle C (riddle)
-- "One order carried both a bargain-bin item (unit price under 15)
--  and a premium item (unit price over 30). Which order_id is it?"


-- TODO: HAVING with conditional sums, or EXISTS pair, or intersect of two subqueries
select order_id from (
  select order_id,
    sum(case when unit_price < 15 then 1 else 0 end) as bargain_count,
    sum(case when unit_price > 30 then 1 else 0 end) as premium_count
  from v_order_lines_detail
  group by order_id
) as t
where bargain_count > 0 and premium_count > 0;

