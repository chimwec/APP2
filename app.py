import email
from datetime import datetime
from turtle import title
from flask import Flask, render_template, url_for, request, redirect, flash
import flask 
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, LoginManager, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError



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


# registration form
class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
  # add email field here:
    email = StringField('Email', validators=[DataRequired(), Email()])
  # add password fields here:
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm(csrf_enabled=False)
    if form.validate_on_submit():
    # define user with data from form here:
        user = User(username=form.username.data, email=form.email.data)
    # set user's password here:
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
    return render_template('register.html', title='Register', form=form)

#added this form lets see how it works
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()

        if user:
            # Check if the entered password is correct
            if check_password_hash(user.password, password):
                login_user(user)

                flask.flash('Logged in succeessfully.')
                
                return redirect(url_for('index'))
            else:
                return 'Invalid password'
        else:
            return 'User not found. Please register.'

    return render_template('login.html')


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

# update User to inherit from UserMixin here:
class User(UserMixin,db.Model):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(50), unique=True, nullable=False)
  password = db.Column(db.String(50), nullable=False)
  email = db.Column(db.String(120), unique=True)

if __name__ == '__main__':
   with app.app_context():
       db.create_all()
   app.run()
           