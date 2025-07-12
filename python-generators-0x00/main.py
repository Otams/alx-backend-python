#!/usr/bin/python3

import seed  # This assumes your seed.py and main.py are in the same folder

# Step 1: Connect to MySQL server (without specifying a database yet)
connection = seed.connect_db()
if connection:
    # Step 2: Create the ALX_prodev database if it doesn't already exist
    seed.create_database(connection)
    connection.close()
    print("✅ Connection successful and database checked.")

    # Step 3: Now connect to the ALX_prodev database specifically
    connection = seed.connect_to_prodev()

    if connection:
        # Step 4: Create the user_data table if it doesn't exist
        seed.create_table(connection)

        # Step 5: Insert data from the CSV file into the user_data table
        seed.insert_data(connection, "user_data.csv")
