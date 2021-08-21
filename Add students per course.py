import mysql.connector

conn = mysql.connector.connect(host='localhost', user='root', passwd='MyNewPass', database='private_school')

myCursor = conn.cursor()

# 2 : queries
Add_student= ('INSERT INTO students'\
              '(stud_id, first_name, last_name, birthdate, fees)'\
              ' VALUES (%s, %s, %s, %s, %s)')
add_student_per_course= ('INSERT INTO courseregistrations'\
                         '(stud_id, course_id)'\
                         ' VALUES (%s, %s)')

print("You are going to add two students per course.")
# 2 : values
for i in range(2):
    import datetime
    from dateutil.parser import parse
    print()
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

    #3: Combine
    Student_data = (Stud_id, First_name, Last_name, datetime.date(year,month,day), Fees)
    print(Student_data)
    myCursor.execute(Add_student, Student_data)
    conn.commit()
    S_id = Stud_id
    student__per_course_data = (S_id, C_id)
    print(student__per_course_data)
    myCursor.execute(add_student_per_course, student__per_course_data)
    conn.commit()
    #Closing my connection and cursor
    myCursor.close()
    conn.close()
