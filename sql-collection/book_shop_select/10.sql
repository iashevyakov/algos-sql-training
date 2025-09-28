SELECT YEAR(date_payment) as 'Год', MONTHNAME(date_payment) as 'Месяц', SUM(price*amount) as 'Сумма'
FROM
    buy_archive
GROUP BY YEAR(date_payment), MONTHNAME(date_payment)

UNION ALL

FROM
    book
    INNER JOIN buy_book USING(book_id)
    INNER JOIN buy USING(buy_id)

ORDER BY 2, 1