SELECT
    p.product_id
FROM Products AS p
WHERE p.low_fats = 'Y' AND p.recyclable = 'Y'
