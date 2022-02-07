from dao.model.director import Director


class DirectorDao:
    def __init__(self, session):
        self.session = session

    def get_one(self, did):
        return self.session.query(Director).get(did)

    def get_all(self):
        return self.session.query(Director).all()

    def put(self):
        pass

    def delete(self):
        pass