from flask import Flask, render_template, url_for

app = Flask(__name__)
app.secret_key = "munthu koma uyu"


@app.route("/hello")
def index():
    return render_template("index.html")

#when i click the link in the browser it should take me to the route
@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == '__main__':
    app.run()
