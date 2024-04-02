SELECT      ins.NAME, ins.DATETIME
FROM        ANIMAL_INS ins
WHERE       NOT EXISTS (
    SELECT      *
    FROM        ANIMAL_OUTS outs
    WHERE       ins.ANIMAL_ID = outs.ANIMAL_ID
)
ORDER BY    ins.DATETIME ASC
LIMIT       3