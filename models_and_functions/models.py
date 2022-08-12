'''Classes and functions for database management'''

from types import ClassMethodDescriptorType
from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)