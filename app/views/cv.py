from flask import Flask, render_template
from app import app, db, models

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cv')
def cv_display():
    return render_template('cv_template.html')

