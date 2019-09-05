from ..app import db


class Project(db.Model):
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.Text)
    is_deactivated = db.Column(db.Boolean, default=False)
