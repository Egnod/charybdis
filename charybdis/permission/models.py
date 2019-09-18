from slugify import slugify

from ..app import db


class Permission(db.Model):
    slug = db.Column(db.String, nullable=False)

    @db.validates("slug")
    def validate_slug(self, key, value) -> str:
        assert slugify(value) == value, "Incorrect slug for user permission!"

        return value
