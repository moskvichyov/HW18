from flask import request
from flask_restx import Resource, Namespace

import service
from container import movie_service
from dao.model.movie import Movie, MovieSchema
from config import Config

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
        return '', 201

@movie_ns.route('/<int: mid>')
class MovieView(Resource):
    def get(self, mid):
        one_movie = movie_service.get_one(mid)
        try:
            return MovieSchema.dump(one_movie), 200
        except:
            return f'Not found {mid}'

    def put(self, mid):
        rj = request.json

        if id not in rj:
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


