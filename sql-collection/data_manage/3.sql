INSERT INTO book (title, author, amount, price)
SELECT title, author, amount, price FROM supply WHERE author NOT IN ('Булгаков М.А.', 'Достоевский Ф.М.');

SELECT * FROM book;