from flask_potion import ModelResource, fields
from flask_potion.routes import ItemRoute, Relation

from ..app import db
from ..app.decorators import role_required
from .models import Project


class ProjectResource(ModelResource):
    users = Relation("user")

    class Meta:
        model = Project

    @ItemRoute.DELETE("/deactivate", rel="destroy")
    @role_required(["admin"])
    def deactivate(self, project) -> fields.Boolean():
        project.is_deactivated = True

        db.session.commit()

        return True

    @ItemRoute.PATCH("/activate")
    @role_required(["admin"])
    def activate(self, project) -> fields.Boolean():
        project.is_deactivated = False

        db.session.commit()

        return True
