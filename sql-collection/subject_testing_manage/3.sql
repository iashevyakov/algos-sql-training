UPDATE attempt
SET attempt.result= (
    SELECT ROUND(SUM(answer.is_correct) / COUNT(answer.answer_id) * 100)
    FROM answer JOIN testing USING (answer_id)
    WHERE testing.attempt_id=8
)
WHERE attempt.attempt_id=8;