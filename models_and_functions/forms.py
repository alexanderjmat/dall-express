from xml.dom import ValidationErr
from flask_wtf import FlaskForm
from wtforms import StringField, FloatField
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

    username = StringField(render_kw={"placeholder": "Username"}, validators=[InputRequired()])
    email = StringField(render_kw={"placeholder": "Email"}, validators=[InputRequired(), Email()])
    password = StringField(render_kw={"placeholder": "Password"}, validators=[InputRequired(), EqualTo('confirm_password', message='Passwords must match'), Length(min=8, message="Password must be at least 8 characters")])
    confirm_password = StringField(render_kw={"placeholder": "Confirm"}, validators=[InputRequired(), validate_password])

class Login(FlaskForm):
    """Form for logging in"""

    username = StringField(render_kw={"placeholder": "Username"}, validators=[InputRequired()])
    password = StringField(render_kw={"placeholder": "Password"}, validators=[InputRequired()])

class Contact(FlaskForm):
    '''Form for contacting DEGA'''
    name = StringField(render_kw={"placeholder": "Name"}, validators=[InputRequired()])
    email = StringField(render_kw={"placeholder": "Email"}, validators=[InputRequired(), Email()])
    message = StringField(render_kw={"placeholder": "Type your message here"}, validators=[InputRequired()])

