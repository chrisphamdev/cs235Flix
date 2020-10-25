import pytest
from movieapp.movieobjects.classes import *

def test_actor():
    actor1 = Actor("Chris Evans")
    actor2 = Actor("Chris Pratt")
    actor1.add_actor_colleague(actor2)

    assert actor1 < actor2
    assert actor1 != actor2
    assert actor1.check_if_this_actor_worked_with(actor2)

def test_director():
    director1 = Director("Trevor")
    director2 = Director("Michael")
    assert director1 != director2

def test_genre():
    action = Genre("Action")
    thriller = Genre("Thriller")
    assert action != thriller

def test_movie():
    movie1 = Movie("Movie Sample 1", 2012)
    movie2 = Movie("Movie Sample 2", 2020)
    assert movie1 < movie2