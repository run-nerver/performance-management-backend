from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_migrate import Migrate

db = SQLAlchemy()
cors = CORS()
migrate = Migrate()


# 注册蓝图
def register_blueprints(app):
    from app.api.v1.login import login_bp
    from app.api.v1.teacher import teacher_bp
    from app.api.v1.config import config_bp
    from app.api.v1.admin import admin_bp
    from app.api.v1.teaching_workload import teaching_workload_bp
    from app.api.v1.scientific_workload import scientific_workload_bp
    from app.api.v1.others_workload import others_workload_bp
    from app.api.v1.counselors_workload import counselors_workload_bp
    app.register_blueprint(login_bp, url_prefix='/v1')
    app.register_blueprint(teacher_bp, url_prefix='/v1')
    app.register_blueprint(config_bp, url_prefix='/v1')
    app.register_blueprint(admin_bp, url_prefix='/v1')
    app.register_blueprint(teaching_workload_bp, url_prefix='/v1')
    app.register_blueprint(scientific_workload_bp, url_prefix='/v1')
    app.register_blueprint(others_workload_bp, url_prefix='/v1')
    app.register_blueprint(counselors_workload_bp, url_prefix='/v1')


def register_plugin(app):
    cors.init_app(app, supports_credentials=True)
    db.init_app(app)
    from app.models.user import User
    from app.models.information import Information
    from app.models.rules import Rules
    from app.models.teaching_workload import TeachingWorkload
    from app.models.setting import Settings
    from app.models.scientific_workload import ScientificWorkload
    from app.models.others_workload import OthersWorkload
    from app.models.counselors_workload import CounselorsWorkload
    migrate.init_app(app, db)


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.settings')
    app.config.from_object('app.config.secure')
    register_blueprints(app)
    register_plugin(app)
    return app
