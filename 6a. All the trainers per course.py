import mysql.connector
import time
conn = mysql.connector.connect(host='localhost', user='root', passwd='MyNewPass', database='private_school')

myCursor = conn.cursor()

see_trainers_per_course = 'SELECT teaching.tr_id,first_name, last_name, title  FROM trainers, teaching, courses WHERE trainers.tr_id = teaching.tr_id AND courses.course_id = teaching.course_id'

myCursor.execute(see_trainers_per_course)

x=' '

print("These are the private school's trainers per course:")
print()
print(2*x,"id", 3*x, "Name", 1*x, "Surname", 1*x,"Title")
for (tr_id,first_name, last_name, title) in myCursor:
    print(tr_id,first_name, last_name, title)
time.sleep(5)

#Closing my connection and cursor
myCursor.close()
conn.close()
