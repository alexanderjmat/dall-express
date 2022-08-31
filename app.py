from flask import Flask, request, render_template,  redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from psycopg2 import connect
from models_and_functions import models, forms
from werkzeug.utils import secure_filename
from flask_sqlalchemy import SQLAlchemy
import bcrypt
import os

app = Flask(__name__)
User = models.User

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///dallexpress'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'aj1234'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)


models.connect_db(app)


images_for_prototype = []
for file in os.listdir("static/content/gallery-images"):

    if '.png' in file:
        
        file_title = file[29:-4]
        file_title = file_title

        images_for_prototype.append([file, file_title])


@app.route('/')
def home():
    if "user_id" not in session:
        return render_template('index.html')
    if "user_id" in session:
        user = User.query.filter_by(id=session["user_id"]).first()
        return render_template('index.html', user=user)



@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = forms.SignUp()
    if form.validate_on_submit():
        uppercase_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        lowercase_alphabet = "abcdefghijklmnopqrstuvwxyz"
        username = form.username.data
        password = form.password.data
        email = form.email.data
        confirmation_salt = str(bcrypt.gensalt())
        confirmation_code = ""
        for char in confirmation_salt:
            if char in uppercase_alphabet or char in lowercase_alphabet:
                confirmation_code += char;

        new_user = User.register(email=email, username=username, password=password, confirmation_code=confirmation_code, profile_url=f"/u/{username}")
        models.db.session.add(new_user)
        models.db.session.commit()
        session["user_id"] = new_user.id


        flash(f"Thanks for signing up, {username}! We just sent you a confirmation email for your account")
        return redirect("/")
    
    else:
        return render_template('sign-up.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = forms.Login()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        user = User.authenticate(username, password)

        if user:
            session["user_id"] = user.id
            return redirect("/")
        else: 
            form.username.errors = ['Bad username/password']
        
        return render_template("login.html", form=form)


    
    else:
        return render_template('login.html', form=form)

@app.route("/logout")
def logout():
    session.pop("user_id")
    return redirect("/")

@app.route("/about")
def about():
    return redirect("/")

@app.route("/gallery")
def gallery():
    if "user_id" not in session:
        return render_template('gallery.html')
    if "user_id" in session:
        user = User.query.filter_by(id=session["user_id"]).first()
        return render_template('gallery.html', user=user)
    
@app.route("/marketplace")
def marketplace():
    marketplace_items = images_for_prototype
    if "user_id" not in session:
        return render_template('marketplace.html', items=marketplace_items)
    if "user_id" in session:
        user = User.query.filter_by(id=session["user_id"]).first()
        return render_template('marketplace.html', user=user, items=marketplace_items)

@app.route("/contact", methods=['GET', 'POST'])
def contact():
    form = forms.Contact()
    if "user_id" not in session:
        if form.validate_on_submit():
            name = form.name.data
            email = form.email.data
            message = form.message.data
            flash(f"Thanks for your message, {name}! We'll get back to you as soon as possible.")
        else:
            return render_template('contact.html', form=form)

        return redirect('/contact')

    if "user_id" in session:
        user = User.query.filter_by(id=session["user_id"]).first()
        if form.validate_on_submit():
            name = form.name.data
            email = form.email.data
            message = form.message.data
            flash(f"Thanks for your message, {name}! We'll get back to you as soon as possible.")
        else:
            return render_template('contact.html', form=form)

        return redirect('/contact', user=user)
    



