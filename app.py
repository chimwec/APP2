from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "munthu koma uyu"


@app.route("/hello")
def index():
    flash("whats your name")
    return render_template("index.html")

if __name__ == '__main':
    app.run(debug=True, port=8000)

@app.route("/greet", methods=["POST", "GET"])
def greet():
    flash
    request.form['name_input']