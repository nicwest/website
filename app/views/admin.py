from flask import Flask, render_template, request
from app import app, db, models, forms

@app.route('/admin')
def admin():
    # categories = models.cv.Category.query.all()
    return render_template('admin_dash.html')


@app.route('/admin/cv/browse')
@app.route('/admin/cv')
def admin_cv_browse():
    cvs = models.CV.query.all()
    return render_template('admin_cv_browse.html', cvs=cvs)

@app.route('/admin/cv/new')
def admin_cv_new():
    return ''

@app.route('/admin/cv/items')
def admin_cv_items():
    items = models.Item.query.filter_by(parent=None).order_by(models.Item.default_order.asc()).all()
    return render_template('admin_cv_items.html', items=items)

@app.route('/admin/cv/categories')
def admin_cv_categories():
    return ''

@app.route('/admin/cv/<id>/edit')
def admin_cv_edit(id):
    return ''

@app.route('/admin/cv/<id>/delete')
def admin_cv_delete(id):
    return ''
@app.route('/admin/cv/item/<id>/edit')
def admin_cv_item_edit(id):
    item = models.Item.query.filter_by(id=id).first()
    form = forms.Item()
    form.admin_title.data = item.admin_title
    form.typ.data = item.typ
    form.parent.data = str(item.parent.id)
    form.key.data = item.key
    form.value.data = item.value
    form.note.data = item.note
    print item.parent.id
    return render_template('admin_cv_item_edit.html', form=form)

@app.route('/admin/cv/item/<id>/delete')
def admin_cv_item_delete(id):
    return ''