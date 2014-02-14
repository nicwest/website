__author__ = 'nic'

from app import db
import datetime

__all__ = ['CV', 'Item', 'Category']


class CV (db.Model):
    __tablename__ = 'cv'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    slug = db.Column(db.String(200), nullable=False, unique=True)
    items = db.relationship('CVItem', backref='cv', lazy='dynamic')
    updated = db.Column(db.DateTime)

    def __init__ (self, title, slug):
        self.title = title
        self.slug = slug
        self.updated = datetime.datetime.now()

    def __repr__(self):
        return "<CV %r:%r>" % (self.id, self.title)

class Item (db.Model):
    __tablename__ = 'item'
    id = db.Column(db.Integer, primary_key=True)
    children = db.relationship('Item', backref=db.backref('parent', remote_side=[id]))
    cvs = db.relationship('CVItem', backref='item', lazy='dynamic')
    parent_id = db.Column(db.Integer, db.ForeignKey('item.id'))
    typ = db.Column(db.String(200), nullable=False)
    key = db.Column(db.Text, nullable=True)
    value = db.Column(db.Text)
    admin_title = db.Column(db.String(200), nullable=False)
    note = db.Column(db.Text, nullable=True)
    icon = db.Column(db.String(200), nullable=True)
    default_order = db.Column(db.Integer)

    def __init__(self, typ, value, admin_title, default_order=0, key=None, note=None, icon=None, parent=None):
        self.typ = typ
        self.value = value
        self.admin_title = admin_title
        self.key = key
        self.note = note
        self.icon = icon
        self.parent = parent
        self.default_order = default_order

    def __repr__(self):
        return "<Item %r:%r>" % (self.id, self.admin_title)

class CVItem (db.Model):
    __tablename__ = 'cvitems'
    id = db.Column(db.Integer, primary_key=True)
    item_id = db.Column(db.Integer, db.ForeignKey('item.id'))
    cv_id = db.Column(db.Integer, db.ForeignKey('cv.id'))
    order = db.Column(db.Integer)
    all_children = db.Column(db.Boolean, default=False)

    def __init__ (self, cv, item, order, all_children=False):
        self.cv = cv
        self.item = item
        self.order = order
        self.all_children = all_children

