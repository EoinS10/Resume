from app import app
from flask import render_template

@app.route('/research')
def research():
    return render_template("research.html")
