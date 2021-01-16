from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_api.config import Config
from flask_migrate import Migrate

db = SQLAlchemy()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    migrate = Migrate(app,db)

    from flask_api.Users.routes import user
    from flask_api.Main.routes import main
    app.register_blueprint(user)
    app.register_blueprint(main)


    return app