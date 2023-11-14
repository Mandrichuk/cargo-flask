import sqlite3 
import os

# a = 2.9

# a = int(a)


# a = int(a)
# a = 

if os.path.exists("Cargo.db"):
    os.remove("Cargo.db")

with sqlite3.connect("Cargo.db") as connect:
    cursor = connect.cursor()
    cursor.execute('PRAGMA foreign_keys = ON;')


    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Providers(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        NAME TEXT NOT NULL, 
        PHONE TEXT NOT NULL);
    """)

    prov =  [('ANTON', '+232323'), ('VASIA' ,'+98989898'), ('PUPKIN' ,'+45454545')]
    prod = [(1, 'PUMPIN', 700, 'image.jpg'), (2, 'KARROT', 12, 'image.jpg'), (3, 'APPLE', 100, 'image.jpg'), (1, 'ORANGE', 48, 'image.jpg'), (2, 'PINEAPPLE', 200, 'image.jpg'), (3, 'NUGGETS', 5, 'image.jpg')]
    
    cursor.executemany("""
        INSERT INTO Providers (NAME, PHONE) VALUES (?, ?);""", prov)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Products(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        PROVIDER_ID INTEGER,
        NAME TEXT NOT NULL,
        PRICE INTEGER NOT NULL,
        IMAGE TEXT NOT NULL,
        FOREIGN KEY (PROVIDER_ID) REFERENCES Providers(ID) ON DELETE CASCADE
    );
    """)

    cursor.executemany("""
        INSERT INTO Products (PROVIDER_ID, NAME, PRICE, IMAGE) VALUES (?, ?, ?, ?);""", 
        prod)

    connect.commit()
