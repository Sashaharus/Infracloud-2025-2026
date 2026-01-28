import sqlite3

DB_FILE = "users.db"

def init_db():
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password_hash TEXT NOT NULL
    );
    """)

    conn.commit()
    conn.close()
    print(f"Database '{DB_FILE}' is klaar.")

if __name__ == "__main__":
    init_db()
