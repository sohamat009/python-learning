
import mysql.connector

def create_table_if_not_exists():
    conn = mysql.connector.connect(
        host="127.0.0.1",
        user="soham",
        password="soham",
        database="python_projects"
    )
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Client (
            id INT AUTO_INCREMENT PRIMARY KEY,
            FirstName VARCHAR(255),
            LastName VARCHAR(255),
            user_id VARCHAR(255),
            Age VARCHAR(255)
        )
    ''')
    print("Table 'Client' is ready")
    conn.close()

def insert_data(FirstName, LastName, user_id, Age):
    create_table_if_not_exists()
    conn = mysql.connector.connect(
        host="127.0.0.1",
        user="soham",
        password="soham",
        database="python_projects"
    )
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO Client (FirstName, LastName, user_id, Age)
        VALUES (%s, %s, %s, %s)
    ''', (FirstName, LastName, user_id, Age))

    conn.commit() 
    print("Data has been inserted successfully!")
    conn.close()

def main():
    print("Enter the following details:")
    FirstName = input("First Name: ")
    LastName = input("Last Name: ")
    user_id = input("User ID: ")
    Age = input("Age: ")

    insert_data(FirstName, LastName, user_id, Age)

if __name__ == "__main__":
    main()
