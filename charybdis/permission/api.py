from flask_potion import ModelResource, fields
from flask_potion.routes import ItemRoute, Route

from ..app.decorators import role_required
from .models import Permission


class PermissionResource(ModelResource):
    class Meta:
        model = Permission

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

    @ItemRoute.PATCH("/deactivate", rel="destroy")
    @role_required(["admin"])
    def deactivate(self, permission) -> fields.Boolean():
        return False
