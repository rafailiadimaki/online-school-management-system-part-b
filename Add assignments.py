import mysql.connector
import datetime

conn = mysql.connector.connect(host='localhost', user='root', passwd='MyNewPass', database='private_school')

myCursor = conn.cursor()

# 1 : query
add_assignment = ('INSERT INTO assignments'\
              '(assignments_id, title, description, due_date, submitted_code_mark, oral_mark)'\
              ' VALUES (%s, %s, %s, %s, %s, %s)')

# 2 : values
print("You are going to add two assignments.")
for y in range(2):
    from dateutil.parser import parse
    print()
    assignments_id = input("Give the assignment's id: ")
    if assignments_id == '':
        import random
        random_identifiers = list(range(1005823,1005900))
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
        
    assignment_data = (assignments_id,title, description, datetime.date(year,month,day), submitted_code_mark, oral_mark)
    print(assignment_data)
    
    # 3 : combine
    myCursor.execute(add_assignment, assignment_data)
    conn.commit()
    #Closing my connection and cursor
    myCursor.close()
    conn.close()