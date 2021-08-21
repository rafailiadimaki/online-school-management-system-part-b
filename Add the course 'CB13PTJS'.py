import mysql.connector

conn = mysql.connector.connect(host='localhost', user='root', passwd='MyNewPass', database='private_school')

myCursor = conn.cursor()

# 1 : query
add_course= ('INSERT INTO courses'\
              '(course_id, title, language, description, Type)'\
              ' VALUES (%s, %s, %s, %s, %s)')

# 2 : values
course_id = 5870147
title = input("Give the title: ")
if title =='':
    title = 'CB13PTJS'
if title != 'CB13PTJS':
    title = 'CB13PTJS'

language = 'JAVASCRIPT'
description = 'JAVASCRIPT 24 weeks'
Type = 'Part Time'

course_data = (course_id, title, language, description, Type)
print(course_data)

# 2 : combine
myCursor.execute(add_course, course_data)
conn.commit()
#Closing my connection and cursor
myCursor.close()
conn.close()