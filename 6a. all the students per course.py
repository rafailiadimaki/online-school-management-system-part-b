import mysql.connector
import time
conn = mysql.connector.connect(host='localhost', user='root', passwd='MyNewPass', database='private_school')

myCursor = conn.cursor()
see_students_per_course = 'SELECT students.stud_id, first_name, last_name, title  FROM students, courseregistrations,courses WHERE students.stud_id = courseregistrations.stud_id AND courses.course_id = courseregistrations.course_id'
myCursor.execute(see_students_per_course)

x= ' '
print("These are the private school's students per course:")
print()
for (stud_id, first_name, last_name, title) in myCursor:
    print('ID:',stud_id,'\n''NAME:', first_name,'\n' 'SURNAME:', last_name,'\n' 'TITLE:', title)
    print('-------------------------------------------------------------------------')
time.sleep(10)

#Closing my connection and cursor
myCursor.close()
conn.close()
