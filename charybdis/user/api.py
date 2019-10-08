from flask_jwt import current_identity
from flask_potion import ModelResource, fields
from flask_potion.routes import ItemRoute, Route

from ..app import db
from ..app.decorators import auth_required, role_required
from .models import Permission, User, UserPermissionLinker, UserRole


class UserResource(ModelResource):
    class Meta:
        model = User
        exclude_fields = [User._password_hash.key]
        read_only_fields = [User.uuid.key]

    @Route.GET("/profile/permissions")
    @auth_required
    def resolve_profile_permissions(self, project_id: fields.Integer(minimum=1)) -> fields.List(fields.String()):
        permissions = (
            UserPermissionLinker.query.filter_by(project_id=project_id, user_id=current_identity.id)
            .join(UserPermissionLinker.permission)
            .with_entities(Permission.slug)
            .all()
        )

        permissions = list(map(lambda x: x.slug, permissions))

        return permissions

    @Route.GET("/profile")
    @auth_required
    def resolve_profile(self) -> fields.Inline("self"):
        return self.manager.read(current_identity.id)

    @ItemRoute.PATCH("/deactivate", rel="deactivate")
    @role_required(["admin"])
    def deactivate(self, user) -> fields.Boolean():
        user.is_active = False

        db.session.commit()

        return True

    @ItemRoute.PATCH("/activate", rel="activate")
    @role_required(["admin"])
    def activate(self, user) -> fields.Boolean():
        user.is_active = True

        db.session.commit()

        return True

    @ItemRoute.GET("/permissions")
    @role_required(["admin"])
    def resolve_permissions(self, user, project_id: fields.Integer(minimum=1)) -> fields.List(fields.String()):
        permissions = (
            UserPermissionLinker.query.filter_by(project_id=project_id, user_id=user.id)
            .join(UserPermissionLinker.permission)
            .with_entities(Permission.slug)
            .all()
        )

        permissions = list(map(lambda x: x.slug, permissions))

        return permissions

    @Route.POST("", rel="create", schema=fields.Inline("self"), response_schema=fields.Inline("self"))
    @role_required(["admin"])
    def create(self, properties):
        return super().create(properties=properties)

    @Route.GET(
        lambda r: "/<{}:id>".format(r.meta.id_converter),
        rel="self",
        attribute="instance",
        response_schema=fields.Inline("self"),
    )
    @role_required(["admin"])
    def read(self, id):
        return super().read(id=id)

    @read.PATCH(
        rel="update",
        schema=fields.Inline("self", patchable=True),
        response_schema=fields.Inline("self", patchable=True),
    )
    @role_required(["admin"])
    def update(self, properties, id):
        item = self.manager.read(id)
        updated_item = self.manager.update(item, properties)
        return updated_item

    @ItemRoute.PATCH("/changePassword", rel="change_password")
    @role_required(["admin"])
    def change_password(self, user, new_password: fields.String()) -> fields.Boolean():
        user.password_hash = new_password
        db.session.commit()

        return True


class UserRoleResource(ModelResource):
    class Meta:
        model = UserRole

    @Route.POST("", rel="create", schema=fields.Inline("self"), response_schema=fields.Inline("self"))
    @role_required(["admin"])
    def create(self, properties):
        return super().create(properties=properties)

    @Route.GET(
        lambda r: "/<{}:id>".format(r.meta.id_converter),
        rel="self",
        attribute="instance",
        response_schema=fields.Inline("self"),
    )
    @role_required(["admin"])
    def read(self, id):
        return super().read(id=id)

    @read.PATCH(
        rel="update",
        schema=fields.Inline("self", patchable=True),
        response_schema=fields.Inline("self", patchable=True),
    )
    @role_required(["admin"])
    def update(self, properties, id):
        item = self.manager.read(id)
        updated_item = self.manager.update(item, properties)
        return updated_item


class UserPermissionLink(ModelResource):
    class Meta:
        model = UserPermissionLinker

    @Route.POST("", rel="create", schema=fields.Inline("self"), response_schema=fields.Inline("self"))
    @role_required(["admin"])
    def create(self, properties):
        return super().create(properties=properties)

    @Route.GET(
        lambda r: "/<{}:id>".format(r.meta.id_converter),
        rel="self",
        attribute="instance",
        response_schema=fields.Inline("self"),
    )
    @role_required(["admin"])
    def read(self, id):
        return super().read(id=id)

    @read.PATCH(
        rel="update",
        schema=fields.Inline("self", patchable=True),
        response_schema=fields.Inline("self", patchable=True),
    )
    @role_required(["admin"])
    def update(self, properties, id):
        item = self.manager.read(id)
        updated_item = self.manager.update(item, properties)
        return updated_item
