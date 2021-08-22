import mysql.connector

conn = mysql.connector.connect(host='localhost', user='root', passwd='MyNewPass', database='private_school')

myCursor = conn.cursor()
# 1 : query
add_trainer = ('INSERT INTO trainers'\
              '(tr_id, first_name, last_name)'\
              ' VALUES (%s, %s, %s)')

print("You are going to add two trainers.")
# 2 : values
for x in range(2):
    print()
    tr_id = input("Give the trainer's id: ")
    if tr_id == '':
        import random
        random_identifiers = list(range(1000533,1000600))
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
        
    trainer_data = (tr_id, first_name,last_name)
    print(trainer_data)
    
    #3: Combine
    myCursor.execute(add_trainer, trainer_data)
    conn.commit()
    #Closing my connection and cursor
    myCursor.close()
    conn.close()