import mysql.connector

conn = mysql.connector.connect(host='localhost', user='root', passwd='MyNewPass', database='private_school')

myCursor = conn.cursor()

# 1 : query
add_student= ('INSERT INTO students'\
              '(stud_id, first_name, last_name, birthdate, fees)'\
              ' VALUES (%s, %s, %s, %s, %s)')

# 2 : values
print("You are going to add two students.")
for i in range(2):
    import datetime
    from dateutil.parser import parse
    print()
    stud_id = input("Give the student's id: ")
    if stud_id == '':
        import random
        random_identifiers = list(range(1000015,1000030))
        random.shuffle(random_identifiers)
        stud_id = random.sample(random_identifiers, 1)
        stud_id = str(stud_id).strip('[]')
    while not stud_id.isdigit():
        stud_id = input("Give the student's id: ")
    else:
        pass
    if stud_id.isdigit():
        stud_id = int(stud_id)
    first_name = input("Give the student's name: ")
    if first_name == '':
        import random
        random_names=['Samantha', 'Kim','Oscar', 'Tom', 'Oz', 'Juliette', 'Diego', 'Jason', 'Carlos', 'Emilio', 'Selena ', 'Mariah','Demi', 'Ariana', 'Rihanna', 'Liam', 'Emma', 'Micaela', 'Hannah', 'Scarlett' ,'Isabella', 'Zoe', 'Camilla', 'Charlotte','Eliana', 'Nora', 'Penelope', 'Mateo', 'Alexander', 'Jack', 'Gabriel','Samuel', 'Matthew']
        random.shuffle(random_names)
        first_name=random.choice(random_names)
    last_name = input("Give the student's surname: ")
    if last_name == '':
        import random
        random_lastnames=['Johnson','Williams','Brown','Jones','Garcia','Miller','Davis','Lopez', 'Jackson', 'White']
        random.shuffle(random_lastnames)
        last_name=random.choice(random_lastnames)
    try:
        birthdate = parse(input("Please enter the student's date of birth in format(m-d-y): "))
    except ValueError:
        import random
        random_dates=['11/12/2003','3/6/2003','4/6/2004','12/27/2004', '12/26/2005', '5/15/2005']
        random.shuffle(random_dates)
        birthdate = random.choice(random_dates)
        birthdate = parse(birthdate)
        month = birthdate.strftime("%m")
        month = int(month)
        day = birthdate.strftime("%d")
        day = int(day)
        year = birthdate.strftime("%Y")
        year = int(year)
    else:
        birthdate = str(birthdate)
        birthdate = parse(birthdate)
        month = birthdate.strftime("%m")
        month = int(month)
        day = birthdate.strftime("%d")
        day = int(day)
        year = birthdate.strftime("%Y")
        year = int(year)
        pass
    fees = input(("Give the student's tuition fees: "))
    if fees =='':
        import random
        random_fees = ['1010','1600','1800','850','1543','2123','1780','2100', '1503', '1450']
        random.shuffle(random_fees)
        fees = random.choice(random_fees)
    while not fees.isdigit():
        fees = input("Give the student's tuition fees: ")
    else:
        pass
    if fees.isdigit():
        fees = int(fees)
        
    student_data = (stud_id, first_name,last_name, datetime.date(year,month,day), fees)
    print(student_data)
    
    #3: Combine
    myCursor.execute(add_student, student_data)
    conn.commit()
    #Closing my connection and cursor
    myCursor.close()
    conn.close()