SELECT courses.title, assignments.title 
FROM assignments, coursework, courses
WHERE assignments.assignments_id = coursework.assignments_id  AND courses.course_id = coursework.course_id
ORDER BY courses.title;