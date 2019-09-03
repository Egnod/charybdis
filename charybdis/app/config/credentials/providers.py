import os

from abc import ABCMeta, abstractmethod, abstractproperty
import typing

class CredentialProvider(metaclass=ABCMeta):
    @abstractproperty
    def provider_code(self) -> str:
        pass

    @abstractmethod
    def get_credential(self, identifier: str) -> typing.Any:
        pass

class SystemProvider(CredentialProvider):
    SYSTEM_PREFIX = "system"

    @property
    def provider_code(self) -> str:
        return "system"

    def prefixize(self, varname: str) -> str:
        return f"{self.SYSTEM_PREFIX}_{varname.upper()}"
    
    def get_credential(self, identifier: str) -> typing.Union[str, None]:
        if identifier in os.environ:
            return os.getenv(self.prefixize(identifier))


class CredentialProviderManager(object):
    @staticmethod
    def get_by_code(code: str) -> typing.Union[CredentialProvider, None]:
        for provider in CredentialProvider.__subclasses__():
            if provider().provider_code == code:
                return provider()


### Simple example with Vault by HashiCorp
"""
from ..config import get_config
import hvac

class VaultProvider(CredentialProvider):
    def __init__(self, token: str) -> None:
        self.client = hvac.Client(url=get_config("vault_url"))
        self.client.token = get_config("vault_token")

    @property
    def provider_code(self) -> str:
        return "vault"
    
    def get_credential(self, identifier: str) -> typing.Dict[str, typing.Any]:
        return self.client.read(identifier)["data"]
"""