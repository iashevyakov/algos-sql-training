SELECT author as 'Автор', COUNT(*) as 'Различных_книг', SUM(amount) as 'Количество_экземпляров'
FROM book
GROUP BY author;