import sqlite3
from werkzeug.security import generate_password_hash

DB_FILE = "users.db"

def add_user(username: str, password: str):
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()

    pw_hash = generate_password_hash(password)  # salted hash

    try:
        cur.execute("INSERT INTO users (username, password_hash) VALUES (?, ?)", (username, pw_hash))
        conn.commit()
        print(f"User '{username}' toegevoegd.")
    except sqlite3.IntegrityError:
        print(f"User '{username}' bestaat al.")
    finally:
        conn.close()

if __name__ == "__main__":
    username = input("Username: ").strip()
    password = input("Password: ").strip()
    add_user(username, password)
