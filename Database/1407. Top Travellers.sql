SELECT
    u.name AS name,
    SUM(ISNULL(r.distance, 0)) AS travelled_distance
FROM Users AS u
LEFT JOIN Rides AS r ON r.user_id = u.id
GROUP BY u.name
ORDER BY SUM(ISNULL(r.distance, 0)) DESC, u.name
