# Here's a basic example of how to connect to a MySQL database, create a table, and insert data:

import mysql.connector

# Connect to the MySQL database
conn = mysql.connector.connect(
    host='localhost',
    user='your_username',
    password='your_password',
    database='your_database'
)

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

# Create a table
create_table_query = """
CREATE TABLE customers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    email VARCHAR(255)
)
"""
cursor.execute(create_table_query)

# Insert data into the table
insert_data_query = """
INSERT INTO customers (name, email) VALUES (%s, %s)
"""
data = [("John", "john@example.com"), ("Jane", "jane@example.com")]
cursor.executemany(insert_data_query, data)

# Commit the changes and close the connection
conn.commit()
conn.close()