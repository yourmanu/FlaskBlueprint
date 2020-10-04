from flask import Blueprint, render_template

users_bp = Blueprint(
    "users_bp", __name__, url_prefix="/users", template_folder="templates"
)


@users_bp.route("/")
def list_users():
    return render_template("users/list.html")

@users_bp.route("admin")
def admin():
    return "Yes, I am admin"