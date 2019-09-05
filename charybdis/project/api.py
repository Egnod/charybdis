from flask_potion import ModelResource, fields
from flask_potion.routes import ItemRoute

from ..project.models import Project
from ..app import db


class ProjectResource(ModelResource):
    class Meta:
        model = Project

    @ItemRoute.DELETE('/deactivate', rel='destroy')
    def deactivate(self, project) -> fields.Boolean():
        project.is_deactivated = True

        db.session.commit()

        return True
