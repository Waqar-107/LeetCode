SELECT p.product_id, p.product_name
FROM Product AS p
INNER JOIN Sales AS s ON s.product_id = p.product_id
GROUP BY p.product_id, p.product_name
HAVING MIN(s.sale_date) >= '2019-01-01' AND MAX(s.sale_date) <= '2019-03-31'
