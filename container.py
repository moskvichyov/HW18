from dao.director import DirectorDao
from dao.genre import GenreDao
from dao.movie import MovieDao
from service.director import DirectorService
from service.genre import GenreService
from service.movie import MovieService
from setup_db import db

movie_dao = MovieDao(session=db.session)
movie_service = MovieService(movie_dao)

director_dao = DirectorDao(session=db.session)
director_service = DirectorService(director_dao)

genre_dao = GenreDao(session=db.session)
genre_service = GenreService(genre_dao)
