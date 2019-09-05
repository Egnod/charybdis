from slugify import slugify

from ..app import db
from ..project.models import Project


class UserPermission(db.Model):
    slug = db.Column(db.String, nullable=False)

    project_id = db.Column(db.Integer, db.ForeignKey(Project.id), nullable=True)
    project = db.relationship(Project)

    @db.validates("slug")
    def validate_slug(self, key, value) -> str:
        assert slugify(value) == value, "Incorrect slug for user role!"

        return value

    __table_args__ = (
        db.UniqueConstraint('slug', 'project_id'),
    )


class User(db.Model):
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    patronymic = db.Column(db.String, nullable=True)

    birthday = db.Column(db.Date, nullable=False)


class UserPermissionLinker(db.Model):
    permission_id = db.Column(db.Integer, db.ForeignKey(UserPermission.id), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey(User.id), nullable=False)

    permission = db.relationship(UserPermission)
    user = db.relationship(User)
