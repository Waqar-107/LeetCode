SELECT src.id, src.type
FROM
(
    SELECT t1.id, 'Root' AS type
    FROM Tree AS t1
    WHERE t1.p_id IS NULL

    UNION

    SELECT t2.id, 'Leaf' AS type
    FROM Tree AS t2
    LEFT JOIN Tree AS t3 ON t3.p_id = t2.id
    WHERE t2.p_id IS NOT NULL AND t3.p_id IS NULL 

    UNION

    SELECT t5.id, 'Inner' AS type
    FROM Tree AS t5
    INNER JOIN Tree AS t6 ON t6.p_id = t5.id
    WHERE t5.p_id IS NOT NULL
) src
ORDER BY src.id
