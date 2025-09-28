SELECT name_author, title, COUNT(buy_book.buy_book_id) as 'Количество'
FROM author
JOIN book USING (author_id)
LEFT JOIN buy_book USING (book_id)
GROUP BY book_id
ORDER BY name_author, title