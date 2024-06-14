SELECT      *
FROM        PLACES a
WHERE       2 <= (
    SELECT  COUNT(*)
    FROM    PLACES b
    WHERE   a.HOST_ID = b.HOST_ID
)
ORDER BY    ID