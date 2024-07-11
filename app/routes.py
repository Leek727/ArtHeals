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
@login_required
def index():
    return render_template("index.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    
    form = LoginForm()
    if form.validate_on_submit():
        user = db.session.scalar(
            sa.select(User).where(User.username == form.username.data))
    
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
    
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or urlsplit(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(url_for('index'))
    
    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

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