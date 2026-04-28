from . import admin_bp
from flask import render_template, request, jsonify
from flask_login import login_required

from .services import (
    get_all_students_service,
    create_student_service,
    get_student_by_id_service,
    update_student_service,
    delete_student_service
)


# PAGE
@admin_bp.route("/students")
@login_required
def students_page():
    return render_template("students.html")


# GET ALL
@admin_bp.route("/api/students", methods=["GET"])
@login_required
def get_students():
    students = get_all_students_service()

    data = []
    for s in students:
        data.append({
            "id": s.id,
            "name": s.name,
            "age": s.age,
            "gender": s.gender,
            "class": s.class_name,
            "batch": s.batch,
            "email": s.email,
            "phone": s.phone,
            "address": s.address,
            "parent": s.parent_name
        })

    return jsonify(data), 200


# CREATE
@admin_bp.route("/api/students", methods=["POST"])
@login_required
def create_student():
    data = request.get_json()

    if not data:
        return jsonify({"error": "No data"}), 400

    create_student_service(data)
    return jsonify({"message": "Student added"}), 201


# GET ONE
@admin_bp.route("/api/students/<int:id>", methods=["GET"])
@login_required
def get_student(id):
    student = get_student_by_id_service(id)

    if not student:
        return jsonify({"error": "Not found"}), 404

    return jsonify({
        "id": student.id,
        "name": student.name,
        "age": student.age,
        "gender": student.gender,
        "class": student.class_name,
        "batch": student.batch,
        "email": student.email,
        "phone": student.phone,
        "address": student.address,
        "parent": student.parent_name
    }), 200


# UPDATE
@admin_bp.route("/api/students/<int:id>", methods=["PUT"])
@login_required
def update_student(id):
    student = get_student_by_id_service(id)

    if not student:
        return jsonify({"error": "Not found"}), 404

    data = request.get_json()
    update_student_service(student, data)

    return jsonify({"message": "Updated"}), 200


# DELETE
@admin_bp.route("/api/students/<int:id>", methods=["DELETE"])
@login_required
def delete_student(id):
    student = get_student_by_id_service(id)

    if not student:
        return jsonify({"error": "Not found"}), 404

    delete_student_service(student)
    return jsonify({"message": "Deleted"}), 200


from .services import (
    get_all_faculty_service,
    create_faculty_service,
    get_faculty_by_id_service,
    update_faculty_service,
    delete_faculty_service
)


# PAGE
@admin_bp.route("/faculty")
@login_required
def faculty_page():
    return render_template("faculty.html")


# GET ALL
@admin_bp.route("/api/faculty", methods=["GET"])
@login_required
def get_faculty():
    faculty_list = get_all_faculty_service()

    data = []
    for f in faculty_list:
        data.append({
            "id": f.id,
            "name": f.name,
            "phone": f.phone,
            "location": f.location,
            "subject": f.subject,
            "class1": f.class1,
            "class2": f.class2,
            "class3": f.class3,
            "class4": f.class4,
            "class5": f.class5,
            "class6": f.class6
        })

    return jsonify(data), 200


# CREATE
@admin_bp.route("/api/faculty", methods=["POST"])
@login_required
def create_faculty():
    data = request.get_json()

    if not data:
        return jsonify({"error": "No data"}), 400

    create_faculty_service(data)
    return jsonify({"message": "Faculty added"}), 201


# GET ONE
@admin_bp.route("/api/faculty/<int:id>", methods=["GET"])
@login_required
def get_one_faculty(id):
    faculty = get_faculty_by_id_service(id)

    if not faculty:
        return jsonify({"error": "Not found"}), 404

    return jsonify({
        "id": faculty.id,
        "name": faculty.name,
        "phone": faculty.phone,
        "location": faculty.location,
        "subject": faculty.subject,
        "class1": faculty.class1,
        "class2": faculty.class2,
        "class3": faculty.class3,
        "class4": faculty.class4,
        "class5": faculty.class5,
        "class6": faculty.class6
    }), 200


# UPDATE
@admin_bp.route("/api/faculty/<int:id>", methods=["PUT"])
@login_required
def update_faculty(id):
    faculty = get_faculty_by_id_service(id)

    if not faculty:
        return jsonify({"error": "Not found"}), 404

    data = request.get_json()
    update_faculty_service(faculty, data)

    return jsonify({"message": "Updated"}), 200


# DELETE
@admin_bp.route("/api/faculty/<int:id>", methods=["DELETE"])
@login_required
def delete_faculty(id):
    faculty = get_faculty_by_id_service(id)

    if not faculty:
        return jsonify({"error": "Not found"}), 404

    delete_faculty_service(faculty)
    return jsonify({"message": "Deleted"}), 200