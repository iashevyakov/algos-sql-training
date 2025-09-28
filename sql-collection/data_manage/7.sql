UPDATE supply,book
SET book.amount = book.amount + supply.amount, book.price = (book.price + supply.price) / 2
WHERE book.title = supply.title AND book.author = supply.author
