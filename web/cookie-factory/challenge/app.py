from dotenv import load_dotenv
from flask import Flask, abort, flash, g, make_response, redirect, render_template, request, session, url_for
import jwt
import os
import random
import string

app = Flask(__name__)


# Load secret environment variables
load_dotenv()

flag = os.getenv("FLAG", "jctf{GEEZ_WHAT_A_TOUGH_COOKIE}")

app.secret_key = os.getenv("FLASK_SECRET_KEY", "".join(random.choice(string.ascii_letters) for _ in range(32)))
secret = os.getenv("SECRET", "".join(random.choice(string.ascii_letters) for _ in range(32)))


# JWT helper functions
def encode_user(username):
    return jwt.encode({"username": username}, secret, algorithm="HS256")


def decode_user(token):
    if token is None:
        return None

    try:
        alg = jwt.get_unverified_header(token)["alg"]

        if alg == "HS256":
            decoded = jwt.decode(token, secret, algorithms=["HS256"])
        elif alg == "none":
            decoded = jwt.decode(token, algorithms=["none"], options={"verify_signature": False})
        else:
            abort(400, "Invalid JWT algorithm")
    except Exception:
        abort(400, "Error decoding token")


    if "username" not in decoded:
        abort(400, "Username missing in JWT")

    return decoded["username"]


# Flask Routes
@app.errorhandler(400)
def handle_error(error):
    return render_template("error.html", error=error), 400


@app.route("/")
def index():
    token = request.cookies.get("user", None)
    return render_template("index.html", user=decode_user(token))


@app.route("/dashboard")
def dashboard():
    token = request.cookies.get("user", None)
    if not token:
        flash("You must be logged in to access this page", "danger")
        session["next"] = dashboard.__name__
        return redirect(url_for(login.__name__))

    return render_template("dashboard.html", user=decode_user(token), flag=flag)


@app.route("/login", methods=["GET", "POST"])
def login():
    if "user" in request.cookies:
        flash("Already logged in", "danger")
        return redirect(url_for(index.__name__))

    if request.method == "GET":
        return render_template("login.html", user=None)

    username = request.form["username"]

    if username == "":
        flash("Username cannot be empty", "danger")
        return redirect(url_for(login.__name__))

    if username == "admin":
        flash("Sorry, you can't login as admin", "danger")
        return redirect(url_for(login.__name__))

    redirect_url = session.pop("next", index.__name__)

    resp = make_response(redirect(url_for(redirect_url)))
    resp.set_cookie("user", encode_user(username))

    return resp


@app.route("/logout")
def logout():
    resp = make_response(redirect(url_for(index.__name__)))
    resp.set_cookie("user", "", expires=0)
    return resp
