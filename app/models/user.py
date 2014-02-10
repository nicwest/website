__author__ = 'nic'
from app import db
from werkzeug.security import generate_password_hash, check_password_hash

__all__ = ['User', 'ROLE_GUEST', 'ROLE_USER', 'ROLE_MODERATOR', 'ROLE_ADMIN']

ROLE_GUEST = 0
ROLE_USER  = 1
ROLE_MODERATOR = 2
ROLE_ADMIN = 3


class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True)
    email = db.Column(db.String(120), unique=True)
    pw_hash = db.Column(db.String(100))
    role = db.Column(db.Integer, default=ROLE_GUEST)

    def __init__(self, username, email, password, role=ROLE_USER):
        self.username = username
        self.email = email
        self.set_password(password)
        self.role = role

    def set_password(self, password):
        self.pw_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.pw_hash, password)