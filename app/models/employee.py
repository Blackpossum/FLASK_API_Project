from app.utils.database import db

class employee(db.Model):
    id = db.Column(db.BigInteger, primary_key= True)
    name = db.Column(db.String(50), nullable = False)
    age =  db.Column(db.Integer, nullable = False)
    specialization = db.Column(db.String(100), nullable=False)
    section_operation = db.Column(db.String(50), nullable=True)











# id
# name
# join_at 
# age
# specialization
# section_operation
