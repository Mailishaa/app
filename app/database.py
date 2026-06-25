import sqlite3 
from contextlib import contextmanager

sqlite_database="school.db"

@contextmanager
def get_db_connection():
    connection=sqlite3.connect(sqlite_database)
    connection.row_factory=sqlite3.Row
    try: # exception handling
        yield connection #connect and hold the connection
    finally:
        connection.close()

def create_table():# this code aquires a connection 
    with get_db_connection()as connection:
        connection.execute('''CREATE TABLE IF NOT EXISTS students(
                           id INTEGER PRIMARY KEY AUTOINCREMENT,
                           name TEXT NOT NULL,
                           age INTEGER NOT NULL,
                           email TEXT NOT NULL,
                           country TEXT NOT NULL,
                           id_number INTEGER NOT NULL)''')
        connection.execute('''CREATE TABLE IF NOT EXISTS teachers(
                           id INTEGER PRIMARY KEY AUTOINCREMENT,
                           name TEXT NOT NULL,
                           tsc_number INTEGER NOT NULL,
                           email TEXT NOT NULL,
                           course TEXT NOT NULL,
                           years_of_experience INTEGER NOT NULL)''')
        
        connection.execute('''CREATE TABLE IF NOT EXISTS courses(
                           id INTEGER PRIMARY KEY AUTOINCREMENT,
                           name TEXT NOT NULL,
                           topics INTEGER NOT NULL,                            
                           course_teacher  TEXT NOT NULL,
                           duration TEXT NOT NULL,
                           is_online BOOLEAN NOT NULL)''')
def add_student(name, age, email, country, id_number):
    with get_db_connection()as connection:
        connection.execute(
            'INSERT INTO students(name,age,email,country,id_number) VALUES (?,?,?,?,?)',
            (name, age, email, country, id_number),
        )
        connection.commit()
def get_students():
    with get_db_connection()as connection:
        return connection.execute('SELECT* FROM students').fetchall()
    
def update_student(old_id_number, name, age, email, country, new_id_number):
    with get_db_connection() as connection:
        connection.execute(
            '''UPDATE students 
               SET name = ?, age = ?, email = ?, country = ?, id_number = ? 
               WHERE id_number = ?''',
            (name, age, email, country, new_id_number, old_id_number)
        )
        connection.commit()

def delete_student(id_number):
    with get_db_connection() as connection:
        connection.execute('DELETE FROM students WHERE id_number = ?', (id_number,))
        connection.commit()
    

    

def add_teacher(name, course, email, tsc_number,years_of_experience):
     with get_db_connection()as connection:
        connection.execute(
             'INSERT INTO teachers(name,course,email, tsc_number,years_of_experience) VALUES (?,?,?,?,?)',
           (name, course, email, tsc_number,years_of_experience),
        )
        connection.commit()
def get_teachers():
    with get_db_connection()as connection:
        return connection.execute('SELECT* FROM teachers').fetchall()
def update_teacher(old_tsc_number, name, course, email, new_tsc_number, years_of_experience):
    with get_db_connection() as connection:
        connection.execute(
            '''UPDATE teachers 
               SET name = ?, course = ?, email = ?, tsc_number = ?, years_of_experience = ? 
               WHERE tsc_number = ?''',
            (name, course, email, new_tsc_number, years_of_experience, old_tsc_number)
        )
        connection.commit()

def delete_teacher(tsc_number):
    with get_db_connection() as connection:
        connection.execute('DELETE FROM teachers WHERE tsc_number = ?', (tsc_number,))
        connection.commit()
    


def add_course(name, topics, duration, course_teacher,is_online):
    with get_db_connection()as connection:
        connection.execute(
            'INSERT INTO courses(name, topics, duration, course_teacher,is_online) VALUES (?,?,?,?,?)',          
                (name, topics, duration, course_teacher,is_online), 
        ) 
        connection.commit()
def get_courses():
        with get_db_connection()as connection:
         return connection.execute('SELECT* FROM courses').fetchall()
def update_course(old_name, name, topics, is_online, course_teacher, duration):
    with get_db_connection() as connection:
        connection.execute(
            '''UPDATE courses 
               SET name = ?, topics = ?, is_online = ?, course_teacher = ?, duration = ? 
               WHERE name = ?''',
            (name, topics, is_online, course_teacher, duration, old_name)
        )
        connection.commit()

def delete_course(name):
    with get_db_connection() as connection:
        connection.execute('DELETE FROM courses WHERE name = ?', (name,))
        connection.commit()
    