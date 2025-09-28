CREATE TABLE applicant AS
SELECT program_id, enrollee.enrollee_id, SUM(result) as itog
FROM enrollee
JOIN program_enrollee USING (enrollee_id)
JOIN program_subject USING (program_id)
JOIN enrollee_subject ON program_subject.subject_id=enrollee_subject.subject_id AND enrollee_subject.enrollee_id=enrollee.enrollee_id
GROUP BY program_id, enrollee.enrollee_id
ORDER BY program_id, 3 DESC;

SELECT * FROM applicant;