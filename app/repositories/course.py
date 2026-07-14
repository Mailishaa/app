from database import get_db_connection
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
    courses=get_courses ()
    return [dict(course) for course in courses]  
def add_course (name, topics, is_online, course_teacher, duration):
    with get_db_connection() as connection:
        connection.execute(
            'INSERT INTO courses (name, topics, is_online, course_teacher, duration) VALUES (?,?,?,?,?)'
            (name, topics, is_online, course_teacher, duration)
        )
        connection.commit()