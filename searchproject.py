from sqlalchemy import create_engine, text
HOST = "Localhost"
USER = "soham"
PASSWORD = "soham"
DATABASE = "python_projects"

connection_string = f"mysql+pymysql://{USER}:{PASSWORD}@{HOST}/{DATABASE}"
engine = create_engine(connection_string)

with engine.connect() as conn:
    First_Name = input("Enter the First Name: ").strip()
    result = conn.execute(text("SELECT * from client WHERE FirstName = :fname"), {"fname": First_Name})

    row = result.first()
    if row:
        print(row) 
    else:
        print("No records found!")