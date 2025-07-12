import mysql.connector
from mysql.connector import Error

def stream_users(connection):
    """
    Generator function to yield user data one row at a time from the user_data table.
    """
    try:
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM user_data")
        for row in cursor:
            yield row
        cursor.close()
    except Error as e:
        print(f"Error while streaming users: {e}")
