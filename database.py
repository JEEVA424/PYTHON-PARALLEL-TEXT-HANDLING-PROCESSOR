import sqlite3

DB_NAME = "results.db"

EXPECTED_COLUMNS = [
    "text",
    "positive_count",
    "negative_count",
    "final_score",
    "final_sentiment"
]


def _get_existing_columns(cursor):
    cursor.execute("PRAGMA table_info(results)")
    rows = cursor.fetchall()
    return [row[1] for row in rows]


def create_table():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS results (
            text TEXT,
            positive_count INTEGER,
            negative_count INTEGER,
            final_score INTEGER,
            final_sentiment TEXT
        )
    """)

    existing_columns = _get_existing_columns(cursor)

    if existing_columns and existing_columns != EXPECTED_COLUMNS:
        cursor.execute("DROP TABLE IF EXISTS results")
        cursor.execute("""
            CREATE TABLE results (
                text TEXT,
                positive_count INTEGER,
                negative_count INTEGER,
                final_score INTEGER,
                final_sentiment TEXT
            )
        """)

    conn.commit()
    conn.close()


def insert_results(results):
    if not results:
        return

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.executemany("""
        INSERT INTO results (
            text, positive_count, negative_count, final_score, final_sentiment
        ) VALUES (?, ?, ?, ?, ?)
    """, results)

    conn.commit()
    conn.close()


def get_all_results():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT text, positive_count, negative_count, final_score, final_sentiment
        FROM results
    """)

    data = cursor.fetchall()
    conn.close()
    return data


def reset_database():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM results")
    conn.commit()
    conn.close()
