import os
import sys
from flask import Flask, render_template, url_for, flash, redirect, request

from movieapp.helper import *
from movieapp.forms import *
from movieapp import app, encryptor, user_database
from flask_login import login_user, current_user, logout_user, login_required
from movieapp.models import User, Review

# obtain the data from the movies dataset
all_movies, all_actors, all_genres, all_directors = get_movies('movieapp/database/Data1000Movies.csv')
movies = movies_dict(all_movies)

# This dictionary will store all username on register, with username as key and User object as values

@account_manager.user_loader
def load_user(user_id):
    return User.id

    
@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/movies')
def movies_page():
    return render_template('movies.html', movies=movies)

# @app.route('/movies/<int:year>/<str:movie_name>')
# def seperated_movie_page(year, movie_name):
#     movie = Movie('None', 1990)
#     for elm in all_movies:
#         if elm.year == year and elm.title == movie_name:
#             movie = elm
#             break
#     return render_template('moviepage.html', movie=movie)

@app.route('/register', methods=['GET', 'POST'])
def register():
    # redirect back to home page if user has already logged in
    form = RegistrationForm()
    if form.validate_on_submit():
        # Success message if account is sucessfully created
        flash(f'{form.username.data}\'s account created, you can now log in.', 'success')
        hashed_password = encryptor.generate_password_hash(form.password.data).decode('utf-8')
        # Create an user instance
        user = User()
        user.username = form.username.data
        user.password = hashed_password
        user.id = len(user_database) + 1
        user_database[user.username] = user
        # Redirect to home page on success
        return redirect(url_for('login'))
    return render_template('register.html', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    # redirect back to home page if user has already logged im
    form = LoginForm()
    if form.validate_on_submit():
        if form.username.data in user_database:
            # validates the password
            if encryptor.check_password_hash(user_database[form.username.data].password, form.password.data):
                user = user_database[form.username.data]
                flash('You have been logged in!', 'success')
                login_user(user, remember=form.remember.data)
                next_page = request.args.get('next')
                return redirect(next_page) if next_page else redirect(url_for('home'))
            else:
                flash('Login unsuccessful, please check credentials.', 'danger')
        else:
            flash('Login unsuccessful, please check credentials.', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route("/account")
@login_required
def account():
    return render_template('account.html')


@app.route("/search", methods=['GET', 'POST'])
def search():
    form = SearchForm()
    output = []
    if form.validate_on_submit():
        invalid_actor = False
        all_actors_names = form.actors.data.split(',')
        search_by_actors = []
        for name in all_actors_names:
            name = name.strip()
            search_by_actors += [Actor(name)]
        for actor in search_by_actors:
            if actor not in all_actors:
                invalid_actor = True
                break
        if invalid_actor == False:
            output = moviefinder(search_by_actors, all_movies)
            output = movies_dict(output)
            return render_template('movies.html', movies=output)
        else:
            flash('Invalid input, please try again.')

        
    return render_template('search.html', form=form)