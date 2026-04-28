from flask import render_template,request, jsonify
from .services import create_admission_service
from . import home_bp


@home_bp.route("/")
def home():
    return render_template("home.html")

@home_bp.route("/about")
def about():
    return render_template("about.html")

@home_bp.route("/contact")
def contact():
    return render_template("contact.html")



# PAGE
@home_bp.route("/admission")
def admission_page():
    return render_template("admission.html"), 200



# API
@home_bp.route("/api/admission", methods=["POST"])
def admission_submit():
    try:
        data = request.get_json()

        if not data:
            return jsonify({"error": "No data provided"}), 400

        required_fields = ["student_name", "email", "phone", "board", "location"]

        for field in required_fields:
            if not data.get(field):
                return jsonify({"error": f"{field} is required"}), 400

        create_admission_service(data)

        return jsonify({"message": "Admission submitted successfully"}), 201

    except Exception:
        return jsonify({"error": "Something went wrong"}), 500




