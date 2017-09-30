# coding: utf-8
from flask import Flask
from itsdangerous import URLSafeTimedSerializer

from pms.extensions import db, login_manager
from pms.blueprints.user.models import User


def create_app():
    """
    Create a Flask app using the app factory pattern.
    
    :return: Flask app
    """
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object('config.settings')
    # silent告诉flask就算文件不在也不会崩溃
    app.config.from_pyfile('settings.py', silent=True)

    from pms.blueprints.user import user
    from pms.blueprints.admin import admin

    app.register_blueprint(user)
    app.register_blueprint(admin)
    extensions(app)
    authentication(app, User)

    return app


def extensions(app):
    """
    Register 0 or more extensions.

    :param app: Flask app instance
    :return: None
    """
    db.init_app(app)
    login_manager.init_app(app)

    return None


def authentication(app, user_model):
    """
    初始化Flask-Login扩展。

    :param app: Flask app instance
    :param user_model: Model that contains the authentication information
    :type user_model: SQLAlchemy model
    :return: None
    """
    login_manager.login_view = 'user.login'

    @login_manager.user_loader
    def load_user(user_id):
        return user_model.query.get(user_id)

    @login_manager.token_loader
    def load_token(token):
        duration = app.confg['REMEMBER_COOKIE_DURATION'].total_seconds()
        serializer = URLSafeTimedSerializer(app.secret_key)

        data = serializer.loads(token, max_age=duration)
        print(data)
        user_id = data[0]

        return user_model.query.get(user_id)