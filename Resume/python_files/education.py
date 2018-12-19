from app import app
from flask import render_template

@app.route('/education')
def education():
    return render_template("education.html")
