import os
import sqlite3

def check_db():
    files = os.listdir()
    if "db.sqlite3" in files:
        return print("Database already exists")
    return create_database()

def create_database():
    dbconn = sqlite3.connect("db.sqlite3")
    dbcursor = dbconn.cursor()

    print("Creating products groups table...")
    dbcursor.execute("""
    CREATE TABLE products_groups (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
	product_group TEXT
    );
    """)

    print("Creating products table...")
    dbcursor.execute("""
    CREATE TABLE products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
	product_name TEXT,
	product_group TEXT,
	product_brand TEXT,
	product_unit TEXT,
	product_barcode TEXT(13)
    );
    """)

    print("Creating products movimentations table...")
    dbcursor.execute("""
    CREATE TABLE products_movimentations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
	movimentation_date TEXT(10),
    movimentation_type TEXT(1),
    movimentation_product TEXT(13),
	movimentation_ammount NUMERIC,
	movimentation_price NUMERIC
    );
    """)
    print("Done")
    dbconn.close()
    return

if __name__ == "__main__":
    check_db()