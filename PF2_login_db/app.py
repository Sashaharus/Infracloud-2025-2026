import sqlite3
from flask import Flask, render_template, request, redirect, url_for, session, g
from werkzeug.security import check_password_hash

app = Flask(__name__)
app.secret_key = "devnet-secret-key"  # demo


# =========================
# DATABASE HANDLING (U1)
# =========================

def get_db():
    """
    Haalt een database connectie op.
    Gebruikt app.config["DB_FILE"] zodat unit tests
    een aparte test-database kunnen gebruiken.
    """
    if "db" not in g:
        db_file = app.config.get("DB_FILE", "users.db")
        g.db = sqlite3.connect(db_file)
        g.db.row_factory = sqlite3.Row
    return g.db


@app.teardown_appcontext
def close_db(error=None):
    """
    Sluit database na elke request.
    Nodig voor tests en proper resource management.
    """
    db = g.pop("db", None)
    if db is not None:
        db.close()


def get_user(username: str):
    """
    Haalt één user op uit de database.
    """
    db = get_db()
    cur = db.cursor()
    cur.execute("SELECT * FROM users WHERE username = ?", (username,))
    return cur.fetchone()


# =========================
# ROUTES
# =========================

@app.route("/")
def home():
    if "username" not in session:
        return redirect(url_for("login"))
    return render_template("index.html", username=session["username"])


@app.route("/login", methods=["GET", "POST"])
def login():
    error = None

    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "").strip()

        user = get_user(username)

        if user and check_password_hash(user["password_hash"], password):
            session["username"] = username
            return redirect(url_for("home"))
        else:
            error = "Foute username of password."

    return render_template("login.html", error=error)


@app.route("/logout")
def logout():
    session.pop("username", None)
    return redirect(url_for("login"))


# =========================
# MAIN
# =========================

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)

