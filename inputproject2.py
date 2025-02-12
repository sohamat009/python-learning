from sqlalchemy import create_engine, text
HOST = "localhost"
USER = "soham"
PASSWORD = "soham"
DATABASE = "python_projects"
engine = create_engine(f"mysql+pymysql://{USER}:{PASSWORD}@{HOST}/{DATABASE}", echo=False)
with engine.connect() as conn:
    client_id = int(input("Client ID: "))
    first_name = input("First Name: ").strip()
    last_name = input("Last Name: ").strip()
    city = input("City: ").strip()
    postal_code = int(input("Postal Code: "))
    country = input("Country: ").strip()

    conn.execute(text(
        "INSERT INTO client (ClientID, FirstName, LastName, City, PostalCode, Country) "
        "VALUES (:id, :fname, :lname, :location, :zip_code, :nation)"
    ), {
        "id": client_id,
        "fname": first_name,
        "lname": last_name,
        "location": city,
        "zip_code": postal_code,
        "nation": country,
    })

    conn.commit()
    print("Data successfully inserted!")
