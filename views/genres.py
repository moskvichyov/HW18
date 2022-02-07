from flask_restx import Resource, Namespace

import service
from dao.model.genre import Genre, GenreSchema

genre_ns = Namespace('genres')


@genre_ns.route('/')
class GenreView(Resource):
    def get_all(self):
        all_directors = service.genre.query.all()
        return GenreSchema(many=True).dump(all_directors)

@genre_ns.route('/<int: gid>')
class GenreView(Resource):
    def get_one(self, gid):
        one_director = service.genre.query.get(gid)
        return GenreSchema.dump(one_director)

