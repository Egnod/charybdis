from passlib.hash import pbkdf2_sha512
from slugify import slugify
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import backref
from uuid import uuid4
from sqlalchemy.dialects.postgresql import UUID

from ..app import db
from ..permission.models import Permission
from ..project.models import Project
from ..domain.models import Domain


class UserRole(db.Model):
    slug = db.Column(db.String, nullable=False)

    @db.validates("slug")
    def validate_slug(self, key, value) -> str:
        assert slugify(value) == value, "Incorrect slug for user role!"

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

    uuid = db.Column(UUID(as_uuid=True), default=uuid4, nullable=False)

    domain_id = db.Column(db.Integer, db.ForeignKey(Domain.id), nullable=False)
    domain = db.relationship(Domain)

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
    permission_id = db.Column(db.Integer, db.ForeignKey(Permission.id), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey(User.id), nullable=False)

    permission = db.relationship(Permission, uselist=False)
    user = db.relationship(User)

    project_id = db.Column(db.Integer, db.ForeignKey(Project.id), nullable=False)
    project = db.relationship(Project, backref=backref("users"), uselist=False)

    __table_args__ = (db.UniqueConstraint("permission_id", "user_id", "project_id"),)
