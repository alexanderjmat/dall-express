'''Classes and functions for database management'''
from types import ClassMethodDescriptorType
from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy_imageattach.entity import Image, image_attachment
import datetime
import bcrypt



db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

class User(db.Model):
    '''User class'''
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(150), nullable=False, unique=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100))
    profile_url = db.Column(db.String(200))
    average_rating = db.Column(db.Float, default=0)
    number_of_photos = db.Column(db.Integer, default=0)
    confirmation_hash = db.Column(db.String(100))

class Image(db.Model):
    '''Image class'''
    __tablename__ = "images"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    image = db.Column(db.Text, unique=True, nullable=False)
    name = db.Column(db.Text, nullable=False)
    mimetype = db.Column(db.Text, nullable=False)
    prompt = db.Column(db.String(400), unique=True, nullable=False)
    posted_by = db.Column(db.Integer, db.ForeignKey('users.username'), nullable=False)
    average_rating = db.Column(db.Float, default=0)
    imagetag_assignment = db.relationship("ImageTag", backref="images")

class UserImages(db.Model):

    '''User picture class'''
    __tablename__ = "user_images"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_username = db.Column(db.String, db.ForeignKey('users.username'))
    photo_id = db.Column(db.Integer, db.ForeignKey('images.id'))


class Tag(db.Model):
    '''Tag class'''
    __tablename__ = "tags"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(30), unique=True, nullable=False)
    imagetag_assignment = db.relationship("ImageTag", backref="tags")

class ImageTag(db.Model):
    '''Image tag class'''
    __tablename__ = "image_tags"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    tag_name = db.Column(db.String(30), db.ForeignKey("tags.name"), primary_key=True)
    image_id = db.Column(db.Integer, db.ForeignKey("images.id"), primary_key=True)

class ArtSubmission(db.Model):
    '''Class for artwork submissions'''
    __tablename__ = "submissions"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_username = db.Column(db.String, db.ForeignKey('users.username'), nullable=False)
    link_1 = db.Column(db.Text, nullable=False)
    link_2 = db.Column(db.Text)
    link_3 = db.Column(db.Text)
    link_4 = db.Column(db.Text)
    link_5 = db.Column(db.Text)
    

