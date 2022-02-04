from flask_restx import Resource, Namespace
from models import Director, DirectorSchema

director_ns = Namespace('directors')

@director_ns.route('/')
class DirectorView(Resource):
    def get(self):
        all_directors = Director.query.all()
        return DirectorSchema(many=True).dump(all_directors)

@director_ns.route('/<int: id>')
class DirectorView(Resource):
    def get(self, id):
        one_director = Director.query.get(id)
        return DirectorSchema.dump(one_director)
