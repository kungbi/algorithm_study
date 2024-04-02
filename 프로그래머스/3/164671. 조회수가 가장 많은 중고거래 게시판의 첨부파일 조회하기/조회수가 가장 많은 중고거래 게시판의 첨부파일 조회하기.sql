SELECT      CONCAT("/home/grep/src/", file.BOARD_ID, "/", file.FILE_ID, file.FILE_NAME, FILE_EXT) AS FILE_PATH
FROM        USED_GOODS_FILE file
WHERE       file.BOARD_ID = (
    SELECT      BOARD_ID
    FROM        USED_GOODS_BOARD board
    ORDER BY    board.VIEWS DESC
    LIMIT       1
)
ORDER BY    file.FILE_ID DESC

