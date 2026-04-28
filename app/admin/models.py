from app.extenstions import db


class Student(db.Model):
    __tablename__ = "students"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    age = db.Column(db.String(10))
    gender = db.Column(db.String(10))
    class_name = db.Column(db.String(20))
    batch = db.Column(db.String(20))
    email = db.Column(db.String(100))
    phone = db.Column(db.String(20))
    address = db.Column(db.String(200))
    parent_name = db.Column(db.String(100))
    


from app.extenstions import db


class Faculty(db.Model):
    __tablename__ = "faculty"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    phone = db.Column(db.String(20))
    location = db.Column(db.String(100))
    subject = db.Column(db.String(100))

    class1 = db.Column(db.String(100))
    class2 = db.Column(db.String(100))
    class3 = db.Column(db.String(100))
    class4 = db.Column(db.String(100))
    class5 = db.Column(db.String(100))
    class6 = db.Column(db.String(100))