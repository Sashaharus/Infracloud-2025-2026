from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "devnet-secret-key" 


USERS = {
    "cisco": "cisco123"
}

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

    
        if username in USERS and USERS[username] == password:
            session["username"] = username
            return redirect(url_for("home"))
        else:
            error = "Foute username of password."

    return render_template("login.html", error=error)

@app.route("/logout")
def logout():
    session.pop("username", None)
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)
