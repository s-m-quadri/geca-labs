-- Task 8: Derived table in FROM
-- From a subquery that computes per-order revenue, select orders where revenue > 30
\c view_lab

-- TODO: SELECT * FROM (
--   SELECT order_id, SUM(ol.qty * p.price) AS rev
--   FROM order_lines ol
--   JOIN products p ON ol.prod_id = p.prod_id
--   GROUP BY order_id
-- ) AS t
-- WHERE t.rev > 30;

select * from(
    select order_id,sum(ol.qty*p.price) as rev
    from order_lines ol
    join products p on ol.prod_id=p.prod_id
    group by order_id
)as t
where t.rev>30;
