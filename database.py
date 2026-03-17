import sqlite3


def create_table():

    conn = sqlite3.connect("results.db")

    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS results(
            text TEXT,
            score INTEGER
        )
    """)

    conn.commit()

    conn.close()


def insert_result(text, score):

    conn = sqlite3.connect("results.db")

    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO results VALUES (?, ?)",
        (text, score)
    )

    conn.commit()

    conn.close()


def get_all_results():

    conn = sqlite3.connect("results.db")

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM results")

    data = cursor.fetchall()

    conn.close()

    return data


def reset_database():

    conn = sqlite3.connect("results.db")

    cursor = conn.cursor()

    cursor.execute("DELETE FROM results")

    conn.commit()

    conn.close()
