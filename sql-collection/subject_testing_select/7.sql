SELECT name_question, name_answer, IF(is_correct=true, 'Верно', 'Неверно') AS 'Результат'
FROM testing
JOIN question USING (question_id)
JOIN answer USING (answer_id)
WHERE attempt_id=7
