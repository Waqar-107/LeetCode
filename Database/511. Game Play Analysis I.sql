SELECT
    a.player_id AS player_id,
    MIN(a.event_date) AS first_login
FROM Activity AS a
GROUP BY a.player_id
