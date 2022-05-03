SELECT src.employee_id
FROM
(
    SELECT e1.employee_id
    FROM Employees AS e1
    LEFT JOIN Salaries AS s1 ON s1.employee_id = e1.employee_id
    WHERE s1.employee_id IS NULL
    
    UNION
    
    SELECT s2.employee_id
    FROM Salaries AS s2
    LEFT JOIN Employees AS e2 ON e2.employee_id = s2.employee_id
    WHERE e2.employee_id IS NULL
) src
ORDER BY src.employee_id
