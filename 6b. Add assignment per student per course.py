import mysql.connector

conn = mysql.connector.connect(host='localhost', user='root', passwd='MyNewPass', database='private_school')

myCursor = conn.cursor()

import datetime
import time

# 1 : queries
add_assignment = ('INSERT INTO assignments'\
              '(assignments_id, title, description, due_date, submitted_code_mark, oral_mark)'\
              ' VALUES (%s, %s, %s, %s, %s, %s)')
Add_student= ('INSERT INTO students'\
              '(stud_id, first_name, last_name, birthdate, fees)'\
              ' VALUES (%s, %s, %s, %s, %s)')
add_student_per_course= ('INSERT INTO courseregistrations'\
                         '(stud_id, course_id)'\
                         ' VALUES (%s, %s)')

add_assignment_per_student_per_course = ('INSERT INTO coursework'\
                                         '(assignments_id,course_id)'\
                                         'VALUES (%s, %s)')


# 2 : values
from dateutil.parser import parse
print("Let's start off with the assignment.")
time.sleep(2)
assignments_id = input("Give the assignment's id: ")
if assignments_id == '':
    import random
    random_identifiers = list(range(1006000,1007000))
    random.shuffle(random_identifiers)
    assignments_id = random.sample(random_identifiers, 1)
    assignments_id = str(assignments_id).strip('[]')
while not assignments_id.isdigit():
    assignments_id = input("Give the assignment's id: ")
else:
    pass
if assignments_id.isdigit():
    assignments_id = int(assignments_id)
title = input("Give the title: ")
if title == '':
    import random
    random_titles = ['Power Calculator.', 'Return the Sum of Two Numbers.','Return Negative.', 'Is it Time for Milk and Cookies?', 'Length of Number', 'Solve the Equation.']
    random.shuffle(random_titles)
    title = random.sample(random_titles, 1)
    title = str(title).strip('[]')
description = input('Give the description: ')
if description == '':
    description = 'Elaborate on the topic.'
try:
    due_date = parse(input("Please enter the date of submission in the format (m-d-y): "))
except ValueError:
    import random
    random_dates=['11/12/2022','3/6/2022','12/8/2022','1/1/2022','6/5/2022','7/9/2022','4/6/2022','12/27/2022', '12/26/2022', '5/15/2022']
    random.shuffle(random_dates)
    due_date = random.choice(random_dates)
    due_date = parse(due_date)
    month = due_date.strftime("%m")
    month = int(month)
    day = due_date.strftime("%d")
    day = int(day)
    year = due_date.strftime("%Y")
    year = int(year)
    pass
else:
    due_date = str(due_date)
    due_date = parse(due_date)
    month = due_date.strftime("%m")
    month = int(month)
    day = due_date.strftime("%d")
    day = int(day)
    year = due_date.strftime("%Y")
    year = int(year)
    pass
submitted_code_mark = input("Give the mark for the submitted code: ")
if submitted_code_mark == '':
    submitted_code_mark = '100'
while not submitted_code_mark.isdigit():
    submitted_code_mark = input("Give the mark for the submitted code: ")
else: 
    pass
if submitted_code_mark.isdigit():
    submitted_code_mark = int(submitted_code_mark)
        
oral_mark = input("Give the mark for the oral mark: ")
if oral_mark == '':
    import random
    random_oral_marks = list(range(5,95))
    random.shuffle(random_oral_marks)
    oral_mark = random.sample(random_oral_marks, 1)
    oral_mark = str(oral_mark).strip('[]')
while not oral_mark.isdigit():
    oral_mark = input("Give the mark for the oral mark: ")
else:
    pass
if oral_mark.isdigit():
    oral_mark = int(oral_mark)
print()
print("Nice work! Now, let's add the student information.")
time.sleep(2)
Stud_id = input("Give the student's id: ")
if Stud_id == '':
    import random
    random_identifiers = list(range(1000031,1000090))
    random.shuffle(random_identifiers)
    Stud_id = random.sample(random_identifiers, 1)
    Stud_id = str(Stud_id).strip('[]')
while not Stud_id.isdigit():
    Stud_id = input("Give the student's id: ")
else:
    pass
if Stud_id.isdigit():
    Stud_id = int(Stud_id)
First_name = input("Give the student's name: ")
if First_name == '':
    import random
    random_names=['Samantha', 'Kim','Oscar', 'Tom', 'Oz', 'Juliette', 'Diego', 'Jason', 'Carlos', 'Emilio', 'Selena ', 'Mariah','Demi', 'Ariana', 'Rihanna', 'Liam', 'Emma', 'Micaela', 'Hannah', 'Scarlett' ,'Isabella', 'Zoe', 'Camilla', 'Charlotte','Eliana', 'Nora', 'Penelope', 'Mateo', 'Alexander', 'Jack', 'Gabriel','Samuel', 'Matthew']
    random.shuffle(random_names)
    First_name = random.choice(random_names)
Last_name = input("Give the student's surname: ")
if Last_name == '':
    import random
    random_lastnames=['Johnson','Williams','Brown','Jones','Garcia','Miller','Davis','Lopez', 'Jackson', 'White']
    random.shuffle(random_lastnames)
    Last_name=random.choice(random_lastnames)
try:
    Birthdate = parse(input("Please enter the student's date of birth in format(m-d-y): "))
except ValueError:
    import random
    random_dates=['11/12/2003','3/6/2003','4/6/2004','12/27/2004', '12/26/2005', '5/15/2005']
    random.shuffle(random_dates)
    Birthdate = random.choice(random_dates)
    Birthdate = parse(Birthdate)
    month = Birthdate.strftime("%m")
    month = int(month)
    day = Birthdate.strftime("%d")
    day = int(day)
    year = Birthdate.strftime("%Y")
    year = int(year)
else:
    Birthdate = str(Birthdate)
    Birthdate = parse(Birthdate)
    month = b= Birthdate.strftime("%m")
    month = int(month)
    day = Birthdate.strftime("%d")
    day = int(day)
    year = Birthdate.strftime("%Y")
    year = int(year)
    pass
Fees = input(("Give the student's tuition fees: "))
if Fees =='':
    import random
    random_fees = ['1010','1600','1800','850','1543','2123','1780','2100', '1503', '1450']
    random.shuffle(random_fees)
    Fees = random.choice(random_fees)
while not Fees.isdigit():
    Fees = input("Give the student's tuition fees: ")
else:
    pass
if Fees.isdigit():
    Fees = int(Fees)
Title = input("Give the course's title? ")
if Title == 'CB13FTPY':
    C_id = 5870140
        
if Title == 'CB13PTPY':
    C_id = 5870141
        
if Title == 'CB13FTC':
    C_id = 5870142
        
if Title == 'CB13PTC':
    C_id = 5870143
        
if Title == 'CB13FTJV':
    C_id = 5870144
        
if Title == 'CB13PTJV':
    C_id = 5870145
        
if Title == 'CB13FTJS':
    C_id = 5870146
        
if Title == 'CB13PTJS':
    C_id = 5870147
        
if Title != 'CB13FTPY' and Title !='CB13PTPY' and Title !='CB13FTC' and Title !='CB13PTC' and Title != 'CB13FTJV' and Title != 'CB13PTJV' and Title != 'CB13FTJS':
    import random
    random_titles=['CB13FTPY', 'CB13PTPY', 'CB13FTC', 'CB13PTC', 'CB13FTJV', 'CB13PTJV', 'CB13FTJS', 'CB13PTJS']
    random.shuffle(random_titles)
    Title = random.choice(random_titles)
    if Title == 'CB13FTPY':
        C_id = 5870140
            
    if Title == 'CB13PTPY':
        C_id = 5870141
            
    if Title == 'CB13FTC':
        C_id = 5870142
            
    if Title == 'CB13PTC':
        C_id = 5870143
            
    if Title == 'CB13FTJV':
        C_id = 5870144
            
    if Title == 'CB13PTJV':
        C_id = 5870145
            
    if Title == 'CB13FTJS':
        C_id = 5870146
            
    if Title == 'CB13PTJS':
        C_id = 5870147
    
    
    
        
    assignment_data = (assignments_id,title, description, datetime.date(year,month,day), submitted_code_mark, oral_mark)
    print(assignment_data)
    
    Student_data = (Stud_id, First_name, Last_name, datetime.date(year,month,day), Fees)
    print(Student_data)
    
    S_id = Stud_id
    student__per_course_data = (S_id, C_id)
    print(student__per_course_data)
    
    coursework_data = (assignments_id, C_id)
    print(coursework_data)

    
    #3: Combine
    myCursor.execute(add_assignment, assignment_data)
    conn.commit()

    myCursor.execute(Add_student, Student_data)
    conn.commit()

    myCursor.execute(add_student_per_course, student__per_course_data)
    conn.commit()
    
    myCursor.execute(add_assignment_per_student_per_course, coursework_data)
    conn.commit()
    
    #Closing my connection and cursor
    myCursor.close()
    conn.close()
