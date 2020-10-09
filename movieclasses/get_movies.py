from movieclasses.movieobjects.classes import *

def get_movies(filename:str):
    file_reader = MovieFileCSVReader(filename)
    file_reader.read_csv_file()

    all_movies = file_reader.dataset_of_movies
    all_actors = file_reader.dataset_of_actors
    all_genres = file_reader.dataset_of_genres
    all_directors = file_reader.dataset_of_directors

    return all_movies, all_actors, all_genres, all_directors

def movies_dict(movies):
    output = []
    for movie in movies:
        output += [
            {
                'title': movie.title,
                'year': str(movie.year),
                'director': movie.director.director_full_name,
                'actors': movie.actors_str(),
                'genres': movie.genres,
                'runtime': movie.runtime_minutes,
                'description': movie.description
            }
        ]
    return output