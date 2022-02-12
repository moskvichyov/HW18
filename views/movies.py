from flask import request
from flask_restx import Resource, Namespace, abort

from container import movie_service
from dao.model.movie import MovieSchema

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
        try:
            return MovieSchema(many=True).dump(movie_service.get_all(filters))
        except:
            abort(404)

    def post(self):
        rj = request.json
        movie = movie_service.create(rj)
        return "New film added", 201, {"location": f"/movies/{movie.id}"}


@movie_ns.route('/<int:mid>')
class MovieView(Resource):
    def get(self, mid):
        try:
            return MovieSchema().dump(movie_service.get_one(mid)), 200
        except:
            movie_ns.abort(404)

    def put(self, mid):
        rj = request.json

        if 'id' not in rj:
            rj['id'] = mid
        movie_service.update(rj)
        return 'Current movie updated', 201

    def patch(self, mid):
        rj = request.json
        rj['id'] = mid

        movie_service.update_part(rj)
        return 'Current movie updated', 201

    def delete(self, mid):
        try:
            return movie_service.delete(mid), 204
        except:
            abort(404)

