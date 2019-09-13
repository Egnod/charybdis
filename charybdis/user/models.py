from passlib.hash import pbkdf2_sha512
from slugify import slugify
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import backref

from ..app import db
from ..project.models import Project


class UserRole(db.Model):
    slug = db.Column(db.String, nullable=False)

    @db.validates("slug")
    def validate_slug(self, key, value) -> str:
        assert slugify(value) == value, "Incorrect slug for user role!"

        return value


class UserPermission(db.Model):
    slug = db.Column(db.String, nullable=False)

    @db.validates("slug")
    def validate_slug(self, key, value) -> str:
        assert slugify(value) == value, "Incorrect slug for user permission!"

        return value


class User(db.Model):
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    patronymic = db.Column(db.String, nullable=True)

    birthday = db.Column(db.Date, nullable=False)

    role_id = db.Column(db.Integer, db.ForeignKey(UserRole.id), nullable=False)
    role = db.relationship(UserRole)

    is_active = db.Column(db.Boolean, default=True, server_default="true")

    username = db.Column(db.String, unique=True)
    _password_hash = db.Column("password_hash", db.String)

    @db.validates("username")
    def validate_username(self, key: str, value: str) -> str:
        assert value == slugify(value), "Incorrect username!"

        return value

    @property
    def rolename(self):
        return self.role.slug

    @classmethod
    def lookup(cls, username):
        return cls.query.filter_by(username=username).one_or_none()

    @hybrid_property
    def password_hash(self) -> str:
        return self._password_hash

    @password_hash.setter
    def password_hash(self, value: str) -> None:
        self._password_hash = pbkdf2_sha512.hash(value)

    def check_password(self, candidate: str) -> bool:
        return pbkdf2_sha512.verify(candidate, self._password_hash)


class UserPermissionLinker(db.Model):
    permission_id = db.Column(db.Integer, db.ForeignKey(UserPermission.id), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey(User.id), nullable=False)

    permission = db.relationship(UserPermission, uselist=False)
    user = db.relationship(User)

    project_id = db.Column(db.Integer, db.ForeignKey(Project.id), nullable=False)
    project = db.relationship(Project, backref=backref("users"), uselist=False)

    __table_args__ = (db.UniqueConstraint("permission_id", "user_id", "project_id"),)
