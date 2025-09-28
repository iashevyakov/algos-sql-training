CREATE TABLE buy_pay AS
SELECT title, name_author, price, buy_book.amount, price * buy_book.amount as 'Стоимость'
FROM buy_book JOIN book USING (book_id)
JOIN author USING (author_id)
WHERE buy_book.buy_id=5
ORDER BY title;

SELECT * FROM buy_pay;