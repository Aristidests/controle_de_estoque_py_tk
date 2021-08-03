import os
import sqlite3

def check_db():
    files = os.listdir()
    if "db.sqlite3" in files:
        return print("Database já existe")
    return create_database()

def create_database():
    dbconn = sqlite3.connect("db.sqlite3")
    dbcursor = dbconn.cursor()
    dbcursor.execute("""
    CREATE TABLE produtos_grupos (
	GRUPO TEXT
    );
    """)
    dbcursor.execute("""
    CREATE TABLE produtos (
	nome TEXT,
	grupo TEXT,
	marca TEXT,
	unidade TEXT,
	codbar TEXT(13)
    );
    """)
    dbcursor.execute("""
    CREATE TABLE mov_produtos (
	"data" TEXT(10),
    tipo TEXT(1),
    produto TEXT,
	quantidade NUMERIC,
	preco NUMERIC
    );
    """)
    dbconn.close()
    return

if __name__ == "__main__":
    check_db()