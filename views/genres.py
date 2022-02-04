from flask_restx import Resource, Namespace
from models import Genre, GenreSchema

genre_ns = Namespace('genres')

