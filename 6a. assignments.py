import mysql.connector
import time
conn = mysql.connector.connect(host='localhost', user='root', passwd='MyNewPass', database='private_school')

myCursor = conn.cursor()

see_assignments = 'SELECT * FROM assignments'
myCursor.execute(see_assignments)

x=' '
print("These are the private school's assignments:")
print()
for (assignments_id, title, description, due_date, submitted_code_mark, oral_mark) in myCursor:
    print("ID: ",assignments_id,'\n''TITLE:', title, '\n''DESCRIPTION:',description,'\n''DUE DATE:', due_date, '\n''CODE MARK:',submitted_code_mark,'\n''ORAL MARK:', oral_mark)
    print('--------------------------------------------------------------------------')
time.sleep(30)

#Closing my connection and cursor
myCursor.close()
conn.close()
