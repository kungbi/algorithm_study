SELECT  ANIMAL_ID, NAME
FROM    ANIMAL_OUTS outs
WHERE   NOT EXISTS (
    SELECT  *
    FROM    ANIMAL_INS ins
    WHERE   ins.ANIMAL_ID = outs.ANIMAL_ID
)
ORDER BY ANIMAL_ID, NAME