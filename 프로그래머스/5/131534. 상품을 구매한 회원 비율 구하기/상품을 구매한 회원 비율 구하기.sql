
SELECT      
    YEAR(sale.SALES_DATE) AS "YEAR",
    MONTH(sale.SALES_DATE) AS MONTH,
    COUNT(DISTINCT sale.user_id) AS PUCHASED_USERS,
    ROUND(COUNT(DISTINCT sale.user_id) / (
        SELECT      COUNT(*)
        FROM        USER_INFO user2
        WHERE       user2.JOINED LIKE '2021-%'
    ), 1) AS PUCHASED_RATIO
FROM        USER_INFO user JOIN ONLINE_SALE sale ON user.user_id = sale.user_id
WHERE       user.JOINED LIKE '2021-%'
GROUP BY    YEAR, MONTH
ORDER BY    YEAR, MONTH
