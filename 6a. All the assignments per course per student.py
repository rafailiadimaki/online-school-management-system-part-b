import mysql.connector
import time
conn = mysql.connector.connect(host='localhost', user='root', passwd='MyNewPass', database='private_school')

myCursor = conn.cursor()

see_assignments_per_course_student = 'SELECT assignments.title, courses.title, students.stud_id, students.first_name, students.last_name FROM assignments, coursework, courses, students, courseregistrations WHERE assignments.assignments_id = coursework.assignments_id  AND courses.course_id = coursework.course_id AND students.stud_id = courseregistrations.stud_id AND courses.course_id = courseregistrations.course_id ORDER BY assignments.title, students.first_name, students.last_name'
myCursor.execute(see_assignments_per_course_student)

x =' ' 
print('These are the courses per course per student:')
print()
for (title) in myCursor:
    time.sleep(2)
    print('-------------------------------------------------------------------------')
    print("Assignment:", title[0], "\n""Course:", title[1], "\n""id:", title[2], "\n""Name:", title[3],  "\n""Surname:", title[4])
    
time.sleep(5)

#Closing my connection and cursor
myCursor.close()
conn.close()

