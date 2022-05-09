SELECT
    u.name AS name,
    SUM(t.amount) AS balance
FROM Users AS u
INNER JOIN Transactions AS t ON t.account = u.account
GROUP BY u.account, u.name
HAVING SUM(t.amount) > 10000
