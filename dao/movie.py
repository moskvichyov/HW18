from dao.model.movie import Movie


class MovieDao:
    def __init__(self, session):
        self.session = session

    def get_one(self, mid):
        return self.session.query(Movie).get(mid)

    def get_all(self):
        return self.session.query(Movie).all()

    def put(self):
        pass

    def delete(self):
        pass