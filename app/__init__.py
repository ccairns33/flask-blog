from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
app = Flask(__name__)
app.config["SECRET_KEY"] = "3521424a54cc99beab3be9202ece2672"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"
# relative path from current file
# create database instance
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
# add funcionality to db models and handles sessions
login_manager = LoginManager(app)
# login is function name for our route, tells where login route is located for @login_required decorater
login_manager.login_view = 'login'
# bootstrap class info
login_manager.login_message_category = 'info'
from app import routes
# need to include routes, so when we run the app it can find the routes
# routes are importing app variable, so we must put the import of routes after the app initialization
