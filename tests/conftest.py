import pytest
from flask import Flask
from app.utils.database import db
from app.routes.Animal_management import animals_Blueprint
from app.routes.Employe_management import employee_Blueprint

# Fixture for animal routes
@pytest.fixture
def app_with_animals():
    app = Flask(__name__)
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    
    db.init_app(app)
    app.register_blueprint(animals_Blueprint)
    
    return app

@pytest.fixture
def client_with_animals(app_with_animals):
    with app_with_animals.test_client() as client:
        with app_with_animals.app_context():
            db.create_all()
        yield client

# Fixture for employee routes
@pytest.fixture
def app_with_employees():
    app = Flask(__name__)
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    
    db.init_app(app)
    app.register_blueprint(employee_Blueprint)
    
    return app

@pytest.fixture
def client_with_employees(app_with_employees):
    with app_with_employees.test_client() as client:
        with app_with_employees.app_context():
            db.create_all()
        yield client
