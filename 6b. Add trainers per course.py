import mysql.connector

conn = mysql.connector.connect(host='localhost', user='root', passwd='MyNewPass', database='private_school')

myCursor = conn.cursor()

# 1 : queries
Add_trainer = ('INSERT INTO trainers'\
              '(tr_id, first_name, last_name)'\
              ' VALUES (%s, %s, %s)')
add_trainer_per_course= ('INSERT INTO teaching'\
                         '(tr_id, course_id)'\
                         ' VALUES (%s, %s)')

# 2 : values
print("You are going to add two trainers per course.")
for x in range(2):
    print()
    tr_id = input("Give the trainer's id: ")
    if tr_id == '':
        import random
        random_identifiers = list(range(1000601,1000800))
        random.shuffle(random_identifiers)
        tr_id = random.sample(random_identifiers, 1)
        tr_id = str(tr_id).strip('[]')
    while not tr_id.isdigit():
        tr_id = input("Give the trainer's id: ")
    else:
        pass
    if tr_id.isdigit():
        tr_id = int(tr_id)
    first_name = input("Give the trainer's name: ")
    if first_name == '':
        import random
        random_names = ['Samantha', 'Kim','Oscar', 'Tom', 'Oz', 'Juliette', 'Diego', 'Jason', 'Carlos', 'Emilio', 'Selena ', 'Mariah','Demi', 'Ariana', 'Rihanna', 'Liam', 'Emma', 'Micaela', 'Hannah', 'Scarlett' ,'Isabella', 'Zoe', 'Camilla', 'Charlotte','Eliana', 'Nora', 'Penelope', 'Mateo', 'Alexander', 'Jack', 'Gabriel','Samuel', 'Matthew']
        random.shuffle(random_names)
        first_name = random.choice(random_names)
    last_name = input("Give the trainer's surname: ")
    if last_name == '':
        import random
        random_lastnames = ['Johnson','Williams','Brown','Jones','Garcia','Miller','Davis','Lopez', 'Jackson', 'White']
        random.shuffle(random_lastnames)
        last_name = random.choice(random_lastnames)
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
    trainer_data = (tr_id, first_name,last_name)
    print(trainer_data)
    myCursor.execute(Add_trainer, trainer_data)
    conn.commit()
    trainer__per_course_data = (tr_id, C_id)
    print(trainer__per_course_data)
    myCursor.execute(add_trainer_per_course, trainer__per_course_data)
    conn.commit()
    #Closing my connection and cursor
    myCursor.close()
    conn.close()