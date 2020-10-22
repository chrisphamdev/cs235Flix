import os
import sys
from flask import Flask, render_template, url_for, flash, redirect

from movieapp.movieobjects.classes import * #Actor, Director, Genre, Movie, MovieFileCSVReader, User, Review
from movieapp.helper import *
from movieapp.forms import *
    

"""Construct the core application."""
app = Flask(__name__)

from movieapp import routes

#@app.route("/browse")
#def browse_movie():