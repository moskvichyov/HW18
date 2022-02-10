from flask_restx import Resource, Namespace

import service
from dao.model.genre import Genre, GenreSchema
from container import genre_service

genre_ns = Namespace('genres')


@genre_ns.route('/')
class GenreView(Resource):
    def get_all(self):
        all_directors = genre_service.get_all()
        return GenreSchema(many=True).dump(all_directors)

@genre_ns.route('/<int: gid>')
class GenreView(Resource):
    def get_one(self, gid):
        one_director = genre_service.get_one(gid)
        if one_director:
            return GenreSchema().dump(one_director)
        else:
            return '', 404

