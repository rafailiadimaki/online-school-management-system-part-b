SELECT teaching.tr_id,first_name, last_name, title 
FROM trainers, teaching, courses
WHERE trainers.tr_id = teaching.tr_id AND courses.course_id = teaching.course_id;