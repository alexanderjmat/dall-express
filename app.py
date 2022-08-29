from flask import Flask, request, render_template,  redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from psycopg2 import connect
from models_and_functions import models, forms
from werkzeug.utils import secure_filename
import bcrypt

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///dallexpress'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'aj1234'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

models.connect_db(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = forms.SignUp()
    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password = form.password.data
        flash(f"Thanks for signing up, {username}! We just sent you a confirmation email for your account")
        return redirect("/signup")
    
    else:
        return render_template('sign-up.html', form=form)
