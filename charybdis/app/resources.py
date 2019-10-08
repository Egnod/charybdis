from typing import Tuple

from charybdis.app import api

from ..domain.api import DomainResource
from ..permission.api import PermissionResource
from ..project.api import ProjectResource
from ..user.api import UserPermissionLink, UserResource, UserRoleResource

RESOURCES: Tuple = (
    UserResource,
    ProjectResource,
    DomainResource,
    PermissionResource,
    UserRoleResource,
    UserPermissionLink,
)

for resource in RESOURCES:
    api.add_resource(resource)
