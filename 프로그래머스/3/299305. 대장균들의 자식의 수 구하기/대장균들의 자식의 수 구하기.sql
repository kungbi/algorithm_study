SELECT      data.ID, (
    SELECT  COUNT(*)
    FROM    ECOLI_DATA child
    WHERE   child.PARENT_ID = data.ID
) AS CHILD_COUNT
FROM        ECOLI_DATA data
ORDER BY    data.ID