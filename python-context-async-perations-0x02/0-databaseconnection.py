import mysql.connector

class DatabaseConnection:
    def __init__(self, host, user, password, database):
        self.config = {
            'host': host,
            'user': user,
            'password': password,
            'database': database
        }
        self.connection = None

    def __enter__(self):
        """Establish and return the database connection"""
        self.connection = mysql.connector.connect(**self.config)
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Ensure the connection is closed"""
        if self.connection and self.connection.is_connected():
            self.connection.close()
            print("✅ Database connection closed")


# Usage Example
if __name__ == "__main__":
    with DatabaseConnection(
        host='localhost',
        user='root',
        password='your_password',  
        database='ALX_prodev'
    ) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users")
        rows = cursor.fetchall()

        for row in rows:
            print(row)

        cursor.close()
