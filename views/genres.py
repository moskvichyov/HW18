from flask_restx import Resource, Namespace, abort

from dao.model.genre import GenreSchema
from container import genre_service

genre_ns = Namespace('genres')


@genre_ns.route('/')
class GenreView(Resource):
    def get(self):
        all_genres = genre_service.get_all()
        return GenreSchema(many=True).dump(all_genres)

@genre_ns.route('/<int:gid>')
class GenreView(Resource):
    def get(self, gid):
        try:
            return GenreSchema().dump(genre_service.get_one(gid))
        except:
            abort(404)
