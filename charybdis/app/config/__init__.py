from sitri import Sitri
from sitri.contrib.system import SystemConfigProvider, SystemCredentialProvider

conf = Sitri(
    config_provider=SystemConfigProvider(project_prefix="charybdis"),
    credential_provider=SystemCredentialProvider(project_prefix="charybdis"),
)


from .base import *  # isort:skip
from .database import *  # isort:skip
from .dramatiq import DramatiqConfig  # isort:skip
from .logging import *  # isort:skip
from .secrets import SecretsConfig  # isort:skip


class Config(BaseConfig, LoggingConfig, DataBaseConfig, DramatiqConfig, SecretsConfig):
    pass
