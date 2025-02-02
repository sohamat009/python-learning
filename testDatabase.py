import mysql.connector
from mysql.connector import Error


connection = mysql.connector.connect(
    host='localhost',  # Replace with your database host
    user='soham',  # Replace with your database username
    password='soham',  # Replace with your database password
    database='test'  # Replace with your database name
)

# Optional: Get server information
db_info = connection.get_server_info()
print("MySQL Server version:", db_info)

# Optional: Create a cursor and execute a query
cursor = connection.cursor()
cursor.execute("SELECT DATABASE();")
record = cursor.fetchone()
print("You're connected to the database:", record)


cursor.close()
connection.close()
print("MySQL connection is closed.")