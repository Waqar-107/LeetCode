SELECT
    c.name
FROM Customer AS c
WHERE c.referee_id IS NULL OR c.referee_id <> 2
