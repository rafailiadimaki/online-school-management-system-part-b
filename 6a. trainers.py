import mysql.connector
import time
conn = mysql.connector.connect(host='localhost', user='root', passwd='MyNewPass', database='private_school')

myCursor = conn.cursor()

see_trainers = 'SELECT * FROM trainers'
myCursor.execute(see_trainers)

x=' '
print("These are the private school's trainers:")
print()
print(2*x,"id", 3*x, "Name", 1*x, "Surname")
for (stud_id, first_name, last_name) in myCursor:
    print(stud_id, first_name, last_name)
time.sleep(10)

#Closing my connection and cursor
myCursor.close()
conn.close()
