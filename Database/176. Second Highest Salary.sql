SELECT 
    ISNULL
    (
        (
            SELECT DISTINCT e.salary
            FROM Employee AS e
            ORDER BY e.salary DESC
            OFFSET 1 ROW 
            FETCH NEXT 1 ROW ONLY
        )
    , NULL) AS SecondHighestSalary
