import os
import sys
from flask import Flask, render_template, url_for, flash, redirect

from movieapp.movieobjects.classes import * #Actor, Director, Genre, Movie, MovieFileCSVReader, User, Review
from movieapp.helper import *
from movieapp.forms import *
from movieapp import app


# obtain the data from the movies dataset
all_movies, all_actors, all_genres, all_directors = get_movies('movieapp/database/Data1000Movies.csv')
movies = movies_dict(all_movies)

# This dictionary will store all username on register, with username as key and User object as values
user_database = {}


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
        # Success message if account is sucessfully created
        flash(f'{form.username.data}\'s account created', 'success')
        # Create an user instance
        user = User(form.username.data, form.password.data)
        user_database[form.username.data]= user
        # Redirect to home page on success
        return redirect(url_for('home'))
    return render_template('register.html', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.username.data in user_database:
            if form.password.data == user_database[form.username.data].password:
                flash('You have been logged in!', 'success')
                return redirect(url_for('home'))
            else:
                flash('Login unsuccessful, please check credentials.', 'danger')
        else:
            flash('Login unsuccessful, please check credentials.', 'danger')
    return render_template('login.html', title='Login', form=form)