import sqlite3

DB_NAME = "text_data.db"


# --------------------------------------------------
# CREATE TABLE IF NOT EXISTS
# --------------------------------------------------

def create_table():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS texts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        content TEXT,
        score INTEGER,
        tag TEXT
    )
    """)

    conn.commit()
    conn.close()


# --------------------------------------------------
# INSERT DATA
# --------------------------------------------------

def insert_data(content, score, tag):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO texts (content, score, tag) VALUES (?, ?, ?)",
        (content, score, tag)
    )

    conn.commit()
    conn.close()
