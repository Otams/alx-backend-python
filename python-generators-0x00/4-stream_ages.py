import mysql.connector

def stream_user_ages():
    """Generator to stream ages from user_data table one by one"""
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='your_password',  # Replace with your MySQL password
        database='ALX_prodev'
    )
    cursor = connection.cursor()
    cursor.execute("SELECT age FROM user_data")

    for (age,) in cursor:
        yield float(age)  # convert to float if age was stored as DECIMAL

    cursor.close()
    connection.close()


def calculate_average_age():
    """Calculate average using the generator (stream_user_ages)"""
    total = 0
    count = 0

    for age in stream_user_ages():  # first and only loop
        total += age
        count += 1

    if count == 0:
        print("No users found.")
    else:
        average = total / count
        print(f"Average age of users: {average:.2f}")


# Run
if __name__ == "__main__":
    calculate_average_age()
