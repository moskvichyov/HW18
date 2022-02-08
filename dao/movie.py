from dao.model.movie import Movie


class MovieDao:
    def __init__(self, session):
        self.session = session

    def get_one(self, mid):
        return self.session.query(Movie).get(mid)

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
        movie = self.get_one(mid)
        if movie:
            try:
                self.session.delete(movie)
                self.session.commit()
            except:
                return '', 404