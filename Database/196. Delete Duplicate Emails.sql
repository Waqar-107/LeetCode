DELETE p1 FROM Person AS p1
INNER JOIN Person AS p2 ON p2.email = p1.email
WHERE p1.id > p2.id
