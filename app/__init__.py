from flask import Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy

#make with the flaskings
app = Flask(__name__)

#load config
app.config.from_object('config')

#open db conection
db = SQLAlchemy(app)

from app import models, views
