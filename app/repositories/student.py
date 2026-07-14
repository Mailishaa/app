from database import get_db_connection

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