from werkzeug.security import generate_password_hash, check_password_hash
from app.extenstions import db
from .models import User
from app.home.models import Admission


# register
def register_user_service(data):
    existing_user = User.query.filter_by(email=data["email"]).first()
    if existing_user:
        return None, "User already exists"

    encrypted_password = generate_password_hash(data["password"])

    user = User(
        name=data["name"],
        email=data["email"],
        password=encrypted_password,
        phone=data.get("phone"),
        role=data.get("role", "user")
    )

    db.session.add(user)
    db.session.commit()

    return user, None  


# login
def login_user_service(email, password):
    user = User.query.filter_by(email=email).first()

    if user and check_password_hash(user.password, password):
        return user   

    return None       


# admission details
def get_all_admissions_service():
    admissions = Admission.query.all()
    return admissions