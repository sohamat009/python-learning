from sqlalchemy import create_engine, text
print("1")
HOST = "Localhost"
USER = "soham"
PASSWORD = "soham"
DATABASE = "python_projects"
print("2")
connection_string = f"mysql+pymysql://{USER}:{PASSWORD}@{HOST}/{DATABASE}"
engine = create_engine(connection_string)
print("3")
with engine.connect() as conn:
    conn.execute(text(f"insert into client ( ClientID, FirstName, LastName, City, PostalCode, Country) values (4, 'Mahesh', 'Lahare', 'Thane', 400603, 'India');"))
    '''conn.commit()'''
    print("Data is successfully enterd")
