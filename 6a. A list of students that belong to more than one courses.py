import mysql.connector
import time
conn = mysql.connector.connect(host='localhost', user='root', passwd='MyNewPass', database='private_school')

myCursor = conn.cursor()

see_students = 'SELECT stud_id,first_name, last_name FROM students WHERE students.stud_id IN (SELECT courseregistrations.stud_id FROM courseregistrations GROUP BY courseregistrations.stud_id HAVING COUNT(*) > 1)'
myCursor.execute(see_students)

mylist=[]
x = '  '

for (stud_id, first_name, last_name) in myCursor:
    students_data = stud_id, first_name, last_name
    mylist.append(students_data)
print("A list of students that belong to more than one courses:")
print()
print(mylist)
time.sleep(5)

#Closing my connection and cursor
myCursor.close()
conn.close()
