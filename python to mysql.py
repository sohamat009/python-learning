import mysql.connector
from tabulate import tabulate
print("before conn")
# Connect to the MySQL databaseso
print ("before connection")
def connect_to_db():
    try:
        print("o.1")
        connection = mysql.connector.connect(
            host="localhost",       
            user="soham",   
            password="soham", 
            database="soham" 
        )
        print("1.0")
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

# Fetch records based on first or last name
def fetch_records(name):
    connection = connect_to_db()
    if not connection:
        return

    try:
        cursor = connection.cursor()
        query = """
        SELECT * FROM your_table_name
        WHERE firstname LIKE %s OR lastname LIKE %s
        """
        cursor.execute(query, (f"%{name}%", f"%{name}%"))
        records = cursor.fetchall()

        # Get column names
        column_names = [desc[0] for desc in cursor.description]

        if records:
            # Display data in table format
            print(tabulate(records, headers=column_names, tablefmt="pretty"))
        else:
            print("No matching records found.")

    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        connection.close()

# Main program
if __name__ == "__main__":
    name = input("Enter the first name or last name to search: ")
    fetch_records(name)
