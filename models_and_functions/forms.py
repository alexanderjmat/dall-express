from xml.dom import ValidationErr
from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, PasswordField, EmailField, TextAreaField
from wtforms.validators import InputRequired, Optional, Email, EqualTo, Length, DataRequired

def validate_password(form, field):
    uppercase_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowercase_alphabet = "abcdefghijklmnopqrstuvwxyz"
    numbers = "1234567890"
    uppercase_count = 0
    lowercase_count = 0
    number_count = 0
    password = field.data
    for character in password:
        if character in uppercase_alphabet:
            uppercase_count += 1
        if character in lowercase_alphabet:
            lowercase_count += 1
        if character in numbers:
            number_count += 1
    if uppercase_count == 0 or lowercase_count == 0 or number_count == 0:
        raise ValidationErr('Password must contain an uppercase letter, lowercase letter, and a number')


class SignUp(FlaskForm):
    """Form for signing up"""

    username = StringField("Username", validators=[InputRequired()])
    email = EmailField("Email", validators=[InputRequired(), Email()])
    password = PasswordField("Password", validators=[InputRequired(), EqualTo('confirm_password', message='Passwords must match'), Length(min=8, message="Password must be at least 8 characters")])
    confirm_password = PasswordField("Confirm Password", validators=[InputRequired(), validate_password])

class Login(FlaskForm):
    """Form for logging in"""

    username = StringField("Username", validators=[InputRequired()])
    password = PasswordField("Password", validators=[InputRequired()])

class Contact(FlaskForm):
    '''Form for contacting DEGA'''
    name = StringField("Name", validators=[InputRequired()])
    email = EmailField("Email", validators=[InputRequired(), Email()])
    message = TextAreaField("Message", validators=[InputRequired()])

