SELECT      DISTINCT car.CAR_ID
FROM        CAR_RENTAL_COMPANY_CAR car
WHERE       EXISTS (
    SELECT      *
    FROM        CAR_RENTAL_COMPANY_RENTAL_HISTORY history
    WHERE       MONTH(history.START_DATE) = 10 AND car.CAR_ID = history.CAR_ID
) AND
car.CAR_TYPE = '세단'
ORDER BY    car.CAR_ID DESC