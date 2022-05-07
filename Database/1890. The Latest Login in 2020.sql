SELECT
    l.user_id AS user_id,
    MAX(l.time_stamp) AS last_stamp
FROM Logins AS l
WHERE YEAR(l.time_stamp) = 2020
GROUP BY l.user_id
