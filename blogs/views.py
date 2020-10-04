from flask import Blueprint, render_template, redirect, session
from flask.helpers import url_for
from .forms import Blog, Bloga
from json import loads

blogs_bp = Blueprint('blogs_bp', __name__, url_prefix='/blogs', template_folder='templates')


@blogs_bp.route("/")
def list_blog():
    if (session["title"]):
        blog = {
            "title": session["title"],
            "author": session["author"],
            "content": session["content"],
        }
    else:  
        blog = {}  
    return render_template("blogs/list.html", blog=blog)


@blogs_bp.route("new", methods=["GET", "POST"])
def new():
    form = Blog()
    if form.validate_on_submit():
        session["title"] = form.title.data
        session["author"] = form.author.data
        session["content"] = form.content.data
        return redirect(url_for("blogs_bp.list_blog"))
    return render_template("blogs/add_blog.html", form=form)
