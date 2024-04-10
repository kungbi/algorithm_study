SELECT      dev.ID, dev.EMAIL, dev.FIRST_NAME, dev.LAST_NAME
FROM        DEVELOPERS dev
WHERE       EXISTS (
    SELECT  *
    FROM    SKILLCODES
    WHERE   NAME IN ("Python", "C#") AND CODE & dev.SKILL_CODE
)
ORDER BY    dev.ID