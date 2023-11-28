
SELECT      board.TITLE,
            board.BOARD_ID,
            reply.REPLY_ID,
            reply.WRITER_ID,
            reply.CONTENTS,
            DATE_FORMAT(reply.CREATED_DATE, '%Y-%m-%d')
FROM        USED_GOODS_BOARD board INNER JOIN USED_GOODS_REPLY reply ON board.BOARD_ID = reply.BOARD_ID
WHERE       YEAR(board.CREATED_DATE) = '2022' AND MONTH(board.CREATED_DATE) = '10'
ORDER BY    reply.CREATED_DATE ASC, board.TITLE ASC