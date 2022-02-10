from dao.model.movie import Movie
from flask_restx import abort


class MovieDao:
    def __init__(self, session):
        self.session = session

    def get_one(self, mid):
        try:
            return self.session.query(Movie).get(mid)
        except:
            abort(404)

    def get_all(self):
        return self.session.query(Movie).all()

    def create(self, data):
        movie = Movie(**data)

        self.session.add(movie)
        self.session.commit()
        return movie

    def update(self, movie):
        self.session.add(movie)
        self.session.commit()

        return movie


    def delete(self, mid):
        try:
            movie = self.get_one(mid)
            self.session.delete(movie)
            self.session.commit()
        except:
            abort(404)