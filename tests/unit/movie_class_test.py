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
