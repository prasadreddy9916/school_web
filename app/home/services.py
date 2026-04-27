from app.extenstions import db

from .models import Admission

def create_admission_service(data):
    admission = Admission(
        student_name=data["student_name"],
        email=data["email"],
        phone=data["phone"],
        board=data["board"],
        location=data["location"],
        message=data.get("message")
    )


    db.session.add(admission)
    db.session.commit()

    return admission