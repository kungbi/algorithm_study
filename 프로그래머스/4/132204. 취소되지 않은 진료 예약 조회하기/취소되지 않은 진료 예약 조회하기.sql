SELECT      app.APNT_NO, pt.PT_NAME, pt.PT_NO, app.MCDP_CD, dr.DR_NAME, app.APNT_YMD
FROM        APPOINTMENT app JOIN PATIENT pt ON app.PT_NO = pt.PT_NO JOIN DOCTOR dr ON app.MDDR_ID = dr.DR_ID
WHERE       
    app.MCDP_CD = 'CS' AND
    DATE(APNT_YMD) = DATE('2022-04-13') AND
    APNT_CNCL_YN = 'N'
ORDER BY    app.APNT_YMD