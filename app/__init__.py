from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SECRET_KEY"] = "3521424a54cc99beab3be9202ece2672"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"
# relative path from current file
# create database instance
db = SQLAlchemy(app)

from app import routes
# need to include routes, so when we run the app it can find the routes