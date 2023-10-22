import sqlite3 

with sqlite3.connect("Cargo.db") as connect:
    cursor = connect.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Providers(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        NAME TEXT NOT NULL,
        PHONE TEXT NOT NULL)
    """)

    prov =  [('ANTON', '+232323'), ('VASIA' ,'+98989898'), ('PUPKIN' ,'+45454545')]
    prod = [(1, 'PUMPIN', 22), (2, 'KARROT', 72), (3, 'APPLE', 12), 
        (1, 'ORANGE', 3), (2, 'PINEAPPLE', 82), (3, 'NUGGETS', 2)]
    

    
    cursor.executemany("""
        INSERT INTO Providers (NAME, PHONE) VALUES (?, ?)""", prov)


    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Products(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        PROVIDER_ID INTEGER NOT NULL,
        NAME TEXT NOT NULL,
        PRICE INTEGER NOT NULL)
    """)

    cursor.executemany("""
        INSERT INTO Products (PROVIDER_ID, NAME, PRICE) VALUES (?, ?, ?)""", prod
        )

    connect.commit()