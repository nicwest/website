from flask.ext.wtf import Form
from wtforms import TextField, TextAreaField, BooleanField, PasswordField, SelectField, validators
from wtforms.validators import Required


class NewCV(Form):
    title = TextField('title', validators=[Required()])
    slug = TextField('slug', validators=[Required()])
    overview = TextAreaField('overview', validators=[Required()])
