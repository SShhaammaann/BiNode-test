from flask import Flask
from flask_bootstrap import Bootstrap
from flask_security import SQLAlchemyUserDatastore, Security
from flask_admin import Admin

from config import config
from app.core.models import db
from app.auth.models import User, Role
from app.auth.helpers import init_security
#from dnd.core.helpers import fill_db_with_sample_data

# create BootStrap and Security instances

bootstrap = Bootstrap()
security = Security()


def create_app(config_name):
    app = Flask(__name__)
    admin = Admin(base_template='admin/master.html',
                  template_mode='bootstrap3')
    # get the config from config.py
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    # register blueprints
    from app.core import core as core_blueprint
    app.register_blueprint(core_blueprint)

    # bind BS, DB, datastore and flask-admin to app
    bootstrap.init_app(app)
    db.init_app(app)
    user_datastore = SQLAlchemyUserDatastore(db, User, Role)
    security.init_app(app, user_datastore)
    admin.init_app(app)

    # init flask-admin views
    from app.auth.admin import init as init_auth_admin_models
    init_auth_admin_models(admin)

    @app.before_first_request
    def before_first_request():
        init_security(user_datastore)

    return app
