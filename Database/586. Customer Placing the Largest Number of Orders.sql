SELECT o.customer_number
FROM Orders AS o
GROUP BY o.customer_number
HAVING COUNT(o.order_number) = (
    SELECT MAX(src.cnt)
    FROM
    (
        SELECT COUNT(o.order_number) as cnt
        FROM Orders AS o
        GROUP BY o.customer_number
    ) src
)
