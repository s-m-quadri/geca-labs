-- Puzzle C (riddle)
-- "One order carried both a bargain-bin item (unit price under 15)
--  and a premium item (unit price over 30). Which order_id is it?"
\c view_lab

-- TODO: HAVING with conditional sums, or EXISTS pair, or intersect of two subqueries
select order_id from order_lines ol
join products p on ol.prod_id = p.prod_id
group by order_id
having sum(case when p.price < 15 then 1 else 0 end) > 0
and sum(case when p.price > 30 then 1 else 0 end) > 0;  