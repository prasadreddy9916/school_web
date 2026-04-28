from .models import Student
from app.extenstions import db


def get_all_students_service():
    return Student.query.all()


def create_student_service(data):
    student = Student(
        name=data.get("name"),
        age=data.get("age"),
        gender=data.get("gender"),
        class_name=data.get("class"),
        batch=data.get("batch"),
        email=data.get("email"),
        phone=data.get("phone"),
        address=data.get("address"),
        parent_name=data.get("parent")
    )

    db.session.add(student)
    db.session.commit()

    return student


def get_student_by_id_service(id):
    return Student.query.get(id)


def update_student_service(student, data):
    student.name = data.get("name")
    student.age = data.get("age")
    student.gender = data.get("gender")
    student.class_name = data.get("class")
    student.batch = data.get("batch")
    student.email = data.get("email")
    student.phone = data.get("phone")
    student.address = data.get("address")
    student.parent_name = data.get("parent")

    db.session.commit()
    return student


def delete_student_service(student):
    db.session.delete(student)
    db.session.commit()



from .models import Faculty
from app.extenstions import db


def get_all_faculty_service():
    return Faculty.query.all()


def create_faculty_service(data):
    faculty = Faculty(
        name=data.get("name"),
        phone=data.get("phone"),
        location=data.get("location"),
        subject=data.get("subject"),
        class1=data.get("class1"),
        class2=data.get("class2"),
        class3=data.get("class3"),
        class4=data.get("class4"),
        class5=data.get("class5"),
        class6=data.get("class6")
    )

    db.session.add(faculty)
    db.session.commit()
    return faculty


def get_faculty_by_id_service(id):
    return Faculty.query.get(id)


def update_faculty_service(faculty, data):
    faculty.name = data.get("name")
    faculty.phone = data.get("phone")
    faculty.location = data.get("location")
    faculty.subject = data.get("subject")

    faculty.class1 = data.get("class1")
    faculty.class2 = data.get("class2")
    faculty.class3 = data.get("class3")
    faculty.class4 = data.get("class4")
    faculty.class5 = data.get("class5")
    faculty.class6 = data.get("class6")

    db.session.commit()
    return faculty


def delete_faculty_service(faculty):
    db.session.delete(faculty)
    db.session.commit()