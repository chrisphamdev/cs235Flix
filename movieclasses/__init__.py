import os
import sys
from flask import Flask, render_template, url_for, flash, redirect

from movieclasses.movieobjects.classes import * #Actor, Director, Genre, Movie, MovieFileCSVReader, User, Review
from movieclasses.get_movies import *
from movieclasses.forms import *
    
def create_app(test_config=None):
    """Construct the core application."""
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'uJsLNNHaLOS2NyKFhfTQryGFSITaeMRq'

    # obtain the data from the movies dataset
    all_movies, all_actors, all_genres, all_directors = get_movies('movieclasses/Data1000Movies.csv')
    movies = movies_dict(all_movies)


    @app.route('/')
    @app.route('/home')
    def home():
        return render_template('home.html')

    @app.route('/movies')
    def movies_page():
        return render_template('movies.html', movies=movies)

    @app.route('/register', methods=['GET', 'POST'])
    def register():
        form = RegistrationForm()
        if form.validate_on_submit():
            flash(f'{form.username.data}\'s account created', 'success')
            return redirect(url_for('home'))
        return render_template('register.html', form=form)

    @app.route('/login') 
    def login():
        form = LoginForm()
        return render_template('login.html', form=form)
        
    return app