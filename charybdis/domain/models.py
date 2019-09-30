from uuid import uuid4

from slugify import slugify
from sqlalchemy.dialects.postgresql import UUID

from ..app import db


class Domain(db.Model):
    slug = db.Column(db.String, nullable=False, unique=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.Text)
    uuid = db.Column("uuid", UUID(as_uuid=True), nullable=False, default=lambda: uuid4(), unique=True)
    is_active = db.Column(db.Boolean, default=True)

    @db.validates("slug")
    def validate_slug(self, key, value) -> str:
        assert slugify(value) == value, "Incorrect slug for domain!"

        return value
