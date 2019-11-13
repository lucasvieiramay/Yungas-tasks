from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_restless import APIManager

from config import Configuration

app = Flask(__name__)
app.config.from_object(Configuration)
db = SQLAlchemy(app)
api = APIManager(app, flask_sqlalchemy_db=db)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)
