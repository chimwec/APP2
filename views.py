from flask import Blueprint, render_template, request

views = Blueprint(__name__, "views")

@views.route("/hello")
def home():
    return render_template("index.html")

