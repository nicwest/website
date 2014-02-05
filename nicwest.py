from flask import Flask, render_template, session, g
from flask.ext.sqlalchemy import SQLAlchemy
from models import *

#make with the flaskings
app = Flask(__name__)

#load config
app.config.from_object('config')

#open db conection
db = SQLAlchemy(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cv')
def cv_display():
    return render_template('cv_template.html')

@app.route('/admin')
def admin():
    categories = models.cv.Category.query.all()
    print categories

    return render_template('admin_dash.html')

if __name__ == '__main__':
    app.run(debug=True)
