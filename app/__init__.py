from flask import Flask
from flask_foundation import Foundation

from app.misc import db
from config import config

foundation = Foundation()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    db.init_app(app)
    foundation.init_app(app)

    from app.main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
