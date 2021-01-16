
class Config:
    SECRET_KEY = 'senha'
    SQLALCHEMY_DATABASE_URI = 'postgres://postgres:root@127.0.0.1/flask_api_example'
    SQLALCHEMY_TRACK_MODIFICATIONS = False