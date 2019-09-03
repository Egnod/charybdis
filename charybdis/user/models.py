from ..app import db


class User(db.Model):
    __tablename__ = "users"

    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    patronymic = db.Column(db.String, nullable=True)

    birthday = db.Column(db.Date, nullable=False)

