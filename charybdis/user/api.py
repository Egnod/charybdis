from flask_jwt import current_identity
from flask_potion import ModelResource, fields
from flask_potion.routes import ItemRoute, Route

from ..app import db
from ..app.decorators import auth_required, role_required
from .models import User, UserPermission, UserPermissionLinker


class UserResource(ModelResource):
    class Meta:
        model = User

    @Route.GET("/profile/permissions")
    @auth_required
    def resolve_profile_permissions(self, project_id: fields.Integer(minimum=1)) -> fields.List(fields.String()):
        permissions = (
            UserPermissionLinker.query.filter_by(project_id=project_id, user_id=current_identity.id)
            .join(UserPermissionLinker.permission)
            .with_entities(UserPermission.slug)
            .all()
        )

        permissions = list(map(lambda x: x.slug, permissions))

        return permissions

    @ItemRoute.DELETE("/deactivate", rel="destroy")
    @role_required(["admin"])
    def deactivate(self, user) -> fields.Boolean():
        user.is_active = False

        db.session.commit()

        return True

    @ItemRoute.GET("/permissions")
    def resolve_permissions(self, user, project_id: fields.Integer(minimum=1)) -> fields.List(fields.String()):
        permissions = (
            UserPermissionLinker.query.filter_by(project_id=project_id, user_id=user.id)
            .join(UserPermissionLinker.permission)
            .with_entities(UserPermission.slug)
            .all()
        )

        permissions = list(map(lambda x: x.slug, permissions))

        return permissions
