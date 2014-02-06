__author__ = 'nic'

from app import db

__all__ = ['CV', 'Item', 'Category']

cvitem = db.Table('cvitem',
    db.Column('cv_id', db.Integer, db.ForeignKey('cv.id')),
    db.Column('item_id', db.Integer, db.ForeignKey('item.id')),
)
cvcategory = db.Table('cvcategory',
    db.Column('cv_id', db.Integer, db.ForeignKey('cv.id')),
    db.Column('category_id', db.Integer, db.ForeignKey('category.id')),
)

class CV (db.Model):
    __tablename__ = 'cv'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    slug = db.Column(db.String(200), nullable=False, unique=True)
    overview = db.Column(db.Text)
    items = db.relationship('Item', backref='cv', secondary=cvitem, lazy='dynamic')
    categories = db.relationship('Category', backref='cv', secondary=cvcategory, lazy='dynamic')
    updated = db.Column(db.DateTime)


class Item (db.Model):

    __tablename__ = 'item'
    id = db.Column(db.Integer, primary_key=True)
    typ = db.Column(db.String(200), nullable=False)
    key = db.Column(db.String(200))
    title = db.Column(db.String(200))
    value = db.Column(db.Text)
    single = db.Column(db.Boolean, default=False)
    footnote = db.Column(db.Text, nullable=True)
    icon = db.Column(db.String(200))
    order = db.Column(db.Integer)
    category = db.Column(db.Integer, db.ForeignKey('category.id'))


class Category (db.Model):

    __tablename__ = 'category'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    key = db.Column(db.String(50))
    subtitle = db.Column(db.String(200))
    icon = db.Column(db.String(200))
    items = db.relationship('Item', backref='cat', lazy='dynamic')
    order = db.Column(db.Integer)