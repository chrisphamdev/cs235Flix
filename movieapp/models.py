import datetime
from flask_login import UserMixin
from movieapp import account_manager
from movieapp.movieobjects.classes import *


@account_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

class User(UserMixin):
    id = 0
    username = 'default'
    password = ''
    reviews = []
    watched_movies = []
    watchlist = []

    def add_movie(self, movie):
        watchlist += [movie]
    
    def add_review(self, review):
        reviews += [review]

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Review:
    def __init__(self, movie: Movie, review_text: str, rating: int):
        if not isinstance(movie, Movie):
            self.__movie = Movie()
        else:
            self.__movie = movie

        if type(review_text) is not str:
            self.__review_text = None
        else:
            self.__review_text = review_text

        if type(rating) is not int:
            self.__rating = None
        elif rating<1 or rating>10:
            self.__rating = None
        else:
            self.__rating = rating
        
        self.__timestamp = datetime.now()

    @property
    def movie(self) -> Movie:
        return self.__movie
    
    @movie.setter
    def movie(self, movie):
        if not isinstance(movie, Movie):
            return
        else:
            self.__movie = movie
    
    @property
    def review_text(self) -> str:
        return self.__review_text
    
    @review_text.setter
    def review_text(self, review_text):
        if type(review_text) is not str:
            return
        else:
            self.__review_text = review_text
    
    @property
    def rating(self) -> int:
        return self.__rating

    @rating.setter
    def rating(self, rating):
        if type(rating) is not int:
            return
        if rating < 1 or rating > 10:
            return
        else:
            self.__rating = rating
    
    def __repr__(self): 
        return "<Rating for {}".format(self.__movie.__repr__())
    
    def __eq__(self, other):
        return self.__movie == other.__movie and self.__review_text == other.__review_text and self.__rating == other.__rating and self.__timestamp == other.__timestamp