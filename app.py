from flask import Flask, request, render_template,  redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from psycopg2 import connect
from models_and_functions import models, forms
from werkzeug.utils import secure_filename
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
import bcrypt
import os

app = Flask(__name__)
User = models.User
Image = models.Image

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///dallexpress'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'aj1234'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)


models.connect_db(app)
models.db.drop_all()
models.db.create_all()


images_for_prototype = []
for file in os.listdir("static/content/gallery-images"):

    if '.png' in file:
        
        file_title = file[29:-4]
        file_title = file_title
        new_image = models.Image(image=file, prompt=file_title)
        images_for_prototype.append(new_image)
        models.db.session.add(new_image)
        models.db.session.commit()


@app.route('/')
def home():
    photos = []
    new_arrivals = []
    for image in images_for_prototype:
        new_arrivals.append(image)
        if len(photos) < 21:
            photos.append(image)
    if "user_id" not in session:
        return render_template('index.html', photos=photos, arrivals=new_arrivals)
    if "user_id" in session:
        user = User.query.filter_by(id=session["user_id"]).first()
        return render_template('index.html', user=user, photos=photos, arrivals=new_arrivals)



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
    cat_photo = Image.query.filter_by(prompt="Grey and white cat wearing a cowboy hat while riding a brown donkey impressionist oil painting").first()
    if "user_id" not in session:
        return render_template('about.html', cat_photo=cat_photo)
    if "user_id" in session:
        user = User.query.filter_by(id=session["user_id"]).first()
        return render_template('about.html', user=user, cat_photo=cat_photo)

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

@app.route("/marketplace/<int:id>")
def marketplace_item(id):
    item = Image.query.filter_by(id=id).first()
    if "user_id" not in session:
        return render_template('marketplace-item.html', item=item)
    if "user_id" in session:
        user = User.query.filter_by(id=session["user_id"]).first()
        return render_template('marketplace-item.html', user=user, item=item)

@app.route("/marketplace/style/<option>")
def marketplace_style(option):
    items = Image.query.filter(Image.prompt.ilike((f"%{option}%"))).all()
    if "user_id" not in session:
        return render_template('marketplace.html', items=items, option=option)
    if "user_id" in session:
        user = User.query.filter_by(id=session["user_id"]).first()
        return render_template('marketplace.html', user=user, items=items, option=option)

@app.route("/marketplace/medium/<option>")
def marketplace_medium(option):
    items = Image.query.filter(Image.prompt.ilike((f"%{option}%"))).all()
    if "user_id" not in session:
        return render_template('marketplace.html', items=items, option=option)
    if "user_id" in session:
        user = User.query.filter_by(id=session["user_id"]).first()
        return render_template('marketplace.html', user=user, items=items, option=option)




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
    



