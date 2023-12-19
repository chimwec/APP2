from flask import Flask, render_template, url_for, request
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, LoginManager
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)

app.config['SECRET_KEY'] = 'you-will-never-guess'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///my_database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

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

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Check if the username is already taken
        if User.query.filter_by(username=username).first():
            return 'Username already taken, please choose another!.'

        new_user = User(username=username, password=password)
        db.session.add(new_user)
        db.session.commit()

        return 'Registration successful! You can now <a href="/login">login</a>.'

    return render_template('register.html')

# update User to inherit from UserMixin here:
class User(UserMixin,db.Model):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(50), unique=True, nullable=False)
  password = db.Column(db.String(50), nullable=False)

  # add the email and password_hash attributes here:
  email = db.Column(db.String(120), index = True, unique = True)
  password_hash = db.Column(db.String(128))


if __name__ == '__main__':
   with app.app_context():
       db.create_all()
   app.run()
           