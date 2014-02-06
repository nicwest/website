from flask import Flask, render_template
from app import app, db, models

@app.route('/admin')
def admin():
    categories = models.cv.Category.query.all()
    return render_template('admin_dash.html')
