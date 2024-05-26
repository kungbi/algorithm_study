SELECT      prod.CATEGORY, prod.PRICE, prod.PRODUCT_NAME
FROM        FOOD_PRODUCT prod
WHERE       prod.CATEGORY IN ('과자', '국', '김치', '식용유') AND NOT EXISTS (
    SELECT  *
    FROM    FOOD_PRODUCT tmp
    WHERE   prod.PRICE < tmp.PRICE AND prod.CATEGORY = tmp.CATEGORY
)
ORDER BY    prod.PRICE DESC