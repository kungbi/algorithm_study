SELECT      type.INGREDIENT_TYPE, SUM(info.TOTAL_ORDER) AS TOTAL_ORDER
FROM        ICECREAM_INFO type JOIN FIRST_HALF info ON type.FLAVOR = info.FLAVOR
GROUP BY    type.INGREDIENT_TYPE
ORDER BY    TOTAL_ORDER 