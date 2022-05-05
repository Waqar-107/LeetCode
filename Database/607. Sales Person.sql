SELECT s.name
FROM Salesperson AS s
WHERE s.name NOT IN
(
    SELECT s.name
    FROM Salesperson AS s
    INNER JOIN Orders AS o ON o.sales_id = s.sales_id
    INNER JOIN Company AS c ON c.com_id = o.com_id
    WHERE c.name = 'RED'
)
