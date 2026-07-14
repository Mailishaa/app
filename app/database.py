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


       
        

    

    

    

    