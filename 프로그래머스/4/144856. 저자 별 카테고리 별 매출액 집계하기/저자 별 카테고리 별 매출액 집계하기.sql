SELECT      author.AUTHOR_ID, author.AUTHOR_NAME, book.CATEGORY, SUM(book.PRICE * sales.SALES) AS TOTAL_SALES
FROM        BOOK_SALES sales 
            JOIN BOOK book ON sales.book_id = book.BOOK_ID 
            JOIN AUTHOR author ON book.AUTHOR_ID = author.AUTHOR_ID
WHERE       sales.SALES_DATE LIKE '2022-01%'
GROUP BY    author.AUTHOR_ID, book.CATEGORY
ORDER BY    author.AUTHOR_ID, book.CATEGORY DESC