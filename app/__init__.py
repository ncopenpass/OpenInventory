import enum
import logging
import os
from logging.handlers import RotatingFileHandler

from flask import Flask
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_bootstrap import Bootstrap
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from config import Config

db = SQLAlchemy()
migrate = Migrate()
bootstrap = Bootstrap()
admin = Admin(name='Open Inventory', template_mode='bootstrap3')

class EquipmentStatus(enum.Enum):
    MISSING = "Missing"
    PRESENT = "Present"
    DAMAGED = "Damaged"

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    admin.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)
    bootstrap.init_app(app)

    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    #from app.errors import bp as errors_bp
    #app.register_blueprint(errors_bp)

    admin.add_view(ModelView(models.District, db.session))
    admin.add_view(ModelView(models.Department, db.session))
    admin.add_view(ModelView(models.Truck, db.session))
    admin.add_view(ModelView(models.Compartment, db.session))
    admin.add_view(ModelView(models.Equipment, db.session))
    admin.add_view(ModelView(models.EquipmentCheckLog, db.session))

    if not app.debug and not app.testing:
        if app.config['LOG_TO_STDOUT']:
            stream_handler = logging.StreamHandler()
            stream_handler.setLevel(logging.INFO)
            app.logger.addHandler(stream_handler)
        else:
            if not os.path.exists('logs'):
                os.mkdir('logs')
            file_handler = RotatingFileHandler('logs/open-inventory.log', maxBytes=10240, backupCount=10)
            file_handler.setFormatter(logging.Formatter(
                '%(asctime)s %(levelname)s: %(message)s '
                '[in %(pathname)s:%(lineno)d]'))
            file_handler.setLevel(logging.INFO)
            app.logger.addHandler(file_handler)

        app.logger.setLevel(logging.INFO)
        app.logger.info("Open Inventory")

    return app


from app import models
