from flask import render_template
from . import mySiteApp

# app routes
@mySiteApp.route("/index/")
@mySiteApp.route("/")
def index():
    return render_template("index.html")

@mySiteApp.route("/about/")
def about():
    return render_template("about.html")

@mySiteApp.route("/blog/")
def blog():
    return render_template("blog.html")

@mySiteApp.route("/projects/")
def projects():
    return render_template("projects.html")

@mySiteApp.route("/connect/")
def connect():
    return render_template("connect.html")

