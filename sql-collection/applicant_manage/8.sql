DELETE FROM enrollee
USING
enrollee
JOIN student USING (name_enrollee)