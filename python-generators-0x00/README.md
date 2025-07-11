# Python Database Seeder - `seed.py`

This project sets up and seeds a MySQL database named **`ALX_prodev`** using a Python script and a CSV file containing user data.

## Features

- Connects to MySQL server
- Creates a database `ALX_prodev` if it doesn't already exist
- Creates a `user_data` table with the following fields:
  - `user_id` (UUID, Primary Key)
  - `name` (VARCHAR, NOT NULL)
  - `email` (VARCHAR, NOT NULL)
  - `age` (DECIMAL, NOT NULL)
- Populates the table with entries from `user_data.csv`
- Prints a preview of the first 5 rows from the `user_data` table

## 📂 Project Structure

python-generators-0x00/
│
├── seed.py # Python script to create and populate the database
├── user_data.csv # Sample user data in CSV format
└── README.md # Project documentation (this file)


## 🧪 Sample Output

```bash
Sample Data from user_data:
('00234e50-34eb-4ce2-94ec-26e3fa749796', 'Dan Altenwerth Jr.', 'Molly59@gmail.com', 67)
('006bfede-724d-4cdd-a2a6-59700f40d0da', 'Glenda Wisozk', 'Miriam21@gmail.com', 119)
('006e1f7f-90c2-45ad-8c1d-1275d594cc88', 'Daniel Fahey IV', 'Delia.Lesch11@hotmail.com', 49)
('00af05c9-0a86-419e-8c2d-5fb7e899ae1c', 'Ronnie Bechtelar', 'Sandra19@yahoo.com', 22)
('00cc08cc-62f4-4da1-b8e4-f5d9ef5dbbd4', 'Alma Bechtelar', 'Shelly_Balistreri22@hotmail.com', 102)

✅ Prerequisites
Python 3.x

MySQL Server installed and running

VS Code or any Python IDE

Install MySQL connector for Python:pip install mysql-connector-python

Running the Script
Ensure user_data.csv is placed in the same directory as seed.py.

Open your terminal or command prompt.

Run the script using: python seed.py

If the database and table are successfully created and seeded, you’ll see the first 5 rows printed out.

Function Breakdown
connect_db(): Connects to the MySQL server

create_database(connection): Creates the ALX_prodev database

connect_to_prodev(): Connects specifically to the ALX_prodev database

create_table(connection): Creates the user_data table if it doesn't exist

insert_data(connection, csv_file): Loads user data from a CSV file


