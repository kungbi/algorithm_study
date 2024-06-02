SELECT      (
CASE
    WHEN  (dev.SKILL_CODE & (
        SELECT  SUM(CODE)
        FROM    SKILLCODES
        WHERE   NAME = 'Python'
    )) AND (dev.SKILL_CODE & (
        SELECT  SUM(CODE)
        FROM    SKILLCODES
        WHERE   CATEGORY = 'Front End'
    ))  THEN 'A'
    WHEN  dev.SKILL_CODE & (
        SELECT  SUM(CODE)
        FROM    SKILLCODES
        WHERE   NAME = 'C#'
    ) THEN 'B'
    WHEN  dev.SKILL_CODE & (
        SELECT  SUM(CODE)
        FROM    SKILLCODES
        WHERE   CATEGORY = 'Front End'
    ) THEN 'C'
END
) AS GRADE, dev.ID, dev.EMAIL
FROM        DEVELOPERS dev
GROUP BY    GRADE, dev.ID, dev.EMAIL
HAVING      GRADE IS NOT NULL
ORDER BY    GRADE, ID
