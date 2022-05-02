SELECT
    a1.sell_date,
    COUNT(DISTINCT a1.product) AS num_sold,
    STUFF
    (
        (
            SELECT DISTINCT ',' + a2.product
            FROM Activities AS a2
            WHERE a2.sell_date = a1.sell_date
            FOR XML PATH('')
        ), 1, 1, '' 
    ) AS products
FROM Activities AS a1
GROUP BY a1.sell_date
ORDER BY a1.sell_date
