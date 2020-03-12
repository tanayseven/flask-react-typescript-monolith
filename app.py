import os
from pathlib import Path

from flask import Flask
from flask_security import PeeweeUserDatastore, Security
from peewee import PostgresqlDatabase

from todo_list.ext import db, ma, login_manager
from todo_list.user.model import UserModel, RoleModel, UserRoleModel

app: Flask = Flask(__name__.split('.')[0])

# Load the config
app.config.from_pyfile(Path(f'./config/common.py'))
app.config.from_pyfile(Path(f'./config/{os.environ.get("APP_ENVIRONMENT", default="dev").lower()}.py'))

# Initialise the peewee orm for postgres
postgres_db = PostgresqlDatabase(
    app.config.get('APP_NAME'),
    host=app.config.get('DB_HOST'),
    port=int(app.config.get('DB_PORT')),
    user=app.config.get('DB_USERNAME'),
    password=app.config.get('DB_PASSWORD'),
)
db.init(postgres_db)

# Initialise Marshmallow
ma.init_app(app)

# Setup Flask-Security
user_data_store = PeeweeUserDatastore(db, UserModel, RoleModel, UserRoleModel)
security = Security(app, user_data_store)

# Setup Flask-Login
login_manager.init_app(app)
