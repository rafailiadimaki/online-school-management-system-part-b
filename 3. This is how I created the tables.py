import mysql.connector

conn1 = mysql.connector.connect(host='localhost', user='root', passwd='MyNewPass')
Cursor = conn1.cursor()
Cursor.execute('CREATE DATABASE private_school')

conn = mysql.connector.connect(host='localhost', user='root', passwd='MyNewPass', database='private_school')

myCursor = conn.cursor()

#TABLE FOR THE STUDENTS
myCursor.execute('CREATE TABLE students(stud_id int NOT NULL,'\
                 'first_name varchar(15),'\
                 'last_name varchar(15),'\
                 'birthdate date,'\
                 'fees int,'\
                 'PRIMARY KEY(stud_id) );')

#TABLE FOR THE TRAINERS
myCursor.execute('CREATE TABLE trainers(tr_id int NOT NULL,'\
                 'first_name varchar(15),'\
                 'last_name varchar(15),'\
                 'PRIMARY KEY(tr_id) );')

#TABLE FOR THE COURSES                
myCursor.execute('CREATE TABLE courses(course_id int NOT NULL,'\
                 'title varchar(8),'\
                 'language varchar(10),'\
                 'description varchar (20),'\
                 'type varchar (10),'\
                 'PRIMARY KEY(course_id) );')

#TABLE FOR THE ASSIGNMENTS
myCursor.execute('CREATE TABLE assignments(assignments_id int NOT NULL,'\
                 'title varchar(60),'\
                 'description varchar(50),'\
                 'due_date date,'\
                 'submitted_code_mark int,'\
                 'oral_mark int,'\
                 'PRIMARY KEY(assignments_id) );')

#TABLE FOR THE COURSE'S REGISTRATIONS
myCursor.execute('CREATE TABLE courseregistrations(stud_id int NOT NULL,'\
                 'course_id int NOT NULL);')

#TABLE FOR THE TEACHING STAFF
myCursor.execute('CREATE TABLE teaching(tr_id int NOT NULL,'\
                 'course_id int NOT NULL);')

#TABLE FOR THE COURSEWORK
myCursor.execute('CREATE TABLE coursework(assignments_id int NOT NULL,'\
                 'course_id int NOT NULL);')
