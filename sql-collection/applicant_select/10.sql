SELECT name_program, name_enrollee
FROM enrollee
JOIN program_enrollee USING (enrollee_id)
JOIN program USING (program_id)
JOIN program_subject USING (program_id)
JOIN enrollee_subject ON enrollee.enrollee_id=enrollee_subject.enrollee_id AND enrollee_subject.subject_id=program_subject.subject_id
GROUP BY name_program, name_enrollee
HAVING SUM(min_result>result) > 0
ORDER BY name_program, name_enrollee