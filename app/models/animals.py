from app.utils.database import db

class animals(db.Model):
    id = db.Column(db.Integer, primary_key= True)
    name = db.Column(db.String(50), nullable = False)
    latin_name = db.Column(db.String(100), nullable = False)
    kingdom_class = db.Column(db.String(100),nullable = False)
    type_of_food = db.Column(db.String(100), nullable = False)  