UPDATE applicant, (
    SELECT enrollee_id, IF(SUM(bonus) is Null, 0, SUM(bonus)) as total_bonus
    FROM enrollee
    LEFT JOIN enrollee_achievement USING (enrollee_id)
    LEFT JOIN achievement USING (achievement_id)
    GROUP BY enrollee_id
) as enrollee_bonus
SET applicant.itog=applicant.itog+enrollee_bonus.total_bonus
WHERE applicant.enrollee_id =enrollee_bonus.enrollee_id
