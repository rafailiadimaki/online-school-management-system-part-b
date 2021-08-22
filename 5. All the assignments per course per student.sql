SELECT assignments.title, courses.title, students.stud_id, students.first_name, students.last_name
FROM assignments, coursework, courses, students, courseregistrations
WHERE assignments.assignments_id = coursework.assignments_id  AND courses.course_id = coursework.course_id
AND students.stud_id = courseregistrations.stud_id AND courses.course_id = courseregistrations.course_id
ORDER BY assignments.title, students.first_name, students.last_name ;