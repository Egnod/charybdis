from typing import Tuple

from charybdis.app import api

from ..project.api import ProjectResource
from ..user.api import UserResource

RESOURCES: Tuple = (UserResource, ProjectResource)

for resource in RESOURCES:
    api.add_resource(resource)
