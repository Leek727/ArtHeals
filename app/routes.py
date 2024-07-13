import bson.errors
from app import app
from app.forms import LoginForm
from flask import render_template, flash, redirect, url_for, request, jsonify
from flask_login import current_user, login_user, logout_user, login_required
import sqlalchemy as sa
from app import db
from app.models import User
from urllib.parse import urlsplit
from app.mongo_client import AtlasClient
import bson
from werkzeug.utils import secure_filename
import os
import json

mongo_client = AtlasClient()

@app.route("/")
@app.route("/index")
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
            next_page = url_for('admin')
        return redirect(url_for('admin'))
    
    return render_template('login.html', title='Sign In', form=form)


@app.route("/admincharacters")
@app.route("/adminother")
@app.route("/adminflowers")
@app.route("/adminanimals")
@login_required
def admin_cards():
    cards = mongo_client.get_card_list(request.path.replace("/", "").replace("admin", ""))
    return render_template("admin_animals.html", cards=cards)

@app.route("/admin")
@login_required
def admin():
    return render_template("admin.html")

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route("/animals")
@app.route("/characters")
@app.route("/flowers")
@app.route("/other")
def characters():
    cards = mongo_client.get_card_list(request.path.replace("/", ""))
    return render_template("animals.html", cards=cards)


@app.route('/update_card', methods=['POST'])
def update_card():
    index = int(request.form['index'])
    title = request.form['title']
    price = request.form['price']
    desc = request.form['desc']
    content = request.form['content']
    image_file = request.files.get('image')


    category = request.form['url'].replace("admin", "").replace("/", "")
    cards = mongo_client.get_card_list(category)
    # save card order first
    cards_updated = []
    order = json.loads(request.form["order"])
    print(order)
    for order_item in order:
        ind = order_item["id"]
        target_card = list(filter(lambda x: x["index"] == int(ind), cards))
        cards_updated.append(target_card[0])

    
    #print(cards_updated)
    # update card data
    card_update = {}
    card_index = 0
    for i,card in enumerate(cards_updated):
        card_index = i
        if card['index'] == index:
            card_update = card
            card_update['title'] = title
            card_update['price'] = price
            card_update['desc'] = desc
            card_update['content'] = content
            
            if image_file:
                filename = secure_filename(image_file.filename)
                image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                image_file.save(image_path)
                card_update['src'] = image_path.replace("app/", "")
            break

    if card_update == {}:
        return jsonify(success=False)
    
    cards_updated[card_index] = card_update
    mongo_client.update_card_list(category, cards_updated)


    return jsonify(success=True)


@app.route("/update_order", methods=["POST"])
def update_order():
    order = request.json
    print(order)
    category = order["url"].replace("admin", "").replace("/", "")
    cards = mongo_client.get_card_list(category)
    cards_updated = []
    for order_item in order["order"]:
        ind = order_item["id"]
        target_card = list(filter(lambda x: x["index"] == int(ind), cards))
        cards_updated.append(target_card[0])

    print(cards_updated)
    mongo_client.update_card_list(category, cards_updated)

    return jsonify(success=True)

@app.route("/new_card", methods=["POST"])
def new_card():
    order = request.json
    category = order["url"].replace("admin", "").replace("/", "")
    cards = mongo_client.get_card_list(category) 

    # insert new card into the list
    new_card = {
        "index": len(cards),
        "title": "New Card",
        "price": "Price",
        "desc": "Description",
        "content": "Content",
        "src": ""
    }

    cards.insert(0, new_card)
    mongo_client.update_card_list(category, cards)

    return jsonify(success=True)


@app.route("/delete_card", methods=["POST"])
def delete_card():
    order = request.json
    category = order["url"].replace("admin", "").replace("/", "")
    cards = mongo_client.get_card_list(category) 

    updated_cards = []
    for card in cards:
        if card["index"] == int(order["index"]):
            continue
        updated_cards.append(card)
    #print(updated_cards)
    mongo_client.update_card_list(category, updated_cards)

    return jsonify(success=True)




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

