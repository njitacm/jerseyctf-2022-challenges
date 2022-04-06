from apscheduler.schedulers.background import BackgroundScheduler
from dotenv import load_dotenv
from flask import Flask, Markup, flash, g, redirect, render_template, request, session, url_for
from uuid import uuid4
import datetime
import os
import random
import sqlite3
import string
import time

app = Flask(__name__)


# Load secret environment variables
load_dotenv()

app.secret_key = os.getenv("FLASK_SECRET_KEY", "".join(random.choice(string.ascii_letters) for _ in range(32)))
admin_password = os.getenv("ADMIN_PASSWORD", "".join(random.choice(string.ascii_letters) for _ in range(32)))

flag = os.getenv("FLAG", "jctf{ALMOST_LIKE_A_NEEDLE_IN_A_HAYSTACK}")
db_name = os.getenv("DATABASE", "temp.db")


# Helper function
def get_db():
    db = getattr(g, "_database", None)
    if db is None:
        db = sqlite3.connect(db_name)
        db.row_factory = sqlite3.Row
        g._database = db
    return db


# Setup database tables
def generate_fake_flag():
    prefix = "jctf"
    while prefix == "jctf":
        prefix = "".join(random.choice(string.ascii_lowercase) for _ in range(4))
    flag = "".join(random.choice(string.ascii_letters + string.digits + "_") for _ in range(random.randint(8, 40)))
    return prefix + "{" + flag + "}"


def setup_db():
    with app.app_context():
        db = get_db()

        # Setup admin user once
        cur = db.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='users'")
        if len(cur.fetchall()) == 0:
            db.execute("CREATE TABLE users (username TEXT, password TEXT)")
            db.execute("INSERT INTO users (username, password) VALUES ('admin', ?)", (admin_password,))

        # Create flags table first time to prevent "no such table"
        db.execute("CREATE TABLE IF NOT EXISTS flags (id TEXT, flag TEXT)")
        db.commit()

        # Reset flags table each time
        num_flags = random.randint(100_000, 1_000_000) - 2 # We add 2 flags manually
        flags = [generate_fake_flag() for _ in range(num_flags)]
        flags.append(flag)
        random.shuffle(flags)

        flags.insert(0, generate_fake_flag())
        flags = [(str(uuid4()), f) for f in flags]

        db.execute("CREATE TABLE flags_new (id TEXT, flag TEXT)")
        db.executemany("INSERT INTO flags_new (id, flag) VALUES (?, ?)", flags)
        db.execute("DROP TABLE flags")
        db.execute("ALTER TABLE flags_new RENAME TO flags")
        db.commit()


scheduler = BackgroundScheduler()
scheduler.add_job(setup_db, "interval", minutes=5, next_run_time=datetime.datetime.now())
scheduler.start()


# Flask Routes
@app.route("/")
def index():
    username = session.get("user", None)
    return render_template("index.html", user=username)


@app.route("/login", methods=["GET", "POST"])
def login():
    if "user" in session:
        flash("Already logged in", "dark")
        return redirect(url_for(index.__name__))

    if request.method == "GET":
        return render_template("login.html", user=None)

    username = request.form["username"]
    password = request.form["password"]

    db = get_db()
    cur = db.execute("SELECT * FROM users WHERE username='" + username + "' AND password='" + password + "'")
    user = cur.fetchone()
    if user is None:
        flash("Username and password not found", "danger")
        return redirect(url_for(login.__name__))

    session["user"] = user["username"]
    redirect_url = session.pop("next", index.__name__)
    return redirect(url_for(redirect_url))


@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for(index.__name__))


@app.route("/flags", methods=["GET", "POST"])
def flags():
    if "user" not in session or session["user"] != "admin":
        flash(Markup("You must be logged in as the <code>admin</code> user to access this page"), "danger")
        session["next"] = flags.__name__
        return redirect(url_for(login.__name__))

    if request.method == "GET":
        return render_template("flags.html", user=session["user"])

    start_time = time.time()

    db = get_db()
    cur = db.execute("SELECT * FROM flags WHERE id='" + request.form["id"] + "'")
    res = cur.fetchall()

    if len(res) == 0:
        flash("No matching flags found", "danger")
        return redirect(url_for(flags.__name__))

    res_id = res[0]["id"]
    res_flag = res[0]["flag"]

    if flag == res_flag:
        flash(
            Markup("""
                <p>Congratulations! You found the flag!</p>
                <p>The entry with <code>id=%s</code> has <code>flag=%s</code>.</p>
                """ % (res_id, res_flag)
            ),
            "success"
        )
    else:
        flash(
            Markup("""
                <p>Here's what your search returned:</p>
                <p>The entry with <code>id=%s</code> has <code>flag=%s</code>.</p>
                <p class="fst-italic">About %d result%s (%.3f seconds)</p>
                """ % (
                    res_id,
                    res_flag,
                    len(res),
                    "s" if len(res) > 1 else "",
                    time.time() - start_time,
                )
            ),
            "dark"
        )

    return redirect(url_for(flags.__name__))
