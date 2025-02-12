from sqlalchemy import create_engine, text
print("1")
HOST = "localhost"
USER = "soham"
PASSWORD = "soham"
DB = "client"
print("2")
connection_string = f"mysql+pymysql://{USER}:{PASSWORD}@{HOST}/{DB}"
engine = create_engine(connection_string)
print("3")
database_name = "client"
try:
    with engine.connect() as connection:
        connection.execute(text(f"insert into client_details ( lastname, firstname ) values ( 'indore' , 'nilesh' );"))
        connection.commit()
except Exception as e:
    print(f"An error occurred: {e}")
    print("4")
"""for row in result:
    print(row)"""

