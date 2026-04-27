from app.extenstions import db
from flask_login import UserMixin

class User(UserMixin,db.Model):
    
    __tablename__ ='users'
    
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(40))
    email= db.Column(db.String(40),unique=True)
    
    password = db.Column(db.String(255) ,nullable=False)
    phone = db.Column(db.String(40))
    
    role = db.Column(db.String(40))
    
    