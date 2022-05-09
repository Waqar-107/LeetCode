SELECT p.email
FROM Person AS p
GROUP BY p.email
HAVING COUNT(*) > 1
