from sqlalchemy import create_engine, text
print("1")
HOST = "localhost"  
USER = "soham"      
PASSWORD = "soham"  
print("2")
connection_string = f"mysql+pymysql://{USER}:{PASSWORD}@{HOST}"
print("3")
try:
    engine = create_engine(connection_string)

    with engine.connect() as connection:
        # Execute a query to list all databases
        result = connection.execute(text("SHOW DATABASES"))

        # Print database names
        print("Databases on the server:")
        for row in result:
            print(row[0])
            print("4")
except Exception as e:
    print(f"An error occurred: {e}")
    print("5")