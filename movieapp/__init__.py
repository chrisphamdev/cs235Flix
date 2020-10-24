import os
import sys
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

# from movieapp.movieobjects.classes import * #Actor, Director, Genre, Movie, MovieFileCSVReader, User, Review
# from movieapp.helper import *
# from movieapp.forms import *
    

"""Construct the core application."""
app = Flask(__name__)
app.config['SECRET_KEY'] = '15BA8A59617F9DD1E62D53EF2A219'
user_database = {}
encryptor = Bcrypt(app)
account_manager = LoginManager(app)
account_manager = LoginManager(app)
account_manager.login_view = 'login'
account_manager.login_message_category = 'info'

from movieapp import routes