import bson.errors
from app import app
from app.forms import LoginForm
from flask import render_template, flash, redirect, url_for, request
from flask_login import current_user, login_user, logout_user, login_required
import sqlalchemy as sa
from app import db
from app.models import User
from urllib.parse import urlsplit
from app.mongo_client import AtlasClient
import bson

mongo_client = AtlasClient()

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/meet-the-team")
def meet_the_team():
    return render_template("meet-the-team.html")

@app.route("/news")
def news():
    return render_template("news.html")

@app.route("/donate")
def donate():
    return render_template("donate.html")

@app.route("/store")
def store():
    return render_template("store.html")


@app.route("/animals")
def animals():
    return render_template("animals.html")

@app.route("/characters")
def characters():
    return render_template("characters.html")

@app.route("/flowers")
def flowers():
    return render_template("flowers.html")

@app.route("/other")
def other():
    return render_template("other.html")