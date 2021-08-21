import mysql.connector
import time
conn = mysql.connector.connect(host='localhost', user='root', passwd='MyNewPass', database='private_school')

myCursor = conn.cursor()

see_students = 'SELECT * FROM students'
myCursor.execute(see_students)

x=' '
print("These are the private school's students:")
print()
print(2*x,"id", 3*x, "Name", 1*x, "Surname", 1*x,
      "Birthdate", "Fees")
for (stud_id, first_name, last_name, birthdate, fees) in myCursor:
    print(stud_id, first_name, last_name, birthdate, fees)
time.sleep(10)

#Closing my connection and cursor
myCursor.close()
conn.close()