import sqlite3

conn = sqlite3.connect(
    "learning.db",
    check_same_thread=False
)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS progress(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    topic TEXT,
    score INTEGER,
    date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

conn.commit()

def save_progress(topic, score):

    cursor.execute(
        "INSERT INTO progress(topic, score) VALUES (?, ?)",
        (topic, score)
    )

    conn.commit()

def get_progress():

    cursor.execute(
        "SELECT * FROM progress"
    )

    return cursor.fetchall()