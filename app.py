from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)

app.config['SECRET_KEY'] = 'you-will-never-guess'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///my_database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


@app.route("/home")
def index():
    return render_template("index.html")

#when i click the link in the browser it should take me to the route
@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/game")
def game():
    return render_template("game.html")

@app.route("/news")
def news():
    return render_template("news.html")

@app.route("/follow_us")
def follow_us():
  return render_template("follow_us.html")

# update User to inherit from UserMixin here:
class User(UserMixin,db.Model):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(64), index=True, unique=True)

  # add the email and password_hash attributes here:
  email = db.Column(db.String(120), index = True, unique = True)
  password_hash = db.Column(db.String(128))


if __name__ == '__main__':
    app.run()