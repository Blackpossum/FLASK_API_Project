from sqlalchemy.orm import relationship
from app.models.animals import animals
from app.utils.database import db

class feeding_schedule(db.Model):
    no = db.Column(db.Integer, primary_key=True)
    animal_id = db.Column(db.Integer, db.ForeignKey('animals.id'), nullable=False)
    food_types = db.Column(db.String(100), nullable=False)
    feeding_times = db.Column(db.DateTime, nullable=False)

    # Define relationship with animals.py module
    animal = db.relationship('animals', back_populates='feeding_schedules')
