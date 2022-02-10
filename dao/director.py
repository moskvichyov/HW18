from dao.model.director import Director
from flask_restx import abort


class DirectorDao:
    def __init__(self, session):
        self.session = session

    def get_one(self, did):
        try:
            return self.session.query(Director).get(did)
        except:
            abort(404)

    def get_all(self):
        return self.session.query(Director).all()

    def create(self, data):
        director = Director(**data)

        self.session.add(director)
        self.session.commit()
        return director


    def update(self, director):
        self.session.add(director)
        self.session.commit()

        return director



    def delete(self, did):
        director = self.get_one(did)

        self.session.delete(director)
        self.session.commit()
