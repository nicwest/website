from flask import Flask, render_template, request
from app import app, db, models

@app.route('/admin')
def admin():
    # categories = models.cv.Category.query.all()
    return render_template('admin_dash.html')


@app.route('/admin/cv/browse')
@app.route('/admin/cv')
def admin_cv_browse():
    cvs = models.cv.CV.query.all()
    return render_template('admin_cv_browse.html', cvs=cvs)

@app.route('/admin/cv/new')
def admin_cv_new():
    return ''

@app.route('/admin/cv/items')
def admin_cv_items():
    return ''

@app.route('/admin/cv/categories')
def admin_cv_categories():
    return ''

@app.route('/admin/cv/edit')
def admin_cv_edit():
    return ''

@app.route('/admin/cv/delete')
def admin_cv_delete():
    return ''