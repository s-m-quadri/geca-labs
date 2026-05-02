-- Puzzle C (riddle)
-- "One order carried both a bargain-bin item (unit price under 15)
--  and a premium item (unit price over 30). Which order_id is it?"


-- TODO: HAVING with conditional sums, or EXISTS pair, or intersect of two subqueries
select order_id from (
  select ol.order_id,
    sum(case when p.price < 15 then 1 else 0 end) as bargain_count,
    sum(case when p.price > 30 then 1 else 0 end) as premium_count
  from order_lines ol
  join products p on ol.prod_id = p.prod_id
  group by ol.order_id
) as t
where t.bargain_count > 0 and t.premium_count > 0;

