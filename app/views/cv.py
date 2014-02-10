from flask import Flask, render_template
from app import app, db, models


@app.route('/cv')
def cv_display():
    return render_template('temp_cv.html')

