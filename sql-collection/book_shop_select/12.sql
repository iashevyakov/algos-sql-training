SELECT name_city, SUM(amount) FROM city
JOIN client USING (city_id)
JOIN buy USING (client_id)
JOIN buy_book USING (buy_id)
GROUP BY name_city
ORDER BY 2 DESC