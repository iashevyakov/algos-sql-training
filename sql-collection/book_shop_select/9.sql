SELECT name_genre, SUM(buy_book.amount) as Количество
FROM genre
JOIN book USING (genre_id)
JOIN buy_book USING (book_id)
GROUP BY name_genre
HAVING SUM(buy_book.amount) =
  (
      SELECT MAX(sum_amount) AS max_sum_amount
      FROM
      (
        SELECT name_genre, SUM(buy_book.amount) as sum_amount
        FROM genre
        JOIN book USING (genre_id)
        JOIN buy_book USING (book_id)
        GROUP BY name_genre
      ) query_in
  );