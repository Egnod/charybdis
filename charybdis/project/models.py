from uuid import UUID, uuid5

from slugify import slugify
from sqlalchemy.dialects.postgresql import UUID as UUIDField
from sqlalchemy.ext.hybrid import hybrid_property

from ..app import db


class Project(db.Model):
    slug = db.Column(db.String, nullable=False, unique=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.Text)
    _uuid = db.Column("uuid", UUIDField(as_uuid=True))
    is_active = db.Column(db.Boolean, default=True)

    domain_id = db.Column(db.Integer, db.ForeignKey("domain.id"), nullable=False)
    domain = db.relationship("Domain", backref="projects")

    @db.validates("slug")
    def validate_slug(self, key, value) -> str:
        assert slugify(value) == value, "Incorrect slug for domain!"

        return value

    @hybrid_property
    def uuid(self) -> UUID:
        if self.domain and self.slug:
            if not self._uuid:
                self._uuid = uuid5(self.domain.uuid, self.slug)
                db.session.commit()

            return self._uuid

        raise ValueError("Domain or slug not found!")
