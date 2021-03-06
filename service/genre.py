from dao.genre import GenreDao
from exception import ItemNotFound


class GenreService:
    def __init__(self, dao: GenreDao):
        self.dao = dao

    def get_one(self, gid):
        result = self.dao.get_one(gid)
        if not result:
            raise ItemNotFound
        return result


    def get_all(self):
        return self.dao.get_all()

    def create(self, data):
        return self.dao.create(data)

    def update(self, data):
        gid = data.get('id')
        genre = self.dao.get_one(gid)

        genre.name = data.get('name')

        self.dao.update(genre)

    def delete(self,gid):
        result = self.dao.delete(gid)
        if not result:
            raise ItemNotFound
        return result