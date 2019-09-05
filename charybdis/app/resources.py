from typing import Tuple, Type
from flask_potion import Resource

from  charybdis.app import api

from ..project.api import ProjectResource

resources: Tuple[Resource] = (ProjectResource,)

for resource in resources:
    api.add_resource(resource)
