import os

from .providers import ConfigProviderManager

import typing

CONFIG_PROVIDER: str = "system"


def get_config(name: str, default: typing.Any = None) -> typing.Union[typing.Any, None]:
    variable = ConfigProviderManager.get_by_code(CONFIG_PROVIDER).get_variable(name)

    return variable if variable else default

