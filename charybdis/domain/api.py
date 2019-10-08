from flask_potion import ModelResource, fields
from flask_potion.routes import ItemRoute, Relation, Route

from ..app import db
from ..app.decorators import role_required
from .models import Domain


class DomainResource(ModelResource):
    projects = Relation("project")

    class Meta:
        model = Domain
        read_only_fields = (Domain.uuid.key,)

    @ItemRoute.PATCH("/deactivate", rel="deactivate")
    @role_required(["admin"])
    def deactivate(self, domain) -> fields.Boolean():
        domain.is_active = False

        db.session.commit()

        return True

    @ItemRoute.PATCH("/activate", rel="activate")
    @role_required(["admin"])
    def activate(self, domain) -> fields.Boolean():
        domain.is_active = True

        db.session.commit()

        return True

    @Route.POST("", rel="create", schema=fields.Inline("self"), response_schema=fields.Inline("self"))
    @role_required(["admin"])
    def create(self, properties):
        item = self.manager.create(properties)
        return item
