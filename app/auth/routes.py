from . import auth_bp
from flask import request, render_template, redirect, url_for
from flask_login import login_user, logout_user, login_required 
from .services import register_user_service, login_user_service, get_all_admissions_service



# register

@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        data = request.form 

      
        if not data.get("name") or not data.get("email") or not data.get("password"):
            return render_template("register.html", error="All fields are required"), 400

        user, error = register_user_service(data)

        if error:
            return render_template("register.html", error=error), 409

        return redirect(url_for("auth.login")), 302

    return render_template("register.html"), 200


# Login

@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        if not email or not password:
            return render_template("login.html", error="Email and password required"), 400

        user = login_user_service(email, password)

        if not user:
            return render_template("login.html", error="Invalid email or password"), 401

        login_user(user)
        return redirect(url_for("auth.dashboard")), 302

    return render_template("login.html"), 200



# Dashboard

@auth_bp.route("/dashboard")
@login_required  
def dashboard():
    admissions = get_all_admissions_service()
    return render_template("dashboard.html", admissions=admissions), 200

# logout
@auth_bp.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("home.home")), 302