from flask import render_template,send_from_directory

from app import app


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/<path:path>')
def send_js(path):
    return send_from_directory('/c/Users/thelonius/git/testunk', path)
