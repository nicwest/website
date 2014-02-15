from flask.ext.wtf import Form
from wtforms import TextField, TextAreaField, BooleanField, PasswordField, SelectField, validators
from wtforms.validators import Required
from app import db, models


class NewCV(Form):
    title = TextField('title', validators=[Required()])
    slug = TextField('slug', validators=[Required()])
    overview = TextAreaField('overview', validators=[Required()])


class Item(Form):
    parent = SelectField('parent', choices=[('None (Category)', None)]+db.session.query(models.Item.id, models.Item.admin_title).all())
    typ = SelectField('server', choices=db.session.query(models.Item.typ, models.Item.typ).group_by(models.Item.typ).all())
    key = TextField('title', validators=[Required()])
    value = TextAreaField('overview', validators=[Required()])
    admin_title = TextField('title', validators=[Required()])
    note =  TextAreaField('overview', validators=[Required()])