SELECT author, title, price
FROM book
WHERE price - (SELECT MIN(price) from book) <= 150
ORDER BY price;