SELECT stud_id,first_name, last_name
FROM students
WHERE students.stud_id IN (SELECT courseregistrations.stud_id
FROM courseregistrations
GROUP BY courseregistrations.stud_id
HAVING COUNT(*) > 1);