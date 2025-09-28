SELECT title, author, ABS(price - (SELECT AVG(price) FROM book))
FROM book;