from flask import Flask
from flask import flash, redirect, render_template, request, session, url_for


app = Flask(__name__)
session = {}
app.config['SECRET_KEY']="sdsadasd"

@app.route("/")
def index():
    flash("Hello World",category="success")
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True) 