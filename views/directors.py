from flask_restx import Resource, Namespace

from service.director import DirectorService
from dao.model.director import Director, DirectorSchema
from container import movie_service, director_service, genre_service

director_ns = Namespace('directors')

@director_ns.route('/')
class DirectorView(Resource):
    def get(self):
        all_directors = director_service.query.all()
        return DirectorSchema(many=True).dump(all_directors)

@director_ns.route('/<int: id>')
class DirectorView(Resource):
    def get(self, id):
        one_director = director_service.query.get(id)
        if one_director:
            return DirectorSchema().dump(one_director)
        else:
            return '', 404
