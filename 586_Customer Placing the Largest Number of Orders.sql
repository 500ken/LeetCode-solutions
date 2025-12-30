WITH RankedCustomers AS (
    SELECT 
        customer_number,
        RANK() OVER (ORDER BY COUNT(*) DESC) as rnk
    FROM Orders
    GROUP BY customer_number
)
SELECT customer_number
FROM RankedCustomers
WHERE rnk = 1;
