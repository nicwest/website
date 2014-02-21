from flask import Flask, render_template
from app import app, models


@app.route('/')
def index():
    posts = models.Post.query.order_by(models.Post.date.desc()).all()
    return render_template('index.html', posts=posts)

@app.route('/blog/<slug>')
def view_post(slug):
    return render_template('index.html')

@app.route('/blog/tag/<slug>')
def view_tag(slug):
    return render_template('blog.html')