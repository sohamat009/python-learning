import mysql.connector
from mysql.connector import Error
import logging

logging.basicConfig(
    level=logging.DEBUG,  # Set the logging level
    format='%(asctime)s - %(levelname)s - %(message)s',  # Define the log format
    filename='app.log',  # Log messages to a file (optional)
    filemode='a'  # Append mode (use 'w' to overwrite the file each time)
)

print("1")
# Establishing a connection to the MySQL server
try:
    connection = mysql.connector.connect(
        host = "192.168.0.105", 
        user = "soham",      
        password = "soham"
    )
except Error as e:
    print(e)
print("2")
cursor = connection.cursor()
print("3")
cursor.execute("SHOW DATABASES")
print("cursor")
