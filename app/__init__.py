from flask import Flask
from app.routes import Animal_management,Employe_management
import os
from app.utils.database import db

app = Flask(__name__)


DATABASE_TYPE = os.getenv('DATABASE_TYPE')
DATABASE_USER = os.getenv('DATABASE_USER')
DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD')
DATABASE_HOST = os.getenv('DATABASE_HOST')
DATABASE_NAME = os.getenv('DATABASE_NAME')
DATABASE_PORT = os.getenv('DATABASE_PORT')
app.config["SQLALCHEMY_DATABASE_URI"] = f"{DATABASE_TYPE}://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}"
db.init_app(app)


@app.route("/")
def home():
    return "Welcome to the Zoo API!"

app.register_blueprint(Animal_management.animals_Blueprint, url_prefix = "/Animal")
app.register_blueprint(Employe_management.Employe_blueprint, url_prefix = "/Employee")