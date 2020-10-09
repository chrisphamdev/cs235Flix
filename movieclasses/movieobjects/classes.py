import datetime
import csv

class Actor:
    def __init__(self, actor_name: str):
        if actor_name == "" or type(actor_name) is not str:
            self.__actor_name = None
        else:
            self.__actor_name = actor_name.strip()
        
        self.__colleague = []
        
    @property
    def actor_name(self) -> str:
        return self.__actor_name
    
    def __repr__(self):
        return f"<Actor {self.__actor_name}>"

    def __eq__(self, other):
        if not isinstance(other, Actor):
            return False
        if self.__actor_name == other.__actor_name:
            return True
        return False

    def __lt__(self, other):
        if not isinstance(other, Actor):
            return False
        return self.__actor_name < other.__actor_name
    
    def __hash__(self):
        return hash(self.__actor_name)
    
    def add_actor_colleague(self, colleague):
        self.__colleague += [colleague]

    def check_if_this_actor_worked_with(self, colleague):
        return colleague in self.__colleague



class Director:

    def __init__(self, director_full_name: str):
        if director_full_name == "" or type(director_full_name) is not str:
            self.__director_full_name = None
        else:
            self.__director_full_name = director_full_name.strip()

    @property
    def director_full_name(self) -> str:
        return self.__director_full_name

    def __repr__(self):
        return f"<Director {self.__director_full_name}>"

    def __eq__(self, other):
        if not isinstance(other, Director):
            return False
        if self.__director_full_name == other.__director_full_name:
            return True
        return False

    def __lt__(self, other):
        if not isinstance(other, Director):
            return False
        return self.__director_full_name < other.__director_full_name

    def __hash__(self):
        return hash(self.__director_full_name)


class Genre:
    def __init__(self, genre_name: str):
        if genre_name == "" or type(genre_name) is not str:
            self.__genre_name = None
        else:
            self.__genre_name = genre_name.strip()

    @property
    def genre_name(self) -> str:
        return self.__genre_name

    def __repr__(self):
        return f"<Genre {self.__genre_name}>"

    def __eq__(self, other):
        if not isinstance(other, Genre):
            return False
        if self.__genre_name == other.__genre_name:
            return True
        return False

    def __lt__(self, other):
        if not isinstance(other, Genre):
            return False
        return self.__genre_name < other.__genre_name

    def __hash__(self):
        return hash(self.__genre_name)

class Movie:
    def __init__(self, title: str, year: int):
        if title == "" or type(title) is not str:
            self.__title = None
        else:
            self.__title = title.strip()
        
        if year < 1900 or type(year) is not int:
            self.__ = None
        else:
            self.__year = year

        self.__description = None
        self.__director = None
        self.__actors = []
        self.__genres = []
        self.__runtime_minutes = None
    
    @property
    def year(self):
        return self.__year

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, text: str):
        if text == "" or type(text) is not str:
            self.__title = None
        else:
            self.__title = text

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, text: str):
        if text == "" or type(text) is not str:
            self.__description = None
        else:
            self.__description = text
    
    @property
    def director(self) -> str:
        return self.__director

    @director.setter
    def director(self, director: Director):
        if not isinstance(director, Director):
            self.__director = None
        else:
            self.__director = director
    
    @property
    def actors(self) -> str: 
        return self.__actors
    
    def actors_str(self):
        output = ''
        for actor in self.__actors:
            output += actor.actor_name
            output += ', '
        output = output[:-2]
        return output
    
    @property
    def genres(self) -> str:
        return self.__genres

    def genres_str(self):
        output = ''
        for genre in self.__genres:
            output += genre.genre_name
            output += ', '
        output = output[:-2]
        return output
    
    @property
    def runtime_minutes(self):
        return self.__runtime_minutes

    @runtime_minutes.setter
    def runtime_minutes(self, num):
        if num <= 0 or type(num) is not int:
            raise ValueError
        else:
            self.__runtime_minutes = num

    def __repr__(self):
        return '<Movie {}, {}>'.format(self.__title, self.__year)
    
    def __eq__(self, other):
        if not isinstance(other, Movie):
            return False
        return self.__title == other.__title and self.__year == other.__year
    
    def __lt__(self, other):
        if not isinstance(other, Movie):
            return False
        if self.__title == other.__title:
            return self.__year < other.__year
        else:
            return self.__title < other.__title
    
    def __hash__(self):
        return hash(self.__title + str(self.__year))

    def add_actor(self, actor: Actor):
        if not isinstance(actor, Actor):
            return 
        self.__actors += [actor]
    
    def remove_actor(self, actor: Actor):
        if not isinstance(actor, Actor):
            return
        if actor in self.__actors:
            i = self.__actors.index(actor)
            self.__actors.pop(i)
        
    def add_genre(self, genre: Genre):
        if not isinstance(genre, Genre):
            return
        self.__genres += [genre]
    
    def remove_genre(self, genre: Genre):
        if not isinstance(genre, Genre):
            return
        if genre in self.__genres:
            i = self.__genres.index(genre)
            self.__genres.pop(i)


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

class User:
    def __init__(self, username: str, password: str):
        if type(username) is not str:
            self.__username = None
        else:
            self.__username = username.strip().lower()
        
        if type(password) is not str:
            self.__password = None
        else:
            self.__password = password
        
        self.__watched_movies = []
        self.__reviews = []
        self.__time_spent_watching_movies_minutes = 0
    
    @property
    def username(self) -> str:
        return self.__username
    
    @username.setter
    def username(self, username: str):
        if type(username) is not str:
            self.__username = self.__username
        else:
            self.__username = username.strip().lower()
    
    @property
    def password(self) -> str:
        return self.__password
    
    @password.setter 
    def password(self, password: str):
        if type(password) is not str:
            return
        else:
            self.__password = password

    @property
    def time_spent_watching_movies_minutes(self) -> int:
        return self.__time_spent_watching_movies_minutes
    
    @time_spent_watching_movies_minutes.setter
    def time_spent_watching_movies_minutes(self, value: int):
        if type(value) is not int:
            return
        if value < 0:
            return
        else:
            self.__time_spent_watching_movies_minutes = value
    
    @property
    def watched_movies(self):
        return self.__watched_movies
    
    @property
    def reviews(self):
        return self.__reviews
    
    @property
    def time_spent_watching_movies_minutes(self):
        return self.__time_spent_watching_movies_minutes
    
    def watch_movie(self, movie: Movie):
        if not isinstance(movie, Movie):
            return
        self.__watched_movies += [movie]
        if movie.runtime_minutes != None:
            self.__time_spent_watching_movies_minutes += movie.runtime_minutes
    
    def add_review(self, review: Review):
        if not isinstance(review, Review):
            return
        self.__reviews += [review]

    def __repr__(self):
        return f"<User {self.username}>"
    
    def __eq__(self, other):
        if not isinstance(other, User):
            return False
        return self.__username == other.username
    
    def __lt__(self, other):
        if not isinstance(other, User):
            return False
        else:
            return self.__username < other.username
    
    def __hash__(self):
        return hash(self.__username + self.__password)


class MovieFileCSVReader:

    def __init__(self, file_name: str):
        self.__file_name = file_name
        self.dataset_of_movies = []
        self.dataset_of_actors = []
        self.dataset_of_directors = []
        self.dataset_of_genres = []

    def read_csv_file(self):
        with open(self.__file_name, mode='r', encoding='utf-8-sig') as csvfile:
            movie_file_reader = csv.DictReader(csvfile)
            for row in movie_file_reader:
                title = row['Title']

                genres = []
                genre_strings = row['Genre'].split(',')
                for g in genre_strings:
                    genres += [Genre(g)]


                actors = []
                actors_strings = row['Actors'].split(',')
                for a in actors_strings:
                    a = a.strip()
                    actors += [Actor(a)]

                description = row['Description']
                director = Director(row['Director'])
                release_year = int(row['Year'])
                runtime = int(row['Runtime (Minutes)'])
                movie_obj = Movie(title, release_year)

                for g in genres:
                    movie_obj.add_genre(g)
                    if g not in self.dataset_of_genres:
                        self.dataset_of_genres += [g]
                for a in actors:
                    movie_obj.add_actor(a)
                    if a not in self.dataset_of_actors:
                        self.dataset_of_actors += [a]
                movie_obj.director = director
                movie_obj.runtime_minutes = runtime

                self.dataset_of_movies += [movie_obj]
                if director not in self.dataset_of_directors:
                    self.dataset_of_directors += [director]
