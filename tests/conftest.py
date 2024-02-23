import pytest
import json
from flask import Flask
from app.utils.database import db
from app.routes.Animal_management import animals_Blueprint

@pytest.fixture
def app():
    # Create a Flask app instance
    app = Flask(__name__)
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    
    # Register the SQLAlchemy instance with the app
    db.init_app(app)
    
    # Register the blueprint with the app
    app.register_blueprint(animals_Blueprint)
    
    # Return the Flask app instance
    return app

@pytest.fixture
def client(app):
    # Create a test client using the Flask app instance
    with app.test_client() as client:
        # Set up a context for the app
        with app.app_context():
            # Create the database schema
            db.create_all()
        # Yield the test client for use in tests
        yield client
