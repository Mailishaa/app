from database import get_db_connection
def create_table():
    with get_db_connection()as connection:
         connection.execute('''CREATE TABLE IF NOT EXISTS teachers(
                           id INTEGER PRIMARY KEY AUTOINCREMENT,
                           name TEXT NOT NULL,
                           tsc_number INTEGER NOT NULL,
                           email TEXT NOT NULL,
                           course TEXT NOT NULL,
                           years_of_experience INTEGER NOT NULL)''')