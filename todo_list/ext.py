from flask_login import LoginManager
from flask_marshmallow import Marshmallow
from peewee import PostgresqlDatabase

db = PostgresqlDatabase(None)
ma = Marshmallow()
login_manager = LoginManager()
