from app.extenstions import db

class Admission(db.Model):
    __tablename__ = "admissions"

    id = db.Column(db.Integer, primary_key=True)
    student_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100),unique=True, nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    
    board = db.Column(db.String(50), nullable=False)  
    
    location = db.Column(db.String(50), nullable=False)   
    message = db.Column(db.String(255))