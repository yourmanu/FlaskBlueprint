from flask import Blueprint,render_template

profile_bp = Blueprint('profile_bp',__name__,url_prefix='/profile',template_folder='templates')

@profile_bp.route("/")
def list_profile():
    return render_template('profile/list.html')

@profile_bp.route("edit")
def edit_profile():
    return render_template('edit_profile.html')    