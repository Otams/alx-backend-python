import mysql.connector
from mysql.connector import Error
import csv
import uuid

# 1. Connect to MySQL server (not yet to a specific database)
def connect_db():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password="Otam'striumph@20" 
        )
        if connection.is_connected():
            return connection
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None

# 2. Create the ALX_prodev database if it doesn't exist
def create_database(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS ALX_prodev")
        cursor.close()
        print("Database ALX_prodev created or already exists")
    except Error as e:
        print(f"Error creating database: {e}")

# 3. Connect specifically to the ALX_prodev database
def connect_to_prodev():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='your_password',
            database='ALX_prodev'
        )
        if connection.is_connected():
            return connection
    except Error as e:
        print(f"Error connecting to ALX_prodev: {e}")
        return None

# 4. Create the user_data table
def create_table(connection):
    try:
        cursor = connection.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS user_data (
                user_id VARCHAR(36) NOT NULL PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                email VARCHAR(255) NOT NULL,
                age DECIMAL(5,2) NOT NULL,
                INDEX (user_id)
            )
        ''')
        connection.commit()
        cursor.close()
        print("Table user_data created successfully")
    except Error as e:
        print(f"Error creating table: {e}")

# 5. Insert data from user_data.csv

def insert_data(connection, file_path):
    try:
        cursor = connection.cursor()
        with open(file_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                cursor.execute('''
                    INSERT INTO user_data (user_id, name, email, age)
                    VALUES (%s, %s, %s, %s)
                    ON DUPLICATE KEY UPDATE email=email
                ''', (
                    row['user_id'],
                    row['name'],
                    row['email'],
                    row['age']
                ))
        connection.commit()
        cursor.close()
        print("Data inserted successfully from CSV")
    except Error as e:
        print(f"Error inserting data: {e}")
