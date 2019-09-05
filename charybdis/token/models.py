import secrets

from ..app import db
from ..user.models import User


class Token(db.Model):
    value = db.Column(db.String, unique=True, nullable=False, default=lambda: secrets.token_urlsafe(1024))
    user_id = db.Column(db.Integer, db.ForeignKey(User.id), nullable=False)

    user = db.relationship(User)
