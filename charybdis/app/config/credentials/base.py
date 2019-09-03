import os

from .providers import CredentialProviderManager

import typing

CREDENTIAL_PROVIDER: str = "system"

def get_credential(name: str, default: typing.Any = None) -> typing.Union[typing.Any, None]:
    variable = CredentialProviderManager.get_by_code(CREDENTIAL_PROVIDER).get_credential(name)

    return variable if variable else default

