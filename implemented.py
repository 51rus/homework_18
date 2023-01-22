from setup_db import db

from dao.movie_dao import MovieDao
from dao.director_dao import DirectorDAO
from dao.genre_dao import GenreDAO

from dao.model.movie import MovieSchema
from dao.model.director import DirectorSchema
from dao.model.genre import GenreSchema

from service.movie_service import MovieService
from service.director_service import DirectorService
from service.genre_service import GenreService

movie_dao = MovieDao(db.session)
movie_service = MovieService(movie_dao)
movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)

director_dao = DirectorDAO(db.session)
director_service = DirectorService(director_dao)
director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)

genre_dao = GenreDAO(db.session)
genre_service = GenreService(genre_dao)
genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)
