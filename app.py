from flask import Flask, render_template, redirect, url_for
from blogs.views import blogs_bp
from users.views import users_bp
from users.profile.views import profile_bp

app = Flask(__name__)
app.config['SECRET_KEY'] = 'shivakumar'

app.register_blueprint(blogs_bp,url_prefix='/blogs')
app.register_blueprint(users_bp,url_prefix='/users')
app.register_blueprint(profile_bp,url_prefix='/profile')

@app.route("/")
def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
