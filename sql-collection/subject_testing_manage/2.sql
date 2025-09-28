INSERT INTO testing(attempt_id, question_id)
SELECT attempt_id, question_id
FROM attempt JOIN question USING (subject_id)
WHERE attempt_id=(SELECT MAX(attempt_id) FROM attempt)
ORDER BY RAND()
LIMIT 3