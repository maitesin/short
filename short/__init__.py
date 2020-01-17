from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from short.config import Config

db = SQLAlchemy()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    from short.routes import short as short_routes

    app.register_blueprint(short_routes)

    return app
