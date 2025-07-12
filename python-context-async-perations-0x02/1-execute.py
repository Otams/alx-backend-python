import mysql.connector

class ExecuteQuery:
    def __init__(self, query, params=None):
        self.query = query
        self.params = params or ()
        self.connection = None
        self.cursor = None

    def __enter__(self):
        """Connect to DB and execute the query"""
        self.connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='your_password',  # <-- Replace with your MySQL password
            database='ALX_prodev'
        )
        self.cursor = self.connection.cursor()
        self.cursor.execute(self.query, self.params)
        return self.cursor.fetchall()

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Close the cursor and connection"""
        if self.cursor:
            self.cursor.close()
        if self.connection and self.connection.is_connected():
            self.connection.close()
            print("✅ Query executed and connection closed.")


# Usage Example
if __name__ == "__main__":
    query = "SELECT * FROM user_data WHERE age > %s"
    param =
