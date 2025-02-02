from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
print("1")
Base = declarative_base()
print("2")
class Client(Base):
    __tablename__ = 'Client'
    id = Column(Integer, primary_key=True, autoincrement=True)
    FirstName = Column(String(255))
    LastName = Column(String(255))
    user_id = Column(String(255))
    Age = Column(String(255))
print("3")
engine = create_engine('mysql+mysqlconnector://soham:soham@127.0.0.1/python_projects')
print("4")
Base.metadata.create_all(engine)
print("Table 'Client' is ready (if it didn't already exist).")
print("5")
Session = sessionmaker(bind=engine)
print("6")
def insert_data(FirstName, LastName, user_id, Age):
    session = Session()  
    new_client = Client(
        FirstName=FirstName,
        LastName=LastName,
        user_id=user_id,
        Age=Age
    )
    session.add(new_client) 
    session.commit()         
    print("Data has been inserted successfully!")
    session.close()          
print("7")
import sys

def main():
    print("Step 1: Starting the program...", flush=True)
    print("4", flush=True)  # This will print 4 and flush immediately
    print("Step 2: Printed 4. Now waiting for user input.", flush=True)
    
    # This input() call may be waiting for your input.
    user_input = input("Please enter your name: ")
    
    print("Step 3: Received input:", user_input, flush=True)
    print("Step 4: Continuing the program...", flush=True)

if __name__ == "__main__":
    main()
print("8")