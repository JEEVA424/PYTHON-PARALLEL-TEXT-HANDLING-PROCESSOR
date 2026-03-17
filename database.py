import sqlite3

def create_table():
    conn = sqlite3.connect("text_results.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS texts(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        text_chunk TEXT,
        sentiment_score INTEGER
    )
    """)

    conn.commit()
    conn.close()


def insert_result(text, score):
    conn = sqlite3.connect("text_results.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO texts(text_chunk, sentiment_score) VALUES (?,?)",
        (text, score)
    )

    conn.commit()
    conn.close()


def get_all_results():
    conn = sqlite3.connect("text_results.db")
    cursor = conn.cursor()

    cursor.execute("SELECT text_chunk, sentiment_score FROM texts")

    data = cursor.fetchall()

    conn.close()
    return data