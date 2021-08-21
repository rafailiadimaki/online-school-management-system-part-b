import mysql.connector
import time
conn = mysql.connector.connect(host='localhost', user='root', passwd='MyNewPass', database='private_school')

myCursor = conn.cursor()

see_assignments_per_course = 'SELECT courses.title, assignments.title FROM assignments, coursework, courses WHERE assignments.assignments_id = coursework.assignments_id  AND courses.course_id = coursework.course_id ORDER BY courses.title'
myCursor.execute(see_assignments_per_course)

x=' '
print("These are the assignments per course:")
print()
time.sleep(1)
print("(Course's title,",x, "Assignment's title)")

for (title) in myCursor:
    time.sleep(2)
    print(title)
    
time.sleep(2)

#Closing my connection and cursor
myCursor.close()
conn.close()
