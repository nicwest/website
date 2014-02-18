from flask import Flask, render_template, request,  flash
from app import app, db, models, forms
import re
import datetime

@app.route('/admin')
def admin():
    # categories = models.cv.Category.query.all()
    return render_template('admin_dash.html')


@app.route('/admin/cv/browse')
@app.route('/admin/cv')
def admin_cv_browse():
    cvs = models.CV.query.all()
    return render_template('admin_cv_browse.html', cvs=cvs)

@app.route('/admin/blog/browse')
@app.route('/admin/blog')
def admin_blog_browse():
    posts = models.Post.query.order_by(models.Post.date.desc()).all()
    return render_template('admin_blog_browse.html', posts=posts)

@app.route('/admin/cv/new')
def admin_cv_new():
    return ''

@app.route('/admin/blog/new', methods=['GET', 'POST'])
def admin_blog_new():
    form = forms.Post()
    replacement = re.compile(r'[^a-z0-9]]')

    if form.validate_on_submit():
        slugtaken = models.Post.query.filter_by(slug=form.slug.data).first()
        if not slugtaken:
            new_post = models.Post(title=form.title.data,
                                   slug=form.slug.data,
                                   date=datetime.datetime.strptime(form.date.data, '%Y-%m-%dT%H:%M'),
                                   body=form.body.data)
            db.session.add(new_post)
            db.session.commit()

            tags = form.tags.data.split(', ')
            for tag in tags:
                tag = tag.lower()
                slug = replacement.sub('-', tag)
                found_tag = models.Tag.query.filter_by(slug=slug).first()

                if not found_tag:
                    found_tag = models.Tag(title=tag, slug=slug)
                    db.session.add(found_tag)
                    db.session.commit()
                new_post.tags.append(found_tag)
                db.session.commit()
        else:
            flash('Slug taken')

    return render_template('admin_blog_edit.html', form=form)

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


@app.route('/admin/ajax/<id>/<func>')
def admin_ajax(id, func):
    return ''