UPDATE book, buy_book
SET book.amount=book.amount-buy_book.amount
WHERE book.book_id=buy_book.book_id AND buy_book.buy_id=5