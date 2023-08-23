from flask import Flask, render_template, url_for

app = Flask(__name__)


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


if __name__ == '__main__':
    app.run()
