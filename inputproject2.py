from sqlalchemy import create_engine, text

HOST = "localhost"
USER = "soham"
PASSWORD = "soham"
DATABASE = "python_projects"

engine = create_engine(f"mysql+pymysql://{USER}:{PASSWORD}@{HOST}/{DATABASE}", echo=False)

with engine.connect() as conn:
    first_name = input("First Name: ").strip()
    last_name = input("Last Name: ").strip()
    city = input("City: ").strip()
    postal_code = int(input("Postal Code: "))
    country = input("Country: ").strip()

    check_query = text("""
        SELECT COUNT(*) FROM client 
        WHERE FirstName = :fname AND LastName = :lname
    """)
    result = conn.execute(check_query, {"fname": first_name, "lname": last_name}).scalar()

    if result > 0:
        print("Client with this name already exists in the Database.")
    else:
        insert_query = text("""
            INSERT INTO client (FirstName, LastName, City, PostalCode, Country)
            VALUES (:fname, :lname, :location, :zip_code, :nation)
        """)
        conn.execute(insert_query, {
            "fname": first_name,
            "lname": last_name,
            "location": city,
            "zip_code": postal_code,
            "nation": country
        })
        conn.commit()
        print("Data successfully inserted!")
