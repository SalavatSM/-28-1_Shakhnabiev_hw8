import sqlite3



def create_connection(db_name):
    connection = None
    try:
        connection = sqlite3.connect(db_name)
        return connection
    except sqlite3.Error as e:
        print(e)
    return connection


def create_table(connection, sql):
    try:
        cursor = connection.cursor()
        cursor.execute(sql)
    except sqlite3.Error as e:
        print(e)


def create_country(connection, countries):
    try:
        sql = '''INSERT INTO countries(title) VALUES (?)'''
        cursor = connection.cursor()
        cursor.execute(sql, countries)
        connection.commit()
    except sqlite3.Error as e:
        print(e)


def create_city(connection, cities):
    try:
        sql = '''INSERT INTO cities(title, area, country_id) VALUES (?, ?, ?)'''
        cursor = connection.cursor()
        cursor.execute(sql, cities)
        connection.commit()
    except sqlite3.Error as e:
        print(e)

def create_employee(connection, employees):
    try:
        sql = '''INSERT INTO employees(first_name, last_name, city_id) VALUES(?, ?, ?)'''
        cursor = connection.cursor()
        cursor.execute(sql, employees)
        connection.commit()
    except sqlite3.Error as e:
        print(e)


db_name = 'hw8.db'

countries = '''
CREATE TABLE countries (
id INTEGER PRIMARY KEY AUTOINCREMENT,
title TEXT NOT NULL) 
'''

cities = '''
CREATE TABLE cities (
id INTEGER PRIMARY KEY AUTOINCREMENT,
title TEXT NOT NULL,
area  FLOAT DEFAULT 0,
country_id INTEGER NOT NULL, 
FOREIGN KEY (country_id) REFERENCES countries (id)
)
'''

employees = '''
CREATE TABLE employees (
id INTEGER PRIMARY KEY AUTOINCREMENT,
first_name TEXT NOT NULL,
last_name TEXT NOT NULL,
city_id INTEGER NOT NULL, FOREIGN KEY (city_id) REFERENCES cities (id)
)
'''

connection_to_db = create_connection(db_name)
if connection_to_db is not None:
    print('Bingo! Successfully connected to data base!')

    # create_table(connection_to_db, countries)

    # create_country(connection_to_db, ('Kyrgyzstan', ))
    # create_country(connection_to_db, ('Kazakhstan', ))
    # create_country(connection_to_db, ('Turkey', ))


    # create_table(connection_to_db, cities)

    # create_city(connection_to_db, ('Biskek', 125, 1))
    # create_city(connection_to_db, ('Osh', 120, 1))
    # create_city(connection_to_db, ('Naryn', 80, 1))
    # create_city(connection_to_db, ('Almaty', 150, 2))
    # create_city(connection_to_db, ('Nursultan', 160, 2))
    # create_city(connection_to_db, ('Ankara', 140, 3))
    # create_city(connection_to_db, ('Istanbul', 190, 3))


    # create_table(connection_to_db, employees)

    # create_employee(connection_to_db, ('Artem', 'Kim', 1))
    # create_employee(connection_to_db, ('Bob', 'Smith', 1))
    # create_employee(connection_to_db, ('Tom', 'Black', 1))
    # create_employee(connection_to_db, ('Sveta', 'Krasnova', 2))
    # create_employee(connection_to_db, ('Oleg', 'Popov', 2))
    # create_employee(connection_to_db, ('Kim', 'In', 2))
    # create_employee(connection_to_db, ('Pavel', 'Belov', 3))
    # create_employee(connection_to_db, ('Ivan', 'Makarov', 3))
    # create_employee(connection_to_db, ('Ron', 'Bill', 3))
    # create_employee(connection_to_db, ('Bob', 'Chester', 4))
    # create_employee(connection_to_db, ('Rob', 'Alen', 4))
    # create_employee(connection_to_db, ('Cris', 'Brawn', 5))
    # create_employee(connection_to_db, ('Lia', 'Belova', 6))
    # create_employee(connection_to_db, ('Max', 'Humelth', 6))
    # create_employee(connection_to_db, ('Simon', 'Hill', 7))

    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute("SELECT id, title FROM cities")
    cities = cursor.fetchall()
    for city in cities:
        print(str(city[0]) + ' - ' + city[1])
    city_id = int(input(f"Вы можете отобразить список сотрудников по выбранному id города из перечня городов ниже, для выхода из программы введите 0 \n"))
    while city_id != 0:
        cursor.execute('''SELECT employees.first_name, employees.last_name countries.title, cities.title
                        FROM employees
                        JOIN cities ON employees.city_id = cities.id
                        JOIN countries ON cities.country_id = countries.id
                        WHERE cities.id = ?''', (city_id,))
        employees = cursor.fetcall()
        print('Employees in city:')
        for employee in employees:
            print(employee[0] + ' ' + employee[1] + ' - ' + employee[2] + ', ' + employee[3])
            city_id = int(input('Input id of city print list of employees or press 0 to exit: '))



    connection_to_db.close()
    print('ALL GOOD! Connection to data base closed!')
else:
    print('Connection failed')





