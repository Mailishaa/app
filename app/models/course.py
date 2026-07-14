from database import get_db_connection

def create_table():
    with get_db_connection()as connection:
        connection.execute('''CREATE TABLE IF NOT EXISTS courses(
         id INTEGER PRIMARY KEY AUTOINCREMENT,
         name TEXT NOT NULL,
         topics INTEGER NOT NULL,                            
         course_teacher  TEXT NOT NULL,
         duration TEXT NOT NULL,
         is_online BOOLEAN NOT NULL)''')