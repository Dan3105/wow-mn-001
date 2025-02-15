import os
from flask import Flask, send_from_directory
from flask_cors import CORS
from .db import db, init_db_command
from app.config import Config
from app.web.hooks import handle_error
from app.web.views import client_views


def create_app():
    app = Flask(__name__, static_folder="../client/dist", instance_path=Config.INSTANCE_PATH)
    app.url_map.strict_slashes = False
    app.debug = True
    app.config.from_object(Config)

    register_extensions(app)
    register_hooks(app)
    register_blueprints(app)
    # if Config.CELERY["broker_url"]:
    #     celery_init_app(app)

    return app

def register_blueprints(app: Flask):
    app.register_blueprint(client_views.bp)

def register_extensions(app):
    db.init_app(app)
    app.cli.add_command(init_db_command)

def register_hooks(app):
    CORS(app)
    app.register_error_handler(Exception, handle_error)