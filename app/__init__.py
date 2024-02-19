from flask import Flask
from app.routes import Animal_management
from app.routes import Employe_management

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to the Zoo API!"

app.register_blueprint(Animal_management.Animal_Blueprint, url_prefix = "/Animal")
app.register_blueprint(Employe_management.Employe_blueprint, url_prefix = "/Employee")