from database import get_db_connection

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
      