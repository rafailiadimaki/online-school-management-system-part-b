SELECT students.stud_id, first_name, last_name, title 
FROM students, courseregistrations,courses
WHERE students.stud_id = courseregistrations.stud_id AND courses.course_id = courseregistrations.course_id;