from sqlalchemy import create_engine, text
print("1")
HOST = "localhost"
USER = "soham"
PASSWORD = "soham"
print("2")
connection_string = f"mysql+pymysql://{USER}:{PASSWORD}@{HOST}"
engine = create_engine(connection_string)
print("3")
database_name = "details"
try:
    with engine.connect() as connection:
        connection.execute(text(f"CREATE DATABASE {"details"}"))
    print(f"Database created successfully.")
except Exception as e:
    print(f"An error occurred: {e}")
    print("4")

