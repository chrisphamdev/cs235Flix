import pytest
from movieapp.helper import *
from movieapp.movieobjects.classes import *

def test_read_csv_file():
    filename = 'tests/data/Data1000Movies.csv'
    output_movie = Movie('Guardians of the Galaxy', 2014)
    all_movies, all_actors, all_genres, all_directors = get_movies(filename)
    assert all_movies[0] == output_movie

def test_moviefinder():
    movie1 = Movie("A", 2011)
    movie2 = Movie("B", 2013)
    movie3 = Movie("C", 2000)
    actor1 = Actor("Ronald Weasley")
    actor2 = Actor("Annabeth Chase")
    actor3 = Actor("Simon Lewis")

    movie1.add_actor(actor1)
    movie1.add_actor(actor2)

    movie2.add_actor(actor1)
    movie2.add_actor(actor2)
    movie2.add_actor(actor3)

    output = [movie1, movie2]
    assert moviefinder([movie1, movie2, movie3], [actor1, actor2]) == output
    