from flask import render_template,send_from_directory

from app import app
import os

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/<path:path>')
def sendfiles(path):
    try:
        return send_from_directory(os.environ['flaskroot'], path)
    except Exception as e:
        return send_from_directory(os.environ['flaskroot'], os.path.join(path, "index.html"))
