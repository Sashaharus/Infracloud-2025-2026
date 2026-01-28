import os
import unittest
import sqlite3
from werkzeug.security import generate_password_hash

from app import app 


class FlaskLoginTests(unittest.TestCase):
    def setUp(self):
        self.test_db = "test_users.db"

        app.config["TESTING"] = True
        app.config["DB_FILE"] = self.test_db
        app.config["SECRET_KEY"] = "test-secret"


        self.client = app.test_client()

        self._init_test_db()
        self._add_user("cisco", "cisco123")

    def tearDown(self):
        if os.path.exists(self.test_db):
            os.remove(self.test_db)

    def _init_test_db(self):
        conn = sqlite3.connect(self.test_db)
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

    def _add_user(self, username, password):
        conn = sqlite3.connect(self.test_db)
        cur = conn.cursor()
        pw_hash = generate_password_hash(password)
        cur.execute(
            "INSERT INTO users (username, password_hash) VALUES (?, ?)",
            (username, pw_hash)
        )
        conn.commit()
        conn.close()

    def test_home_redirects_when_not_logged_in(self):
        resp = self.client.get("/", follow_redirects=False)
        self.assertEqual(resp.status_code, 302)
        self.assertIn("/login", resp.headers.get("Location", ""))

    def test_login_success(self):
        resp = self.client.post(
            "/login",
            data={"username": "cisco", "password": "cisco123"},
            follow_redirects=False
        )
        self.assertEqual(resp.status_code, 302)
        self.assertIn("/", resp.headers.get("Location", ""))

    def test_login_fail_wrong_password(self):
        resp = self.client.post(
            "/login",
            data={"username": "cisco", "password": "WRONG"},
            follow_redirects=True
        )
        self.assertEqual(resp.status_code, 200)
        self.assertIn(b"Foute username of password", resp.data)

    def test_logout_clears_session(self):
        self.client.post(
            "/login",
            data={"username": "cisco", "password": "cisco123"},
            follow_redirects=True
        )

        resp = self.client.get("/logout", follow_redirects=False)
        self.assertEqual(resp.status_code, 302)
        self.assertIn("/login", resp.headers.get("Location", ""))


if __name__ == "__main__":
    unittest.main(verbosity=2)
