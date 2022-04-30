SELECT
    c.name AS Customers
FROM Customers AS c
LEFT JOIN Orders AS o ON o.customerId = c.id
WHERE o.customerId IS NULL
