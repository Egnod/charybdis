from slugify import slugify

from ..app import db


class Project(db.Model):
    slug = db.Column(db.String, nullable=False)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.Text)
    is_deactivated = db.Column(db.Boolean, default=False)

    @db.validates("slug")
    def validate_slug(self, key, value) -> str:
        assert slugify(value) == value, "Incorrect slug for user role!"

        return value
