import sqlite3

DB_NAME = "text_data.db"

def get_connection():
    conn = sqlite3.connect(DB_NAME, timeout=10)
    conn.execute("PRAGMA journal_mode=WAL;")  # Enable WAL mode
    return conn

def create_table():
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS texts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            text_chunk TEXT,
            sentiment_score INTEGER,
            tag TEXT
        )
        """)
        conn.commit()

def clear_table():
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM texts")
        conn.commit()

def insert_data(text, score, tag):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO texts (text_chunk, sentiment_score, tag) VALUES (?, ?, ?)",
            (text, score, tag)
        )
        conn.commit()
