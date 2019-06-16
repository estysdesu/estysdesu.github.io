from flask import render_template
from flaskApp import estysdesu

# app routes
@estysdesu.route("/index/")
@estysdesu.route("/")
def index():
    return render_template("index.html")

@estysdesu.route("/about/")
def about():
    return render_template("about.html")

# @estysdesu.route("/blog/")
# def blog():
#     return render_template("blog.html")

# @estysdesu.route("/projects/")
# def projects():
#     return render_template("projects.html")

@estysdesu.route("/connect/")
def connect():
    return render_template("connect.html")

