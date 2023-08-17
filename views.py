from flask import Blueprint, render_template, request

views = Blueprint(__name__, "views")

@views.route("/hello")
def home():
    return render_template("index.html")

@views.route("/Games")
def Games():
    return render_template("Games")