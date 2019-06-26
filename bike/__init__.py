from flask import Flask
from bike.models.base import db
from flask_login import LoginManager


login_manager = LoginManager()


def create_app():
    app = Flask(__name__)
    app.config.from_object('bike.secure')
    register_blueprint(app)

    db.init_app(app)
    login_manager.init_app(app)
    # 创建所有继承了db中db.Model类的类对应的数据库表
    db.create_all(app=app)

    return app


def register_blueprint(app):
    from bike.web import web
    app.register_blueprint(web)