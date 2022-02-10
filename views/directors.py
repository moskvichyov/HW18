from flask_restx import Resource, Namespace

from dao.model.director import DirectorSchema
from container import director_service

director_ns = Namespace('directors')

@director_ns.route('/')
class DirectorView(Resource):
    def get(self):
        all_directors = director_service.get_all()
        return DirectorSchema(many=True).dump(all_directors)

@director_ns.route('/<int: did>')
class DirectorView(Resource):
    def get(self, did):
        one_director = director_service.get_one(did)
        return DirectorSchema().dump(one_director)