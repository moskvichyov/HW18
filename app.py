from flask import Flask
from flask_restx import Api

from config import Config
from setup_db import db
from views.directors import director_ns
from views.movies import movie_ns
from views.genres import genre_ns

def create_app(config: Config):
     app = Flask(__name__)
     app.config.from_object(config)
     app.app_context().push()
     # register_extensions(app)
     return app

def configure_app(app: Flask):
     db.init_app(app)
     api = Api(app)
     api.add_namespace(director_ns)
     api.add_namespace(movie_ns)
     api.add_namespace(genre_ns)




if __name__ == '__main__':
     app_config = Config()
     app = create_app(app_config)
     app.run(host="localhost", port=10001, debug=True)



