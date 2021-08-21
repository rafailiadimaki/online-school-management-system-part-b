import mysql.connector
import time
conn = mysql.connector.connect(host='localhost', user='root', passwd='MyNewPass', database='private_school')

myCursor = conn.cursor()

see_courses = 'SELECT * FROM courses'
myCursor.execute(see_courses)
x=' '
print("These are the private school's courses:")
print()
for (course_id, title, language, description, type) in myCursor:
    print('ID:',course_id,'\n''TITLE:', title,'\n''LANGUAGE:',language, '\n''DESCRIPTION:', description, '\n''TYPE:',type)
    print('-------------------------------------------------------------------------')
time.sleep(15)

#Closing my connection and cursor
myCursor.close()
conn.close() 
