from flask import request
from flask_restx import Resource, Namespace

from container import movie_service
from dao.model.movie import MovieSchema
# from config import Config

movie_ns = Namespace('movies')


@movie_ns.route('/')
class MovieView(Resource):
    def get(self):
        director = request.args.get('director_id')
        genre = request.args.get('genre_id')
        year = request.args.get('year')
        filters = {
            'director_id': director,
            'genre_id': genre,
            'year': year,
        }
        all_movies = movie_service.get_all(filters)
        return MovieSchema(many=True).dump(all_movies)

    def post(self):
        rj = request.json
        movie = movie_service.create(rj)
        return "", 201, {"location": f"/movies/{movie.id}"}


@movie_ns.route('/<int:mid>')
class MovieView(Resource):
    def get(self, mid):
        one_movie = movie_service.get_one(mid)
        return MovieSchema().dump(one_movie), 200


    def put(self, mid):
        rj = request.json

        if 'id' not in rj:
            rj['id'] = mid
        movie_service.update(rj)
        return 'New movie added', 204

    def patch(self, mid):
        rj = request.json
        rj ['id'] = mid

        movie_service.update_part(rj)
        return '', 204

    def delete(self, mid):
        movie_service.delete(mid)
        return 'Movie deleted', 204


