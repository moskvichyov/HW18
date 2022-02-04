from setup_db import db
from marshmallow import Schema, fields


class Director(db.Model):
     __tablename__ = 'director'
     id = db.Column(db.Integer, primary_key=True)
     name = db.Column(db.String)


class DirectorSchema(Schema):
     id = fields.Int()
     name = fields.Str()



class Genre(db.Model):
     __tablename__ = 'genre'
     id = db.Column(db.Integer, primary_key=True)
     name = db.Column(db.String)


class GenreSchema(Schema):
     id = fields.Int()
     name = fields.Str()


class Movie(db.Model):
     __tablename__ = 'movie'
     id = db.Column(db.Integer, primary_key=True)
     title = db.Column(db.String)
     description = db.Column(db.String)
     trailer = db.Column(db.String)
     year = db.Column(db.Integer)
     genre_id = db.Column(db.Integer, db.ForeignKey('genre.id'))
     director_id = db.Column(db.Integer, db.ForeignKey('director.id'))


class MovieSchema(Schema):
     id = fields.Int(dump_only=True)
     title = fields.Str()
     description = fields.Str()
     trailer = fields.Str()
     year = fields.Int()
     genre_id = fields.Int()
     director_id = fields.Int()


