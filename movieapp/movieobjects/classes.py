import datetime
import csv
from flask_login import UserMixin
from movieapp import account_manager

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
