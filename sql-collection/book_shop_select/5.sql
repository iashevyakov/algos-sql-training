SELECT buy_id, name_client, SUM(book.price*buy_book.amount) as 'Стоимость'
FROM client JOIN buy USING (client_id)
JOIN buy_book USING (buy_id)
JOIN book USING (book_id)
GROUP BY buy_id
ORDER BY buy_id