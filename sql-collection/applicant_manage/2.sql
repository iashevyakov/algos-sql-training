DELETE FROM applicant
USING
applicant JOIN (
    SELECT program_id, enrollee.enrollee_id
    FROM enrollee
    JOIN program_enrollee USING (enrollee_id)
    JOIN program USING (program_id)
    JOIN program_subject USING (program_id)
    JOIN enrollee_subject ON enrollee.enrollee_id=enrollee_subject.enrollee_id AND enrollee_subject.subject_id=program_subject.subject_id
    GROUP BY program_id, enrollee.enrollee_id
    HAVING SUM(min_result>result) > 0
) as pr_en ON applicant.program_id=pr_en.program_id AND applicant.enrollee_id=pr_en.enrollee_id