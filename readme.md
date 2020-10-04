to keep same named files in templates folder,

allways create the blueprint like below:

users_bp = Blueprint(
    "users_bp", __name__, url_prefix="/users", template_folder="templates"
)

and when rendering the file, call like this:

return render_template('profile/list.html')

