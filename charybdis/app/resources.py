from typing import Tuple

from charybdis.app import api

from ..domain.api import DomainResource
from ..project.api import ProjectResource
from ..permission.api import PermissionResource
from ..user.api import UserResource

RESOURCES: Tuple = (UserResource, ProjectResource, DomainResource, PermissionResource)

for resource in RESOURCES:
    api.add_resource(resource)
